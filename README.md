# Eduly

**Anti-brainrot Doom Learning** — Game the brain into educating itself.

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

- **Ultra short-form** (<1 min) explanations of technical concepts through videos and visual explanations
- **Trending research** by monitoring arXiv and conferences, breaking down papers into core concepts that spark curiosity
- **Explicit citations** and links back to longer-form content when something ignites interest

## Current Implementation

Eduly is in early development (v0.1.0). The current focus is building the **content breakdown pipeline** — the foundation for generating short-form educational videos from academic papers and documents.

### Features

#### Document Breakdown

The core feature breaks down PDF documents (especially research papers) into **atomic topics** — self-contained knowledge units designed for ~60 second video explanations.

Each atomic topic contains:
- **Name** — Clear, engaging heading
- **Summary** — 2-3 sentence hook for video introduction
- **Full explanation** — Self-contained markdown content with all necessary context
- **Key takeaways** — 2-4 bullet points of the most important concepts

The breakdown uses Google's Gemini models with:
- Structured JSON output via Pydantic models
- Google Search integration to add modern context (papers get outdated quickly!)
- Configurable thinking levels for more nuanced analysis

#### Storyboard Generation

Transform atomic topics into **visual screenplays** — filmmaker-style scripts with exhaustively detailed animation descriptions. Each storyboard contains scenes that tell a complete visual narrative.

Each storyboard scene contains:
- **Scene type** — `hook` (attention grabber), `mid` (core content), or `closing` (summary)
- **Title** — An evocative name for the scene
- **Visual description** — A filmmaker's screenplay describing exactly what appears on screen, frame by frame

### Installation

```bash
pip install eduly
```

Or with uv:

```bash
uv add eduly
```

### Requirements

- Python 3.12+
- Google Gemini API key
- `brew install cairo pkg-config ffmpeg`
- LaTeX (https://www.tug.org/mactex/)
- build manim_llm.txt with `sphinx-build -t skip-manim -b html docs/source docs/build/html`

### Quick Start

```python
from eduly import EdulyClient

# Initialize with your Gemini API key
client = EdulyClient(api_key="your-gemini-api-key")

# Break down a PDF into atomic topics
breakdown, raw_response = client.breakdown("path/to/paper.pdf")

# Access the structured content
print(breakdown.document_title)
print(breakdown.document_summary)

for topic in breakdown.topics:
    print(f"📚 {topic.name}")
    print(f"   {topic.summary}")
    print(f"   Key takeaways: {topic.key_takeaways}")

# Generate a storyboard for a specific topic
storyboard, raw_storyboard_response = client.storyboard(topic=breakdown.topics[0])

# Access storyboard scenes
print(f"Visual Concept: {storyboard.visual_concept}")
for scene in storyboard.scenes:
    print(f"[{scene.scene_type}] {scene.title}")
    print(f"{scene.visual_description[:200]}...")
```

### Example Output

Running the breakdown on the ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762) paper produces:

```python
>>> breakdown.document_title
'Attention Is All You Need'

>>> breakdown.document_summary
'This seminal 2017 paper introduced the Transformer, a novel neural network architecture for sequence transduction that relies entirely on self-attention mechanisms, completely discarding recurrent and convolutional layers. By allowing for significantly more parallelization and modeling global dependencies regardless of distance, the Transformer achieved new state-of-the-art results in machine translation while being much faster to train'

>>> for topic in breakdown.topics:
...     print(f"📚 {topic.name}")
...     print(f"   {topic.summary}\n")

📚 The Shift from Recurrence to Attention
   Before the Transformer, sequence modeling relied on complex Recurrent Neural 
   Networks (RNNs) that processed data step-by-step. The Transformer changed 
   everything by using 'attention' to process entire sequences at once, removing 
   the sequential bottleneck.

📚 Scaled Dot-Product Attention
   At the heart of the Transformer is a mechanism called Scaled Dot-Product 
   Attention, which calculates how much 'focus' one word should place on others 
   in a sentence.

📚 Multi-Head Attention
   Rather than looking at a sentence in just one way, Multi-Head Attention allows 
   the model to simultaneously track different types of relationships between words.

📚 Positional Encoding: Adding Spatial Awareness
   Because Transformers process all words at once, they have no inherent sense of 
   word order. Positional Encoding 'injects' this missing information using 
   mathematical waves.

📚 The Encoder-Decoder Architecture
   The Transformer uses a two-part structure: the Encoder to understand the input 
   and the Decoder to generate the output, one token at a time.

📚 Efficiency and Complexity: Why Transformers Won
   Transformers are faster than RNNs not just because of hardware, but because 
   their mathematical structure allows them to connect distant words in a single step.
```

