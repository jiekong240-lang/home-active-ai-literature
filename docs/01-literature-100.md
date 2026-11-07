# 家用机「主动式 AI」文献清单（100 篇）
> 本文件**只含文献资料**：出处、内容要点、与主题的关联、核验记录。不含方案设计、架构图、代码、部署步骤，也不构建任何项目。
> 检索完成时间：2026-11-06（GMT+8）。命题待验证，**本步不作论证**：家用消费级电脑不本地运行大模型，仅通过调用云端 LLM API 进行编排，是否足以构成具备主动触发、记忆、规划与工具调用能力的常驻个人助理。

## 一、检索口径
1. **工作定义**：此处「主动式 AI」指不必等用户发问，而能由时间、外部事件或环境变化触发，长期保持状态与记忆，自主规划并调用工具、再通过 API 完成推理的常驻软件代理。
2. **纳入优先级**：① 厂商 / 标准组织官方技术文档与规范；② arXiv、会议与期刊论文；③ 官方开源仓库与其 README；④ 厂商工程指南、白皮书、官方帮助文档；⑤ 可复现的公开评测基准。
3. **排除范围**：信息安全、网络攻击、越狱与提示注入攻防、隐私泄露、红队、内容审核、合规治理类文献一律不收；纯营销软文、二手转载、无出处的教程不收。
4. **时间范围**：以 2023–2026 年为主，奠基性论文与现行标准不受此限；官方文档页若无标注日期，记为 `n.d.`，不推断年份。
5. **出处要求**：每条须有可直接打开的 URL；标题、作者、时间、要点均须与页面实际内容一致，并摘录页面原文短语作为「页面依据」供反向核对。数字（价格、限额、参数、规模）只抄页面原文，不推算。
6. **主题收敛**：候选中与「家用机 / API 编排 / 主动性」关联较弱的条目（如具身游戏智能体、代码修复基准、多智能体失效分析、本地模型量化对照、重复主题的综述）予以剔除，优先保留密度更高的一手资料。

## 二、出处核验方法与可复现结果
**第一步（逐条检索）**：12 个子领域并行检索，共得 120 条候选，每条均由检索时实际打开正文确认，并摘录页面原文短语；其中标注「已打开正文」120 条。
**第二步（批量直连核验）**：对全部候选 URL 并发发起 HTTP 请求，记录状态码，并抽取页面 `<title>` / `citation_title` 与文献标题做字符串相似度比对。结果（120 条）：BLOCKED 12 条、FAIL 7 条、OK 89 条、TITLE_MISMATCH 12 条。
- `OK` = 返回 200 且页面标题与文献标题吻合；`TITLE_MISMATCH` = 返回 200 但站点使用通用标题、重定向页或 PDF 无 HTML 标题；`BLOCKED` = 403/429 反爬或地区限制；`FAIL` = 本机代理链路 502 / SSL 超时。
- 判定口径：**`BLOCKED` 与 `FAIL` 不代表链接失效**。对其中 17 条改用独立抓取通道或 curl 二次确认，均证实资源真实存在（读回页面标题/正文，或确认 PDF 文件类型与 200 响应），明细见下表；典型如 OpenAI Platform Docs（403）、Anthropic Docs（地区重定向）、Gemini API / Mistral Docs / ADK / Docker Docs / Hugging Face（代理 502）、Kaggle（reCAPTCHA）、ChatGPT 与 Gemini 的定时任务帮助页。
- 定价类页面会随时间变动，文档内的价格仅代表检索时页面所示，复核时应以实时页面为准。

**二次确认明细**（直连异常 → 独立抓取通道 / curl 读回的结果）：

| 检索号 | 直连结果 | 二次读回的页面标题 / 文件 | 是否入清单 |
|---|---|---|---|
| C-03 | TITLE_MISMATCH | Tool use with Claude - Claude Platform Docs | 是 |
| C-05 | FAIL | Function calling with the Gemini API - Gemini API \| Google AI Studio | 是 |
| C-06 | FAIL | Function Calling \| Mistral Docs | 是 |
| D-07 | TITLE_MISMATCH | 腾讯混元大模型 混元 OpenAI 兼容接口相关调用示例_腾讯云 | 是 |
| E-03 | FAIL | Get started - Agent Development Kit (ADK) | 是 |
| G-08 | FAIL | Overview - A2A Protocol | 是 |
| K-01 | BLOCKED | Business Pricing \| OpenAI（Pricing） | 是 |
| K-09 | FAIL | Resource constraints \| Docker Docs | 是 |
| L-03 | TITLE_MISMATCH | Agents \| Kaggle（作者 Julia Wiesinger, Patrick Marlow, Vladimir Vuskovic） | 是 |
| L-06 | FAIL | Introducing smolagents: simple agents that write actions in code. | 是 |
| L-07 | BLOCKED | Scheduled tasks in ChatGPT \| OpenAI Help Center | 是 |
| L-08 | FAIL | Schedules in Gemini Apps - Computer - Gemini Apps Help | 是 |
| C-08 | BLOCKED | Tool Use Overview - GroqDocs | 是 |
| C-10 | BLOCKED | Function calling patterns - Together AI docs | 是 |
| D-09 | TITLE_MISMATCH | 豆包助手 - 火山方舟 - 火山引擎（旧地址 200 并跳转新文档域） | 是 |
| L-02 | TITLE_MISMATCH | A practical guide to building agents（官方 PDF，直连 200，Content-Type: application/pdf） | 是 |
| I-10 | BLOCKED | WebSub（W3C Recommendation，直连 403 为站点反爬） | 否（主题收敛剔除） |

共二次确认 17 条，其中 16 条进入最终 100 篇；未二次确认而保留的条目，其直连 403 均属站点反爬，检索时已逐条打开正文并留有页面依据。

**第三步（去重与收敛）**：检出 3 组重复 URL，剔除 A-05、A-06、I-06（保留 B-06、B-07、G-07）；再按主题相关度剔除 17 条，共剔除 20 条，最终保留 100 条、恰好 100 篇，停止检索。
最终 100 篇的核验分布：BLOCKED 10 篇、FAIL 7 篇、OK 73 篇、TITLE_MISMATCH 10 篇。全部条目均有可访问出处与页面依据；其中存在直连限制的条目已在「核验」字段逐条注明原因。
**复跑方式**（中间材料与核验脚本，非交付物）：候选原文见 `.workbuddy-ai/research/raw-A.md` … `raw-L.md`，结构化候选见 `items.json`，逐条状态码与标题相似度见 `verify-report.json`；在 `.workbuddy-ai/research/` 下执行 `python verify.py check` 可重做批量核验，`python build.py` 可重新生成本清单。

## 三、分类索引
| 类 | 主题 | 篇数 | 编号 |
|---|---|---:|---|
| A | 主动式 / 常驻式智能体学术研究 | 8 | 001–008 |
| B | LLM 智能体基础架构与经典论文 | 9 | 009–017 |
| C | 国际云厂商 LLM API 官方文档 | 8 | 018–025 |
| D | 国内大模型平台官方 API 文档 | 9 | 026–034 |
| E | 智能体编排框架与 SDK 官方文档 | 9 | 035–043 |
| F | 家用机自托管编排 / 自动化平台官方文档 | 8 | 044–051 |
| G | 开放协议与工具调用标准 | 9 | 052–060 |
| H | 智能体记忆与长期状态 | 9 | 061–069 |
| I | 事件驱动、调度与常驻运行 | 8 | 070–077 |
| J | 智能体评测基准与成本 / 可靠性工程 | 6 | 078–083 |
| K | 家用硬件门槛与 API 成本一手资料 | 9 | 084–092 |
| L | 厂商工程指南、综述与主动任务产品证据 | 8 | 093–100 |
| **合计** | — | **100** | **001–100** |

## 四、文献清单（001–100）

### A 类｜主动式 / 常驻式智能体学术研究（8 篇）

#### 001｜Foundations of Proactive Agents: Principles, Technical Layers, and Proactivity-Gym

- **检索号**：A-01　**类别**：A 主动式 / 常驻式智能体学术研究
- **作者 / 机构**：Jio Oh、Seunghyun Do、Young-Jun Lee、Steven Euijong Whang、Dongyeop Kang（arXiv 预印本，cs.AI）
- **时间**：2026-09　**类型**：arXiv 预印本（主动式智能体基础研究/框架 + 评测平台）
- **出处**：<https://arxiv.org/abs/2609.37267>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Proactive LLM agents can turn idle compute into useful support before users ask.
- **要点**：给出 proactivity 的定义与 3T 联合原则（Task Capability、Temporal Allocation、Trust），并把设计空间拆成 task scope、anticipation horizon、activation trigger、processing timing、intervention depth 五个维度；另提出仿真评测平台 PROACTIVITY-GYM（多日场景、有状态环境、persona 条件模拟用户），30 人实验发现用户偏好 sleep-time assistance。
- **与主题关联**：它把主动式助理的核心归结为"空闲算力 + 触发时机 + 信任"的编排设计，本地无需大模型，按触发条件调度云 LLM API 即可实现。

#### 002｜Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance

- **检索号**：A-02　**类别**：A 主动式 / 常驻式智能体学术研究
- **作者 / 机构**：Yaxi Lu、Shenzhi Yang、Cheng Qian 等（清华大学等，见检索结果；arXiv 预印本）
- **时间**：2024-10　**类型**：arXiv 预印本（cs.AI / cs.CL）
- **出处**：<https://arxiv.org/abs/2410.12361>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：developing proactive agents capable of anticipating and initiating tasks without explicit human instructions
- **要点**：针对多数 agent 仍是被动响应的问题，先从真实人类活动生成"主动任务预测"并由人工标注 accepted/rejected，训练 reward model 作为主动性自动评估器；再构建含 6,790 个事件的 ProactiveBench 数据集，微调后模型主动提供帮助的 F1 达 66.47%。
- **与主题关联**：主动预测由"观察事件 → 判断是否主动出手"的编排实现，家用机只需轻量事件源 + 云 API 即可承担该闭环。

#### 003｜Communication Policy Evolution for Proactive LLM Agents

- **检索号**：A-03　**类别**：A 主动式 / 常驻式智能体学术研究
- **作者 / 机构**：Xinbei Ma、Jiyang Qiu、Yao Yao、Zhuosheng Zhang、Hai Zhao 等（arXiv 预印本，cs.AI）
- **时间**：2026-06　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2606.14314>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Building information asymmetry for proactive agents, we set up two complementary settings, User-Agent and Planner-Executor.
- **要点**：形式化"通信策略"，在文本与结构化 UI 两种通道下比较 User-Agent 与 Planner-Executor 设置，发现文本利于任务完成、结构化 UI 提升响应质量与 persona 一致性；提出 CPE 自进化框架，仅用 rollout + prompt 级演化（不改模型）即取得最佳任务成功率。
- **与主题关联**：主动式助理"何时、以何种方式"与用户沟通可在编排层用提示词演化实现，完全依赖调用云 LLM API 而非本地权重。

#### 004｜VisionClaw: Always-On AI Agents through Smart Glasses

- **检索号**：A-04　**类别**：A 主动式 / 常驻式智能体学术研究
- **作者 / 机构**：Xiaoan Liu、DaeHo Lee、Eric J Gonzalez、Mar Gonzalez-Franco、Ryo Suzuki（arXiv 预印本，cs.HC）
- **时间**：2026-04　**类型**：arXiv 预印本（常驻式系统 + 用户研究）
- **出处**：<https://arxiv.org/abs/2604.03486>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：an always-on wearable AI agent that integrates live egocentric perception with agentic task execution
- **要点**：在 Meta Ray-Ban 智能眼镜上运行常驻式智能体，持续感知现实情境，并通过语音把任务委派给 OpenClaw AI agents（加购物车、从纸质文档生成笔记、收会议简报、从海报建日程、控 IoT）；实验室（N=12）与纵向部署（N=5）显示任务更"机会主义地"被发起、执行更多被委派而非手动控制。
- **与主题关联**：直接展示"常驻 + 实时感知 + 委派给云端 agent"的范式，家用机只承担轻感知/触发与 API 编排。

#### 005｜Personal LLM Agents: Insights and Survey about the Capability, Efficiency and Security

- **检索号**：A-07　**类别**：A 主动式 / 常驻式智能体学术研究
- **作者 / 机构**：Yuanchun Li、Hao Wen、Weijun Wang、Xiangyu Li 等（综述；arXiv 预印本）
- **时间**：2024-01　**类型**：综述 / arXiv 预印本（cs.HC / cs.AI / cs.SE）
- **出处**：<https://arxiv.org/abs/2401.05459>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Personal LLM Agents, which are LLM-based agents that are deeply integrated with personal data and personal devices and used for personal assistance
- **要点**：系统讨论与个人数据、个人设备深度集成的 Personal LLM Agents，指出传统智能个人助理（IPA）受限于缺乏意图理解、任务规划、工具使用、个人数据管理等能力，而 LLM 可补足；综述其架构、能力、效率与安全挑战及代表方案，并汇集领域专家意见。
- **与主题关联**：直接给出"个人助理 = LLM + 意图理解 + 规划 + 工具 + 个人数据"的架构蓝图，支撑家用机以编排方式调用云 API 实现个人助理（此文为能力/架构综述，非攻击类主题）。

#### 006｜Lifelong Learning of Large Language Model based Agents: A Roadmap

- **检索号**：A-08　**类别**：A 主动式 / 常驻式智能体学术研究
- **作者 / 机构**：Junhao Zheng、Chengming Shi、Xidi Cai、Qiuke Li、Duzhen Zhang、Qianli Ma 等（综述；已被 IEEE TPAMI 接收）
- **时间**：2025-01　**类型**：综述 / arXiv 预印本（期刊录用）
- **出处**：<https://arxiv.org/abs/2501.07278>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：This survey is the first to systematically summarize the potential techniques for incorporating lifelong learning into LLM-based agents.
- **要点**：首个系统梳理 LLM 智能体终身学习（continual/incremental learning）的综述，把智能体拆为感知（多模态输入整合）、记忆（存取演化知识）、行动（与动态环境交互）三模块，讨论持续适应、缓解灾难性遗忘、提升长期性能，并给出趋势、评测指标与应用场景路线图。
- **与主题关联**：常驻式助理需"持续在线、随环境演化"，其感知-记忆-行动闭环可由编排层 + 云 API 长期维持，不必本地训练大模型。

#### 007｜A Survey on Large Language Model based Autonomous Agents

