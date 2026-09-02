<div align="center">

# Awesome LLM Bench

Top 10 of the most reliable LLM leaderboards, auto-synced daily.

[![Sync](https://github.com/leoncuhk/awesome-llm-bench/actions/workflows/sync.yml/badge.svg)](https://github.com/leoncuhk/awesome-llm-bench/actions/workflows/sync.yml)
[![License](https://img.shields.io/badge/license-MIT-000.svg)](LICENSE)
[![中文](https://img.shields.io/badge/lang-中文-000.svg)](README.zh-CN.md)

<!-- LAST_SYNC -->Last sync: **2026-09-02** (UTC, daily auto-update)<!-- /LAST_SYNC -->

</div>

<br>

> **Data source:** [benchlm.ai](https://benchlm.ai). For the full leaderboards (43+ models per benchmark), pricing dashboards, and methodology, please visit the canonical site. This repository is a Top-10 mirror with attribution, not a replacement.

<br>

## About

The LLM evaluation landscape is noisy. LMArena measures preference, not capability; vendor-published numbers are cherry-picked; most aggregators lag months behind frontier model releases. [benchlm.ai](https://benchlm.ai) is the most honest, frequently-updated aggregator I have found. This repository distills the **Top 10** of each high-signal benchmark for fast scanning, paired with a curated AI coding-tools landscape that benchlm.ai does not cover.

<br>

---

## Contents

**Coding** — [SWE-bench Verified](#swe-bench-verified) · [LiveCodeBench](#livecodebench)  
**Agentic** — [Terminal-Bench 2.0](#terminal-bench-20) · [OSWorld-Verified](#osworld-verified) · [BrowseComp](#browsecomp)  
**Reasoning** — [ARC-AGI-2](#arc-agi-2)  
**Knowledge** — [Humanity's Last Exam](#humanitys-last-exam)  
**Tools** — [AI Coding Tools Landscape](#ai-coding-tools-landscape)  
**Reference** — [How to read](#how-to-read-these-numbers) · [Caveats](#caveats) · [Attribution](#data-source-and-attribution)

<br>

---

## Coding

### SWE-bench Verified

Real GitHub issues from popular Python repositories (Django, Flask, scikit-learn). Human-verified subset of SWE-bench. The gold standard for AI coding agents.

<!-- AUTO:START slug=sweVerified lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Claude Opus 5](https://benchlm.ai/models/claude-opus-5) | Anthropic | Closed | 96.0% |
| 2 | [Claude Mythos 5](https://benchlm.ai/models/claude-mythos-5) | Anthropic | Closed | 95.5% |
| 3 | [Claude Fable 5](https://benchlm.ai/models/claude-fable) | Anthropic | Closed | 95.0% |
| 4 | [Claude Opus 4.8](https://benchlm.ai/models/claude-opus-4-8) | Anthropic | Closed | 88.6% |
| 5 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 87.6% |
| 6 | [Ornith-1.5-397B](https://benchlm.ai/models/ornith-1-5-397b) | Ornith AI | Open | 86.0% |
| 7 | [Claude Sonnet 5](https://benchlm.ai/models/claude-sonnet-5) | Anthropic | Closed | 85.2% |
| 8 | [GPT-5.3 Codex](https://benchlm.ai/models/gpt-5-3-codex) | OpenAI | Closed | 85.0% |
| 9 | [Ornith-1.0-397B](https://benchlm.ai/models/ornith-1-0-397b) | DeepReinforce AI | Open | 82.4% |
| 10 | [Claude Opus 4.5](https://benchlm.ai/models/claude-opus-4-5) | Anthropic | Closed | 80.9% |

*Source: [https://benchlm.ai/benchmarks/sweVerified](https://benchlm.ai/benchmarks/sweVerified) · Updated 2026-09-01 · Total models: 69*
<!-- AUTO:END slug=sweVerified -->

### LiveCodeBench

Contamination-free code generation. Fresh problems are sampled continuously, mitigating training-data leakage.

<!-- AUTO:START slug=liveCodeBench lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Qwen3.7 Max](https://benchlm.ai/models/qwen3-7-max) | Alibaba | Closed | 91.6% |
| 2 | [Qwen3.7 Plus](https://benchlm.ai/models/qwen3-7-plus) | Alibaba | Closed | 89.6% |
| 3 | [GLM-4.7](https://benchlm.ai/models/glm-4-7) | Z.AI | Open | 84.9% |
| 4 | [Qwen3.6-27B](https://benchlm.ai/models/qwen3-6-27b) | Alibaba | Open | 83.9% |
| 5 | [Qwen3.6-35B-A3B](https://benchlm.ai/models/qwen3-6-35b-a3b) | Alibaba | Open | 80.4% |
| 6 | [Mercury 2](https://benchlm.ai/models/mercury-2) | Inception | Closed | 67.3% |
| 7 | [DeepSeek V3](https://benchlm.ai/models/deepseek-v3) | DeepSeek | Open | 37.6% |

*Source: [https://benchlm.ai/benchmarks/liveCodeBench](https://benchlm.ai/benchmarks/liveCodeBench) · Updated 2026-09-01 · Total models: 7*
<!-- AUTO:END slug=liveCodeBench -->

<br>

---

## Agentic

### Terminal-Bench 2.0

Multi-step terminal and CLI workflows. Models inspect files, run commands, edit code, and recover from errors over interactive sessions.

<!-- AUTO:START slug=terminalBench2 lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [GPT-5.6 Sol](https://benchlm.ai/models/gpt-5-6-sol) | OpenAI | Closed | 91.9% |
| 2 | [Claude Mythos 5](https://benchlm.ai/models/claude-mythos-5) | Anthropic | Closed | 88.0% |
| 3 | [GPT-5.6 Terra](https://benchlm.ai/models/gpt-5-6-terra) | OpenAI | Closed | 87.4% |
| 4 | [GPT-5.6 Luna](https://benchlm.ai/models/gpt-5-6-luna) | OpenAI | Closed | 84.7% |
| 5 | [Claude Fable 5](https://benchlm.ai/models/claude-fable) | Anthropic | Closed | 84.3% |
| 6 | [Grok 4.5](https://benchlm.ai/models/grok-4-5) | xAI | Closed | 83.3% |
| 7 | [Sakana Fugu-Ultra](https://benchlm.ai/models/sakana-fugu-ultra) | Sakana AI | Closed | 82.1% |
| 8 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 82.0% |
| 9 | [SWE-1.7](https://benchlm.ai/models/swe-1-7) | Cognition | Closed | 81.5% |
| 10 | [GLM-5.2](https://benchlm.ai/models/glm-5-2) | Z.AI | Open | 81.0% |

*Source: [https://benchlm.ai/benchmarks/terminalBench2](https://benchlm.ai/benchmarks/terminalBench2) · Updated 2026-09-01 · Total models: 48*
<!-- AUTO:END slug=terminalBench2 -->

### OSWorld-Verified

Computer-use tasks in desktop GUIs. Navigation, editing, and complex multi-step workflows.

<!-- AUTO:START slug=osWorldVerified lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Qwen3.8 Max](https://benchlm.ai/models/qwen3-8-max) | Alibaba | Open | 86.1% |
| 2 | [Claude Fable 5](https://benchlm.ai/models/claude-fable) | Anthropic | Closed | 85.0% |
| 3 | [Claude Mythos 5](https://benchlm.ai/models/claude-mythos-5) | Anthropic | Closed | 85.0% |
| 4 | [Qwen3.8-27B](https://benchlm.ai/models/qwen3-8-27b) | Alibaba | Open | 84.3% |
| 5 | [Claude Opus 4.8](https://benchlm.ai/models/claude-opus-4-8) | Anthropic | Closed | 83.4% |
| 6 | [Gemini 3.6 Flash](https://benchlm.ai/models/gemini-3-6-flash) | Google | Closed | 83.0% |
| 7 | [Holo3-35B-A3B](https://benchlm.ai/models/holo3-35b-a3b) | H Company | Open | 82.6% |
| 8 | [Claude Sonnet 5](https://benchlm.ai/models/claude-sonnet-5) | Anthropic | Closed | 81.2% |
| 9 | [Muse Spark 1.1](https://benchlm.ai/models/muse-spark-1-1) | Meta | Closed | 80.8% |
| 10 | [Holo3-122B-A10B](https://benchlm.ai/models/holo3-122b-a10b) | H Company | Closed | 78.8% |

*Source: [https://benchlm.ai/benchmarks/osWorldVerified](https://benchlm.ai/benchmarks/osWorldVerified) · Updated 2026-09-01 · Total models: 30*
<!-- AUTO:END slug=osWorldVerified -->

### BrowseComp

Web-research agents. Models search, inspect sources, gather evidence, and return correct answers to research-oriented questions.

<!-- AUTO:START slug=browseComp lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [GPT-5.6 Sol](https://benchlm.ai/models/gpt-5-6-sol) | OpenAI | Closed | 92.2% |
| 2 | [Kimi K3](https://benchlm.ai/models/kimi-k3) | Moonshot AI | Pending | 91.2% |
| 3 | [Claude Opus 5](https://benchlm.ai/models/claude-opus-5) | Anthropic | Closed | 90.8% |
| 4 | [GPT-5.5 Pro](https://benchlm.ai/models/gpt-5-5-pro) | OpenAI | Closed | 90.1% |
| 5 | [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) | OpenAI | Closed | 89.3% |
| 6 | [Claude Mythos 5](https://benchlm.ai/models/claude-mythos-5) | Anthropic | Closed | 88.0% |
| 7 | [GPT-5.6 Terra](https://benchlm.ai/models/gpt-5-6-terra) | OpenAI | Closed | 87.5% |
| 8 | [Ornith-1.5-397B](https://benchlm.ai/models/ornith-1-5-397b) | Ornith AI | Open | 86.6% |
| 9 | [Claude Sonnet 5](https://benchlm.ai/models/claude-sonnet-5) | Anthropic | Closed | 84.7% |
| 10 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 84.4% |

*Source: [https://benchlm.ai/benchmarks/browseComp](https://benchlm.ai/benchmarks/browseComp) · Updated 2026-09-01 · Total models: 40*
<!-- AUTO:END slug=browseComp -->

<br>

---

## Reasoning

### ARC-AGI-2

Abstraction and reasoning grid puzzles. A frontier general-intelligence test where humans solve nearly all tasks but models struggle.

<!-- AUTO:START slug=arcAgi2 lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [GPT-5.6 Sol](https://benchlm.ai/models/gpt-5-6-sol) | OpenAI | Closed | 92.5% |
| 2 | [Claude Opus 5](https://benchlm.ai/models/claude-opus-5) | Anthropic | Closed | 90.4% |
| 3 | [Claude Fable 5.1](https://benchlm.ai/models/claude-fable-5-1) | Anthropic | Closed | 90.0% |
| 4 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 85.0% |
| 5 | [GPT-5.6 Terra](https://benchlm.ai/models/gpt-5-6-terra) | OpenAI | Closed | 83.9% |
| 6 | [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) | OpenAI | Closed | 83.3% |
| 7 | [dots3-note Preview](https://benchlm.ai/models/dots3-note-preview) | Dots Studio | Open | 81.4% |
| 8 | [Gemini 3.1 Pro](https://benchlm.ai/models/gemini-3-1-pro) | Google | Closed | 77.1% |
| 9 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 75.8% |
| 10 | [GPT-5.4](https://benchlm.ai/models/gpt-5-4) | OpenAI | Closed | 74.0% |

*Source: [https://benchlm.ai/benchmarks/arcAgi2](https://benchlm.ai/benchmarks/arcAgi2) · Updated 2026-09-01 · Total models: 22*
<!-- AUTO:END slug=arcAgi2 -->

<br>

---

## Knowledge

### Humanity's Last Exam

Expert-level questions across all academic domains. Designed to be hard for frontier models.

<!-- AUTO:START slug=hle lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Claude Fable 5.1](https://benchlm.ai/models/claude-fable-5-1) | Anthropic | Closed | 65.0% |
| 2 | [Claude Opus 5](https://benchlm.ai/models/claude-opus-5) | Anthropic | Closed | 64.7% |
| 3 | [Claude Mythos 5](https://benchlm.ai/models/claude-mythos-5) | Anthropic | Closed | 64.5% |
| 4 | [Muse Spark 1.1](https://benchlm.ai/models/muse-spark-1-1) | Meta | Closed | 62.1% |
| 5 | [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) | OpenAI | Closed | 58.7% |
| 6 | [Claude Opus 4.8](https://benchlm.ai/models/claude-opus-4-8) | Anthropic | Closed | 57.9% |
| 7 | [Claude Sonnet 5](https://benchlm.ai/models/claude-sonnet-5) | Anthropic | Closed | 57.4% |
| 8 | [GPT-5.5 Pro](https://benchlm.ai/models/gpt-5-5-pro) | OpenAI | Closed | 57.2% |
| 9 | [Apodex 1.1](https://benchlm.ai/models/apodex-1-1) | Apodex | Closed | 56.1% |
| 10 | [Kimi K3](https://benchlm.ai/models/kimi-k3) | Moonshot AI | Pending | 56.0% |

*Source: [https://benchlm.ai/benchmarks/hle](https://benchlm.ai/benchmarks/hle) · Updated 2026-09-01 · Total models: 57*
<!-- AUTO:END slug=hle -->

<br>

---

## AI Coding Tools Landscape

The tools practitioners actually ship code with. Selection bar is high — only tools with verifiable adoption and active maintenance. Full table with criteria, pricing, and update cadence: [tools/ai-coding-tools.md](tools/ai-coding-tools.md).

#### CLI agents

| Tool | Provider | Distinguishing capability |
| :-- | :-- | :-- |
| [Claude Code](https://www.anthropic.com/claude-code) | Anthropic | Sub-agents, hooks, MCP, slash commands, skills |
| [Codex CLI](https://github.com/openai/codex) | OpenAI | Official agent CLI with sandboxed execution |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Google | Native Search grounding, generous free tier |
| [Aider](https://aider.chat) | Open source | Git-native diffs, repo-map, model-agnostic |

#### IDE-native

| Tool | Provider | Distinguishing capability |
| :-- | :-- | :-- |
| [Cursor](https://cursor.com) | Anysphere | Composer multi-file edit, fastest Tab completion |
| [Windsurf](https://windsurf.com) | Codeium / OpenAI | Cascade flow, supercomplete |
| [Zed AI](https://zed.dev) | Zed Industries | Built into the fastest editor (Rust) |
| [GitHub Copilot](https://github.com/features/copilot) | GitHub | Largest deployment, broadest IDE coverage |

#### VS Code extensions (open source, BYOK)

| Tool | Provider | Distinguishing capability |
| :-- | :-- | :-- |
| [Cline](https://cline.bot) | Open source | Plan/Act modes, MCP, browser use |
| [Roo Code](https://roocode.com) | Open source | Cline fork with custom agent modes |
| [Continue](https://continue.dev) | Open source | Customizable assistants and slash commands |

#### Cloud agents and codebase Q&A

| Tool | Provider | Distinguishing capability |
| :-- | :-- | :-- |
| [Devin](https://devin.ai) | Cognition | Long-running autonomous SWE agent |
| [Replit Agent](https://replit.com/ai) | Replit | End-to-end app generation in browser |
| [Sourcegraph Cody](https://sourcegraph.com/cody) | Sourcegraph | Code-graph context, repo-scale awareness |

<br>

---

## How to read these numbers

- **Do not compare across benchmarks.** Different scales, different ceilings.
- **Look at the spread.** Top 10 within 2–3 points means saturation; differences are noise. A 10+ point lead means the leader is genuinely ahead.
- **Check the date.** Each table links back to the source page; benchmarks refresh asynchronously.
- **For your own use case, run your own evaluation.** Public benchmarks measure averages on someone else's tasks.

## Caveats

- benchlm.ai is also an aggregator with judgment calls (category weights, inclusion criteria). I mirror their judgment because it is the best I have found, not because it is objective truth.
- Benchmark contamination is real and growing. Treat any single benchmark with skepticism — consensus across multiple is the signal.
- Model identity drift: vendors silently update models behind the same name. Scores from different dates are not strictly comparable.

## Data source and attribution

All leaderboard data is mirrored from [benchlm.ai](https://benchlm.ai) with full attribution. Each table links back to the canonical page. Excluded by design: benchmarks tagged "Display only" on benchlm.ai itself (GAIA, BFCL v4, FrontierMath, …) — they have incomplete public snapshots and including them would mislead.

For full leaderboards, pricing, methodology, dashboards, and category weights, please visit [benchlm.ai](https://benchlm.ai).

<br>

---

## Update cadence

A GitHub Actions workflow runs daily at 02:00 UTC, fetches the source pages, parses the leaderboard, and commits to `data/` and the README sections only when something has changed. The commit message names what changed. See [`.github/workflows/sync.yml`](.github/workflows/sync.yml).

## Contributing

PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Add a benchmark by editing `scripts/benchmarks.yaml`; add a tool by editing `tools/ai-coding-tools.md`. Keep the bar high: only `Current` or `Refreshing` benchmarks on benchlm.ai, only tools with real adoption.

## Related

- [benchlm.ai](https://benchlm.ai) — canonical source
- [Awesome Quant AI](https://github.com/leoncuhk/awesome-quant-ai) — sister list
- [Artificial Analysis](https://artificialanalysis.ai/) — alternative aggregator (price/perf focus)
- [LMArena](https://lmarena.ai/) — pairwise human preference

## License

[MIT](LICENSE) for the curation, code, and original commentary. Leaderboard data is mirrored from benchlm.ai — see their terms for data use.

<br>

<div align="center">
<sub>Maintained by <a href="https://github.com/leoncuhk">@leoncuhk</a> · Sister project: <a href="https://github.com/leoncuhk/awesome-quant-ai">awesome-quant-ai</a></sub>
</div>