#### Each topic also includes a `full_explanation` with detailed markdown content and `key_takeaways` as a list of bullet points.

> #### Scaled Dot-Product Attention
> The core mathematical operation of the Transformer is **Scaled Dot-Product Attention**. It operates on three vectors: **Queries (Q)**, **Keys (K)**, and **Values (V)**. The query represents the word we are currently looking at, keys represent all words in the sequence that we are comparing against, and values contain the actual information of those words. The attention is calculated using the formula: $\text{Attention}(Q, K, V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V$. The dot product of $Q$ and $K$ determines the compatibility (or 'attention weight') between words. We divide by $\sqrt{d_k}$ (the dimension of the keys) to prevent the dot product from growing too large, which would push the **softmax** function into regions with tiny gradients. **Modern Context:** This specific scaling factor is crucial for stable training in large models. Today, variations like **FlashAttention** have been developed to make this calculation even faster on modern GPU hardware without changing the underlying math.

#### Storyboard Generation

Once you have atomic topics from the breakdown, you can generate **visual screenplays** — filmmaker-style scripts with exhaustively detailed scene descriptions designed for animation.

```python
>>> storyboard, _ = client.storyboard(topic=breakdown.topics[1])
>>> print(storyboard.topic_name)
'Scaled Dot-Product Attention: The Core Mechanism'

>>> print(storyboard.visual_concept)
'The attention mechanism is visualized as a spotlight operator in a theater...'

>>> for scene in storyboard.scenes:
...     print(f"[{scene.scene_type}] {scene.title}")
...     print(f"{scene.visual_description[:100]}...\n")

[hook] The Ambiguity Problem
SCENE OPENS on a dark charcoal background. The sentence 'The chef cooked the...

[mid] The Three Vectors
The sentence fades to 20% opacity and shifts upward. Three distinct shapes m...

[mid] The Dot Product Dance
The Q block (electric blue) and K block (amber) detach from the row and move...

[mid] The Softmax Redistribution
Five vertical bars appear, arranged horizontally across the center. Each bar...

[closing] The Complete Formula
All visual elements fade. The complete attention equation materializes in th...
```

Each scene includes:
- **scene_type** — `hook`, `mid`, or `closing` to structure the visual narrative
- **title** — An evocative name for the scene
- **visual_description** — A filmmaker's screenplay describing exactly what appears on screen

#### Manim Animation Generation (Work in Progress)

The final step transforms storyboards into actual **animated videos** using [Manim](https://www.manim.community/) — the mathematical animation library made famous by 3Blue1Brown.

##### The Challenge with LLM-Generated Animation Code

LLMs are trained on older versions of libraries, and Manim's API evolves frequently. Asking an LLM to "write Manim code" often produces:
- Deprecated method calls
- Incorrect parameter names
- Non-existent classes from older API versions
- Code that simply doesn't compile

##### Our Solution: Custom Coding Agents with Live Documentation

Instead of relying on stale training data, we built a **custom coding agent** that has access to up-to-date Manim documentation at runtime. The agent:

1. **Researches before coding** — Always looks up the exact API signatures, parameters, and examples from the docs before writing any code
2. **Has a complete documentation workspace** — Markdown files covering tutorials, guides, and full API reference
3. **Uses file system tools** — Can `ls`, `read_file`, `grep`, `glob`, and `edit_file` to explore docs and write code
4. **Iterates on errors** — When rendering fails, it reads the error output and fixes the code

The agent workspace contains:
- `manim_docs/` — Complete Manim documentation (tutorials, guides, 385 API reference files)
- `workspace/` — Where the agent writes and iterates on `scene.py`

##### Example Output


## Roadmap

- [x] Storyboard creation from atomic topics
- [x] Manim coding agent with live documentation access
- [ ] Video QA feedback loop (LLM watches video, suggests fixes)
- [ ] Content delivery platform (Vertical scrolling feed Web/iOS/Android)
- [ ] Citation graph and "continue learning" recommendations
- [ ] arXiv monitoring and automatic trending paper analysis
- [ ] Longer Term - Personalisation. (Ranking, Quiz, Reccomendations)
- [ ] Expand to more content types : Younger students (GCSE, A-Level)

## License

AGPL-3.0