- **检索号**：A-09　**类别**：A 主动式 / 常驻式智能体学术研究
- **作者 / 机构**：Lei Wang、Chen Ma、Xueyang Feng、Wayne Xin Zhao、Ji-Rong Wen 等（中国人民大学等；综述）
- **时间**：2023-08（v7 2025-03）　**类型**：综述 / arXiv 预印本（cs.AI / cs.CL）
- **出处**：<https://arxiv.org/abs/2308.11432>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：we propose a unified framework that encompasses a majority of the previous work
- **要点**：从整体视角系统综述 LLM 自主智能体研究，先提出涵盖多数既有工作的统一构建框架，再梳理其在社科、自然科学、工程中的应用与常用评测策略，最后讨论挑战与未来方向，并维护持续更新的文献库。
- **与主题关联**：为"会规划、会调用工具的自主智能体"提供权威架构综述，说明能力来自编排框架而非本地模型规模。

#### 008｜From Reactive to Proactive: Assessing the Proactivity of Voice Agents via ProVoice-Bench

- **检索号**：A-10　**类别**：A 主动式 / 常驻式智能体学术研究
- **作者 / 机构**：Ke Xu、Yuhao Wang、Yu Wang（arXiv 预印本；投稿 Interspeech 2026）
- **时间**：2026-04　**类型**：会议投稿 / 评测基准（arXiv 预印本，cs.AI / cs.CL / cs.SD）
- **出处**：<https://arxiv.org/abs/2604.15037>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：overlooking the complexities of proactive intervention and monitoring
- **要点**：指出现有基准偏重被动响应、忽视"主动干预与监测"的复杂性，提出首个面向主动语音智能体的评测框架 ProVoice-Bench（4 个任务、1,182 条高质量样本）；对 SOTA 多模态 LLM 的评测显示明显性能差距，尤其是 over-triggering（过度触发）与推理能力。
- **与主题关联**：把"事件触发的时机判断"作为主动式助理的关键可评测维度，说明常驻助理需在编排层解决"何时主动出手"，而非依赖本地模型。

### B 类｜LLM 智能体基础架构与经典论文（9 篇）

#### 009｜ReAct: Synergizing Reasoning and Acting in Language Models

- **检索号**：B-01　**类别**：B LLM 智能体基础架构与经典论文
- **作者 / 机构**：Shunyu Yao、Jeffrey Zhao、Dian Yu 等（Princeton University、Google Research）
- **时间**：2022-10　**类型**：会议论文（ICLR 2023；arXiv 预印本 v3 标注为 ICLR camera ready 版）
- **出处**：<https://arxiv.org/abs/2210.03629>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：generate both reasoning traces and task-specific actions in an interleaved manner
- **要点**：提出让 LLM 交错地生成「推理轨迹」与「任务特定动作」，用推理来归纳、跟踪、更新行动计划并处理异常，用动作对接外部知识库或环境以补充信息。在 HotpotQA、FEVER 上通过与简单 Wikipedia API 交互缓解思维链的幻觉，在 ALFWorld、WebShop 上仅用一两个上下文示例即超过模仿学习与强化学习方法。
- **与主题关联**：确立「推理—行动」循环只需模型调用外部 API 即可闭环，家用机不必本地跑模型，编排云端 LLM 就能驱动会查证、会行动的助理。

#### 010｜Toolformer: Language Models Can Teach Themselves to Use Tools

- **检索号**：B-02　**类别**：B LLM 智能体基础架构与经典论文
- **作者 / 机构**：Timo Schick、Jane Dwivedi-Yu、Roberto Dessì 等（Meta AI / FAIR、University of Washington 等）
- **时间**：2023-02　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2302.04761>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：LMs can teach themselves to use external tools via simple APIs
- **要点**：提出 Toolformer，以自监督方式让语言模型自己学会「调用哪些 API、何时调用、传什么参数、如何把结果并入后续生成」，每个 API 仅需少量示范。融入计算器、问答、两种搜索引擎、翻译系统和日历后，在多种下游任务上显著提升零样本表现且未牺牲核心语言建模能力。
- **与主题关联**：说明工具调用能力可由「模型 + 简单 API」构成，能力在云端、编排在本地，正是家用机靠 API 编织助理的底层机制。

#### 011｜Reflexion: Language Agents with Verbal Reinforcement Learning

- **检索号**：B-03　**类别**：B LLM 智能体基础架构与经典论文
- **作者 / 机构**：Noah Shinn、Federico Cassano、Edward Berman 等（Northeastern University、Princeton University、MIT 等）
- **时间**：2023-03　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2303.11366>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer
- **要点**：提出不更新权重、而用「语言反馈」强化语言智能体的 Reflexion 框架，智能体对任务反馈作口头反思并把反思文本存入情景记忆缓冲，以改进后续试验的决策。在序列决策、编码与语言推理任务上明显优于基线，HumanEval 上 pass@1 达 91%，超过当时 GPT-4 的 80%。
- **与主题关联**：自我反思与经验记忆都可作为文本经 API 反复读写实现，无需本地训练或本地大模型，为常驻助理的「越用越聪明」提供轻量路径。

#### 012｜Tree of Thoughts: Deliberate Problem Solving with Large Language Models

- **检索号**：B-04　**类别**：B LLM 智能体基础架构与经典论文
- **作者 / 机构**：Shunyu Yao、Dian Yu、Jeffrey Zhao、Thomas L. Griffiths 等（Princeton University、Google DeepMind）
- **时间**：2023-05　**类型**：会议论文（NeurIPS 2023；arXiv 预印本 v2 标注为 camera ready 版）
- **出处**：<https://arxiv.org/abs/2305.10601>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：enables exploration over coherent units of text (thoughts) that serve as intermediate steps toward problem solving
- **要点**：提出 Tree of Thoughts（ToT），把思维链推广为对连贯「思维单元」的树状搜索，允许模型考虑多条推理路径、自我评估选择并在需要时前瞻或回溯。在 24 点、创意写作、迷你填字三类需规划与搜索的任务上大幅提升解题能力，24 点上 GPT-4 思维链仅 4% 而 ToT 达 74%。
- **与主题关联**：把「规划」实现为对云端 LLM 的多路调用与自评选择，本地只做搜索编排，无需本地算力即可获得审慎规划能力。

#### 013｜Generative Agents: Interactive Simulacra of Human Behavior

- **检索号**：B-06　**类别**：B LLM 智能体基础架构与经典论文
- **作者 / 机构**：Joon Sung Park、Joseph C. O'Brien、Carrie J. Cai、Percy Liang、Michael S. Bernstein 等（Stanford University、Google Research）
- **时间**：2023-04　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2304.03442>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：store a complete record of the agent's experiences using natural language, synthesize those memories over time into higher-level reflections, and retrieve them dynamically to plan behavior
- **要点**：提出可模拟可信人类行为的生成式智能体架构，用自然语言完整记录经历、把记忆逐步综合为更高层反思、并动态检索以规划行为。在类《模拟人生》沙盒中 25 个智能体仅凭一条「想办情人节派对」的设定，便自发传播邀请、结交、约会并协同准时到场；消融表明观察、规划、反思三者都关键。
- **与主题关联**：证明记忆、反思、规划与自主发起行为可由「LLM + 外部存储检索」支撑，家用机只需编排云端模型与本地记忆库即可让助理自主触发、带记忆、会规划。

#### 014｜MemGPT: Towards LLMs as Operating Systems

- **检索号**：B-07　**类别**：B LLM 智能体基础架构与经典论文
- **作者 / 机构**：Charles Packer、Sarah Wooders、Kevin Lin、Ion Stoica、Joseph E. Gonzalez 等（UC Berkeley）
- **时间**：2023-10　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2310.08560>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：virtual context management, a technique drawing inspiration from hierarchical memory systems in traditional operating systems
- **要点**：受操作系统分层内存启发提出「虚拟上下文管理」，让系统在快慢存储间搬运数据以突破 LLM 有限上下文窗口，并用中断管理自身与用户之间的控制流。在文档分析上可处理远超底层 LLM 上下文长度的文档，在多会话聊天上可创建能记忆、反思、随长期交互动态演化的对话智能体。
- **与主题关联**：把长期记忆做成操作系统式的外置分层管理，本地只需调度上下文，云端 LLM 提供推理，支撑常驻个人助理跨会话不遗忘。

#### 015｜Cognitive Architectures for Language Agents

- **检索号**：B-08　**类别**：B LLM 智能体基础架构与经典论文
- **作者 / 机构**：Theodore R. Sumers、Shunyu Yao、Karthik Narasimhan、Thomas L. Griffiths（Princeton University）
- **时间**：2023-09　**类型**：期刊论文（TMLR；arXiv 预印本 v3 标注为 TMLR camera ready 版）
- **出处**：<https://arxiv.org/abs/2309.02427>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：describes a language agent with modular memory components, a structured action space to interact with internal memory and external environments
- **要点**：借鉴认知科学与符号 AI 提出 CoALA 认知架构，用模块化记忆组件、与内部记忆及外部环境交互的结构化动作空间、以及通用的动作选择决策过程来刻画语言智能体。以此回顾并组织大量近期工作，并前瞻性指出通往更强智能体的方向，为把 LLM 放进经典 AI 脉络提供统一框架。
- **与主题关联**：给出「记忆 + 动作空间 + 决策循环」的通用蓝图，说明主动式助理是编排问题而非本地算力问题，家用机按此架构调用云端 LLM 即可搭建。

#### 016｜HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face

- **检索号**：B-09　**类别**：B LLM 智能体基础架构与经典论文
- **作者 / 机构**：Yongliang Shen、Kaitao Song、Xu Tan、Dongsheng Li、Weiming Lu、Yueting Zhuang（浙江大学、Microsoft Research Asia）
- **时间**：2023-03　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2303.17580>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：LLMs could act as a controller to manage existing AI models to solve complicated AI tasks
- **要点**：主张以 LLM 作控制器、以语言为通用接口管理既有 AI 模型来解决复杂任务，提出 HuggingGPT：收到请求后由 ChatGPT 做任务规划，按 Hugging Face 模型功能描述选模型、执行各子任务并汇总结果。借助 ChatGPT 的语言能力与社区海量模型，可覆盖语言、视觉、语音等多模态多领域复杂任务。
- **与主题关联**：是「家用机当编排器、云端 LLM 当大脑、外部模型/工具当手脚」的直接范例，复杂能力全部经 API 调度获得。

#### 017｜MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework

- **检索号**：B-10　**类别**：B LLM 智能体基础架构与经典论文
- **作者 / 机构**：Sirui Hong、Mingchen Zhuge、Jiaqi Chen、Jürgen Schmidhuber 等（DeepWisdom、KAUST 等）
- **时间**：2023-08　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2308.00352>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：encodes Standardized Operating Procedures (SOPs) into prompt sequences for more streamlined workflows
- **要点**：针对多智能体简单串联 LLM 易生级联幻觉的问题，提出把标准化操作流程（SOP）编码进提示序列的元编程框架，让具备类人领域专长的智能体验证中间结果、减少错误，并以流水线范式分配多样角色、把复杂任务拆解给多智能体协作。在协作式软件工程基准上生成比此前基于聊天的多智能体系统更连贯的解决方案。
- **与主题关联**：展示多智能体协作与任务分解可由提示词与 API 编排实现，家用机无需本地大模型即可组建分工协作的常驻助理团队。

### C 类｜国际云厂商 LLM API 官方文档（8 篇）

#### 018｜Structured model outputs | OpenAI API

- **检索号**：C-01　**类别**：C 国际云厂商 LLM API 官方文档
- **作者 / 机构**：OpenAI
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://platform.openai.com/docs/guides/structured-outputs>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验
- **页面依据**：章节 "Structured Outputs vs JSON mode"、"When to use Structured Outputs via function calling vs via text.format"；请求参数 `text: { format: { type: "json_schema", "strict": true, "schema": ... } }` 与 `response_format: {type: "json_schema", ...}`；原文短语 "Reliable type-safety"
- **要点**：定义 Structured Outputs 能力，要求模型输出严格符合开发者提供的 JSON Schema，通过 `text.format`／`response_format` 的 `json_schema` 加 `strict: true` 开启，并列出支持模型与 JSON Schema 约束。页面明确区分结构化输出、JSON mode 与经由 function calling 的约束路径，说明其"无需校验或重试格式错误响应"的类型安全保证。
- **与主题关联**：家用机把助理的决策结果（待办、日程、动作指令）交给云端按 Schema 稳定产出，本地只做轻量解析与执行，无需本地模型即可获得可编排的结构化状态。

#### 019｜Tool use with Claude - Claude Platform Docs

- **检索号**：C-03　**类别**：C 国际云厂商 LLM API 官方文档
- **作者 / 机构**：Anthropic
- **时间**：n.d.（官方文档）　**类型**：官方 API 文档
- **出处**：<https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview>
- **核验**：直连 200 · 页面标题为站点通用标题或重定向页，已按正文核验；二次抓取确认「Tool use with Claude - Claude Platform Docs」
- **页面依据**：章节 "How tool use works"、"When Claude uses tools"、"Choose a tool"、"Pricing"；原文 "Tool use (also called function calling) lets Claude call functions that you define or that Anthropic provides."；参数与字段 `tools`、`input_schema`、`tool_choice={"type": "auto"}`、`stop_reason: "tool_use"`、`tool_use`、`tool_result`、`strict: true`
- **要点**：完整定义 Claude 的工具调用（function calling）机制，区分在应用侧执行的 client tools 与在 Anthropic 基础设施执行的 server tools（web_search、code_execution 等），并给出 `tool_use` → 本地执行 → `tool_result` 回传的 agentic loop 往返流程。页面还规定 `tool_choice` 的自动／强制行为、strict tool use 的 schema 强一致、以及工具调用按 `tools` 参数 token 与服务端用量计费的定价结构。
- **与主题关联**：这是"主动式代理"的核心一环——家用机只需注册本地函数、把云端返回的 `tool_use` 执行后回传，即可让助理主动查信息、跑脚本、操作系统，而无需本地跑模型。

#### 020｜Function calling with the Gemini API - Gemini API | Google AI Studio

- **检索号**：C-05　**类别**：C 国际云厂商 LLM API 官方文档
- **作者 / 机构**：Google（Gemini API / Google AI Studio）
- **时间**：n.d.（官方文档）　**类型**：官方 API 文档
- **出处**：<https://ai.google.dev/gemini-api/docs/function-calling>
- **核验**：本机直连受代理链路影响（代理 502 / SSL 超时）；二次抓取确认「Function calling with the Gemini API - Gemini API | Google AI Studio」
- **页面依据**：章节 "How function calling works"、"Function calling modes"、"Parallel function calling"、"Compositional function calling"、"Stream tool calls"、"Remote MCP (Model Context Protocol)"；原文 "Function calling lets you connect models to external tools and APIs."；参数 `tools`、`tool_choice`（`auto`／`any`／`none`／`validated`）、`previous_interaction_id`、`function_call`、`function_result`
- **要点**：定义 Gemini 的函数调用流程，通过 `tools` 传入函数声明、`generation_config`／`tool_choice` 控制调用模式，并支持并行调用、组合式多步调用与流式工具调用。页面还覆盖 Remote MCP 服务器接入、结构化输出与函数调用的配合以及函数声明的 JSON Schema 字段，给出从声明、调用、执行到结果回传的四步链路。
- **与主题关联**：家用机把操作系统、日历、家居设备封装成函数声明交给云端，模型自主决定调用顺序并串起多步任务，本机只负责执行回传，形成主动式代理的行动层。

