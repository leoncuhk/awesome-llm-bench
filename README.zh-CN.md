<div align="center">

# Awesome LLM Bench (中文版)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Sync Leaderboards](https://github.com/leoncuhk/awesome-llm-bench/actions/workflows/sync.yml/badge.svg)](https://github.com/leoncuhk/awesome-llm-bench/actions/workflows/sync.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](https://img.shields.io/badge/lang-English-blue.svg)](README.md)

**精选、自动同步的 LLM 排行榜镜像 + AI 编码工具动态。**

<!-- LAST_SYNC -->最近同步: **2026-04-29** (UTC,每日自动更新)<!-- /LAST_SYNC -->

*只取 Top 10 · 每日更新 · 来源 [benchlm.ai](https://benchlm.ai)*

</div>

---

## 为什么有这个项目?

LLM 评测领域噪音极大: LMArena 反映的是用户偏好而非能力,厂商自报数字挑樱桃,聚合榜单滞后前沿模型几个月。本仓库镜像 **[benchlm.ai](https://benchlm.ai)** —— 我们目前找到最靠谱、更新最及时、方法论最诚实的聚合站 —— 蒸馏出每个高信号 benchmark 的 **Top 10**,便于快速扫视。

**你能得到:**
- 7 个高信号 benchmark 的 Top 10,覆盖 **Agentic / Coding / Reasoning / Knowledge** 四个类别
- 精选的 AI **CLI / IDE 工具**全景(Claude Code, Cursor, Cline, Aider, ...)
- 通过 GitHub Actions 每日自动同步,历史数据以 JSON 形式留存于 [`data/`](data/)
- [English](README.md) + 中文双语

**这里不是:** 重新评测、重新排序,也不是 benchlm.ai 的替代品。我们只是带 attribution 的镜像。完整榜单(每个 benchmark 43+ 模型)、价格、方法论、仪表盘 —— **请始终去 [benchlm.ai](https://benchlm.ai)**, 真正的脏活累活是他们做的。

## 目录

- [Top 10 排行榜](#top-10-排行榜)
  - [Agentic 智能体](#agentic-智能体) · [Coding 编码](#coding-编码) · [Reasoning 推理](#reasoning-推理) · [Knowledge 知识](#knowledge-知识)
- [AI 编码工具全景](#ai-编码工具全景)
- [方法论说明](#方法论说明)
- [局限与诚实声明](#局限与诚实声明)
- [如何看这些数字](#如何看这些数字)
- [贡献](#贡献)
- [License](#license)

---

## Top 10 排行榜

### Agentic 智能体

#### Terminal-Bench 2.0
> 多步终端/CLI 工作流 —— 检查、执行、编辑、错误恢复。

<!-- AUTO:START slug=terminalBench2 lang=zh -->
| 排名 | 模型 | 提供商 | 开闭源 | 分数 |
| :-: | :-- | :-- | :-: | --: |
| 1 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 82.7% |
| 2 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 69.4% |
| 3 | [MiMo-V2.5-Pro](https://benchlm.ai/models/mimo-v2-5-pro) | Xiaomi | Closed | 68.4% |
| 4 | [DeepSeek V4 Pro (Max)](https://benchlm.ai/models/deepseek-v4-pro-max) | DeepSeek | Open | 67.9% |
| 5 | [Kimi 2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 66.7% |
| 6 | [MiMo-V2.5](https://benchlm.ai/models/mimo-v2-5) | Xiaomi | Closed | 65.8% |
| 7 | [Qwen 3.6 Max (preview)](https://benchlm.ai/models/qwen-3-6-max-preview) | Alibaba | Closed | 65.4% |
| 8 | [DeepSeek V4 Pro (High)](https://benchlm.ai/models/deepseek-v4-pro-high) | DeepSeek | Open | 63.3% |
| 9 | [Composer 2](https://benchlm.ai/models/composer-2) | Cursor | Closed | 61.7% |
| 10 | [Qwen3.6-27B](https://benchlm.ai/models/qwen3-6-27b) | Alibaba | Open | 59.3% |

*来源: [https://benchlm.ai/benchmarks/terminalBench2](https://benchlm.ai/benchmarks/terminalBench2) · 更新于 2026-04-28 · 共 17 个模型*
<!-- AUTO:END slug=terminalBench2 -->

#### OSWorld 验证版
> 桌面 GUI 计算机使用任务 —— 导航、编辑、流程完成。

<!-- AUTO:START slug=osWorldVerified lang=zh -->
| 排名 | 模型 | 提供商 | 开闭源 | 分数 |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Claude Mythos Preview](https://benchlm.ai/models/claude-mythos-preview) | Anthropic | Closed | 79.6% |
| 2 | [Holo3-122B-A10B](https://benchlm.ai/models/holo3-122b-a10b) | H Company | Closed | 78.8% |
| 3 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 78.7% |
| 4 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 78.0% |
| 5 | [Holo3-35B-A3B](https://benchlm.ai/models/holo3-35b-a3b) | H Company | Open | 77.8% |
| 6 | [GPT-5.4](https://benchlm.ai/models/gpt-5-4) | OpenAI | Closed | 75.0% |
| 7 | [Kimi 2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 73.1% |
| 8 | [Claude Opus 4.6](https://benchlm.ai/models/claude-opus-4-6) | Anthropic | Closed | 72.7% |
| 9 | [Claude Sonnet 4.6](https://benchlm.ai/models/claude-sonnet-4-6) | Anthropic | Closed | 72.5% |
| 10 | [GPT-5.4 mini](https://benchlm.ai/models/gpt-5-4-mini) | OpenAI | Closed | 72.1% |

*来源: [https://benchlm.ai/benchmarks/osWorldVerified](https://benchlm.ai/benchmarks/osWorldVerified) · 更新于 2026-04-28 · 共 18 个模型*
<!-- AUTO:END slug=osWorldVerified -->

#### BrowseComp
> Web 研究 agent —— 搜索、查证、返回准确答案。

<!-- AUTO:START slug=browseComp lang=zh -->
| 排名 | 模型 | 提供商 | 开闭源 | 分数 |
| :-: | :-- | :-- | :-: | --: |
| 1 | [GPT-5.5 Pro](https://benchlm.ai/models/gpt-5-5-pro) | OpenAI | Closed | 90.1% |
| 2 | [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) | OpenAI | Closed | 89.3% |
| 3 | [Claude Mythos Preview](https://benchlm.ai/models/claude-mythos-preview) | Anthropic | Closed | 86.9% |
| 4 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 84.4% |
| 5 | [Claude Opus 4.6](https://benchlm.ai/models/claude-opus-4-6) | Anthropic | Closed | 83.7% |
| 6 | [DeepSeek V4 Pro (Max)](https://benchlm.ai/models/deepseek-v4-pro-max) | DeepSeek | Open | 83.4% |
| 7 | [Kimi 2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 83.2% |
| 8 | [GPT-5.4](https://benchlm.ai/models/gpt-5-4) | OpenAI | Closed | 82.7% |
| 9 | [DeepSeek V4 Pro (High)](https://benchlm.ai/models/deepseek-v4-pro-high) | DeepSeek | Open | 80.4% |
| 10 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 79.3% |

*来源: [https://benchlm.ai/benchmarks/browseComp](https://benchlm.ai/benchmarks/browseComp) · 更新于 2026-04-28 · 共 21 个模型*
<!-- AUTO:END slug=browseComp -->

### Coding 编码

#### SWE-bench 验证版
> 真实 GitHub issue 修复任务,AI 编码 agent 的黄金标准。

<!-- AUTO:START slug=sweVerified lang=zh -->
| 排名 | 模型 | 提供商 | 开闭源 | 分数 |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Claude Mythos Preview](https://benchlm.ai/models/claude-mythos-preview) | Anthropic | Closed | 93.9% |
| 2 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 87.6% |
| 3 | [GPT-5.3 Codex](https://benchlm.ai/models/gpt-5-3-codex) | OpenAI | Closed | 85.0% |
| 4 | [Claude Opus 4.5](https://benchlm.ai/models/claude-opus-4-5) | Anthropic | Closed | 80.9% |
| 5 | [Claude Opus 4.6](https://benchlm.ai/models/claude-opus-4-6) | Anthropic | Closed | 80.8% |
| 6 | [DeepSeek V4 Pro (Max)](https://benchlm.ai/models/deepseek-v4-pro-max) | DeepSeek | Open | 80.6% |
| 7 | [Kimi 2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 80.2% |
| 8 | [GPT-5.2](https://benchlm.ai/models/gpt-5-2) | OpenAI | Closed | 80.0% |
| 9 | [Claude Sonnet 4.6](https://benchlm.ai/models/claude-sonnet-4-6) | Anthropic | Closed | 79.6% |
| 10 | [DeepSeek V4 Pro (High)](https://benchlm.ai/models/deepseek-v4-pro-high) | DeepSeek | Open | 79.4% |

*来源: [https://benchlm.ai/benchmarks/sweVerified](https://benchlm.ai/benchmarks/sweVerified) · 更新于 2026-04-28 · 共 43 个模型*
<!-- AUTO:END slug=sweVerified -->

#### LiveCodeBench
> 防污染代码生成,持续采样新题目。

<!-- AUTO:START slug=liveCodeBench lang=zh -->
| 排名 | 模型 | 提供商 | 开闭源 | 分数 |
| :-: | :-- | :-- | :-: | --: |
| 1 | [DeepSeek V4 Pro (Max)](https://benchlm.ai/models/deepseek-v4-pro-max) | DeepSeek | Open | 93.5% |
| 2 | [DeepSeek V4 Flash (Max)](https://benchlm.ai/models/deepseek-v4-flash-max) | DeepSeek | Open | 91.6% |
| 3 | [DeepSeek V4 Pro (High)](https://benchlm.ai/models/deepseek-v4-pro-high) | DeepSeek | Open | 89.8% |
| 4 | [Kimi 2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 89.6% |
| 5 | [DeepSeek V4 Flash (High)](https://benchlm.ai/models/deepseek-v4-flash-high) | DeepSeek | Open | 88.4% |
| 6 | [Kimi K2.5](https://benchlm.ai/models/kimi-k2-5) | Moonshot AI | Open | 85.0% |
| 7 | [GLM-4.7](https://benchlm.ai/models/glm-4-7) | Z.AI | Open | 84.9% |
| 8 | [Qwen3.6-27B](https://benchlm.ai/models/qwen3-6-27b) | Alibaba | Open | 83.9% |
| 9 | [Qwen3.6-35B-A3B](https://benchlm.ai/models/qwen3-6-35b-a3b) | Alibaba | Open | 80.4% |
| 10 | [Nemotron 3 Nano Omni 30B A3B](https://benchlm.ai/models/nemotron-3-nano-omni-30b-a3b) | NVIDIA | Open | 63.2% |

*来源: [https://benchlm.ai/benchmarks/liveCodeBench](https://benchlm.ai/benchmarks/liveCodeBench) · 更新于 2026-04-28 · 共 13 个模型*
<!-- AUTO:END slug=liveCodeBench -->

### Reasoning 推理

#### ARC-AGI-2
> 抽象推理网格谜题 —— 前沿通用智能测试。

<!-- AUTO:START slug=arcAgi2 lang=zh -->
| 排名 | 模型 | 提供商 | 开闭源 | 分数 |
| :-: | :-- | :-- | :-: | --: |
| 1 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 85.0% |
| 2 | [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) | OpenAI | Closed | 83.3% |
| 3 | [Gemini 3.1 Pro](https://benchlm.ai/models/gemini-3-1-pro) | Google | Closed | 77.1% |
| 4 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 75.8% |
| 5 | [Grok 4.20](https://benchlm.ai/models/grok-4-20-beta) | xAI | Closed | 53.3% |
| 6 | [GPT-5.2](https://benchlm.ai/models/gpt-5-2) | OpenAI | Closed | 52.9% |
| 7 | [Gemini 3 Pro Deep Think](https://benchlm.ai/models/gemini-3-pro-deep-think) | Google | Closed | 45.1% |
| 8 | [Muse Spark](https://benchlm.ai/models/muse-spark) | Meta | Closed | 42.5% |
| 9 | [Gemini 3 Pro](https://benchlm.ai/models/gemini-3-pro) | Google | Closed | 31.1% |
| 10 | [Claude Sonnet 4.5](https://benchlm.ai/models/claude-sonnet-4-5) | Anthropic | Closed | 13.6% |

*来源: [https://benchlm.ai/benchmarks/arcAgi2](https://benchlm.ai/benchmarks/arcAgi2) · 更新于 2026-04-28 · 共 10 个模型*
<!-- AUTO:END slug=arcAgi2 -->

### Knowledge 知识

#### 人类最后考试 (HLE)
> 跨学科专家级难题,被设计为前沿模型也难以攻克。

<!-- AUTO:START slug=hle lang=zh -->
| 排名 | 模型 | 提供商 | 开闭源 | 分数 |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Claude Mythos Preview](https://benchlm.ai/models/claude-mythos-preview) | Anthropic | Closed | 64.7% |
| 2 | [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) | OpenAI | Closed | 58.7% |
| 3 | [GPT-5.5 Pro](https://benchlm.ai/models/gpt-5-5-pro) | OpenAI | Closed | 57.2% |
| 4 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 54.7% |
| 5 | [Claude Opus 4.6](https://benchlm.ai/models/claude-opus-4-6) | Anthropic | Closed | 53.0% |
| 6 | [GLM-5.1](https://benchlm.ai/models/glm-5-1) | Z.AI | Open | 52.3% |
| 7 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 52.2% |
| 8 | [GPT-5.4](https://benchlm.ai/models/gpt-5-4) | OpenAI | Closed | 52.1% |
| 9 | [GLM-5](https://benchlm.ai/models/glm-5) | Z.AI | Open | 50.4% |
| 10 | [Muse Spark](https://benchlm.ai/models/muse-spark) | Meta | Closed | 50.4% |

*来源: [https://benchlm.ai/benchmarks/hle](https://benchlm.ai/benchmarks/hle) · 更新于 2026-04-28 · 共 31 个模型*
<!-- AUTO:END slug=hle -->

---

## AI 编码工具全景

精挑出从业者真正用来出货的 AI CLI/IDE 工具。完整带备注、更新节奏、特性的表格见 [tools/ai-coding-tools.md](tools/ai-coding-tools.md)。

| 工具 | 形态 | 提供方 | 收费模式 | 备注 |
| :-- | :-- | :-- | :-- | :-- |
| [Claude Code](https://www.anthropic.com/claude-code) | CLI + IDE 插件 | Anthropic | 订阅 (Pro/Max) + API | 深度 agent 循环、hooks、子 agent、slash 命令 |
| [Cursor](https://cursor.com) | IDE (VS Code fork) | Anysphere | 订阅 + API | Composer 模式,Tab 补全,多模型 |
| [Windsurf](https://windsurf.com) | IDE (VS Code fork) | Codeium | 订阅 + API | Cascade flow,多文件编辑 |
| [Cline](https://cline.bot) | VS Code 扩展 | 开源 | BYOK | Plan/Act 模式,MCP 支持 |
| [Roo Code](https://roocode.com) | VS Code 扩展 | 开源 | BYOK | Cline 分支,自定义 mode |
| [Aider](https://aider.chat) | CLI | 开源 | BYOK | Git 原生,成熟,模型无关 |
| [Codex CLI](https://github.com/openai/codex) | CLI | OpenAI | API | OpenAI 官方 agent CLI |
| [Continue](https://continue.dev) | VS Code / JetBrains | 开源 | BYOK | 可定制助手 |
| [Zed AI](https://zed.dev) | IDE | Zed | 订阅 + API | 内置于高速 Rust 编辑器 |
| [GitHub Copilot](https://github.com/features/copilot) | IDE 插件 + CLI | GitHub/MS | 订阅 | 部署量最大的助手 |
| [Sourcegraph Cody](https://sourcegraph.com/cody) | IDE 插件 | Sourcegraph | 订阅 | 代码库感知(图谱上下文) |
| [Replit Agent](https://replit.com/ai) | 云 IDE | Replit | 订阅 | 端到端应用生成 |
| [Devin](https://devin.ai) | 云 agent | Cognition | 订阅 | 自主 SWE agent |
| [Tabnine](https://tabnine.com) | IDE 插件 | Tabnine | 订阅 | 私有部署 / 隐私优先选项 |

---

## 方法论说明

**benchlm.ai 如何排名。** 加权分类得分: Agentic 22%, Coding 20%, Reasoning 17%, Multimodal 12%, Knowledge 12%, Multilingual 7%, Instruction Following 5%, Math 5%。每个 benchmark 在所属类别中有子权重(如 SWE-bench Verified 占 Coding 类别的 13%)。每个 benchmark 都有 **新鲜度标签**(`Current` / `Refreshing` / `Display only`),一眼看出某个数字是否还有信号、是否已陈旧。完整评分策略见 [BenchLM 方法论页](https://benchlm.ai/methodology)。

**为什么镜像而不自建。** 维护好一个排行榜是全职工作: 来源核验、新鲜度审计、污染检查、评测脚本版本管理、方法论披露。benchlm.ai 把这些事做得很认真。我们的增量价值是: (a) 蒸馏到 Top 10,扫视极快; (b) 配上他们不覆盖的 AI 工具全景; (c) 提供中文版。

**更新节奏。** GitHub Actions 每日 02:00 UTC 抓源页,解析 Top 10,有变化才提交到 [`data/`](data/)。提交信息会指出变了什么(如 `chore(sync): SWE-Verified leader changed from X to Y`)。

## 局限与诚实声明

- **benchlm.ai 也是带主观判断的聚合者** —— 类别权重是主观的,benchmark 入选是编辑判断。我们镜像他们的判断是因为目前找到的最好,不是说它就是客观真理。
- **"Display only" benchmark**(GAIA, BFCL v4, FrontierMath, ...)在本镜像中被刻意排除,直到 benchlm.ai 上升级为完整验证榜单。包含部分快照会误导读者。
- **Benchmark 污染**是真实且日益严重的问题。即便 SWE-bench Verified 也不能完全免疫 —— 模型厂商对 issue 有可见性。任何单一 benchmark 都应保持怀疑;多榜共识才是信号。
- **模型身份漂移** —— 厂商常常静默更新同名模型。"GPT-5.3" 在 2026-01 和 2026-04 的得分可能不是同一个模型。
- **厂商自报 vs 独立评测** —— benchlm.ai 正向独立验证迁移,但旧数据可能仍是厂商自报。他们用新鲜度标签暴露这一点;我们在 JSON 中保留,但表格中暂未显示。

## 如何看这些数字

1. **不要跨 benchmark 比。** SWE-Verified 的 93% 和 HLE 的 64% 不在同一标度上。每个 benchmark 各自的天花板不同。
2. **看分布。** 当 Top 10 集中在 2-3 分内时, benchmark 已饱和 —— 微小差异是噪声。当头部领先中段 10+ 分时, 领跑者真有领先。
3. **按 license 过滤** —— 表格中标注 `Closed` / `Open`,在意开源的人按需筛选。
4. **看日期**, 链接到来源页可看 benchmark 的最近更新日期。各 benchmark 异步刷新, 2025 年的老 benchmark 可能没反映最新模型。
5. **想用在自己场景上,自己跑评测。** 公开 benchmark 测的是别人任务上的平均值。你的任务是你的任务。

## 贡献

欢迎 PR:
- **新增 benchmark**: 编辑 [`scripts/benchmarks.yaml`](scripts/benchmarks.yaml),用 benchlm.ai 的 camelCase slug(如 `mmlu`, `aimE2025`)。跑 `python scripts/fetch_benchmark.py --slug <new>` 验证 parser 兼容。
- **更新 AI 工具全景**: 编辑 [`tools/ai-coding-tools.md`](tools/ai-coding-tools.md)。门槛保持高 —— 只收有实质采用的工具。
- **翻译修订** [`README.zh-CN.md`](README.zh-CN.md)。
- **报告解析失败**: 提 issue,带上 slug 和日期。

请**不要** PR 重排序、删除 attribution、或抓取超出 Top 10 的内容。

## 相关

- 📊 [benchlm.ai](https://benchlm.ai) —— 权威来源(完整榜单去这里)
- 🧪 [Awesome Quant AI](https://github.com/leoncuhk/awesome-quant-ai) —— 姊妹项目,聚焦 quant + AI
- 🤖 [Artificial Analysis](https://artificialanalysis.ai/) —— 另一个聚合站(主打价格/性能)
- 🏟 [LMArena](https://lmarena.ai/) —— 人类两两偏好(不同信号,非能力)

## License

MIT, 适用于本仓库的策展、代码与原创注释。排行榜数据来自 benchlm.ai 并标注归属;数据使用条款请参考其官网。

---

<div align="center">
<sub>由 <a href="https://github.com/leoncuhk">@leoncuhk</a> 维护 · 姊妹项目 <a href="https://github.com/leoncuhk/awesome-quant-ai">awesome-quant-ai</a></sub>
</div>
