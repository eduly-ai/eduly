"""Eduly clients for document processing and animation generation."""

import copy
import os
import pathlib
import subprocess
import time
from collections.abc import Callable

from google import genai
from google.genai import types as gemini_types
from langchain_core.language_models import BaseChatModel

from eduly.models import AnimationResult, AtomicTopic, Breakdown, TopicStoryboard
from eduly.prompts import (
    BREAKDOWN_PROMPT,
    MANIM_CODING_AGENT_PROMPT,
    SCENE_BOILERPLATE,
    STORYBOARD_PROMPT,
    format_storyboard_prompt,
    format_topic_input,
)


class EdulyBreakdownClient:
    """Client for breaking down documents and generating storyboards."""

    def __init__(self, gemini_client: genai.Client):
        """Initialize the breakdown client.

        Args:
            gemini_client: Google Gemini client for API calls.
        """
        self.gemini_client = gemini_client

    def breakdown(
        self,
        file_path: str | pathlib.Path,
        model: str = "gemini-3-flash-preview",
        thinking_level: str = "high",
    ) -> tuple[Breakdown, gemini_types.GenerateContentResponse]:
        """Break down a PDF document into atomic, self-contained topics.

        Args:
            file_path: Path to the PDF file to analyze.
            model: Gemini model to use for the breakdown.
            thinking_level: Thinking level to use for the breakdown.

        Returns:
            A tuple of (Breakdown object, raw Gemini response).
        """
        file_path = pathlib.Path(file_path)

        # Upload the PDF using the File API
        uploaded_file = self.gemini_client.files.upload(file=file_path)

        # Generate content with structured output
        response = self.gemini_client.models.generate_content(
            model=model,
            config=gemini_types.GenerateContentConfig(
                tools=[gemini_types.GoogleSearch()],
                response_mime_type="application/json",
                response_json_schema=Breakdown.model_json_schema(),
                thinking_config=gemini_types.ThinkingConfig(thinking_level=thinking_level),
            ),
            contents=[uploaded_file, BREAKDOWN_PROMPT],
        )

        # Parse and return the breakdown with raw response
        try:
            breakdown = Breakdown.model_validate_json(response.text)
        except Exception as e:
            print(f"Error parsing breakdown: {e}")
            print("only returning the raw response")
            print(response.text)
            return None, response

        return breakdown, response

    def storyboard(
        self,
        topic: AtomicTopic,
        source_file: str | pathlib.Path | None = None,
        model: str = "gemini-3-flash-preview",
        thinking_level: str = "high",
    ) -> tuple[TopicStoryboard, gemini_types.GenerateContentResponse]:
        """Create a storyboard for an atomic topic.

        Args:
            topic: The AtomicTopic to transform into a storyboard.
            source_file: Optional path to the source PDF for additional context.
            model: Gemini model to use for storyboard generation.
            thinking_level: Thinking level to use for generation.

        Returns:
            A tuple of (TopicStoryboard object, raw Gemini response).
        """
        # Build the full prompt with topic input
        final_prompt = STORYBOARD_PROMPT + format_topic_input(topic)

        # Prepare contents - optionally include source file
        contents: list = []
        if source_file is not None:
            source_file = pathlib.Path(source_file)
            uploaded_file = self.gemini_client.files.upload(file=source_file)
            contents.append(uploaded_file)
        contents.append(final_prompt)

        # Generate content with structured output
        response = self.gemini_client.models.generate_content(
            model=model,
            config=gemini_types.GenerateContentConfig(
                tools=[
                    gemini_types.GoogleSearch(),
                    gemini_types.Tool(code_execution=gemini_types.ToolCodeExecution),
                ],
                response_mime_type="application/json",
                response_json_schema=TopicStoryboard.model_json_schema(),
                thinking_config=gemini_types.ThinkingConfig(thinking_level=thinking_level),
            ),
            contents=contents,
        )

        # Parse and return the storyboard with raw response
        try:
            storyboard = TopicStoryboard.model_validate_json(response.text)
        except Exception as e:
            print(f"Error parsing storyboard: {e}")
            print("only returning the raw response")
            print(response.text)
            return None, response

        return storyboard, response