#### 021｜Function Calling | Mistral Docs

- **检索号**：C-06　**类别**：C 国际云厂商 LLM API 官方文档
- **作者 / 机构**：Mistral AI
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://docs.mistral.ai/capabilities/function_calling>
- **核验**：本机直连受代理链路影响（代理 502 / SSL 超时）；二次抓取确认「Function Calling | Mistral Docs」
- **页面依据**：章节 "Five Steps"（Step 1–5）、"Full Example"；参数 `client.chat.complete(...)` 中的 `tools`、`tool_choice`（`auto`／`any`／`none`）、`parallel_tool_calls`；字段 `tool_calls`、`tool_call.function.arguments`、`tool_call_id`；原文 "allows Mistral models to connect to external local tools"
- **要点**：以"五步"流程定义 Mistral 的函数调用：开发者定义函数与系统提示、用户提问、模型生成函数参数、开发者执行函数、模型生成最终回答。页面规定 `tools` 中的 `function`／`parameters` JSON Schema、`tool_choice` 三种取值与 `parallel_tool_calls` 开关，以及 `response.choices[0].message.tool_calls` 的读取方式。
- **与主题关联**：提供又一家可替换的云端后端，家用机用同一套"声明工具—执行—回传"编排即可切换模型厂商，避免被单一供应商锁定，也无需本地算力。

#### 022｜Basic usage of tool use (function calling) | Cohere

- **检索号**：C-07　**类别**：C 国际云厂商 LLM API 官方文档
- **作者 / 机构**：Cohere
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://docs.cohere.com/docs/tool-use>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：章节 "Tool use workflow"、"State management"、"Multi-step tool use (agents)"、"Parallel tool calling"；调用 `co.chat(model="command-a-plus-05-2026", messages=messages, tools=tools)`；字段 `tool_plan`、`tool_calls`、`tool_call_id`、citations；原文 "Tool use connects models to external tools like search engines and APIs."
- **要点**：以端到端示例定义 Cohere Chat endpoint 的工具使用：`tools` 定义函数 schema，模型先产出 `tool_plan` 与 `tool_calls`，应用执行后以 `role="tool"` 消息回传，并在 `messages` 中做状态管理以支撑多步代理。页面还说明带引用的响应生成、并行工具调用与 `Step 1`–`Step 4` 的显式工作流。
- **与主题关联**：文档把"多步工具使用（agents）"和状态管理写进 API 用法，家用机可据此让常驻助理跨轮次持续跟踪任务状态，而不必在本地维护大模型推理。

#### 023｜Tool Use Overview - GroqDocs

- **检索号**：C-08　**类别**：C 国际云厂商 LLM API 官方文档
- **作者 / 机构**：Groq
- **时间**：n.d.（官方文档）　**类型**：官方 API 文档
- **出处**：<https://console.groq.com/docs/tool-use>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验；二次抓取确认「Tool Use Overview - GroqDocs」
- **页面依据**：章节 "How Tool Use Works"、"Groq Built-In Tools"、"Remote Tool Calling with MCP"、"Local Tool Calling (Function Calling)"、"Why Groq's Speed Matters"；原文 "Tool use (or function calling) is what transforms a language model from a conversational interface into an autonomous agent capable of taking action"；参数 `tools`、`tool_calls`、`tool_call_id`、`parallel tool use`
- **要点**：定义工具调用的四步循环（请求带 `tools` 定义→模型返回 `tool_calls`→执行并回传 `tool_result`→模型继续或结束），并对比三种模式：Groq 内置工具、经 MCP 的远端工具、本地函数调用，还列出支持模型的并行工具与 JSON mode 能力表。页面强调代理循环常需 2–10+ 次推理调用，而 Groq 的 300–1,000+ tokens/秒推理速度使多步代理体验接近瞬时。
- **与主题关联**：主动式代理是多轮推理密集负载，家用机把推理全部外包给高速云端即可获得"即时"响应，本地仅承担工具执行，正是"不本地跑大模型"的直接论据。

#### 024｜OpenRouter Quickstart Guide

- **检索号**：C-09　**类别**：C 国际云厂商 LLM API 官方文档
- **作者 / 机构**：OpenRouter
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://openrouter.ai/docs/quickstart>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：章节 "Using the OpenRouter API"、"Using the Client SDKs"、"Using the Agent SDK"、"Using the OpenAI SDK"；原文 "OpenRouter gives you access to hundreds of AI models through a single API endpoint. It handles fallbacks automatically and picks the most cost-effective option for each request."；`/api/v1/responses`、`@openrouter/agent`、`callModel`、`@openrouter/sdk`、`GET /api/v1/models`、链接 "free models and rate limits" FAQ
- **要点**：定义通过单一 `POST /api/v1/responses` 端点访问数百个模型的接入方式，说明三种集成路径：原生 API、类型安全的 Client SDK、以及处理多轮循环／工具执行／状态管理的 Agent SDK（`callModel`）。页面还说明自动 fallback、按成本选路、OpenAI SDK 作为 drop-in 替换、可选的 `HTTP-Referer`／`X-OpenRouter-Title` 归属头，以及免费模型与速率限制 FAQ 入口。
- **与主题关联**：家用机只需一个 API Key 和一个端点即可在多家模型间自动切换与降级，Agent SDK 把工具循环与状态管理托管到云端侧能力，是"轻本地、重编排"最省事的落地形态。

#### 025｜Function calling patterns - Together AI docs

- **检索号**：C-10　**类别**：C 国际云厂商 LLM API 官方文档
- **作者 / 机构**：Together AI
- **时间**：n.d.（官方文档）　**类型**：官方参考
- **出处**：<https://docs.together.ai/docs/function-calling>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验；二次抓取确认「Function calling patterns - Together AI docs」
- **页面依据**：章节 "Patterns"、"Supported models"、"Next steps"；原文 "Function calling lets LLMs respond with structured function names and arguments your application can execute."；参数 `tools`、`tool_calls`；模式条目 "Simple"、"Parallel"、"Multi-step"、"Multi-turn"、"Agentic patterns"
- **要点**：把函数调用归纳为 Simple／Multiple／Parallel／Parallel multiple／Multi-step／Multi-turn／Vision 七种模式，并给出各自适用场景与可运行示例入口，说明向 `tools` 参数传函数描述、模型返回 `tool_calls` 后由应用执行并可回传结果。页面还提供支持函数调用的 serverless 与专用端点模型目录指引。
- **与主题关联**：文档把"多步、多轮、人在回路"的代理模式直接列为标准用法，家用机按模式表选择编排方式即可让云端模型持续推进任务，无需本地承载模型推理。

### D 类｜国内大模型平台官方 API 文档（9 篇）

#### 026｜首次调用 API | DeepSeek API Docs

- **检索号**：D-01　**类别**：D 国内大模型平台官方 API 文档
- **作者 / 机构**：深度求索 DeepSeek（DeepSeek API Docs / 开放平台）
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://platform.deepseek.com/api-docs/zh-cn/api/deepseek-api>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："DeepSeek API 使用与 OpenAI/Anthropic 兼容的 API 格式"、"您可以将 stream 设置为 true 来使用流式输出"、`https://api.deepseek.com/chat/completions`、`"model": "deepseek-flash"`、`"stream": false`
- **要点**：页面给出 curl/Python/Node 三种首次调用对话补全的样例，并说明 API 采用与 OpenAI/Anthropic 兼容的格式、只需替换 base_url 与 api_key。示例明确用 `stream` 参数在流式与非流式之间切换。
- **与主题关联**：家用机只需按 OpenAI 兼容格式发一个 HTTP 请求即可调用云端模型，无需本地部署权重。

#### 027｜DeepSeek API 创新采用硬盘缓存，价格再降一个数量级

- **检索号**：D-02　**类别**：D 国内大模型平台官方 API 文档
- **作者 / 机构**：深度求索 DeepSeek（DeepSeek API Docs）
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://api-docs.deepseek.com/zh-cn/news/news0802>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："上下文硬盘缓存技术"、"缓存命中的部分，DeepSeek 收费 0.1元 每百万 tokens"、`prompt_cache_hit_tokens`、`prompt_cache_miss_tokens`、"对所有用户均不限流、不限并发"、"最高可以节省 90% 的费用"
- **要点**：官方说明上下文硬盘缓存自动生效、无需修改代码，重复前缀按缓存命中计费，并在 usage 中返回命中/未命中 token 数。文档同时给出定价、缓存命中率与并发限流说明。
- **与主题关联**：常驻助理的长系统提示与多轮历史由云端缓存承担，家用机既不存权重也不承担重复上下文的算力与成本。

#### 028｜如何通过Function Calling 实现工具调用-大模型服务平台百炼(Model Studio)-阿里云帮助中心

- **检索号**：D-03　**类别**：D 国内大模型平台官方 API 文档
- **作者 / 机构**：阿里云 · 大模型服务平台百炼（Model Studio）/ 阿里云帮助中心
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://help.aliyun.com/zh/model-studio/qwen-function-calling>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Function Calling 允许模型调用外部工具（API、数据库、自定义函数等）"、"方式一：通过 tools 参数传入（推荐）"、`tool_calls`、`tool_choice`、`parallel_tool_calls`、`tool_call_id`、章节"流式输出"、"运行工具函数的过程由您的计算环境而非大模型来完成"
- **要点**：文档完整描述"定义工具→发起调用→应用端执行工具→回传结果→模型总结"的多步 Function Calling 流程，并列出 tools、tool_calls、tool_choice、parallel_tool_calls 等参数。还给出并行工具调用、强制工具调用、流式输出与 Responses API 工具调用等进阶用法。
- **与主题关联**：明确"工具在本地执行、模型在云端决策"，正是家用机只做编排、把推理交给云端的分工依据。

#### 029｜首次调用千问API-大模型服务平台百炼(Model Studio)-阿里云帮助中心

- **检索号**：D-04　**类别**：D 国内大模型平台官方 API 文档
- **作者 / 机构**：阿里云 · 大模型服务平台百炼（Model Studio）/ 阿里云帮助中心
- **时间**：2026　**类型**：官方指南
- **出处**：<https://help.aliyun.com/zh/model-studio/product-overview/call-qwen-by-calling-api>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："阿里云百炼支持通过 API 调用大模型，涵盖 OpenAI 兼容接口、DashScope SDK 等接入方式"、`compatible-mode/v1/chat/completions`、`https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1`、"API 调用与操作系统版本无关，只要网络能连通即可正常使用"、`messages`、`model="qwen-plus"`
- **要点**：页面按账号、API Key、环境变量、SDK 安装的顺序引导完成首次 API 调用，并给出 Python/Node.js/curl/Go/PHP/C# 的 OpenAI 兼容 HTTP 示例。原文明确"API 调用与操作系统版本无关，只要网络能连通即可正常使用"。
- **与主题关联**：直接证明常驻助理对本地硬件无要求，只要一台能联网的家用机按兼容接口编排即可。

#### 030｜GLM-5 - 智谱AI开放文档

- **检索号**：D-05　**类别**：D 国内大模型平台官方 API 文档
- **作者 / 机构**：智谱 AI（智谱AI开放文档 / bigmodel.cn 开放平台）
- **时间**：n.d.（官方文档）　**类型**：官方参考
- **出处**：<https://docs.bigmodel.cn/cn/guide/models/text/glm-5>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："面向 Agentic Engineering 打造"、"MCP 可灵活调用外部 MCP 工具与数据源"、"MCP-Atlas（工具调用和多步骤任务执行）"、`https://open.bigmodel.cn/api/paas/v4/chat/completions`、`"stream": true`"启用流式输出"、`thinking`、`max_tokens`
- **要点**：模型页列出 200K 上下文窗口与 Agent、工具调用、MCP 等能力，并给出 cURL、Python、Java 的基础调用与流式调用示例。示例展示 `chat/completions` 端点与 `stream: true` 的流式返回处理。
- **与主题关联**：云端模型原生具备长程 Agent 与工具调用能力，编排逻辑放在家用机即可驱动主动式助理。

#### 031｜如何在 Kimi API 中使用官方工具 - Kimi API 开放平台

- **检索号**：D-06　**类别**：D 国内大模型平台官方 API 文档
- **作者 / 机构**：月之暗面 Moonshot AI（Kimi API 开放平台）
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://platform.moonshot.cn/docs/guide/use-official-tools>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Formula API 官方工具通道（OpenAI 协议，标准 `function` tool）"、`POST /v1/chat/completions`、`tools`、`tool_calls`、`finish_reason=tool_calls`、`tool_call_id`、章节"在 Chat Completions 中接入官方工具"
- **要点**：文档说明如何在 Chat Completions API 中通过标准 `function` tool 协议接入官方工具（联网搜索、记忆、Excel、日期、fetch 等），并给出四步调用链路与完整 Python 示例。工具由平台以 Formula 形式托管执行，本地仅负责拼接 messages 与回传 tool 结果。
- **与主题关联**：连工具执行都能托管到云端，家用机只需做请求编排与结果拼装，最适合轻量常驻助理。

#### 032｜混元 OpenAI 兼容接口相关调用示例（腾讯混元大模型 兼容接口 - Tencent Cloud）

- **检索号**：D-07　**类别**：D 国内大模型平台官方 API 文档
- **作者 / 机构**：腾讯云 · 腾讯混元大模型（Tencent Cloud 文档中心）
- **时间**：2026　**类型**：官方 API 文档
- **出处**：<https://cloud.tencent.com/document/product/1729/111007>
- **核验**：直连 200 · 页面标题为站点通用标题或重定向页，已按正文核验；二次抓取确认「腾讯混元大模型 混元 OpenAI 兼容接口相关调用示例_腾讯云」
- **页面依据**："混元 API 兼容了 OpenAI 的接口规范，这意味着您可以直接使用 OpenAI 官方提供的 SDK 来调用混元大模型"、`base_url：https://api.hunyuan.cloud.tencent.com/v1`、`https://api.hunyuan.cloud.tencent.com/v1/chat/completions`、章节"Function Calling"、`tools`、`tool_calls`、`finish_reason`
- **要点**：页面提供对话、多轮对话、图生文、Function Calling、Embedding 的 OpenAI 兼容调用示例，并强调仅替换 `base_url` 和 `api_key` 即可无缝迁移。还列出 `tools`、`tool_calls`、`tool_call_id` 等字段与"默认限制为5个并发"的配额说明。
- **与主题关联**：一套 OpenAI SDK 即可接入云端混元，家用机不用改应用架构就能编排对话与函数调用。

