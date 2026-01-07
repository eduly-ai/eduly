<p align="center">
  <img src="examples/deepseek_mhc_renders/deepseek_mhc.gif" alt="Eduly Demo" width="300"/>
</p>

<h1 align="center">Eduly</h1>

<p align="center">
  <strong>Transform any content into beautiful animated explanations</strong>
</p>

<p align="center">
  <a href="https://landing.eduly.ai">Website</a> •
  <a href="https://github.com/eduly-ai/eduly">GitHub</a> •
  <a href="https://discord.gg/eduly">Discord</a>
</p>

---

## The Vision

### Learning shouldn't feel like decoding

Every day, students stare at textbooks wondering what the words *really* mean. Researchers wade through papers, trying to visualize abstract concepts in their minds. Educators spend hours creating materials that still fail to click.

**The issue isn't intelligence—it's medium.**

Text is powerful, but it's not always the right tool. Some ideas need to be *seen* to be understood.

Eduly is a **Manim Coding Agent** that transforms any content into stunning, 3Blue1Brown-style animated visualizations. Built with [Gemini 2.5](https://deepmind.google/models/gemini/) and [LangChain](https://github.com/langchain-ai/langchain).

---

## Use Cases

**One tool, many transformations.** Eduly adapts to how you work.

| Who | Input | Output |
|-----|-------|--------|
| 🎓 **Students** | PDF, notes, textbook chapters | Animated explainer videos — study smarter, not harder |
| 🏫 **Educators** | PowerPoint slides | Slides with contextual animations — no more static bullet points |
| 🔬 **Researchers** | Academic papers | Visual concept breakdowns — grasp dense papers quickly, share your work effectively |
| 🎥 **Content Creators** | Script or outline | Production-ready animations — no code required |
| 💼 **Enterprise** | Docs, diagrams, specs | Visual explainers & walkthroughs for training materials teams actually engage with |
| 📖 **Open Source** | Technical documentation | Animated onboarding guides — help contributors understand your architecture faster |

---

## Open Source

### Education should be free

We believe the tools for learning shouldn't be locked behind paywalls. Eduly is open source because **knowledge belongs to everyone**. We're building in public, with the community, for the community.

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

## How It Works

Eduly uses a three-stage pipeline to convert content into animated educational videos:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              EDULY PIPELINE                                     │
└─────────────────────────────────────────────────────────────────────────────────┘

  ┌──────────┐         ┌───────────────┐         ┌────────────────┐
  │          │         │               │         │                │
  │  INPUT   │────────▶│   BREAKDOWN   │────────▶│   STORYBOARD   │
  │  (PDF,   │         │    AGENT      │         │     AGENT      │
  │  slides) │         │               │         │                │
  └──────────┘         └───────────────┘         └───────┬────────┘
                              │                          │
                              ▼                          ▼
                       ┌─────────────┐           ┌─────────────┐
                       │  Atomic     │           │  Visual     │
                       │  Topics     │           │  Scenes     │
                       │  (5-15)     │           │  (8-15/     │
                       │             │           │   topic)    │
                       └─────────────┘           └──────┬──────┘
                                                        │
                              ┌──────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          MANIM CODING AGENT                                     │
│                         (Iterative Refinement)                                  │
│                                                                                 │
│   ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐             │
│   │  PROMPT  │────▶│  LLM     │────▶│  MANIM   │────▶│ SUCCESS? │             │
│   │          │     │  AGENT   │     │  RENDER  │     │          │             │
│   └──────────┘     └────┬─────┘     └──────────┘     └────┬─────┘             │
│                         │                                  │                   │
│                         │         ┌────────────────────────┘                   │
│                         │         │ NO (retry with error feedback)             │
│                         │         ▼                                            │
│                    ┌────────────────┐                                          │
│                    │  ERROR         │◀─────────────────────────────────────────│
│                    │  FEEDBACK      │──────────────────────────────────────────│
│                    └────────────────┘                                          │
│                                                                                 │
│   Tools: ls, glob, grep, read_file, edit_file, write_file                      │
│   Docs:  Full Manim documentation available to agent                           │
└───────────────────────────────────────────────────────────────────────────┬─────┘
                                                                            │ YES
                                                                            ▼
                                                               ┌────────────────────┐
                                                               │   MP4 VIDEO        │
                                                               │   (1080×1920)      │
                                                               │   Mobile-Ready     │
                                                               └────────────────────┘
```

### Stage 1: Document Breakdown

The `EdulyBreakdownClient` uses Gemini with Google Search to:
- Extract **atomic topics** — self-contained concepts that can stand alone as ~5 minute videos
- Generate comprehensive explanations with modern context
- Identify key takeaways for each topic

### Stage 2: Storyboard Generation

For each atomic topic, generate a **visual storyboard** in the style of 3Blue1Brown:
- Define a core **visual metaphor** that makes the concept intuitive
- Create 8-15 **scenes** with detailed visual descriptions
- Write **narration** optimized for text-to-speech
- Use concrete examples with actual numbers

### Stage 3: Manim Animation Agent

The `EdulyAnimationClient` powers an **iterative coding agent** that:
1. Receives the storyboard prompt with full context
2. Researches Manim documentation using file system tools
3. Generates a Manim `Scene` class
4. Renders the animation
5. Iterates on errors — if rendering fails, the error is fed back to the agent

---

## Roadmap

### 🎙️ Narration & Text-to-Speech
- Integration with TTS APIs (ElevenLabs, Google Cloud TTS, OpenAI TTS)
- Automatic audio synchronization with animations
- Multi-language support

### 📱 Web & Mobile Platform
- Mobile-first design with vertical video player
- Personalized feed based on interests
- Paper submissions for automatic processing
- Progress tracking

### 🎬 Multimodal Feedback Loop
- Video-to-feedback pipeline using vision-language models
- Storyboard alignment scoring
- Visual quality assessment
- Educational clarity evaluation

### 🤖 RL Environment for Manim
- Train specialized models to become expert Manim animators
- Reward signals for render success, alignment, aesthetics, and educational value

---

## Contributing

**Help us build the future of learning.**

We're just getting started. Join the mission—contribute code, share ideas, or simply spread the word.

- 🐛 **Found a bug?** [Open an issue](https://github.com/eduly-ai/eduly/issues)
- 💡 **Have an idea?** Start a [discussion](https://github.com/eduly-ai/eduly/discussions)
- 🔧 **Want to contribute?** Check out our [contributing guide](CONTRIBUTING.md)
- 💬 **Join the community:** [Discord](https://discord.gg/eduly)

---

## License

This project is licensed under **CC-BY-NC-SA-4.0** — free to share and adapt for non-commercial purposes with attribution.

---

<p align="center">
  <strong>Knowledge belongs to everyone.</strong>
</p>
