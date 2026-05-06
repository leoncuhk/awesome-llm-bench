<div align="center">

# Awesome LLM Bench

最靠谱 LLM 排行榜的 Top 10 镜像,每日自动同步。

[![Sync](https://github.com/leoncuhk/awesome-llm-bench/actions/workflows/sync.yml/badge.svg)](https://github.com/leoncuhk/awesome-llm-bench/actions/workflows/sync.yml)
[![License](https://img.shields.io/badge/license-MIT-000.svg)](LICENSE)
[![English](https://img.shields.io/badge/lang-English-000.svg)](README.md)

<!-- LAST_SYNC -->最近同步: **2026-05-06** (UTC,每日自动更新)<!-- /LAST_SYNC -->

</div>

<br>

> **数据来源:** [benchlm.ai](https://benchlm.ai)。完整榜单(每榜 43+ 模型)、价格仪表盘与方法论请访问其官网。本仓库是带 attribution 的 Top-10 镜像,不是替代品。

<br>

## 关于

LLM 评测领域噪音极大: LMArena 测的是用户偏好而非能力,厂商自报数字挑樱桃,多数聚合站滞后前沿模型几个月。[benchlm.ai](https://benchlm.ai) 是我目前找到最诚实、更新最及时的聚合站。本仓库蒸馏每个高信号 benchmark 的 **Top 10**,便于快速扫视,再配上他们不覆盖的 AI 编码工具全景。

<br>

---

## 目录

**Coding** — [SWE-bench Verified](#swe-bench-verified) · [LiveCodeBench](#livecodebench)  
**Agentic** — [Terminal-Bench 2.0](#terminal-bench-20) · [OSWorld-Verified](#osworld-verified) · [BrowseComp](#browsecomp)  
**Reasoning** — [ARC-AGI-2](#arc-agi-2)  
**Knowledge** — [Humanity's Last Exam](#humanitys-last-exam)  
**Tools** — [AI 编码工具全景](#ai-编码工具全景)  
**参考** — [如何看这些数字](#如何看这些数字) · [局限](#局限) · [归属](#数据来源与归属)

<br>

---

## Coding

### SWE-bench Verified

真实 GitHub issue 修复任务,来自 Django、Flask、scikit-learn 等热门 Python 仓库,人工核验子集。AI 编码 agent 的黄金标准。

<!-- AUTO:START slug=sweVerified lang=zh -->
| 排名 | 模型 | 提供商 | 开闭源 | 分数 |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Claude Mythos Preview](https://benchlm.ai/models/claude-mythos-preview) | Anthropic | Closed | 93.9% |
| 2 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-max) | Anthropic | Closed | 87.6% |
| 3 | [GPT-5.3 Codex](https://benchlm.ai/models/gpt-5-3-codex) | OpenAI | Closed | 85.0% |
| 4 | [Claude Opus 4.5](https://benchlm.ai/models/claude-opus-4-5) | Anthropic | Closed | 80.9% |
| 5 | [Claude Opus 4.6](https://benchlm.ai/models/claude-opus-4-6) | Anthropic | Closed | 80.8% |
| 6 | [DeepSeek V4 Pro (Max)](https://benchlm.ai/models/deepseek-v4-pro-max) | DeepSeek | Open | 80.6% |
| 7 | [Kimi K2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 80.2% |
| 8 | [GPT-5.2](https://benchlm.ai/models/gpt-5-2) | OpenAI | Closed | 80.0% |
| 9 | [Claude Sonnet 4.6](https://benchlm.ai/models/claude-sonnet-4-6) | Anthropic | Closed | 79.6% |
| 10 | [DeepSeek V4 Pro (High)](https://benchlm.ai/models/deepseek-v4-pro-high) | DeepSeek | Open | 79.4% |

*来源: [https://benchlm.ai/benchmarks/sweVerified](https://benchlm.ai/benchmarks/sweVerified) · 更新于 2026-05-05 · 共 44 个模型*
<!-- AUTO:END slug=sweVerified -->

### LiveCodeBench

防污染代码生成。持续采样新题目,缓解训练数据泄漏。

<!-- AUTO:START slug=liveCodeBench lang=zh -->
| 排名 | 模型 | 提供商 | 开闭源 | 分数 |
| :-: | :-- | :-- | :-: | --: |
| 1 | [DeepSeek V4 Pro (Max)](https://benchlm.ai/models/deepseek-v4-pro-max) | DeepSeek | Open | 93.5% |
| 2 | [DeepSeek V4 Flash (Max)](https://benchlm.ai/models/deepseek-v4-flash-max) | DeepSeek | Open | 91.6% |
| 3 | [DeepSeek V4 Pro (High)](https://benchlm.ai/models/deepseek-v4-pro-high) | DeepSeek | Open | 89.8% |
| 4 | [Kimi K2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 89.6% |
| 5 | [DeepSeek V4 Flash (High)](https://benchlm.ai/models/deepseek-v4-flash-high) | DeepSeek | Open | 88.4% |
| 6 | [Kimi K2.5](https://benchlm.ai/models/kimi-k2-5) | Moonshot AI | Open | 85.0% |
| 7 | [GLM-4.7](https://benchlm.ai/models/glm-4-7) | Z.AI | Open | 84.9% |
| 8 | [Qwen3.6-27B](https://benchlm.ai/models/qwen3-6-27b) | Alibaba | Open | 83.9% |
| 9 | [Qwen3.6-35B-A3B](https://benchlm.ai/models/qwen3-6-35b-a3b) | Alibaba | Open | 80.4% |
| 10 | [Nemotron 3 Nano Omni 30B A3B](https://benchlm.ai/models/nemotron-3-nano-omni-30b-a3b) | NVIDIA | Open | 63.2% |

*来源: [https://benchlm.ai/benchmarks/liveCodeBench](https://benchlm.ai/benchmarks/liveCodeBench) · 更新于 2026-05-05 · 共 13 个模型*
<!-- AUTO:END slug=liveCodeBench -->

<br>

---

## Agentic

### Terminal-Bench 2.0

多步终端与 CLI 工作流。模型需要在交互会话中检查文件、执行命令、编辑代码、从错误中恢复。

<!-- AUTO:START slug=terminalBench2 lang=zh -->
| 排名 | 模型 | 提供商 | 开闭源 | 分数 |
| :-: | :-- | :-- | :-: | --: |
| 1 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 82.0% |
| 2 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-max) | Anthropic | Closed | 69.4% |
| 3 | [MiMo-V2.5-Pro](https://benchlm.ai/models/mimo-v2-5-pro) | Xiaomi | Closed | 68.4% |
| 4 | [DeepSeek V4 Pro (Max)](https://benchlm.ai/models/deepseek-v4-pro-max) | DeepSeek | Open | 67.9% |
| 5 | [Kimi K2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 66.7% |
| 6 | [MiMo-V2.5](https://benchlm.ai/models/mimo-v2-5) | Xiaomi | Closed | 65.8% |
| 7 | [Qwen 3.6 Max (preview)](https://benchlm.ai/models/qwen3-6-max-preview) | Alibaba | Closed | 65.4% |
| 8 | [DeepSeek V4 Pro (High)](https://benchlm.ai/models/deepseek-v4-pro-high) | DeepSeek | Open | 63.3% |
| 9 | [Composer 2](https://benchlm.ai/models/composer-2) | Cursor | Closed | 61.7% |
| 10 | [Qwen3.6-27B](https://benchlm.ai/models/qwen3-6-27b) | Alibaba | Open | 59.3% |

*来源: [https://benchlm.ai/benchmarks/terminalBench2](https://benchlm.ai/benchmarks/terminalBench2) · 更新于 2026-05-05 · 共 17 个模型*
<!-- AUTO:END slug=terminalBench2 -->

### OSWorld-Verified

桌面 GUI 计算机使用任务。导航、编辑、复杂多步工作流。

<!-- AUTO:START slug=osWorldVerified lang=zh -->
| 排名 | 模型 | 提供商 | 开闭源 | 分数 |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Holo3-35B-A3B](https://benchlm.ai/models/holo3-35b-a3b) | H Company | Open | 82.6% |
| 2 | [Claude Mythos Preview](https://benchlm.ai/models/claude-mythos-preview) | Anthropic | Closed | 79.6% |
| 3 | [Holo3-122B-A10B](https://benchlm.ai/models/holo3-122b-a10b) | H Company | Closed | 78.8% |
| 4 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 78.7% |
| 5 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-max) | Anthropic | Closed | 78.0% |
| 6 | [GPT-5.4](https://benchlm.ai/models/gpt-5-4) | OpenAI | Closed | 75.0% |
| 7 | [Kimi K2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 73.1% |
| 8 | [Claude Opus 4.6](https://benchlm.ai/models/claude-opus-4-6) | Anthropic | Closed | 72.7% |
| 9 | [Claude Sonnet 4.6](https://benchlm.ai/models/claude-sonnet-4-6) | Anthropic | Closed | 72.1% |
| 10 | [GPT-5.4 mini](https://benchlm.ai/models/gpt-5-4-mini) | OpenAI | Closed | 72.1% |

*来源: [https://benchlm.ai/benchmarks/osWorldVerified](https://benchlm.ai/benchmarks/osWorldVerified) · 更新于 2026-05-05 · 共 18 个模型*
<!-- AUTO:END slug=osWorldVerified -->

### BrowseComp

Web 研究 agent。模型需要搜索、查证、收集证据,并对研究型问题给出准确答案。

<!-- AUTO:START slug=browseComp lang=zh -->
| 排名 | 模型 | 提供商 | 开闭源 | 分数 |
| :-: | :-- | :-- | :-: | --: |
| 1 | [GPT-5.5 Pro](https://benchlm.ai/models/gpt-5-5-pro) | OpenAI | Closed | 90.1% |
| 2 | [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) | OpenAI | Closed | 89.3% |
| 3 | [Claude Mythos Preview](https://benchlm.ai/models/claude-mythos-preview) | Anthropic | Closed | 86.9% |
| 4 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 84.4% |
| 5 | [Claude Opus 4.6](https://benchlm.ai/models/claude-opus-4-6) | Anthropic | Closed | 83.7% |
| 6 | [DeepSeek V4 Pro (Max)](https://benchlm.ai/models/deepseek-v4-pro-max) | DeepSeek | Open | 83.4% |
| 7 | [Kimi K2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 83.2% |
| 8 | [GPT-5.4](https://benchlm.ai/models/gpt-5-4) | OpenAI | Closed | 82.7% |
| 9 | [DeepSeek V4 Pro (High)](https://benchlm.ai/models/deepseek-v4-pro-high) | DeepSeek | Open | 80.4% |
| 10 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-max) | Anthropic | Closed | 79.3% |

*来源: [https://benchlm.ai/benchmarks/browseComp](https://benchlm.ai/benchmarks/browseComp) · 更新于 2026-05-05 · 共 21 个模型*
<!-- AUTO:END slug=browseComp -->

<br>

---

## Reasoning

### ARC-AGI-2

抽象推理网格谜题。前沿通用智能测试 —— 人类几乎全对,模型仍然挣扎。

<!-- AUTO:START slug=arcAgi2 lang=zh -->
| 排名 | 模型 | 提供商 | 开闭源 | 分数 |
| :-: | :-- | :-- | :-: | --: |
| 1 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 85.0% |
| 2 | [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) | OpenAI | Closed | 83.3% |
| 3 | [Gemini 3.1 Pro](https://benchlm.ai/models/gemini-3-1-pro) | Google | Closed | 77.1% |
| 4 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-max) | Anthropic | Closed | 75.8% |
| 5 | [Grok 4.20](https://benchlm.ai/models/grok-4-20-beta) | xAI | Closed | 53.3% |
| 6 | [GPT-5.2](https://benchlm.ai/models/gpt-5-2) | OpenAI | Closed | 52.9% |
| 7 | [Gemini 3 Pro Deep Think](https://benchlm.ai/models/gemini-3-pro-deep-think) | Google | Closed | 45.1% |
| 8 | [Muse Spark](https://benchlm.ai/models/muse-spark) | Meta | Closed | 42.5% |
| 9 | [Gemini 3 Pro](https://benchlm.ai/models/gemini-3-pro) | Google | Closed | 31.1% |
| 10 | [Claude Sonnet 4.5](https://benchlm.ai/models/claude-sonnet-4-5) | Anthropic | Closed | 13.6% |

*来源: [https://benchlm.ai/benchmarks/arcAgi2](https://benchlm.ai/benchmarks/arcAgi2) · 更新于 2026-05-05 · 共 10 个模型*
<!-- AUTO:END slug=arcAgi2 -->

<br>

---

## Knowledge

### Humanity's Last Exam

跨学科专家级难题,被刻意设计为前沿模型也难以攻克。

<!-- AUTO:START slug=hle lang=zh -->
| 排名 | 模型 | 提供商 | 开闭源 | 分数 |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Claude Mythos Preview](https://benchlm.ai/models/claude-mythos-preview) | Anthropic | Closed | 64.7% |
| 2 | [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) | OpenAI | Closed | 58.7% |
| 3 | [GPT-5.5 Pro](https://benchlm.ai/models/gpt-5-5-pro) | OpenAI | Closed | 57.2% |
| 4 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-max) | Anthropic | Closed | 54.7% |
| 5 | [Claude Opus 4.6](https://benchlm.ai/models/claude-opus-4-6) | Anthropic | Closed | 53.0% |
| 6 | [GLM-5.1](https://benchlm.ai/models/glm-5-1) | Z.AI | Open | 52.3% |
| 7 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 52.2% |
| 8 | [GPT-5.4](https://benchlm.ai/models/gpt-5-4) | OpenAI | Closed | 52.1% |
| 9 | [GLM-5](https://benchlm.ai/models/glm-5) | Z.AI | Open | 50.4% |
| 10 | [Muse Spark](https://benchlm.ai/models/muse-spark) | Meta | Closed | 50.4% |

*来源: [https://benchlm.ai/benchmarks/hle](https://benchlm.ai/benchmarks/hle) · 更新于 2026-05-05 · 共 32 个模型*
<!-- AUTO:END slug=hle -->

<br>

---

## AI 编码工具全景

从业者真正用来出货的工具。门槛保持高 —— 只收有可验证采用度且活跃维护的项目。完整表格(选入标准、价格、更新节奏)见 [tools/ai-coding-tools.md](tools/ai-coding-tools.md)。

#### CLI agent

| 工具 | 提供方 | 关键能力 |
| :-- | :-- | :-- |
| [Claude Code](https://www.anthropic.com/claude-code) | Anthropic | 子 agent、hooks、MCP、slash 命令、skills |
| [Codex CLI](https://github.com/openai/codex) | OpenAI | 官方 agent CLI,沙箱执行 |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Google | 原生 Search 接地,免费额度大方 |
| [Aider](https://aider.chat) | 开源 | Git 原生 diff,repo-map,模型无关 |

#### IDE 原生

| 工具 | 提供方 | 关键能力 |
| :-- | :-- | :-- |
| [Cursor](https://cursor.com) | Anysphere | Composer 多文件编辑,Tab 补全最快 |
| [Windsurf](https://windsurf.com) | Codeium / OpenAI | Cascade flow,supercomplete |
| [Zed AI](https://zed.dev) | Zed Industries | 内置于最快编辑器(Rust) |
| [GitHub Copilot](https://github.com/features/copilot) | GitHub | 部署量最大,IDE 覆盖最全 |

#### VS Code 扩展(开源,BYOK)

| 工具 | 提供方 | 关键能力 |
| :-- | :-- | :-- |
| [Cline](https://cline.bot) | 开源 | Plan/Act 模式,MCP,浏览器 |
| [Roo Code](https://roocode.com) | 开源 | Cline 分支,自定义 agent mode |
| [Continue](https://continue.dev) | 开源 | 可定制助手,slash 命令 |

#### 云 agent 与代码库问答

| 工具 | 提供方 | 关键能力 |
| :-- | :-- | :-- |
| [Devin](https://devin.ai) | Cognition | 长时间运行的自主 SWE agent |
| [Replit Agent](https://replit.com/ai) | Replit | 浏览器内端到端应用生成 |
| [Sourcegraph Cody](https://sourcegraph.com/cody) | Sourcegraph | 代码图谱上下文,代码库感知 |

<br>

---

## 如何看这些数字

- **不要跨 benchmark 比较。** 标度不同,天花板不同。
- **看分布。** Top 10 集中在 2–3 分内 = 已饱和,差异是噪声。领先 10+ 分 = 真有领先。
- **看日期。** 每个表都链回来源页;各 benchmark 异步刷新。
- **想用在自己场景, 自己跑评测。** 公开 benchmark 测的是别人任务上的平均值。

## 局限

- benchlm.ai 也是带主观判断的聚合者(类别权重、入选标准)。镜像他们的判断是因为目前最好,不是说就是客观真理。
- Benchmark 污染真实且日益严重。任何单一 benchmark 都应保持怀疑;多榜共识才是信号。
- 模型身份漂移: 厂商常静默更新同名模型。不同日期的得分不严格可比。

## 数据来源与归属

所有排行榜数据均镜像自 [benchlm.ai](https://benchlm.ai),完整 attribution。每个表都链回原页。**有意排除**: benchlm.ai 自身标记为 "Display only" 的 benchmark(GAIA、BFCL v4、FrontierMath …),因公开快照不完整,放进来会误导。

完整榜单、价格、方法论、仪表盘、类别权重 —— 请访问 [benchlm.ai](https://benchlm.ai)。

<br>

---

## 更新节奏

GitHub Actions workflow 每日 02:00 UTC 运行,抓源页、解析榜单,仅当 `data/` 或 README 区块发生变化时才提交。提交信息标注变更内容。详见 [`.github/workflows/sync.yml`](.github/workflows/sync.yml)。

## 贡献

欢迎 PR —— 见 [CONTRIBUTING.md](CONTRIBUTING.md)。新增 benchmark 改 `scripts/benchmarks.yaml`,新增工具改 `tools/ai-coding-tools.md`。门槛保持高: 只收 benchlm.ai 上 `Current` 或 `Refreshing` 状态的 benchmark,只收有实质采用的工具。

## 相关

- [benchlm.ai](https://benchlm.ai) —— 权威来源
- [Awesome Quant AI](https://github.com/leoncuhk/awesome-quant-ai) —— 姊妹项目
- [Artificial Analysis](https://artificialanalysis.ai/) —— 另一聚合站(主打价格/性能)
- [LMArena](https://lmarena.ai/) —— 人类两两偏好

## License

[MIT](LICENSE),适用于策展、代码与原创注释。排行榜数据来自 benchlm.ai —— 数据使用条款请参考其官网。

<br>

<div align="center">
<sub>由 <a href="https://github.com/leoncuhk">@leoncuhk</a> 维护 · 姊妹项目: <a href="https://github.com/leoncuhk/awesome-quant-ai">awesome-quant-ai</a></sub>
</div>