#### 033｜Create a Chat Completion

- **检索号**：D-08　**类别**：D 国内大模型平台官方 API 文档
- **作者 / 机构**：硅基流动 SiliconFlow（SiliconFlow 文档中心）
- **时间**：n.d.（官方文档）　**类型**：官方 API 文档
- **出处**：<https://docs.siliconflow.cn/cn/api-reference/chat-completions/chat-completions>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`stream` "Server-Sent Events"、"data: [DONE]"、`response_format`、`{ "type": "json_schema", "json_schema": {...} }` "enables Structured Outputs"、`tools` "A list of tools the model may call"、`429` "Request was rejected due to rate limiting"、"TPM limit reached"、`prompt_cache_hit_tokens`、`https://api.siliconflow.cn/v1/chat/completions`
- **要点**：官方 Chat Completions API 参考列出 model、messages、stream、response_format（json_schema 结构化输出）、tools、reasoning_effort 等参数，并给出 OpenAI SDK（base_url 指向 `api.siliconflow.cn/v1`）与 Function Calling 流式示例。响应示例含 `prompt_cache_hit_tokens`、`prompt_cache_miss_tokens`，错误码含 429 限流。
- **与主题关联**：结构化输出、流式、工具调用与限流配额全部由云端 API 提供，家用机只处理编排与解析。

#### 034｜豆包助手 - 火山方舟 - 火山引擎

- **检索号**：D-09　**类别**：D 国内大模型平台官方 API 文档
- **作者 / 机构**：火山引擎 · 火山方舟（字节跳动）
- **时间**：n.d.（官方文档）　**类型**：官方 API 文档
- **出处**：<https://www.volcengine.com/docs/82379/1978533>
- **核验**：直连 200 · 页面标题为站点通用标题或重定向页，已按正文核验；二次抓取确认「豆包助手 - 火山方舟 - 火山引擎（旧地址 200 并跳转新文档域）」
- **页面依据**："通过 Responses API，您可将豆包 App 同款 AI 能力…快速集成至自有应用"、`https://ark.cn-beijing.volces.com/api/v3/responses`、`"stream": true`、`tools`、`store`、`previous_response_id`、"Function Calling（函数调用）"、"单个账号调用频率上限为 2 QPS"
- **要点**：文档说明豆包助手 API 通过 Responses API 以 tools 方式提供日常沟通、深度沟通、联网搜索、边想边搜，含 stream、store、previous_response_id 等参数与 cURL/Python/Java/Go 示例。并给出按次计费、2 QPS 默认限流及与 Function Calling 的互斥说明。
- **与主题关联**：连搜索、角色设定与上下文保存都由云端工具托管，家用机只需编排 responses 请求即可获得常驻助理能力。

### E 类｜智能体编排框架与 SDK 官方文档（9 篇）

#### 035｜LangGraph overview - Docs by LangChain

- **检索号**：E-01　**类别**：E 智能体编排框架与 SDK 官方文档
- **作者 / 机构**：LangChain, Inc.（LangGraph 团队）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://docs.langchain.com/oss/python/langgraph/overview>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Low-level orchestration framework and runtime for long-running, stateful agents；durable execution, streaming, human-in-the-loop, and persistence；Persistence: Checkpoint state and resume after failures or pauses.
- **要点**：以"共享 state + nodes + edges"的图定义工作流，把确定性节点与 LLM 驱动节点混排在同一图内；运行时原语提供 Persistence（Checkpoint state and resume after failures or pauses）、Human-in-the-loop（Pause execution, inspect or edit state, then continue）与 Memory（Short-term thread state and longer-term memory across sessions）。
- **与主题关联**：状态保存、中断恢复与长时循环都被做成编排层能力，家用机只需运行轻量图调度并把推理交给云端 LLM API。

#### 036｜Quickstart - OpenAI Agents SDK

- **检索号**：E-02　**类别**：E 智能体编排框架与 SDK 官方文档
- **作者 / 机构**：OpenAI
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://openai.github.io/openai-agents-python/quickstart>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Give your agent tools；The runner handles executing individual agents, any handoffs, and any tool calls.；Full manual control and provider-agnostic history
- **要点**：用 Agent（instructions + name + model）与 Runner.run 组成最小智能体循环，通过 @tool 装饰器注册函数工具、通过 handoffs 列表在多个 specialist agent 之间转交；Quickstart 明确列出 session=... 由 SDK 保存历史以及 provider-agnostic history 的记忆策略。
- **与主题关联**：几行代码即可在本地跑"智能体循环 + 工具注册 + 多智能体转交"，模型推理全部由云端 API 承担。

#### 037｜Get started - Agent Development Kit (ADK)

- **检索号**：E-03　**类别**：E 智能体编排框架与 SDK 官方文档
- **作者 / 机构**：Google（Agent Development Kit / google/adk-docs）
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://google.github.io/adk-docs/get-started/quickstart>
- **核验**：本机直连受代理链路影响（代理 502 / SSL 超时）；二次抓取确认「Get started - Agent Development Kit (ADK)」
- **页面依据**：Agent Development Kit (ADK) is designed to empower developers to quickly build, manage, evaluate and deploy AI-powered agents.；Python Quickstart；Migrate existing agents and workflows to ADK with Agents CLI.
- **要点**：官方给出 Python / TypeScript / Go / Java / Kotlin 多语言 Quickstart 以及 Agents CLI Quickstart，均为 code-first 地创建、管理与部署 agent；页面还单列 Migrate to ADK，用于把既有 agents and workflows 迁入 ADK。
- **与主题关联**：ADK 把"定义 agent 与工作流"放在本地开发侧，部署与模型调用交给托管服务/API，家用机不承担算力。

#### 038｜AutoGen — AutoGen

- **检索号**：E-04　**类别**：E 智能体编排框架与 SDK 官方文档
- **作者 / 机构**：Microsoft（AutoGen 团队 / microsoft/autogen）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://microsoft.github.io/autogen>
- **核验**：直连 200 · 页面标题为站点通用标题或重定向页，已按正文核验
- **页面依据**：A programming framework for building conversational single and multi-agent applications.；An event-driven programming framework for building scalable multi-agent AI systems.；Deterministic and dynamic agentic workflows for business processes.
- **要点**：分层提供 AgentChat（对话式单/多智能体）、Core（事件驱动、可分布式的多智能体运行时，用于 Deterministic and dynamic agentic workflows）与 Extensions（MCP 工具、代码执行器、gRPC 分布式 runtime 等）；首页示例以 OpenAIChatCompletionClient(model="gpt-4o") 把模型作为可替换客户端接入。
- **与主题关联**：本地只跑事件驱动的多智能体编排与工具调度，模型通过 model client 指向云端 LLM API。

#### 039｜Semantic Kernel documentation | Microsoft Learn

- **检索号**：E-05　**类别**：E 智能体编排框架与 SDK 官方文档
- **作者 / 机构**：Microsoft（Microsoft Learn / Semantic Kernel 团队）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://learn.microsoft.com/en-us/semantic-kernel>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Concepts — Kernel、Plugins、Memory；Frameworks — Process Framework、Agent Framework；Learn to build robust, future-proof AI solutions that evolve with technological advancements.
- **要点**：以 Kernel 作为容器统一组织 AI 服务、Plugins 与 Memory，并在 Frameworks 下提供 Process Framework（有状态多步流程）与 Agent Framework 两类编排能力；文档自述其目标是 future-proof、可随模型技术演进的 AI 方案，即底层模型服务可替换。
- **与主题关联**：Kernel/Plugins/Memory 只是把云模型调用与本地函数封装成可组合编排单元，家用机是编排宿主而非推理硬件。

#### 040｜GitHub - crewAIInc/crewAI: Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. · GitHub

- **检索号**：E-06　**类别**：E 智能体编排框架与 SDK 官方文档
- **作者 / 机构**：CrewAI Inc.（crewAIInc/crewAI）
- **时间**：n.d.（官方文档）　**类型**：官方 GitHub 仓库 README
- **出处**：<https://github.com/crewAIInc/crewAI>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Flows offer precise, event-driven control；with `@start`, `@listen`, or `@router` decorators；Crews provide autonomous agent collaboration；Understanding Flows and Crews
- **要点**：README 把能力拆成 Crews（Crews provide autonomous agent collaboration）与 Flows（Flows offer precise, event-driven control），Flow 用 @start / @listen / @router 装饰器组织事件驱动分支；并设 Using Crews and Flows Together、Connecting Your Crew to a Model、Can CrewAI automate human-in-the-loop workflows? 等章节。
- **与主题关联**：Crew/Flow 的状态机与事件回调都在本地进程内运行，而 Crew 所连接的模型可指向云端 LLM API。

#### 041｜Introduction | Developer Documentation（LlamaIndex Workflows）

- **检索号**：E-07　**类别**：E 智能体编排框架与 SDK 官方文档
- **作者 / 机构**：LlamaIndex, Inc.（run-llama / LlamaIndex）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://developers.llamaindex.ai/python/llamaagents/workflows>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：A workflow is an event-driven, step-based way to control the execution flow of an application.；Loops are steps that return an event handled by an earlier step.；workflow runs can be interactive and stateful. In this case, to collect input from a human.
- **要点**：以 @step 与 Event 的输入/输出类型推断数据流并在运行前校验 event graph；原生提供 Loops（步骤返回由更早步骤处理的事件）、Branches and loops、有状态运行与 human-in-the-loop 输入收集，章节含 Defining Workflow Events、Workflow Entry Points、Workflow Exit Points、Validation、Examples。
- **与主题关联**：把循环、分支、状态与人机协同固化为本地工作流图，步骤里的 LLM 调用走云端 API 即可。

#### 042｜Pydantic AI | Pydantic Docs

- **检索号**：E-08　**类别**：E 智能体编排框架与 SDK 官方文档
- **作者 / 机构**：Pydantic（PydanticAI 团队）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://ai.pydantic.dev>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Any model, one Python API.；typed dependency injection, typed tools；Agents, realtime voice, image generation, embeddings.
- **要点**：以一套 Python API 屏蔽不同模型供应商差异（Any model, one Python API），并用 Pydantic 类型系统实现 typed dependency injection 与 typed tools 的结构化校验；文档章节覆盖 What are you building?、Why Pydantic AI、Putting it together: a bank support agent、Instrumentation with Pydantic Logfire。
- **与主题关联**：本地只做类型化的工具/依赖编排与结果校验，模型可任意指向云端 LLM API。

#### 043｜smolagents/README.md at main · huggingface/smolagents · GitHub

- **检索号**：E-09　**类别**：E 智能体编排框架与 SDK 官方文档
- **作者 / 机构**：Hugging Face（huggingface/smolagents）
- **时间**：n.d.（官方文档）　**类型**：官方 GitHub 仓库 README
- **出处**：<https://github.com/huggingface/smolagents/blob/main/README.md>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Model-agnostic: smolagents supports any LLM.；Our library is LLM-agnostic: you could switch the example above to any inference provider.；First-class support for Code Agents. Our CodeAgent writes its actions in code；LiteLLM to access 100+ LLMs
- **要点**：README 明确 Model-agnostic 与 Tool-agnostic：通过 InferenceClientModel（HF inference providers 网关）、LiteLLMModel（100+ LLMs）、OpenAIModel、AzureOpenAIModel、AmazonBedrockModel 等把模型作为可替换组件；CodeAgent 以 Python 代码片段作为动作来发起工具调用，主体逻辑集中在约 1,000 行的 agents.py。
- **与主题关联**：极简库在本地只负责"想代码 + 调工具"的循环，LLM 推理通过 model 对象指向任意云端 API 供应商。

### F 类｜家用机自托管编排 / 自动化平台官方文档（8 篇）

#### 044｜Schedule Trigger | Nodes | n8n Docs

- **检索号**：F-01　**类别**：F 家用机自托管编排 / 自动化平台官方文档
- **作者 / 机构**：n8n 官方（n8n Docs）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Use the Schedule Trigger node to run workflows at fixed intervals and times. This works in a similar way to the Cron software utility in Unix-like systems."；章节 "Custom (Cron) interval"；"You must publish the workflow"
- **要点**：该节点按秒、分、时、日、周、月或自定义 Cron 表达式触发工作流，可在同一节点叠加多条 Trigger Rules 并设置停机后 missed execution 的补跑策略。使用定时触发必须保存并发布工作流，自托管实例默认时区为 `America/New York`，可通过环境变量调整。
- **与主题关联**：为自托管在家用机上的 n8n 提供纯时间驱动的主动触发，使常驻工作流能定时唤起云端 LLM API 而无需人工发起。

#### 045｜HTTP Request | Nodes | n8n Docs

- **检索号**：F-02　**类别**：F 家用机自托管编排 / 自动化平台官方文档
- **作者 / 机构**：n8n 官方（n8n Docs）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："HTTP Request"；"make HTTP requests to query data from any app or service with a REST API"；"you're creating a REST API call"；章节 "Import curl command"
- **要点**：节点可配置 Method、URL、Send Query Parameters、Send Headers、Send Body（JSON / Form-Data / Raw 等）与 Pagination，并支持直接导入 curl 命令。官方 FAQ 专设 "How do I call an API without writing code?"，明确其定位是零代码构造 REST 调用。
- **与主题关联**：让常驻工作流主动向云端 LLM API 发起 HTTP/REST 请求，是"编排 + 云 API"取代本地模型的关键执行节点。

#### 046｜Automation triggers - Home Assistant

- **检索号**：F-03　**类别**：F 家用机自托管编排 / 自动化平台官方文档
- **作者 / 机构**：Home Assistant 官方文档团队
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://www.home-assistant.io/docs/automation/trigger>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Automation triggers"；"A trigger is the part of an automation that makes the automation start when something specific happens"；"Types of triggers" 章节下的 "Time trigger"、"Time pattern trigger"、"State changed trigger"、"Webhook trigger"、"Numeric state crossed threshold trigger"、"MQTT trigger"、"Zone trigger"
- **要点**：官方把触发器定义为"当特定事情发生时启动自动化"的部分，并列出时间、时间模式、状态变化、数值越阈、Webhook、MQTT、Zone、Sun、Template 等十余种类型。文档同时说明多触发器并存、YAML 写法、Trigger ID 以及按不同触发器分支执行动作。
- **与主题关联**：把时间、家庭传感器状态、Webhook 与 MQTT 事件统一变成自动化起点，正好对应"主动式助理"所需的事件触发底座。

#### 047｜Deploy Dify with Docker Compose - Dify Docs

