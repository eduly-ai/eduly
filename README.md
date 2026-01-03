# Eduly

**Anti-brainrot Doom Learning** — Game the brain into educating itself.

🌐 **[landing.eduly.ai](https://landing.eduly.ai)**

![example](examples/deepseek_mhc_renders/deepseek_mhc.gif) 
---

## TL;DR

Eduly is a **Manim Coding Agent** built to break down and explain any content through beautiful, animated visualizations. It transforms complex papers and documents into short-form educational videos in the style of 3Blue1Brown.

**Built with:** [Gemini 2.5](https://deepmind.google/models/gemini/) + [LangChain's Deepagents](https://github.com/langchain-ai/deepagents)

---

## The Problem

Since the rise of short-form content (TikTok, YouTube Shorts, Instagram Reels), "brain-rot" has emerged as the term describing cognitive decline from reliance on content designed for short attention spans. While governments respond with bans, we believe there's a better approach.

**There is no equivalent form of "anti-brain-rot"** — until now.

### Why Existing Tools Fall Short

Current learning tools share common barriers:
- **Paid subscriptions** — $10-20/month discourages students and casual learners
- **Traditional curriculum flow** — Learning styles that haven't evolved in decades
- **Still too long-form** — 10-minute podcasts feel quick, but younger generations seek <1 minute instant gratification

The barrier to entry is simply too high.

## Our Vision

We model the solution like a social media platform. Open Eduly and instantly dive into short, TikTok-style educational content.

### Goals

- **Short-form** (~5 min) explanations of technical concepts through videos and visual explanations
- **Trending research** by monitoring arXiv and conferences, breaking down papers into core concepts that spark curiosity
- **Explicit citations** and links back to longer-form content when something ignites interest

---

## Quickstart

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- LaTeX distribution (for Manim text rendering) — e.g., [MacTeX](https://www.tug.org/mactex/) on macOS
- Google AI API key (Gemini)
- [Manim](https://docs.manim.community/en/stable/installation.html)

### Installation

```bash
# Clone the repository
git clone https://github.com/eduly-ai/eduly.git
cd eduly

# Install dependencies with uv
uv sync

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys:
# GOOGLE_API_KEY=your_gemini_api_key
```

### Basic Usage

```python
import pathlib
import pickle
from google import genai
from eduly import EdulyBreakdownClient, EdulyAnimationClient

# Initialize Gemini client
gemini_client = genai.Client(api_key="your_api_key")

# ═══════════════════════════════════════════════════
# Step 1: Break down a PDF into atomic topics
# ═══════════════════════════════════════════════════
breakdown_client = EdulyBreakdownClient(gemini_client)

breakdown, _ = breakdown_client.breakdown(
    file_path=pathlib.Path("./paper.pdf"),
    model="gemini-2.5-flash-preview",
    thinking_level="high"
)

print(f"Document: {breakdown.document_title}")
for i, topic in enumerate(breakdown.topics):
    print(f"  Topic {i}: {topic.name}")

# ═══════════════════════════════════════════════════
# Step 2: Generate storyboards for each topic
# ═══════════════════════════════════════════════════
storyboards = {}
for topic in breakdown.topics:
    storyboard, _ = breakdown_client.storyboard(
        topic=topic,
        model="gemini-2.5-flash-preview",
        thinking_level="high"
    )
    storyboards[topic.name] = storyboard

# ═══════════════════════════════════════════════════
# Step 3: Animate storyboards with the Manim agent
# ═══════════════════════════════════════════════════
from langchain_google_genai import ChatGoogleGenerativeAI

langchain_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro-preview",
    temperature=1.0,
)

animation_client = EdulyAnimationClient(
    langchain_model=langchain_model,
    agent_workspace_path="./examples/agent_workspace/"
)

# Animate a single topic
result = animation_client.animate_single(
    breakdown=breakdown,
    storyboard=storyboards["Multi-Head Attention"],
    topic_index=3,
    max_iterations=5
)

if result.success:
    print(f"Video saved to: {result.video_path}")
else:
    print(f"Failed: {result.error_message}")
```

See [`examples/processing.ipynb`](examples/processing.ipynb) for a complete walkthrough processing the "Attention Is All You Need" paper.

---

## Architecture

Eduly uses a three-stage pipeline to convert academic papers into animated educational videos:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              EDULY PIPELINE                                     │
└─────────────────────────────────────────────────────────────────────────────────┘

  ┌──────────┐         ┌───────────────┐         ┌────────────────┐
  │          │         │               │         │                │
  │   PDF    │────────▶│   BREAKDOWN   │────────▶│   STORYBOARD   │
  │  INPUT   │         │    AGENT      │         │     AGENT      │
  │          │         │               │         │                │
  └──────────┘         └───────────────┘         └───────┬────────┘
                              │                          │
                              │                          │
                              ▼                          ▼
                       ┌─────────────┐           ┌─────────────┐
                       │  Atomic     │           │  Visual     │
                       │  Topics     │           │  Scenes     │
                       │  (5-15)     │           │  (8-15/     │
                       │             │           │   topic)    │
                       └─────────────┘           └──────┬──────┘
                                                        │
                                                        │
                              ┌──────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                          MANIM CODING AGENT                                     │
│                         (Iterative Refinement)                                  │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │                                                                         │   │
│   │   ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐      │   │
│   │   │          │     │          │     │          │     │          │      │   │
│   │   │  PROMPT  │────▶│  LLM     │────▶│  MANIM   │────▶│ SUCCESS? │      │   │
│   │   │          │     │  AGENT   │     │  RENDER  │     │          │      │   │
│   │   │          │     │          │     │          │     │          │      │   │
│   │   └──────────┘     └────┬─────┘     └──────────┘     └────┬─────┘      │   │
│   │                         │                                  │           │   │
│   │                         │                                  │           │   │
│   │                         │    ┌─────────────────────────────┘           │   │
│   │                         │    │                                         │   │
│   │                         │    │  NO (iteration < max)                   │   │
│   │                         │    │                                         │   │
│   │                         │    ▼                                         │   │
│   │                    ┌────────────────┐                                  │   │
│   │                    │                │                                  │   │
│   │                    │  ERROR         │──────────────────────────────────│───│──┐
│   │                    │  FEEDBACK      │                                  │   │  │
│   │                    │                │◀─────────────────────────────────│───│──┘
│   │                    │                │                                  │   │
│   │                    └────────────────┘                                  │   │
│   │                                                                         │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│   Tools Available:                                                              │
│   • ls / glob / grep - Navigate manim documentation                             │
│   • read_file - Read docs and examples                                          │
│   • edit_file - Modify scene.py                                                 │
│   • write_file - Create new files                                               │
│                                                                                 │
└───────────────────────────────────────────────────────────────────────────┬─────┘
                                                                            │
                                                                            │ YES
                                                                            │
                                                                            ▼
                                                               ┌────────────────────┐
                                                               │                    │
                                                               │   MP4 VIDEO        │
                                                               │   (1080×1920)      │
                                                               │   Vertical Format  │
                                                               │                    │
                                                               └────────────────────┘
```

### Stage 1: Document Breakdown

The `EdulyBreakdownClient` uses Gemini with Google Search to:
- Extract **atomic topics** — self-contained concepts that can stand alone as ~5 minute videos
- Generate comprehensive explanations with modern context (papers can be outdated)
- Identify key takeaways for each topic

**Output:** `Breakdown` object containing 5-15 `AtomicTopic` objects

### Stage 2: Storyboard Generation

For each atomic topic, generate a **visual storyboard** in the style of 3Blue1Brown:
- Define a core **visual metaphor** that makes the concept intuitive
- Create 8-15 **scenes** with detailed visual descriptions
- Write **narration** optimized for text-to-speech (complements visuals, doesn't duplicate)
- Use concrete examples with actual numbers (3×3 matrices, not abstract shapes)

**Output:** `TopicStoryboard` with `Scene` objects containing visual descriptions and narration

### Stage 3: Manim Animation Agent

The `EdulyAnimationClient` powers an **iterative coding agent** that:

1. **Receives** the storyboard prompt with full context
2. **Researches** Manim documentation using file system tools
3. **Generates** a Manim `Scene` class in `scene.py`
4. **Renders** the animation using `manim -ql scene.py`
5. **Iterates** on errors — if rendering fails, the error is fed back to the agent

The agent has access to:
- `manim_docs/` — Full Manim documentation (tutorials, guides, API reference)
- `animation_workspace/` — Working directory for `scene.py` and renders
- File tools: `ls`, `read_file`, `write_file`, `edit_file`, `glob`, `grep`

**Key features:**
- **Vertical video format** (1080×1920) optimized for mobile/TikTok
- **Concept caption bar** at the bottom of every scene
- **Rich, detailed visualizations** — labeled components, real numbers, color-coded elements
- **Up to N retry iterations** with error feedback for self-correction

---

## Workspace Structure

```
agent_workspace/
├── manim_docs/              # Manim documentation (read-only)
│   ├── tutorials/           # Getting started guides
│   ├── guides/              # In-depth how-to guides
│   ├── reference/           # API documentation (385 files)
│   └── reference_index/     # Category indices
├── animation_workspace/     # Working directory
│   ├── scene.py             # Generated Manim code
│   └── media/               # Rendered output
└── rendered_videos/         # Final output (auto-created)
    └── {topic_name}_{index}.mp4
```

---

## Key Models

| Model | Description |
|-------|-------------|
| `Breakdown` | Document breakdown with title, summary, and list of topics |
| `AtomicTopic` | Self-contained topic with name, summary, full explanation, key takeaways |
| `TopicStoryboard` | Visual storyboard with concept and list of scenes |
| `Scene` | Individual scene with type (hook/mid/closing), visual description, narration |
| `AnimationResult` | Result of animation generation (success, video path, iterations, errors) |

---

## Future Work

### 🎙️ Narration & Text-to-Speech

Currently, storyboards generate narration text but don't synthesize audio. Planned features:
- Integration with TTS APIs (ElevenLabs, Google Cloud TTS, OpenAI TTS)
- Automatic audio synchronization with Manim animations
- Voice cloning for consistent narrator voice across series
- Multi-language support via translation + localized TTS

### 📱 Web & Mobile Application

Transform Eduly from a library into a full platform:
- **Mobile-first design** — Vertical video player with swipe navigation
- **Social features** — Like, share, save to collections
- **Personalized feed** — AI-curated content based on interests and skill level
- **Paper submissions** — Users can submit arXiv links for automatic processing
- **Progress tracking** — Track topics learned, suggest next videos
- **Offline mode** — Download videos for learning without connectivity

### 🔬 Research Monitoring

Automated pipeline for new content:
- Monitor arXiv categories (cs.LG, cs.CV, cs.CL, etc.)
- Detect trending papers by citation velocity
- Auto-generate breakdowns and queue for animation
- Push notifications for topics users follow

### 🎬 Multimodal LLM-as-Judge Feedback

Enhance the iterative refinement loop with visual feedback from multimodal models:
- **Video-to-feedback pipeline** — After rendering, pass the MP4 to a vision-language model (Gemini Pro Vision, GPT-4o, Claude) to evaluate the output
- **Storyboard alignment scoring** — LLM compares rendered video against original storyboard descriptions to identify mismatches
- **Visual quality assessment** — Detect issues like overlapping text, elements cut off at edges, poor color contrast, or animations that are too fast/slow
- **Educational clarity scoring** — Evaluate whether the visualization actually teaches the concept effectively
- **Actionable improvement suggestions** — Generate specific, code-level feedback ("The attention matrix at 0:34 should highlight row 2, not row 3")
- **Multi-turn refinement** — Chain multiple judge → fix → render cycles for higher quality output

### 🤖 RL Environment for Manim Coders

Train specialized open-source models to become expert Manim animators:
- **Gymnasium environment** — Define state (storyboard + current code), actions (code edits), and rewards (render success + quality scores)
- **Reward signal composition**:
  - Binary: Does the code render without errors?
  - Alignment: How well does output match storyboard (via LLM-as-Judge)?
  - Aesthetics: Visual quality metrics (layout, timing, readability)
  - Educational: Does it effectively teach the concept?

---

## License

This project is licensed under **CC-BY-NC-SA-4.0** — you're free to share and adapt the work for non-commercial purposes with attribution.

---

## Contributing
Please open an issue to discuss your ideas if you wish to submit a PR! Thanks
