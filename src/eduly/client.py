"""Eduly client for document processing."""

import pathlib

from google import genai
from google.genai import types as gemini_types

from eduly.models import AtomicTopic, Breakdown, TopicStoryboard
from eduly.prompts import BREAKDOWN_PROMPT, STORYBOARD_PROMPT, format_topic_input


class EdulyClient:
    """Client for interacting with Eduly services."""

    def __init__(self, gemini_client: genai.Client):
        """Initialize the Eduly client.

        Args:
            gemini_client: Google Gemini client.
        """
        self.gemini_client = gemini_client

    def breakdown(self, file_path: str | pathlib.Path, model: str = "gemini-3-flash-preview", thinking_level: str = "high") -> tuple[Breakdown, gemini_types.GenerateContentResponse]:
        """Break down a PDF document into atomic, self-contained topics using a Gemini model.

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