- **检索号**：F-04　**类别**：F 家用机自托管编排 / 自动化平台官方文档
- **作者 / 机构**：Dify / LangGenius 官方（Dify Docs）
- **时间**：2026　**类型**：官方指南
- **出处**：<https://docs.dify.ai/en/self-host/deploy/quick-start/docker-compose>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Run Dify on one machine with Docker Compose"；"CPU: at least 2 cores"；"RAM: at least 4 GiB"；"docker compose up -d"
- **要点**：官方给出单机 Docker Compose 部署的最低硬件为 2 核 CPU、4 GiB 内存，并要求 Docker Compose 2.35.0 或更高版本。默认一键拉起 bundled PostgreSQL、Weaviate 等依赖服务，之后在 `http://localhost/install` 完成初始化。
- **与主题关联**：以官方最低配置证明工作流/agent 编排平台在普通家用机即可常驻自托管，而模型能力可由外部 API 提供。

#### 048｜Running Node-RED locally : Node-RED

- **检索号**：F-05　**类别**：F 家用机自托管编排 / 自动化平台官方文档
- **作者 / 机构**：Node-RED 项目官方（Node-RED Docs）
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://nodered.org/docs/getting-started/local>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Running Node-RED locally"；"sudo npm install -g node-red"；"docker run -it -p 1880:1880 --name mynodered nodered/node-red"；"Server now running at http://127.0.0.1:1880/"
- **要点**：官方给出在 Windows / Linux / Raspberry Pi 上以 npm 全局安装或 Docker 一条命令启动的方式，仅需受支持的 Node.js 版本，启动后编辑器在 `localhost:1880` 常驻、流程存于 `flows.json`。文末导航指向 "Starting Node-RED on boot"，支持开机自启。
- **与主题关联**：提供极轻量的家用机常驻运行时，配合 inject / http in 等节点即可实现定时与 Webhook 触发并转发云端 API。

#### 049｜Overview of installing Docker Compose | Docker Docs

- **检索号**：F-06　**类别**：F 家用机自托管编排 / 自动化平台官方文档
- **作者 / 机构**：Docker Inc. 官方（Docker Docs）
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://docs.docker.com/compose/install>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Overview of installing Docker Compose"；"The easiest and recommended way to get Docker Compose is to install Docker Desktop"；"Docker Desktop includes Docker Compose along with Docker Engine and Docker CLI which are Compose prerequisites"
- **要点**：官方推荐通过 Docker Desktop（Windows / Mac / Linux）获得 Compose，也可在 Linux 上单独安装 Compose plugin，独立 standalone 方式仅作向后兼容保留。Compose 与 Engine、CLI 一同构成运行多容器应用的前置条件。
- **与主题关联**：提供把 n8n、Dify、Huginn 等多个服务以容器方式长期常驻在同一台家用机上的统一部署底座。

#### 050｜GitHub - huginn/huginn: Create agents that monitor and act on your behalf. Your agents are standing by! · GitHub

- **检索号**：F-08　**类别**：F 家用机自托管编排 / 自动化平台官方文档
- **作者 / 机构**：Huginn 项目官方（GitHub 组织 huginn）
- **时间**：n.d.（官方文档）　**类型**：官方仓库
- **出处**：<https://github.com/huginn/huginn>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Create agents that monitor and act on your behalf. Your agents are standing by!"；"Try it with Docker"；"Docker Compose on your own server"；"always-on worker"
- **要点**：官方仓库把系统定义为可自建、代用户监控并行动的常驻 agent，README 提供 "Try it with Docker"、"Docker Compose on your own server"、"Manual installation on any server" 等自托管路径。文档说明部署形态包含持续运行的后台 worker，用于周期性轮询与事件响应。
- **与主题关联**：几乎是"主动式常驻个人助理"的原型：事件驱动的常驻 agent 可轮询邮件/网页并在条件满足时主动触发动作，再转交云端 LLM 处理。

#### 051｜Self-host | Windmill（正文 H1：Self-host Windmill）

- **检索号**：F-09　**类别**：F 家用机自托管编排 / 自动化平台官方文档
- **作者 / 机构**：Windmill Labs 官方（Windmill Docs）
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://www.windmill.dev/docs/advanced/self_host>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Self-host Windmill"；"Self-host Windmill on your own infrastructure."；"Using Docker and Caddy, Windmill can be deployed using 3 files:"；"docker compose up -d"；"Setup Windmill on localhost"
- **要点**：官方自托管页覆盖 Architecture、Docker、Helm chart、外部 PostgreSQL、Health endpoints、First time login 等章节，并给出在 localhost 用三个文件起服务的步骤。正文含 "Setup Windmill on localhost" 小节，明确支持单机本地部署。
- **与主题关联**：以脚本/工作流为单位的自托管编排器，可由定时与 Webhook 触发并调用任意 HTTP API，适合家用机常驻编排云端 LLM。

### G 类｜开放协议与工具调用标准（9 篇）

#### 052｜Specification - Model Context Protocol

- **检索号**：G-01　**类别**：G 开放协议与工具调用标准
- **作者 / 机构**：Model Context Protocol 项目（Anthropic 发起，现由 Linux Foundation 旗下 Agentic AI Foundation 托管）
- **时间**：2026-07-28（/specification/latest 现行版；页面链接标注 2026-07-28）　**类型**：官方规范
- **出处**：<https://modelcontextprotocol.io/specification/latest>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：This specification defines the authoritative protocol requirements, based on the TypeScript schema in schema.ts；The protocol uses JSON-RPC 2.0 messages；Tools: Functions for the AI model to execute；Hosts / Clients / Servers；页面链接 https://modelcontextprotocol.io/specification/2026-07-28
- **要点**：定义 MCP 的权威协议要求，采用 JSON-RPC 2.0 在 Hosts、Clients、Servers 之间通信，服务端以 Resources、Prompts、Tools 三类能力暴露上下文与可执行函数。现行 2026-07-28 版改为无状态、按请求协商能力，并提供 Tasks、Skills over MCP、MCP Apps 等可选扩展。
- **与主题关联**：家用机只要实现 MCP 客户端，就能用统一协议把本地文件、数据库与云端 API 等外部工具/数据源接入云端 LLM 的编排链路，而不必本地跑模型。

#### 053｜Architecture overview - Model Context Protocol

- **检索号**：G-02　**类别**：G 开放协议与工具调用标准
- **作者 / 机构**：Model Context Protocol 项目（Anthropic 发起，现由 Agentic AI Foundation 托管）
- **时间**：2026-07-28（文档版本，规范 URL 为 /docs/2026-07-28/learn/architecture）　**类型**：官方指南
- **出处**：<https://modelcontextprotocol.io/docs/learn/architecture>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：MCP follows a client-server architecture where an MCP host ... establishes connections to one or more MCP servers；MCP supports two transport mechanisms；Stdio transport: Uses standard input/output streams for direct process communication between local processes on the same machine；Streamable HTTP transport: Uses HTTP POST for client-to-server messages with optional Server-Sent Events；章节 Data layer / Transport layer / Primitives；tools/list；tools/call
- **要点**：说明 MCP 的分层架构（数据层 + 传输层）与 host/client/server 参与者，服务端原语 Tools、Resources、Prompts 通过 tools/list、tools/call 等方法被发现与执行。传输层规定两种机制：stdio 用于同机本地进程直连，Streamable HTTP（可配合 SSE）用于远程服务。
- **与主题关联**：直接给出家用机以 stdio 拉起本地 MCP server、以 Streamable HTTP 连接远程数据源的标准做法，是把外部工具接进编排器的实现依据。

#### 054｜GitHub - modelcontextprotocol/typescript-sdk: The official TypeScript SDK for Model Context Protocol servers and clients

- **检索号**：G-03　**类别**：G 开放协议与工具调用标准
- **作者 / 机构**：Model Context Protocol 项目（官方 SDK 维护方）
- **时间**：2026（main 分支 v2 稳定线，实现 2026-07-28 MCP 规范；仓库持续更新）　**类型**：官方 SDK 仓库
- **出处**：<https://github.com/modelcontextprotocol/typescript-sdk>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：This is the `main` branch: v2 of the SDK ... implementing the 2026-07-28 MCP spec；This repository contains the TypeScript SDK implementation of the MCP specification；MCP server libraries (tools/resources/prompts, Streamable HTTP, stdio, auth helpers)；npm install @modelcontextprotocol/server；MCP TypeScript SDK
- **要点**：官方 TypeScript SDK 提供 MCP server/client 库，覆盖 tools/resources/prompts 原语、stdio 与 Streamable HTTP 两种传输，并附带 Express、Fastify、Hono、Node.js HTTP 等运行时适配中间件。仓库同时给出可运行示例与构建首个 server/client 的入门教程。
- **与主题关联**：家用机可直接用官方 SDK 起一个本地 MCP server 暴露工具、或写客户端连接现成 MCP server，把外部数据源挂到云端 LLM 编排上。

#### 055｜OpenAPI Specification v3.1.0

- **检索号**：G-04　**类别**：G 开放协议与工具调用标准
- **作者 / 机构**：OpenAPI Initiative（编辑 Darrel Miller、Jeremy Whitlock、Marsh Gardiner、Mike Ralphson、Ron Ratovsky、Uri Sarid）
- **时间**：2021（Version 3.1.0，15 February 2021）　**类型**：官方规范
- **出处**：<https://spec.openapis.org/oas/v3.1.0.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：OpenAPI Specification v3.1.0；Version 3.1.0；15 February 2021；The source-of-truth for this specification is the HTML file referenced above as _This version_.；4.8.10 Operation Object；4.8.24 Schema Object；4.8.18 Callback Object；Copyright © 2021 the Linux Foundation
- **要点**：定义厂商中立、可移植的 HTTP API 描述格式，用 OpenAPI Document 描述 paths、operations、parameters、request/response、schema 与 callbacks 等对象，使机器可读地发现与调用 REST API。页面明确以该 HTML 文件为规范的权威来源，并给出版本、编辑者与修订历史。
- **与主题关联**：云端 LLM 的函数调用/工具描述可复用现成 OpenAPI 文档，把家用机能访问的 Web API 自动转成可编排的工具清单。

#### 056｜Specification — JSON Schema

- **检索号**：G-05　**类别**：G 开放协议与工具调用标准
- **作者 / 机构**：JSON Schema 组织（json-schema.org / json-schema-org）
- **时间**：2020-12（The current version is 2020-12!）　**类型**：官方规范
- **出处**：<https://json-schema.org/specification>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：The current version is *2020-12*! The previous version was 2019-09.；The specification is split into two parts, Core and Validation.；JSON Schema Core defines the basic foundation of JSON Schema；The latest meta-schema is **2020-12**.；Core/Validation Dialect meta-schema
- **要点**：定义用于标注与校验 JSON 文档的声明式语言，规范拆分为 Core（基础）与 Validation（校验关键字）两部分，并提供 2020-12 元模式、单一词汇表元模式与推荐输出结构。页面还列出各 draft 之间的迁移说明与按词汇表拆分的元模式链接。
- **与主题关联**：LLM 工具调用的参数/返回值以及 MCP 工具的 inputSchema 都以 JSON Schema 描述，家用机编排器据此生成并校验结构化工具参数。

#### 057｜HTML Living Standard — 9.2 Server-sent events

- **检索号**：G-06　**类别**：G 开放协议与工具调用标准
- **作者 / 机构**：WHATWG（Web Hypertext Application Technology Working Group）
- **时间**：n.d.（现行规范，Living Standard；页面标注 Last Updated 5 November 2026）　**类型**：标准文档
- **出处**：<https://html.spec.whatwg.org/multipage/server-sent-events.html>
- **核验**：直连 200 · 页面标题为站点通用标题或重定向页，已按正文核验
- **页面依据**：HTML Living Standard — Last Updated 5 November 2026；9.2 Server-sent events；9.2.2 The `EventSource` interface；To enable servers to push data to web pages over HTTP or using dedicated server-push protocols, this specification introduces the `EventSource` interface.；This event stream format's MIME type is `text/event-stream`.；Clients will reconnect if the connection is closed
- **要点**：规定服务器经 HTTP 向客户端单向推送事件的标准机制，定义 EventSource 接口、text/event-stream MIME 类型、事件流解析与 UTF-8 解码、Last-Event-ID 头及断线重连行为。该标准以 Living Standard 形式持续更新，不设固定发布版本。
- **与主题关联**：为家用机常驻助理提供免轮询的长连接事件通道，MCP Streamable HTTP 的流式响应、云端 LLM 流式输出与工具进度通知都建立在这一格式之上。

#### 058｜CloudEvents - Version 1.0.2

- **检索号**：G-07　**类别**：G 开放协议与工具调用标准
- **作者 / 机构**：CloudEvents 项目（CNCF Serverless Working Group）
- **时间**：1.0.2（Version 1.0.2；specversion 值为 1.0）　**类型**：官方规范
- **出处**：<https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md>
- **核验**：直连 200 · 页面标题为站点通用标题或重定向页，已按正文核验
- **页面依据**：CloudEvents - Version 1.0.2；CloudEvents is a vendor-neutral specification for defining the format of event data.；Compliant event producers MUST use a value of 1.0 when referring to this version of the specification.；Context Attributes；REQUIRED Attributes: id, source, specversion, type；All implementations MUST support the JSON format.；Protocol Binding
- **要点**：定义跨服务、平台与系统描述事件数据的厂商中立通用格式，规定 id、source、specversion、type 等必需上下文属性与可选扩展属性，并要求实现支持 JSON 事件格式。规范同时定义 Event、Producer、Consumer、Event Format、Message、Protocol Binding 等术语与尺寸限制。
- **与主题关联**：家用机常驻助理接收外部 SaaS 与云服务的 webhook/事件推送时，可用统一信封格式解析、过滤与转发，不必为每个数据源编写专用适配器。

#### 059｜Agent2Agent (A2A) Protocol Specification（页面标题 Overview - A2A Protocol）

- **检索号**：G-08　**类别**：G 开放协议与工具调用标准
- **作者 / 机构**：A2A Project（原由 Google 开发并捐赠 Linux Foundation，由 Technical Steering Committee 维护）
- **时间**：1.0.0（Latest Released Version 1.0.0）　**类型**：官方规范
- **出处**：<https://a2a-protocol.org/latest/specification>
- **核验**：本机直连受代理链路影响（代理 502 / SSL 超时）；二次抓取确认「Overview - A2A Protocol」
- **页面依据**：Agent2Agent (A2A) Protocol Specification；Latest Released Version 1.0.0；Reuse existing, well-understood standards (HTTP, JSON-RPC 2.0, Server-Sent Events).；2.2. Core Concepts（Agent Card / Task / Message / Artifact）；3.1. Core Operations；4.4.1. AgentCard；Section 9: JSON-RPC Protocol Binding；Section 10: gRPC Protocol Binding；Section 11: HTTP+JSON/REST Protocol Binding
- **要点**：定义独立、彼此不透明 AI 智能体之间的互操作通信协议，规定 Agent Card 能力发现、Task 状态生命周期、Message/Artifact 数据模型以及 Send Message、Send Streaming Message、Get Task、Push Notification 等核心操作。协议复用 HTTP、JSON-RPC 2.0 与 SSE，并给出 JSON-RPC、gRPC、HTTP+JSON/REST 三种协议绑定。
- **与主题关联**：家用机上的编排器可作为 A2A 客户端发现并委派任务给远端专职智能体，与 MCP（接工具）形成分工，从而在单机上扩展能力而无需本地部署模型。