class EdulyAnimationClient:
    """Client for generating Manim animations from storyboards.

    This client uses a coding agent to generate Manim code from storyboards
    and renders them to video files.

    Example usage:
        ```python
        from langchain_google_genai import ChatGoogleGenerativeAI

        # Set up your langchain model
        langchain_model = ChatGoogleGenerativeAI(
            model="gemini-3-pro-preview",
            temperature=1.0,
        )

        # Create the animation client
        animation_client = EdulyAnimationClient(
            langchain_model=langchain_model,
            agent_workspace_path="./agent_workspace",
        )

        # Generate animations
        results = animation_client.animate(breakdown, storyboards)
        ```

    Expected folder structure:
        agent_workspace/
        ├── manim_docs/           # Manim documentation (tutorials/, guides/, reference/)
        ├── animation_workspace/  # Where scene.py is created and videos are rendered
        └── rendered_videos/      # Final output videos (auto-created)
    """

    def __init__(
        self,
        langchain_model: BaseChatModel,
        agent_workspace_path: str | pathlib.Path,
    ):
        """Initialize the animation client.

        Args:
            langchain_model: A LangChain chat model for the coding agent.
                Can be any model (Gemini, OpenAI, vLLM, etc.) wrapped in LangChain.
            agent_workspace_path: Path to the agent workspace folder.
                This folder should contain:
                - manim_docs/: Manim documentation (tutorials/, guides/, reference/)
                - animation_workspace/: Where scene files are created and rendered
        """
        self.langchain_model = langchain_model
        self.agent_workspace_path = pathlib.Path(agent_workspace_path).resolve()

        # Derived paths within the agent workspace
        self.manim_docs_path = self.agent_workspace_path / "manim_docs"
        self.animation_workspace_path = self.agent_workspace_path / "animation_workspace"
        self.rendered_videos_path = self.agent_workspace_path / "rendered_videos"

        # Validate paths
        if not self.agent_workspace_path.exists():
            raise ValueError(f"agent_workspace_path does not exist: {self.agent_workspace_path}")
        if not self.manim_docs_path.exists():
            raise ValueError(f"manim_docs folder not found: {self.manim_docs_path}")
        if not self.animation_workspace_path.exists():
            self.animation_workspace_path.mkdir(parents=True, exist_ok=True)
        if not self.rendered_videos_path.exists():
            self.rendered_videos_path.mkdir(parents=True, exist_ok=True)

    def _create_agent(self):
        """Create a new coding agent instance."""
        from deepagents import create_deep_agent
        from deepagents.backends import FilesystemBackend

        return create_deep_agent(
            model=self.langchain_model,
            system_prompt=MANIM_CODING_AGENT_PROMPT,
            backend=FilesystemBackend(root_dir=str(self.agent_workspace_path), virtual_mode=True),
        )

    def _prepare_workspace(self):
        """Clear the workspace and write the boilerplate scene file."""
        # Clear existing files in workspace (except keep the directory)
        for item in self.animation_workspace_path.iterdir():
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                import shutil
                shutil.rmtree(item)

        # Write boilerplate scene file
        scene_file = self.animation_workspace_path / "scene.py"
        scene_file.write_text(SCENE_BOILERPLATE)

    def _render_scene(self) -> subprocess.CompletedProcess:
        """Run manim to render the scene.

        Returns:
            CompletedProcess with stdout/stderr from manim.
        """
        my_env = os.environ.copy()
        # Add TeX to PATH for LaTeX rendering (macOS)
        my_env["PATH"] = "/Library/TeX/texbin:" + os.environ.get("PATH", "")

        return subprocess.run(
            ["uv", "run", "manim", "-ql", "scene.py"],
            capture_output=True,
            text=True,
            cwd=str(self.animation_workspace_path),
            env=my_env,
        )

    def _check_render_success(self) -> bool:
        """Check if manim successfully rendered a video.

        Returns:
            True if a video file was created, False otherwise.
        """
        video_dir = self.animation_workspace_path / "media" / "videos" / "scene" / "1920p15"
        if not video_dir.exists():
            return False
        return len(list(video_dir.glob("*.mp4"))) > 0

    def _get_video_path(self) -> pathlib.Path | None:
        """Get the path to the rendered video file.

        Returns:
            Path to the video file, or None if not found.
        """
        video_dir = self.animation_workspace_path / "media" / "videos" / "scene" / "1920p15"
        if not video_dir.exists():
            return None
        video_files = list(video_dir.glob("*.mp4"))
        return video_files[0] if video_files else None

    def _sanitize_filename(self, name: str) -> str:
        """Sanitize a string for use in a filename.

        Args:
            name: The string to sanitize.

        Returns:
            A sanitized string safe for use in filenames.
        """
        import re
        # Replace spaces with underscores
        sanitized = name.replace(" ", "_")
        # Remove any character that's not alphanumeric, underscore, or hyphen
        sanitized = re.sub(r"[^\w\-]", "", sanitized)
        # Limit length to avoid filesystem issues
        return sanitized[:50].lower()

    def animate(
        self,
        breakdown: Breakdown,
        storyboards: list[TopicStoryboard],
        topic_indices: list[int] | None = None,
        max_iterations: int = 5,
        on_progress: Callable[[int, int, str], None] | None = None,
        ratelimit: int = 0,
    ) -> list[AnimationResult]:
        """Generate Manim animations for storyboards.

        Args:
            breakdown: The document breakdown containing all topics.
            storyboards: List of storyboards (one per topic) to animate.
            topic_indices: Optional list of topic indices to animate.
                If None, animates all topics that have storyboards.
            max_iterations: Maximum retry iterations for failed renders.
            on_progress: Optional callback(topic_index, iteration, status_message)
                for progress updates.
            ratelimit: Optional ratelimit in seconds to wait between iterations.

        Returns:
            List of AnimationResult objects, one per topic attempted.
            Videos are saved to rendered_videos/{topic_name}_{topic_index}.mp4
        """
        import shutil

        # Determine which topics to animate
        if topic_indices is None:
            topic_indices = list(range(len(storyboards)))

        results: list[AnimationResult] = []

        for topic_idx in topic_indices:
            if topic_idx >= len(storyboards):
                results.append(AnimationResult(
                    topic_index=topic_idx,
                    topic_name=breakdown.topics[topic_idx].name if topic_idx < len(breakdown.topics) else "Unknown",
                    success=False,
                    error_message=f"No storyboard found for topic index {topic_idx}",
                ))
                continue

            if topic_idx >= len(breakdown.topics):
                results.append(AnimationResult(
                    topic_index=topic_idx,
                    topic_name="Unknown",
                    success=False,
                    error_message=f"No topic found in breakdown for index {topic_idx}",
                ))
                continue

            storyboard = storyboards[topic_idx]
            topic_name = breakdown.topics[topic_idx].name

            if on_progress:
                on_progress(topic_idx, 0, f"Starting animation for topic: {topic_name}")

            # Prepare workspace
            self._prepare_workspace()

            # Create a fresh agent for each topic
            agent = self._create_agent()

            # Format the prompt for this topic
            prompt = format_storyboard_prompt(breakdown, storyboard, topic_idx)

            # Run the agent
            if on_progress:
                on_progress(topic_idx, 0, "Running coding agent...")

            if ratelimit > 0:
                time.sleep(ratelimit)
            result = agent.invoke({"messages": [{"role": "user", "content": prompt}]})

            # Try to render
            manim_result = self._render_scene()
            success = self._check_render_success()

            iteration = 0
            while not success and iteration < max_iterations:
                iteration += 1
                if on_progress:
                    on_progress(topic_idx, iteration, f"Render failed, retrying (iteration {iteration}/{max_iterations})...")

                # Send error back to agent
                history = copy.deepcopy(result["messages"])
                history.append({"role": "assistant", "content": manim_result.stderr})
                result = agent.invoke({"messages": history})
                if ratelimit > 0:
                    time.sleep(ratelimit)
                manim_result = self._render_scene()
                success = self._check_render_success()

            # Collect results
            scene_file = self.animation_workspace_path / "scene.py"
            scene_code = scene_file.read_text() if scene_file.exists() else None

            if success:
                video_path = self._get_video_path()

                # Copy video to rendered_videos folder
                if video_path is not None:
                    sanitized_name = self._sanitize_filename(topic_name)
                    output_file = self.rendered_videos_path / f"{sanitized_name}_{topic_idx}.mp4"
                    shutil.copy(video_path, output_file)
                    video_path = output_file

                if on_progress:
                    on_progress(topic_idx, iteration, f"Success! Video saved to {video_path}")

                results.append(AnimationResult(
                    topic_index=topic_idx,
                    topic_name=topic_name,
                    success=True,
                    video_path=video_path,
                    scene_code=scene_code,
                    iterations=iteration,
                ))
            else:
                if on_progress:
                    on_progress(topic_idx, iteration, f"Failed after {iteration} iterations")

                results.append(AnimationResult(
                    topic_index=topic_idx,
                    topic_name=topic_name,
                    success=False,
                    scene_code=scene_code,
                    error_message=manim_result.stderr if manim_result else "Unknown error",
                    iterations=iteration,
                ))

        return results

    def animate_single(
        self,
        breakdown: Breakdown,
        storyboard: TopicStoryboard,
        topic_index: int,
        max_iterations: int = 5,
        on_progress: Callable[[int, int, str], None] | None = None,
        ratelimit: int = 0,
    ) -> AnimationResult:
        """Generate a Manim animation for a single storyboard.

        Convenience method for animating one topic at a time.

        Args:
            breakdown: The document breakdown containing all topics.
            storyboard: The storyboard for this topic.
            topic_index: Index of this topic in the breakdown.
            max_iterations: Maximum retry iterations for failed renders.
            on_progress: Optional callback for progress updates.
            ratelimit: Optional ratelimit in seconds to wait between iterations.
        Returns:
            AnimationResult for the animation attempt.
            Video is saved to rendered_videos/{topic_name}_{topic_index}.mp4
        """
        import shutil

        topic_name = breakdown.topics[topic_index].name if topic_index < len(breakdown.topics) else "Unknown"

        if on_progress:
            on_progress(topic_index, 0, f"Starting animation for topic: {topic_name}")

        # Prepare workspace
        self._prepare_workspace()

        # Create agent
        agent = self._create_agent()

        # Format prompt
        prompt = format_storyboard_prompt(breakdown, storyboard, topic_index)

        # Run agent
        if on_progress:
            on_progress(topic_index, 0, "Running coding agent...")

        if ratelimit > 0:
            time.sleep(ratelimit)
        result = agent.invoke({"messages": [{"role": "user", "content": prompt}]})

        # Render
        manim_result = self._render_scene()
        success = self._check_render_success()

        iteration = 0
        while not success and iteration < max_iterations:
            iteration += 1
            if on_progress:
                on_progress(topic_index, iteration, f"Render failed, retrying (iteration {iteration}/{max_iterations})...")

            history = copy.deepcopy(result["messages"])
            history.append({"role": "assistant", "content": manim_result.stderr})

            result = agent.invoke({"messages": history})
            if ratelimit > 0:
                time.sleep(ratelimit)
            manim_result = self._render_scene()
            success = self._check_render_success()

        # Collect result
        scene_file = self.animation_workspace_path / "scene.py"
        scene_code = scene_file.read_text() if scene_file.exists() else None

        if success:
            video_path = self._get_video_path()

            # Copy to rendered_videos folder
            if video_path is not None:
                sanitized_name = self._sanitize_filename(topic_name)
                output_file = self.rendered_videos_path / f"{sanitized_name}_{topic_index}.mp4"
                shutil.copy(video_path, output_file)
                video_path = output_file

            if on_progress:
                on_progress(topic_index, iteration, f"Success! Video saved to {video_path}")

            return AnimationResult(
                topic_index=topic_index,
                topic_name=topic_name,
                success=True,
                video_path=video_path,
                scene_code=scene_code,
                iterations=iteration,
            )
        else:
            if on_progress:
                on_progress(topic_index, iteration, f"Failed after {iteration} iterations")

            return AnimationResult(
                topic_index=topic_index,
                topic_name=topic_name,
                success=False,
                scene_code=scene_code,
                error_message=manim_result.stderr if manim_result else "Unknown error",
                iterations=iteration,
            )


# Backwards compatibility alias
EdulyClient = EdulyBreakdownClient
