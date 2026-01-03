"""Prompts for Eduly document processing."""

from eduly.prompts.animate import (
    MANIM_CODING_AGENT_PROMPT,
    SCENE_BOILERPLATE,
    format_storyboard_prompt,
)
from eduly.prompts.breakdown import BREAKDOWN_PROMPT
from eduly.prompts.storyboard import STORYBOARD_PROMPT, format_topic_input

__all__ = [
    "BREAKDOWN_PROMPT",
    "MANIM_CODING_AGENT_PROMPT",
    "SCENE_BOILERPLATE",
    "STORYBOARD_PROMPT",
    "format_storyboard_prompt",
    "format_topic_input",
]