#### 060｜OpenTelemetry GenAI Semantic Conventions（仓库 open-telemetry/semantic-conventions-genai）

- **检索号**：G-10　**类别**：G 开放协议与工具调用标准
- **作者 / 机构**：OpenTelemetry（CNCF；semantic-conventions-genai 仓库维护方）
- **时间**：n.d.（现行规范，开发中；README 中 Schema URL 标注 TODO，可见最近提交 Jun 4, 2026）　**类型**：官方规范
- **出处**：<https://github.com/open-telemetry/semantic-conventions-genai>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：OpenTelemetry GenAI Semantic Conventions；Semantic Conventions for Generative AI (GenAI), including spans, metrics, and events for GenAI clients, MCP (Model Context Protocol), and provider-specific conventions (OpenAI, etc.).；This repository extends the OpenTelemetry Semantic Conventions with GenAI-specific conventions；The human-readable version of the semantic conventions resides in the docs folder.；## Schema URL — TODO；另：原页面 https://opentelemetry.io/docs/specs/semconv/gen-ai/ 已标注 Moved: Generative AI semantic conventions 并指向本仓库
- **要点**：为 GenAI 客户端调用、MCP 交互与各模型厂商定义统一的 span、metric、event 语义属性（gen_ai.*、a2a.*），人类可读文档由 model 目录下的 YAML 定义生成。原 opentelemetry.io 的 GenAI 语义约定页已迁至本仓库，规范仍在推进（Schema URL 尚为 TODO）。
- **与主题关联**：使家用机常驻助理的云端 LLM 调用、工具执行与跨智能体委派可被统一追踪与计量，便于在单机上排查编排链路与成本。

### H 类｜智能体记忆与长期状态（9 篇）

#### 061｜Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

- **检索号**：H-01　**类别**：H 智能体记忆与长期状态
- **作者 / 机构**：Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, Deshraj Yadav（Mem0 团队）
- **时间**：2025　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2504.19413>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：dynamically extracting, consolidating, and retrieving salient information from ongoing conversations
- **要点**：提出以记忆为中心的可扩展架构，从持续对话中动态抽取、整合与检索显著信息，并给出基于图的记忆变体。在 LOCOMO 基准上，相比全上下文方法 p95 延迟降低 91%、token 成本节省 90% 以上。
- **与主题关联**：家用机只需在本地持久化这些被抽取的结构化记忆片段并按需检索，生成与推理交由云端 LLM API 完成。

#### 062｜Memory blocks (core memory) | Letta Docs

- **检索号**：H-02　**类别**：H 智能体记忆与长期状态
- **作者 / 机构**：Letta（Letta Docs 维护方）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://docs.letta.com/guides/core-concepts/memory/memory-blocks>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Memory blocks are structured sections of the agent’s context window
- **要点**：官方文档说明 memory blocks（core memory）是始终驻留在智能体上下文窗口中的结构化片段。智能体可自主读取并更新这些核心记忆块；本条为官方文档页，非 MemGPT 经典架构论文。
- **与主题关联**：家用机可用一个轻量本地文件/数据库维护常驻记忆块，每次调用云端 LLM 时把该块注入上下文即可保持长期状态。

#### 063｜Zep: A Temporal Knowledge Graph Architecture for Agent Memory

- **检索号**：H-03　**类别**：H 智能体记忆与长期状态
- **作者 / 机构**：Preston Rasmussen, Pavlo Paliychuk, Travis Beauvais, Jack Ryan, Daniel Chalef（Zep AI）
- **时间**：2025　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2501.13956>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：a temporally-aware knowledge graph engine that dynamically synthesizes both unstructured conversational data and structured business data while maintaining historical relationships
- **要点**：提出面向 AI 智能体的时序知识图谱记忆层服务 Zep，其核心组件 Graphiti 动态整合对话数据与结构化数据并保留历史关系。论文在 DMR 与 LongMemEval 上报告优于静态 RAG 框架的表现。
- **与主题关联**：表明记忆可完全外置为独立的轻量服务或本地库，家用机无需承载任何模型权重即可维护带时间维度的长期状态。

#### 064｜Introduction - Chroma Docs

- **检索号**：H-04　**类别**：H 智能体记忆与长期状态
- **作者 / 机构**：Chroma（chroma-core 开源项目，Apache 2.0）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://docs.trychroma.com/docs/overview/introduction>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Chroma is the open-source data infrastructure for AI. It comes with everything you need to get started built-in.
- **要点**：官方介绍页说明 Chroma 内置 embeddings 与元数据存储、稠密/稀疏向量检索与元数据过滤。文档明确写出可本地运行、自托管或使用托管云。
- **与主题关联**：家用机可用它在本地持久化向量化的对话记忆，检索出的相关片段再交给云端 LLM 做编排与生成。

#### 065｜Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

- **检索号**：H-05　**类别**：H 智能体记忆与长期状态
- **作者 / 机构**：Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela
- **时间**：2020　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2005.11401>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：models which combine pre-trained parametric and non-parametric memory for language generation
- **要点**：RAG 奠基论文，提出把参数化记忆（预训练 seq2seq 模型）与非参数化记忆（可检索的稠密向量索引）结合用于生成。其中非参数化记忆是 Wikipedia 的稠密向量索引，由预训练神经检索器访问。
- **与主题关联**：论证了"知识/记忆可外置为可检索索引"，家用机只需维护索引，生成环节可由云端 LLM 承担。

#### 066｜Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs

- **检索号**：H-06　**类别**：H 智能体记忆与长期状态
- **作者 / 机构**：Yu. A. Malkov, D. A. Yashunin
- **时间**：2016　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/1603.09320>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：We present a new approach for the approximate K-nearest neighbor search based on navigable small world graphs with controllable hierarchy (Hierarchical NSW, HNSW).
- **要点**：提出 HNSW 分层可导航小世界图近似最近邻索引，为纯图结构、无需额外粗检索结构，并实现对数复杂度 scaling。该索引后被众多向量数据库用作底层实现。
- **与主题关联**：此类轻量索引让家用机在 CPU 与小内存上即可完成记忆的近似最近邻检索，无需本地运行大模型。

#### 067｜LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory

- **检索号**：H-07　**类别**：H 智能体记忆与长期状态
- **作者 / 机构**：Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, Dong Yu
- **时间**：2024　**类型**：评测基准
- **出处**：<https://arxiv.org/abs/2410.10813>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention
- **要点**：提出评测聊天助手五项长期记忆能力的基准，并把长期记忆设计拆为索引、检索、阅读三阶段。论文给出会话分解、事实增强键扩展、时间感知查询扩展等优化，显著提升记忆召回与下游问答。
- **与主题关联**：为家用常驻助理的"记忆"提供可量化维度，以及可在本地轻量实现的索引/检索三阶段设计依据。

#### 068｜A-MEM: Agentic Memory for LLM Agents

- **检索号**：H-09　**类别**：H 智能体记忆与长期状态
- **作者 / 机构**：Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, Yongfeng Zhang
- **时间**：2025　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2502.12110>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Following the basic principles of the Zettelkasten method, we designed our memory system to create interconnected knowledge networks through dynamic indexing and linking.
- **要点**：借鉴 Zettelkasten 方法，让新记忆以含上下文描述、关键词、标签的结构化笔记形式写入，并通过动态索引与链接形成互联知识网络，还能随新记忆触发对历史记忆的演化更新。
- **与主题关联**：这种"笔记 + 链接"的记忆组织完全可落在本地轻量数据库中，由云端 LLM 负责生成笔记与更新决策。

#### 069｜A Survey on the Memory Mechanism of Large Language Model based Agents

- **检索号**：H-10　**类别**：H 智能体记忆与长期状态
- **作者 / 机构**：Zeyu Zhang, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Quanyu Dai, Jieming Zhu, Zhenhua Dong, Ji-Rong Wen
- **时间**：2024　**类型**：综述
- **出处**：<https://arxiv.org/abs/2404.13501>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：we propose a comprehensive survey on the memory mechanism of LLM-based agents
- **要点**：系统综述 LLM 智能体记忆机制，先讨论"记忆是什么、为何需要"，再梳理记忆模块的设计与评估方法。文中还汇总记忆发挥作用的智能体应用，并分析局限与未来方向。
- **与主题关联**：为家用常驻助理选择记忆的来源、写入与检索策略提供总览性文献依据，说明记忆模块可作为独立外置组件而非模型能力。

### I 类｜事件驱动、调度与常驻运行（8 篇）

#### 070｜crontab(5) — Linux manual page

- **检索号**：I-01　**类别**：I 事件驱动、调度与常驻运行
- **作者 / 机构**：Linux man-pages project（man7.org）
- **时间**：n.d.（现行规范）　**类型**：官方手册
- **出处**：<https://man7.org/linux/man-pages/man5/crontab.5.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`crontab - files used to schedule the execution of programs`；`"run this command at this time on this date"`；`five time-and-date fields`；字段名 `minute` / `hour` / `day of month` / `month` / `day of week`；`@reboot`、`@daily`
- **要点**：NAME 段把 crontab 定义为"用于调度程序执行的文件"，正文中以五个时间日期字段（minute、hour、day of month、month、day of week）加待执行命令构成一条调度指令，由 cron(8) 守护进程读取执行。手册还定义 `@reboot`、`@hourly`、`@daily`、`@weekly`、`@monthly`、`@yearly` 等特殊时间别名及 `CRON_TZ` 等环境变量。
- **与主题关联**：为"由时间触发"提供最经典、可移植的规范性定义，是主动式助理按时刻唤醒执行的语义基线。

#### 071｜systemd.timer — Timer unit configuration

- **检索号**：I-02　**类别**：I 事件驱动、调度与常驻运行
- **作者 / 机构**：systemd / freedesktop.org
- **时间**：n.d.（现行规范）　**类型**：官方手册
- **出处**：<https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html>
- **核验**：直连 200 · 页面标题为站点通用标题或重定向页，已按正文核验
- **页面依据**：`systemd.timer — Timer unit configuration`；`A unit configuration file whose name ends in ".timer" encodes information about a timer controlled and supervised by systemd, for timer-based activation.`；`OnCalendar=`、`OnBootSec=`、`OnUnitActiveSec=`、`OnClockChange=`、`Persistent=`、`AccuracySec=`
- **要点**：该手册说明以 `.timer` 结尾的单元文件编码由 systemd 常驻守护进程监督和控制的定时器信息，用于 `timer-based activation`。[Timer] 段提供日历触发 `OnCalendar=`、相对单调计时 `OnBootSec=` / `OnUnitActiveSec=`、以及 `Persistent=`（错过触发后补执行）等选项。
- **与主题关联**：说明常驻系统服务如何把"时间到达"转化为对服务单元的激活，是常驻助理被定时唤醒的官方机制。

#### 072｜Task Scheduler for developers - Win32 apps | Microsoft Learn

- **检索号**：I-03　**类别**：I 事件驱动、调度与常驻运行
- **作者 / 机构**：Microsoft（Microsoft Learn / Win32 文档）
- **时间**：n.d.（现行规范）　**类型**：官方文档
- **出处**：<https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`The Task Scheduler enables you to automatically perform routine tasks on a chosen computer. The Task Scheduler does so by monitoring whatever criteria you choose (referred to as triggers) and then executing the tasks when those criteria are met.`；`When a specific system event occurs.`；`At a specific time.`；`When the computer enters an idle state.`；`When the system is booted.`；`When a user logs on.`
- **要点**：官方页说明任务计划程序通过监视用户选定的判定条件（称为 triggers）并在条件满足时执行任务，实现例行任务自动化。页面逐条列出可响应的触发条件，涵盖特定系统事件、特定时刻、每日/每周/每月计划、月度星期计划、计算机空闲、任务注册、系统启动、用户登录与终端会话状态变化。
- **与主题关联**：在消费级 Windows 主机上提供"无需用户提问、由时间或系统事件自动启动"的官方触发语义。

#### 073｜apscheduler.triggers.cron — APScheduler 3.11.3.post3 documentation

- **检索号**：I-04　**类别**：I 事件驱动、调度与常驻运行
- **作者 / 机构**：APScheduler 项目（官方 readthedocs 文档）
- **时间**：n.d.（现行规范）　**类型**：官方文档
- **出处**：<https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`Triggers when current time matches all specified time constraints, similarly to how the UNIX cron scheduler works.`；`You can specify a variety of different expressions on each field, and when determining the next execution time, it finds the earliest possible time that satisfies the conditions in every field.`；参数 `year`、`month`、`day`、`day_of_week`、`hour`、`minute`、`second`、`start_date`、`end_date`、`jitter`
- **要点**：官方 API 文档定义 CronTrigger：当当前时间满足所有指定时间约束时触发作业，行为与 UNIX cron 一致，并可在每个字段上写表达式以求出下一次满足全部条件的最早时间。参数列表包含 year/month/day/hour/minute/second 以及 `start_date`、`end_date`、`timezone`、`jitter`。
- **与主题关联**：把 cron 风格的时间触发语义嵌入常驻 Python 进程，便于助理在同一进程内编排定时任务而无需依赖系统 crontab。

#### 074｜MQTT Version 3.1.1 OASIS Standard

- **检索号**：I-05　**类别**：I 事件驱动、调度与常驻运行
- **作者 / 机构**：OASIS Open（MQTT Technical Committee）
- **时间**：2014　**类型**：官方标准
- **出处**：<https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`MQTT Version 3.1.1`；`OASIS Standard`；`29 October 2014`；`MQTT is a Client Server publish/subscribe messaging transport protocol.`；`Use of the publish/subscribe message pattern which provides one-to-many message distribution and decoupling of applications.`；`The Server sends a copy of the Application Message to each Client that has a matching Subscription.`
- **要点**：OASIS 标准把 MQTT 定义为轻量、开放的客户端-服务器发布/订阅消息传输协议，以 Topic Name 与 Topic Filter 实现一对多分发和应用解耦。服务器职责被描述为把匹配订阅的 Application Message 副本发送给每个订阅客户端，并提供三级 QoS。
- **与主题关联**：为传感器、设备与外部消息提供"发布即到达、订阅方被动接收"的标准事件通道，是主动触发的核心传输语义。

#### 075｜Creating webhooks - GitHub Docs

