"""
Eduly - Anti-brainrot Doom Learning
"""

from eduly.client import EdulyAnimationClient, EdulyBreakdownClient, EdulyClient
from eduly.models import AnimationResult, AtomicTopic, Breakdown, Scene, TopicStoryboard

__version__ = "0.1.0"

__all__ = [
    "AnimationResult",
    "AtomicTopic",
    "Breakdown",
    "EdulyAnimationClient",
    "EdulyBreakdownClient",
    "EdulyClient",  # Backwards compatibility alias for EdulyBreakdownClient
    "Scene",
    "TopicStoryboard",
]

