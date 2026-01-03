"""Pydantic models for document breakdown and storyboard generation."""

import pathlib
from typing import Literal

from pydantic import BaseModel, Field


class AtomicTopic(BaseModel):
    """A self-contained topic extracted from a document."""

    name: str = Field(
        description="A clear, descriptive heading for this topic (e.g., 'Self-Attention Mechanism', 'Positional Encoding')"
    )
    summary: str = Field(
        description="A 2-3 sentence summary explaining the core idea, suitable as a video hook/introduction"
    )
    full_explanation: str = Field(
        description="Complete, self-contained markdown text covering this topic. Must include all necessary context, definitions, equations, and explanations so a viewer can understand this topic WITHOUT having seen other topics. Reference figures and tables by their numbers with descriptions."
    )
    key_takeaways: list[str] = Field(
        description="2-4 bullet points of the most important things to remember"
    )

    def to_text(self) -> str:
        """Convert the topic to a formatted markdown string."""
        takeaways = "\n".join(f"- {t}" for t in self.key_takeaways)
        return (
            f"**name**: {self.name}\n\n"
            f"**summary**: {self.summary}\n\n"
            f"**full_explanation**:\n{self.full_explanation}\n\n"
            f"**key_takeaways**:\n{takeaways}"
        )


class Breakdown(BaseModel):
    """A structured breakdown of a document into atomic topics."""

    document_title: str = Field(description="Title of the paper/document")
    document_summary: str = Field(
        description="Brief 2-3 sentence overview of the entire document"
    )
    topics: list[AtomicTopic] = Field(
        description="List of atomic, self-contained topics extracted from the document"
    )


class Scene(BaseModel):
    """A single scene in the storyboard - a complete visual and audio sequence."""

    scene_type: Literal["hook", "mid", "closing"] = Field(
        default="mid",
        description="Type of scene: 'hook' for opening, 'mid' for main content, 'closing' for finale",
    )
    title: str = Field(
        description="A brief title for this scene (e.g., 'The Attention Spotlight', 'Matrix Multiplication Dance')"
    )
    visual_description: str = Field(
        description="""A filmmaker's script describing exactly what appears on screen. Written as a detailed visual 
        screenplay - every object, color, position, movement, transformation, and visual relationship must be 
        precisely specified. A reader should be able to perfectly visualize the animation without seeing it.
        Include: what appears, where it appears, how it moves, what colors/sizes, what transforms into what,
        spatial relationships, visual metaphors, and the emotional arc of the scene."""
    )
    narration: str = Field(
        description="The spoken narration for this scene, written for text-to-speech. "
        "Should complement (not duplicate) the visuals - explain what the viewer sees, "
        "provide context, and guide their understanding. Paced to match the visual flow."
    )

    def to_text(self) -> str:
        """Convert the scene to a formatted string."""
        return (
            f"## [{self.scene_type}] {self.title}\n\n"
            f"**Visual Description:**\n{self.visual_description}\n"
            f"**Narration:**\n{self.narration}\n"
        )


class TopicStoryboard(BaseModel):
    """A complete visual storyboard for one atomic topic - a filmmaker's screenplay."""

    topic_name: str = Field(description="Name of the atomic topic being visualized")
    visual_concept: str = Field(
        description="The overarching visual metaphor or analogy that ties the entire storyboard together. What is the 'big picture' visual idea?"
    )
    scenes: list[Scene] = Field(
        description="Ordered scenes (hook → mid scenes → closing) that tell the complete visual story. Each scene must have exhaustively detailed visual descriptions."
    )


class AnimationResult(BaseModel):
    """Result of an animation generation attempt."""

    topic_index: int = Field(description="Index of the topic in the breakdown")
    topic_name: str = Field(description="Name of the topic")
    success: bool = Field(description="Whether the animation was successfully generated")
    video_path: pathlib.Path | None = Field(default=None, description="Path to the generated video file")
    scene_code: str | None = Field(default=None, description="The generated Manim scene code")
    error_message: str | None = Field(default=None, description="Error message if generation failed")
    iterations: int = Field(default=0, description="Number of iterations taken to generate the animation")