- **检索号**：I-07　**类别**：I 事件驱动、调度与常驻运行
- **作者 / 机构**：GitHub, Inc.（GitHub Docs）
- **时间**：n.d.（现行规范）　**类型**：官方文档
- **出处**：<https://docs.github.com/en/webhooks/using-webhooks/creating-webhooks>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`You can create webhooks to subscribe to specific events that occur on GitHub.`；`"Which events would you like to trigger this webhook?"`；`"Payload URL", type the URL where you'd like to receive payloads`；`GitHub will send you a simple ping event to let you know you've set up the webhook correctly`；`application/json will deliver the JSON payload directly as the body of the POST request`
- **要点**：官方文档说明可创建 webhook 订阅 GitHub 上发生的特定事件，配置 Payload URL 作为接收端点，并在"Which events would you like to trigger this webhook?"中选择触发事件，交付以 POST 请求发送 JSON 载荷。创建完成后 GitHub 会先发送 `ping` 事件验证端点连通。
- **与主题关联**：给出"外部系统事件发生即主动向常驻端点推送通知"的官方 webhook 触发范式。

#### 076｜RFC 2177: IMAP4 IDLE command

- **检索号**：I-08　**类别**：I 事件驱动、调度与常驻运行
- **作者 / 机构**：IETF / RFC Editor（B. Leiba, IBM T.J. Watson Research Center）
- **时间**：1997　**类型**：RFC
- **出处**：<https://www.rfc-editor.org/rfc/rfc2177>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`RFC 2177: IMAP4 IDLE command`；`IMAP4 IDLE command`；`June 1997`；`Category: Standards Track`；`This document specifies the syntax of an IDLE command, which will allow a client to tell the server that it's ready to accept such real-time updates.`；`as long as an IDLE command is active, the server is now free to send untagged EXISTS, EXPUNGE, and other messages at any time`
- **要点**：该 Standards Track RFC 指出 IMAP4 原本要求客户端轮询邮箱变化（新邮件、删除），而 IDLE 命令允许客户端声明已准备好接收服务器实时更新。IDLE 期间服务器可随时发送未请求的 untagged `EXISTS`、`EXPUNGE` 等响应，并建议客户端至少每 29 分钟重新发起 IDLE 以免被判为 inactive。
- **与主题关联**：为"新邮件到达即触发"提供标准化的服务器主动通知机制，是外部消息触发的规范依据。

#### 077｜RFC 4287 - The Atom Syndication Format

- **检索号**：I-09　**类别**：I 事件驱动、调度与常驻运行
- **作者 / 机构**：IETF / RFC Editor（M. Nottingham, Ed.; R. Sayre, Ed.）
- **时间**：2005　**类型**：RFC
- **出处**：<https://datatracker.ietf.org/doc/html/rfc4287>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`RFC 4287 - The Atom Syndication Format`；`The Atom Syndication Format`；`December 2005`；`This document specifies Atom, an XML-based Web content and metadata syndication format.`；`The primary use case that Atom addresses is the syndication of Web content such as weblogs and news headlines to Web sites as well as directly to user agents.`；`atom:updated`
- **要点**：该 RFC 把 Atom 定义为基于 XML 的 Web 内容与元数据联合（syndication）格式，feed 由多条 entry 组成，主要用例是将博客与新闻标题联合发布到站点及用户代理。`atom:updated` 元素标识条目或 feed 最近一次被发布者认为有实质修改的时刻，处理器可据 `latest atom:updated timestamp` 识别新内容。
- **与主题关联**：为"内容源出现新条目即触发"提供可比对的标准数据结构与更新时间语义。

### J 类｜智能体评测基准与成本 / 可靠性工程（6 篇）

#### 078｜AgentBench: Evaluating LLMs as Agents

- **检索号**：J-01　**类别**：J 智能体评测基准与成本 / 可靠性工程
- **作者 / 机构**：Xiao Liu、Hao Yu、Hanchen Zhang 等（THUDM / 清华大学，摘要注明数据与评测包发布于 github.com/THUDM/AgentBench；ICLR 2024）
- **时间**：2023　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2308.03688>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：「We present AgentBench, a multi-dimensional benchmark that consists of 8 distinct environments to assess LLM-as-Agent's reasoning and decision-making abilities.」
- **要点**：以 8 个不同的交互环境系统评测 LLM 作为智能体的推理与决策能力，覆盖 API 商业模型与开源模型。结果显示顶级商业 LLM 在复杂环境中表现强，但与参数量不超过 70B 的开源模型存在显著差距；作者归纳失败主因为长期推理、决策与指令遵循能力不足。
- **与主题关联**：直接证明「调用商业 API 的智能体」在多维度任务上明显强于家用机可本地承载的小参数开源模型，为「家用机 + 云端 API 编排」提供能力侧证据，同时指出长程推理与指令遵循是当前边界。

#### 079｜GAIA: a benchmark for General AI Assistants

- **检索号**：J-02　**类别**：J 智能体评测基准与成本 / 可靠性工程
- **作者 / 机构**：Grégoire Mialon、Clémentine Fourrier、Craig Swift、Thomas Wolf、Yann LeCun、Thomas Scialom（Meta AI / Hugging Face 等）
- **时间**：2023　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2311.12983>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：「GAIA proposes real-world questions that require a set of fundamental abilities such as reasoning, multi-modality handling, web browsing, and generally tool-use proficiency.」
- **要点**：构建 466 道真实世界问题，考察推理、多模态处理、网页浏览与工具使用等通用助手基础能力，答案仅公开 300 题以外的部分以支撑榜单。量化结论是人类作答正确率 92%，而带插件的 GPT-4 仅 15%。
- **与主题关联**：说明常驻个人助理的瓶颈在于「编排工具与浏览」而非模型参数规模，正是云端 API 编排可发力的方向，同时量化了当前能力天花板。

#### 080｜τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

- **检索号**：J-03　**类别**：J 智能体评测基准与成本 / 可靠性工程
- **作者 / 机构**：Shunyu Yao、Noah Shinn、Pedram Razavi、Karthik Narasimhan（Sierra）
- **时间**：2024　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2406.12045>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：「We also propose a new metric (pass^k) to evaluate the reliability of agent behavior over multiple trials.」
- **要点**：模拟「LM 驱动的用户」与「配备领域 API 工具及政策指南的智能体」之间的动态多轮对话，以对话结束时的数据库状态与标注目标状态比对来评测功能正确性，并提出 pass^k 度量多次试验下行为可靠性。实验显示即便 gpt-4o 这类先进函数调用智能体，任务成功率仍不足 50%，零售域 pass^8 低于 25%。
- **与主题关联**：直接量化「干得稳不稳」——云端最强模型在重复运行下的一致性依然很差，是常驻助理可靠性边界的关键证据。

#### 081｜WebArena: A Realistic Web Environment for Building Autonomous Agents

- **检索号**：J-04　**类别**：J 智能体评测基准与成本 / 可靠性工程
- **作者 / 机构**：Shuyan Zhou、Frank F. Xu、Hao Zhu、Graham Neubig 等（Carnegie Mellon University；ICLR 2024）
- **时间**：2023　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2307.13854>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：「our best GPT-4-based agent only achieves an end-to-end task success rate of 14.41%, significantly lower than the human performance of 78.24%.」
- **要点**：搭建电商、社交论坛、协作软件开发、内容管理四类功能完整、可复现的真实网站环境，并发布以「任务完成的功能正确性」为目标的长时程基准任务。最佳 GPT-4 智能体端到端成功率仅 14.41%，远低于人类 78.24%。
- **与主题关联**：说明「云端 API + 网页工具编排」已能跑通真实日常任务，但成功率仍低，给出家用机做常驻 Web 助理的可行性下限与改进空间。

#### 082｜Berkeley Function Calling Leaderboard（Blog 8: Berkeley Function-Calling Leaderboard）

- **检索号**：J-07　**类别**：J 智能体评测基准与成本 / 可靠性工程
- **作者 / 机构**：Fanjia Yan、Huanzhi Mao、Charlie Cheng-Jie Ji、Ion Stoica、Joseph E. Gonzalez、Tianjun Zhang、Shishir G. Patil（UC Berkeley，页面含 people.eecs.berkeley.edu 作者主页链接）
- **时间**：2024　**类型**：官方基准站点
- **出处**：<https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：「It consists of 2k question-function-answer pairs with multiple languages (python, java, javascript, restAPI), diverse application domains and complex use cases.」
- **要点**：首个系统评测 LLM 函数与工具调用能力的公开榜单，含 2,000 组 question-function-answer 对，覆盖 Python、Java、JavaScript、REST API、SQL 多语言，并含单次调用、并行调用、多函数选择与函数相关性检测等复杂场景；页面标注 Last updated: 2024-08-19、引用年份 year={2024}。
- **与主题关联**：函数调用/工具编排正是「家用机只做编排、把推理交给云端 API」的核心能力，该榜单可直接用于云端模型选型。

#### 083｜FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance

- **检索号**：J-08　**类别**：J 智能体评测基准与成本 / 可靠性工程
- **作者 / 机构**：Lingjiao Chen、Matei Zaharia、James Zou（Stanford / UC Berkeley）
- **时间**：2023　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2305.05176>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：「FrugalGPT can match the performance of the best individual LLM (e.g. GPT-4) with up to 98% cost reduction or improve the accuracy over GPT-4 by 4% with the same cost.」
- **要点**：梳理查询 GPT-4、ChatGPT、J1-Jumbo 等 API 的定价（费用可差两个数量级），归纳提示适配、LLM 近似、LLM 级联三类降本策略，并提出按查询学习选用不同 LLM 组合的级联方法。实验可在匹配 GPT-4 表现的同时降低最多 98% 成本，或在同等成本下把准确率提高 4%。
- **与主题关联**：直接论证「成本能否承受」——通过 API 级联与按需选模，常驻助理的长期调用开销可被压缩一到两个数量级。

### K 类｜家用硬件门槛与 API 成本一手资料（9 篇）

#### 084｜Business Pricing | OpenAI（正文 H1：Pricing）

- **检索号**：K-01　**类别**：K 家用硬件门槛与 API 成本一手资料
- **作者 / 机构**：OpenAI
- **时间**：n.d.（现行定价页）　**类型**：官方定价页
- **出处**：<https://openai.com/api/pricing>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验；二次抓取确认「Business Pricing | OpenAI（Pricing）」
- **页面依据**："Input:$10.00 / 1M tokens"、"Cached input:$1.00 / 1M tokens"、"Output:$50.00 / 1M tokens"；"StandardBatch -50%Data residency +10%"；"Pricing above reflects standard processing rates for context lengths under 272K."
- **要点**：页面按每百万 token 明码标价，GPT-6 Astra 为输入 $10.00 / 1M、缓存输入 $1.00 / 1M、输出 $50.00 / 1M，最便宜的 GPT-6 Luna 为输入 $0.10 / 1M、缓存输入 $0.01 / 1M、输出 $0.50 / 1M。页面同时列出 Standard、Batch（-50%）、Data residency（+10%）三种处理模式的计费维度，并注明上述价格适用于 272K 以下上下文。
- **与主题关联**：把"输入/缓存输入/输出"三类 token 单价与批处理折扣公开，常驻助理的月度云端开销可直接按用量核算，家用机无需为本地算力付费。

#### 085｜Models & Pricing | DeepSeek API Docs

- **检索号**：K-02　**类别**：K 家用硬件门槛与 API 成本一手资料
- **作者 / 机构**：深度求索 DeepSeek（DeepSeek API Docs）
- **时间**：n.d.（现行定价页）　**类型**：官方定价页
- **出处**：<https://api-docs.deepseek.com/quick_start/pricing>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Model prices are listed in units of per 1M tokens."；"1M INPUT TOKENS (CACHE HIT) OFF-PEAK$0.003 ... PEAK$0.006"；"1M OUTPUT TOKENS OFF-PEAK$0.6 ... PEAK$1.2"；"Off-peak rates are half of the peak rates."；"CONTEXT LENGTH1M"；"Concurrency Limit(3)2500500"
- **要点**：官方按每百万 tokens 计价，deepseek-flash 的缓存命中/未命中输入与输出在低谷时段为 $0.003 / $0.15 / $0.6，高峰时段为 $0.006 / $0.3 / $1.2，并明确"Off-peak rates are half of the peak rates"。页面还列出上下文长度 1M、最大输出 384K、并发限制 2500（flash）/ 500（v4-pro），以及 Search 与 Fetch 每 1000 次成功请求各 $0.75。
- **与主题关联**：低谷价与缓存命中价把定时轮询、批量编排的边际成本压到极低，家用机按量调用即可，成本可逐项对照价目表计算。

#### 086｜Pricing - Claude Platform Docs

- **检索号**：K-03　**类别**：K 家用硬件门槛与 API 成本一手资料
- **作者 / 机构**：Anthropic（Claude Platform Docs）
- **时间**：n.d.（现行定价页）　**类型**：官方定价页
- **出处**：<https://docs.anthropic.com/en/docs/about-claude/pricing>
- **核验**：直连 200 · 页面标题为站点通用标题或重定向页，已按正文核验
- **页面依据**："All prices are in USD."；"Claude Haiku 5.5 ... $0.10 / MTok ... $0.50 / MTok"；"The Batch API allows asynchronous processing of large volumes of requests with a 50 percent discount on both input and output tokens."；"Batch API and prompt caching discounts can be combined."
- **要点**：页面以 $/MTok 列出各档模型输入/输出价，Claude Haiku 5.5 为输入 $0.10 / MTok、输出 $0.50 / MTok，Claude Sonnet 5.5 为 $2 / $10、Claude Opus 5.5 为 $4 / $20。官方写明 Batch API 对输入与输出 token 均给 50% 折扣，prompt caching 缓存读取按 0.1x 基准输入价计费，且两种折扣可以叠加。
- **与主题关联**：缓存与批处理可叠加折扣，使长期常驻助理的重复系统提示成本被摊薄，成本项全部发生在云端而非本机。

#### 087｜Rate limits | OpenAI API

- **检索号**：K-04　**类别**：K 家用硬件门槛与 API 成本一手资料
- **作者 / 机构**：OpenAI
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://platform.openai.com/docs/guides/rate-limits>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验
- **页面依据**："Rate limits use metrics such as RPM (requests per minute), RPD (requests per day), TPM (tokens per minute), TPD (tokens per day), IPM (images per minute)"；"The three paid usage tiers are Build, Launch, and Grow."；表格 "BuildAstra, Sol, Terra5,0001,000,000"；"Free ... $100 / month"、"Build $5 in total credit purchases $500 / month"
- **要点**：文档定义 RPM、RPD、TPM、TPD、IPM 等限额维度，并给出付费层级资格与月度额度：Free $100 / month、Build（累计 $5）$500 / month、Launch（$100）$5,000 / month、Grow（$500）$200,000 / month。标准限额表列出 Build 层 Astra/Sol/Terra 为 5,000 RPM 与 1,000,000 TPM，Grow 层 Luna 为 30,000 RPM 与 180,000,000 TPM。
- **与主题关联**：吞吐上限由账号 usage tier 与云端配额决定，与家用机 CPU/内存无关，常驻助理只需按限额节奏发请求。

#### 088｜Batch API | OpenAI API

- **检索号**：K-05　**类别**：K 家用硬件门槛与 API 成本一手资料
- **作者 / 机构**：OpenAI
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://platform.openai.com/docs/guides/batch>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验
- **页面依据**："Better cost efficiency: 50% cost discount compared to synchronous APIs"；"Each batch completes within 24 hours (and often more quickly)"；`"completion_window": "24h"`；"A single batch may include up to 50,000 requests, and a batch input file can be up to 200 MB in size."；"using the Batch API will not consume tokens from your standard per-model rate limits"
- **要点**：Batch API 相对同步调用给 50% 成本折扣、承诺 24 小时内完成，单个 batch 最多 50,000 个请求 / 200 MB 输入文件，每小时最多创建 2,000 个 batch，结果文件在完成后 30 天自动删除。文档还说明批处理使用独立限额池，不占用同步请求的 per-model rate limits，并写明 "You will be charged for tokens consumed from any completed requests."。
- **与主题关联**：夜间离线整理、批量摘要用半价窗口提交即可，家用机无需长时间高负载运行，也无需为突发吞吐升级硬件。

#### 089｜Understanding and counting tokens | OpenAI Help Center

- **检索号**：K-06　**类别**：K 家用硬件门槛与 API 成本一手资料
- **作者 / 机构**：OpenAI（OpenAI Help Center）
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验
- **页面依据**："1 token is approximately 4 characters."；"100 tokens are approximately 75 words."；"Use the Tokenizer to see how text is divided into tokens."、"For programmatic plain-text tokenization, use tiktoken."；"Counting input tokens with the Responses input-token counting API ... is free and does not consume your model's normal inference quota."
- **要点**：官方给出英文文本的经验换算（1 token ≈ 4 字符、100 tokens ≈ 75 词），并区分输入、输出、缓存输入与推理 token 四类计费口径。页面说明可用 Tokenizer 页面或 tiktoken 库精确计数，而 Responses input-token counting API 免费且"does not consume your model's normal inference quota"。
- **与主题关联**：发请求前即可用官方工具把文本换算成 token 并估算费用，家用机只需运行极轻量的计数逻辑，无需本地模型。

#### 090｜Getting started with the Realtime API | OpenAI API

- **检索号**：K-07　**类别**：K 家用硬件门槛与 API 成本一手资料
- **作者 / 机构**：OpenAI
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://platform.openai.com/docs/guides/realtime>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验
- **页面依据**："Build a speech-to-speech voice agent with the Realtime API."；"The model works directly with audio, maintains conversation state, and can call tools."；"The session connects over WebRTC in the browser or WebSocket on the server."；示例 `model: "gpt-realtime-2.1"`
- **要点**：官方把 Realtime API 定义为直接处理音频、维持会话状态并可调用工具的 speech-to-speech 接口，浏览器端经 WebRTC、服务端经 WebSocket 建立会话，示例模型为 gpt-realtime-2.1。文档另列出打断（barge-in）、低首音频延迟、VAD 自动轮次检测与 Realtime MCP 工具等能力入口。
- **与主题关联**：语音输入与合成全部由云端实时端点承担，家用机只需麦克风、扬声器和网络，不必本地部署 STT/TTS 模型。

#### 091｜Buy a Raspberry Pi 5 – Raspberry Pi

- **检索号**：K-08　**类别**：K 家用硬件门槛与 API 成本一手资料
- **作者 / 机构**：Raspberry Pi Ltd（Raspberry Pi 官方）
- **时间**：n.d.　**类型**：官方规格书
- **出处**：<https://www.raspberrypi.com/products/raspberry-pi-5>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验
- **页面依据**："Broadcom BCM2712 2.4GHz quad-core 64-bit Arm Cortex-A76 CPU"；"LPDDR4X-4267 SDRAM (1GB, 2GB, 4GB, 8GB, and 16GB)"；"5V/5A DC power via USB-C, with Power Delivery support"；"Raspberry Pi 5 16GB is available now for $305."
- **要点**：官方规格表列出 BCM2712 2.4GHz 四核 Cortex-A76（512KB 每核 L2、2MB 共享 L3）、LPDDR4X-4267 内存 1GB/2GB/4GB/8GB/16GB、2 × USB 3.0（5Gbps）、PCIe 2.0 x1 与 5V/5A USB-C 供电，配套官方 27W USB-C 电源。页面标明 16GB 版本售价 $305，并称产品"will remain in production until at least January 2036"。
- **与主题关联**：以单板机官方规格、5V/5A 供电与整机价格界定最低硬件门槛，证明编排云端 API 的常驻助理可运行在几十瓦级、数十美元级设备上。

#### 092｜Resource constraints | Docker Docs

- **检索号**：K-09　**类别**：K 家用硬件门槛与 API 成本一手资料
- **作者 / 机构**：Docker Inc.（Docker Docs）
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://docs.docker.com/engine/containers/resource_constraints>
- **核验**：本机直连受代理链路影响（代理 502 / SSL 超时）；二次抓取确认「Resource constraints | Docker Docs」
- **页面依据**："By default, a container has no resource constraints and can use as much of a given resource as the host's kernel scheduler allows."；"`-m` or `--memory=` The maximum amount of memory the container can use. If you set this option, the minimum allowed value is `6m` (6 megabytes)."；"So if `--memory=\"300m\"` and `--memory-swap=\"1g\"`, the container can use 300m of memory and 700m (1g - 300m) swap."
- **要点**：官方说明容器默认无资源约束，可用 `-m/--memory` 设硬性内存上限（最小 6m）、`--memory-swap` 设内存加交换总量、`--memory-swappiness` 取 0 到 100。示例 `--memory="300m"` 配 `--memory-swap="1g"` 表示 300m 内存加 700m swap，另说明硬限与软限的区别及 OOM 风险。
- **与主题关联**：编排服务可被显式约束在很小的内存配额内长期常驻，家用机无需为"本地跑大模型"预留大内存或显存。

### L 类｜厂商工程指南、综述与主动任务产品证据（8 篇）

#### 093｜Building effective agents

- **检索号**：L-01　**类别**：L 厂商工程指南、综述与主动任务产品证据
- **作者 / 机构**：Erik Schluntz、Barry Zhang（Anthropic）
- **时间**：2024-12　**类型**：官方工程指南
- **出处**：<https://www.anthropic.com/engineering/building-effective-agents>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns.
- **要点**：基于与数十个团队合作的经验，主张成功落地几乎不依赖复杂框架，而是用「简单、可组合的模式」把 LLM 调用、工具与工作流串起来。文中区分 workflow 与 agent，并建议优先用最简方案、只在必要时增加自主性。
- **与主题关联**：它把智能体能力定位为「编排模式」而非本地重资产，家用机只需调度云端 LLM API 与工具即可复现同类系统。

#### 094｜A practical guide to building agents

- **检索号**：L-02　**类别**：L 厂商工程指南、综述与主动任务产品证据
- **作者 / 机构**：OpenAI
- **时间**：2025-04　**类型**：白皮书
- **出处**：<https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf>
- **核验**：直连 200 · PDF 无 HTML 标题，已确认响应类型与文件大小；二次抓取确认「A practical guide to building agents（官方 PDF，直连 200，Content-Type: application/pdf）」
- **页面依据**：Agents are systems that independently accomplish tasks on your behalf.
- **要点**：面向产品与工程团队给出首个智能体的设计基础，明确 agent 是「由 LLM 管理流程执行、动态选择工具」的系统，并给出编排模式、单 agent 与多 agent 及护栏的最佳实践。全篇围绕调用模型与工具构建逻辑，不涉及本地训练或本地部署大模型。
- **与主题关联**：把「智能体」定义为对 LLM 与工具的编排层，正好支撑家用机通过 API 调用云端模型完成编排、无需本地跑大模型。

#### 095｜Agents

- **检索号**：L-03　**类别**：L 厂商工程指南、综述与主动任务产品证据
- **作者 / 机构**：Julia Wiesinger、Patrick Marlow、Vladimir Vuskovic（Google，Kaggle 白皮书）
- **时间**：n.d.　**类型**：白皮书
- **出处**：<https://www.kaggle.com/whitepaper-agents>
- **核验**：直连 200 · 页面标题为站点通用标题或重定向页，已按正文核验；二次抓取确认「Agents | Kaggle（作者 Julia Wiesinger, Patrick Marlow, Vladimir Vuskovic）」
- **页面依据**：This combination of reasoning, logic, and access to external information that are all connected to a Generative AI model invokes the concept of an agent, or a program that extends beyond the standalone capabilities of a Generative AI model.
- **要点**：系统讲生成式 AI Agent 的基础构件与认知架构，强调模型通过工具访问实时信息、发起 API 调用（发邮件、完成事务等）来扩展自身能力。白皮书给出扩展、函数、数据存储等工具形态与编排方式。
- **与主题关联**：明确指出 Agent 是「模型 + 工具/API 调用」的扩展程序，能力来自云端模型与外部接口，而非本地算力。

#### 096｜Introducing ambient agents

- **检索号**：L-04　**类别**：L 厂商工程指南、综述与主动任务产品证据
- **作者 / 机构**：Harrison Chase（LangChain）
- **时间**：2025-01　**类型**：官方博文
- **出处**：<https://blog.langchain.com/introducing-ambient-agents>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Ambient agents listen to an event stream and act on it accordingly, potentially acting on multiple events at a time
- **要点**：提出「ambient agents」范式：不再由用户每次发起聊天，而是监听事件流、在后台常驻并主动响应，可同时跑多个 agent；配套 LangGraph 提供持久化、human-in-the-loop、长期记忆与内置 cron jobs。文中还给出已落地的邮件助理参考实现（Agent Inbox）。
- **与主题关联**：这是「常驻、主动、定时触发」助理的直接工程范式，且明确指出许多 ambient agents 靠 schedule/cron 运行，家用机做轻量编排即可承载。

#### 097｜Agentic Design Patterns Part 3, Tool Use

- **检索号**：L-05　**类别**：L 厂商工程指南、综述与主动任务产品证据
- **作者 / 机构**：Andrew Ng（DeepLearning.AI, The Batch）
- **时间**：2024-04　**类型**：官方博文
- **出处**：<https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Tool Use, in which an LLM is given functions it can request to call for gathering information, taking action, or manipulating data, is a key design pattern of AI agentic workflows.
- **要点**：吴恩达在 The Batch 系列信件中系统阐述 agentic workflow 的四种设计模式（Reflection、Tool Use、Planning、Multi-agent collaboration），本篇专讲 Tool Use：让 LLM 请求调用搜索、代码执行、邮件与日历等外部函数。他强调 agentic workflow 是「多次提示 LLM 逐步迭代」而非一次性零样本输出。
- **与主题关联**：权威论述把价值放在「工作流编排 + 工具/API 调用」上，说明能力增量来自编排层，家用机调用云端 LLM 即可实现。

#### 098｜Introducing smolagents: simple agents that write actions in code.

- **检索号**：L-06　**类别**：L 厂商工程指南、综述与主动任务产品证据
- **作者 / 机构**：Hugging Face
- **时间**：2024-12　**类型**：官方博文
- **出处**：<https://huggingface.co/blog/smolagents>
- **核验**：本机直连受代理链路影响（代理 502 / SSL 超时）；二次抓取确认「Introducing smolagents: simple agents that write actions in code.」
- **页面依据**：For the `model`, you can use any LLM, either open models using our `HfApiModel` class, that leverages Hugging Face's free inference API (as shown in the leopard example above), or you can use `LiteLLMModel` to leverage litellm and pick from a list of 100+ different cloud LLMs.
- **要点**：发布极简 agent 库 smolagents，核心逻辑仅约千行代码、抽象压到最低；模型层可任意替换，既可用 HF 免费推理 API，也可经 LiteLLM 接入 100+ 云端 LLM。它以「代码即动作」的 CodeAgent 让轻量客户端驱动智能体行为。
- **与主题关联**：直接证明智能体框架可以极轻、模型可以完全云端化，家用消费级电脑只需跑编排逻辑而不必本地加载大模型。

#### 099｜Scheduled tasks in ChatGPT | OpenAI Help Center

- **检索号**：L-07　**类别**：L 厂商工程指南、综述与主动任务产品证据
- **作者 / 机构**：OpenAI Help Center
- **时间**：n.d.　**类型**：官方帮助文档
- **出处**：<https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验；二次抓取确认「Scheduled tasks in ChatGPT | OpenAI Help Center」
- **页面依据**：ChatGPT can run one-time or recurring tasks, monitor for changes, and respond to supported events when available.
- **要点**：官方文档确认 ChatGPT 已上线「Scheduled tasks」：可创建一次性或周期性任务、监测变化、按支持的应用事件（Gmail/Slack/GitHub）触发，并在后台执行模型处理、通过推送或邮件通知用户。文档还列出不同套餐的活跃任务上限与每小时执行频率。
- **与主题关联**：这是云端产品已落地的「定时/主动执行」证据，说明主动式个人助理的运行与算力在云侧，用户端只需配置与接收结果。

#### 100｜Schedules in Gemini Apps - Computer - Gemini Apps Help

- **检索号**：L-08　**类别**：L 厂商工程指南、综述与主动任务产品证据
- **作者 / 机构**：Google（Gemini Apps Help）
- **时间**：n.d.　**类型**：官方帮助文档
- **出处**：<https://support.google.com/gemini/answer/16316416>
- **核验**：本机直连受代理链路影响（代理 502 / SSL 超时）；二次抓取确认「Schedules in Gemini Apps - Computer - Gemini Apps Help」
- **页面依据**：You can make Gemini a part of your daily, weekly, and monthly routines by scheduling recurring actions.
- **要点**：官方帮助文档确认 Gemini Apps 支持 Schedules（定时主动动作）：可设置每日、每周、每月的重复任务（新闻摘要、日历与邮件日报、市场报告等），Gemini 在后台提前准备内容并按设定时间投递与通知，用户最多可保留 10 个活跃计划。文档还说明计划可暂停、编辑并在 Scheduled 页统一管理。
- **与主题关联**：与 ChatGPT Tasks 并列，构成厂商级「已落地定时主动任务」产品证据，证明常驻主动助理由云端服务承载，家用机不必本地运行大模型。

---

**边界说明**：本清单是资料集合，不构成对上述命题的结论性论证，也不含任何实现建议、选型比较或项目计划。清单中「与主题关联」一句仅说明该文献可支撑命题的哪一环，供后续取证时定位。
