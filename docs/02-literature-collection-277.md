# 家用机「主动式 AI」文献总集（277 篇／含 CUA 全量补收）
> **本文件只含文献资料**：可核验出处、内容要点、影响力证据、核验记录。不含方案设计、架构图、代码、部署步骤，也不构建任何项目。
> 本文件**完整收录并替代**此前的《家用机主动式 AI 文献清单（100 篇）》；原有 001–100 的全部条目保留，本轮按用户需求补收其他模块，尤其是**能在本地计算机实际实现 CUA（Computer Use Agent）**的学术与技术文献。
> 检索完成时间：2026-11-06（GMT+8）。命题待验证，**本步不作论证**：家用消费级电脑不本地运行大模型，仅通过调用云端 LLM API 进行编排，是否足以构成具备主动触发、记忆、规划与工具调用能力的常驻个人助理；补收部分同样只提供 CUA 相关一手资料，不给出选型或实现结论。

## 一、检索口径与范围
1. **工作定义**：「主动式 AI」指不必等用户发问，而能由时间、外部事件或环境变化触发，长期保持状态与记忆，自主规划并调用工具、再通过 API 完成推理的常驻软件代理。「CUA」指能读屏、理解 GUI、规划动作并把鼠标/键盘/触控事件注入真实桌面、浏览器或移动端的智能体。
2. **纳入优先级**：① 厂商 / 标准组织官方技术文档与规范；② arXiv、顶会与期刊论文；③ 官方开源仓库及 README（高星须有 GitHub API 硬证据）；④ 官方工程指南、白皮书、帮助文档；⑤ 可复现的公开评测基准、数据集与 leaderboard。
3. **排除范围**：信息安全、网络攻击、越狱与提示注入攻防、隐私泄露、红队、内容审核、合规治理类文献一律不收；纯营销软文、二手转载、无出处教程不收。三轮检索均在采集口径中明确排除安全类主题，并对候选逐条做关键词复核。
4. **时间范围**：以 2023–2026 年为主，奠基性论文、现行标准与长期维护的官方仓库不受此限；页面未标注日期记 `n.d.`，不推断年份。
5. **出处要求**：每条须有可直接打开的 URL；标题、作者、时间、要点须与页面实际内容一致，并摘录页面原文短语作为「页面依据」供反向核对。数字（价格、限额、参数、star、分数）只抄页面或官方 API 原文，不推算、不凭记忆补写。
6. **三轮检索边界**：第一轮 12 类（A–L）围绕「家用机 + API 编排 + 主动性」，收敛为 100 篇；第二轮 12 类（M–X）围绕 CUA 与其他配套模块；第三轮 3 类（Y / Z / AA）针对第二轮暴露的缺口——本地控制接口官方文档、高星实现仓库、评测榜单与关键方法论文——做补漏。

## 二、出处核验方法与可复现结果
**第一步（逐条检索）**：按类别并行检索，每条均由检索时实际打开正文确认，摘录页面原文短语；三轮合计候选 120 + 144 + 38 = 302 条，验证字段全部标注「已打开正文」。
**第二步（批量直连核验）**：对全部候选 URL 发起 HTTP 请求，记录状态码，抽取页面 `<title>` / `citation_title` 与文献标题做字符串相似度（SequenceMatcher 与 Jaccard 取大值）比对；`OK` = 200 且标题吻合，`TITLE_MISMATCH` = 200 但站点用通用标题 / 重定向 / PDF 无 HTML 标题，`BLOCKED` = 403/429 反爬或地区限制，`FAIL` = 本机代理 502 / SSL 超时。
- 第二轮首次以 24 并发核验时出现 78 条假 `FAIL`（代理抖动），改用 8 并发重试两轮后收敛为 7 条；第三轮直接用 6 并发并自动重试。**`BLOCKED` 与 `FAIL` 均不代表链接失效**。
- 最终入集 277 篇的直连核验分布：`BLOCKED` 13 篇、`FAIL` 17 篇、`OK` 200 篇、`TITLE_MISMATCH` 47 篇。
- 对其中 40 条改用独立抓取通道或 curl 二次确认，读回页面标题 / 正文或确认 PDF 响应类型，明细见下表；典型如 OpenAI Platform Docs（403）、Anthropic Docs（地区重定向）、Gemini / Hugging Face / Android Developers / GitHub（代理 502）、Kaggle（reCAPTCHA）。
- `TITLE_MISMATCH` 的第二轮主体是 12 个 R 类高星仓库：GitHub 页标题形如 `GitHub - owner/repo: description`，与以仓库名记录的文献标题不同，属站点通用标题；其余为项目官网短标题（如 `The Agent Company`）、微软文档改版重定向、PDF 无 HTML 标题，均已在直连 200 时读回真实页面标题并保留。
- 定价、star 数、leaderboard 分数会随时间变动，文内数字仅代表 2026-11-06 查询时页面 / 官方 API 所示，复核时应以实时结果为准。

**二次确认明细**（直连异常 → 独立抓取通道 / curl 读回的结果）：

| 检索号 | 轮次 | 直连结果 | 二次读回的页面标题 / 文件 | 是否入集 |
|---|---|---|---|---|
| C-03 | 1 | TITLE_MISMATCH | Tool use with Claude - Claude Platform Docs | 是 |
| C-05 | 1 | FAIL | Function calling with the Gemini API - Gemini API \| Google AI Studio | 是 |
| C-06 | 1 | FAIL | Function Calling \| Mistral Docs | 是 |
| D-07 | 1 | TITLE_MISMATCH | 腾讯混元大模型 混元 OpenAI 兼容接口相关调用示例_腾讯云 | 是 |
| E-03 | 1 | FAIL | Get started - Agent Development Kit (ADK) | 是 |
| G-08 | 1 | FAIL | Overview - A2A Protocol | 是 |
| K-01 | 1 | BLOCKED | Business Pricing \| OpenAI（Pricing） | 是 |
| K-09 | 1 | FAIL | Resource constraints \| Docker Docs | 是 |
| L-03 | 1 | TITLE_MISMATCH | Agents \| Kaggle（作者 Julia Wiesinger, Patrick Marlow, Vladimir Vuskovic） | 是 |
| L-06 | 1 | FAIL | Introducing smolagents: simple agents that write actions in code. | 是 |
| L-07 | 1 | BLOCKED | Scheduled tasks in ChatGPT \| OpenAI Help Center | 是 |
| L-08 | 1 | FAIL | Schedules in Gemini Apps - Computer - Gemini Apps Help | 是 |
| C-08 | 1 | BLOCKED | Tool Use Overview - GroqDocs | 是 |
| C-10 | 1 | BLOCKED | Function calling patterns - Together AI docs | 是 |
| D-09 | 1 | TITLE_MISMATCH | 豆包助手 - 火山方舟 - 火山引擎（旧地址 200 并跳转新文档域） | 是 |
| L-02 | 1 | TITLE_MISMATCH | A practical guide to building agents（官方 PDF，直连 200，Content-Type: application/pdf） | 是 |
| I-10 | 1 | BLOCKED | WebSub（W3C Recommendation，直连 403 为站点反爬） | 否（主题收敛剔除） |
| C-01 | 1 | BLOCKED | Structured model outputs \| OpenAI API（直连 403，独立抓取可读正文） | 是 |
| K-04 | 1 | BLOCKED | Rate limits \| OpenAI API（直连 403，独立抓取可读正文） | 是 |
| K-08 | 1 | BLOCKED | Buy a Raspberry Pi 5 – Raspberry Pi（直连 403，独立抓取读回官方 Specification 表） | 是 |
| M-02 | 2 | BLOCKED | Computer-Using Agent \| OpenAI（页面标注 January 23, 2025） | 是 |
| M-03 | 2 | BLOCKED | Computer use \| OpenAI API（原文 "Computer use lets a model operate a browser or desktop interface."） | 是 |
| M-04 | 2 | TITLE_MISMATCH | Computer use tool - Claude Platform Docs（独立抓取未出现地区重定向） | 是 |
| M-05 | 2 | FAIL | Computer use - Gemini API \| Google AI Studio | 是 |
| M-09 | 2 | FAIL | GitHub - QwenLM/Qwen3-VL（独立抓取确认仓库存在，README / Cookbook 含 Visual Agent、Computer-Use Agent 段落） | 是 |
| M-12 | 2 | FAIL | GitHub - bytedance/UI-TARS-desktop: The Open-Source Multimodal AI Agent Stack · GitHub | 是 |
| Q-11 | 2 | TITLE_MISMATCH | GitHub - droidrun/mobilerun（droidrun 仓库改名，直连 301 到新地址） | 是 |
| S-07 | 2 | FAIL | Write automated tests with UI Automator \| Test your app on Android \| Android Developers | 是 |
| S-08 | 2 | FAIL | Create an accessibility service \| Android Developers | 是 |
| T-07 | 2 | FAIL | likaixin/ScreenSpot-Pro · Datasets at Hugging Face（含官方 leaderboard 与 citation） | 是 |
| W-12 | 2 | FAIL | SmolVLM - small yet mighty Vision Language Model（Published November 26, 2024） | 是 |
| X-11 | 2 | TITLE_MISMATCH | Durable Functions Overview: Stateful Serverless Workflows \| Microsoft Learn（微软文档改版重定向） | 是 |
| X-12 | 2 | TITLE_MISMATCH | App Notifications Overview for Windows Apps - Windows apps \| Microsoft Learn | 是 |
| AA-01 | 3 | TITLE_MISMATCH | WebArena-x（WebArena 官方项目主页，站点 title 为项目短名） | 是 |
| AA-02 | 3 | TITLE_MISMATCH | Blog（webarena.dev 官方 WebArena-Infinity 发布页，站点通用 title） | 是 |
| AA-05 | 3 | TITLE_MISMATCH | Gradio（GAIA benchmark leaderboard 托管于 Hugging Face Space，页面 title 为框架通用名） | 是 |
| AA-09 | 3 | FAIL | osunlp/Online-Mind2Web · Datasets at Hugging Face（数据集卡含 136 个网站、300 个任务与 arXiv:2504.01382 引用） | 是 |
| Y-04 | 3 | BLOCKED | WebDriver — W3C Recommendation 05 June 2018（直连 403，独立抓取读回 W3C 状态行） | 是 |
| Y-05 | 3 | FAIL | Android Debug Bridge (adb) \| Android Studio \| Android Developers | 是 |
| Y-12 | 3 | FAIL | Remote debug Android devices \| Chrome DevTools \| Chrome for Developers | 是 |

共二次确认 40 条，其中 39 条进入总集。其余未逐条二次确认而保留的 `BLOCKED` 条目，均为 OpenAI Platform Docs / Help Center 等已知的站点反爬 403，检索时已逐条打开正文、摘录页面依据；`TITLE_MISMATCH` 中未在表内列出的条目，均属直连 200 且已读回页面标题的通用标题或规范短标题。

**独立抽检记录**（对最易出错的两类条目——2026 年新编号论文、直连异常页——在批量核验之外再用独立抓取通道逐页读回的结论）：

| 出处 | 独立读回的标题 / 事实 | 结论 |
|---|---|---|
| arXiv:2606.29537 | OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks；Submitted 28 Jun 2026（v2 13 Jul 2026） | 页面真实存在，标题与 N-11 一致 |
| arXiv:2610.27645 | CUA-Recovery: Benchmarking Error Recovery in Long-Horizon Computer-Use Agents；Submitted 20 Oct 2026 | 页面真实存在，标题与 V-10 一致 |
| arXiv:2606.03103 | DeskCraft: Benchmarking Desktop Agents on Professional Workflows and Human-in-the-Loop Collaboration；Submitted 2 Jun 2026 | 页面真实存在，标题与 V-12 一致 |
| arXiv:2605.26114 | MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research；Submitted 25 May 2026（v3 23 Sep 2026），Comments: EMNLP 2026 Main Conference | 页面真实存在，标题与 Q-12 一致；会议信息取自页面 Comments 字段 |
| arXiv:2511.21631 | Qwen3-VL Technical Report；Submitted 26 Nov 2025（v2 27 Nov 2025） | 页面真实存在，标题与 U-06 一致 |
| arXiv:2606.20785 | Fara-1.5: Scalable Learning Environments for Computer Use Agents；Submitted 18 Jun 2026（v2 22 Jul 2026） | R-12 影响力字段引用的配套论文真实存在 |
| openai.com/index/computer-using-agent | Computer-Using Agent \| OpenAI；January 23, 2025 | 直连 403 但页面可读，标题与 M-02 一致 |
| platform.openai.com/docs/guides/tools-computer-use | Computer use \| OpenAI API；原文 "Computer use lets a model operate a browser or desktop interface." | 直连 403 但页面可读，标题与 M-03 一致 |
| docs.anthropic.com/.../computer-use | Computer use tool - Claude Platform Docs；独立抓取未出现地区重定向 | 直连被重定向，独立通道可读正文 |
| github.com/bytedance/UI-TARS-desktop | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra；非 404 | 直连 502 但仓库页存在 |
| huggingface.co/datasets/likaixin/ScreenSpot-Pro | likaixin/ScreenSpot-Pro · Datasets at Hugging Face；含官方 leaderboard 与 BibTeX citation | 直连 502 但数据集页存在 |
| developer.android.com/.../accessibility/service | Create an accessibility service \| Android Developers | 直连 502 但文档页存在 |
| github.com/simular-ai/Agent-S | README Updates："The Agent S paper is accepted to ICLR 2025!"、"won the Best Paper Award at ICLR 2025 Agentic AI for Science Workshop" | R-06 影响力字段的会议与获奖背书逐句核到原文 |
| github.com/openai/openai-cua-sample-app | 仓库描述 "Learn how to use CUA (our Computer Using Agent) via the API on multiple computer environments."；非 404 | Z-11 官方示例仓库真实存在 |
| github.com/anthropics/claude-quickstarts | 仓库描述 "A collection of projects designed to help developers quickly get started with building deployable applications using the Claude API"；README 含 "### Computer Use Demo" 章节；非 404 | Z-09 官方 quickstart 仓库真实存在 |
| arXiv:2510.02250 | Scaling Agents for Computer Use；Submitted 2 Oct 2025（v2 3 Feb 2026）；OSWorld 72.6% | AA-13 页面真实存在；注意 Agent-S README 引用的长标题与 arXiv 实际标题不同，总集以 arXiv 页标题为准 |
| arXiv:2610.28601 | Evolving Agent Interfaces；Submitted 20 Oct 2026；OSWorld V2 21.3% | AA-14 页面真实存在，标题与摘要数字逐项核到 |
| w3.org/TR/webdriver1 | WebDriver；状态行 "W3C Recommendation 05 June 2018" | 直连 403 但独立抓取读回 W3C 推荐标准状态 |
| developer.android.com/tools/adb | Android Debug Bridge (adb) \| Android Studio \| Android Developers | 直连 502 但官方文档页存在 |
| developer.chrome.com/.../remote-debugging | Remote debug Android devices \| Chrome DevTools \| Chrome for Developers | 直连 502 但官方文档页存在 |
| huggingface.co/datasets/osunlp/Online-Mind2Web | osunlp/Online-Mind2Web · Datasets at Hugging Face；数据集卡含 136 网站 / 300 任务 | 直连 502 但数据集页存在 |

抽检结论：21 处独立打开均读回与条目一致的内容，未发现编造的 arXiv 编号、论文标题或 star 数。

**第三步（去重与收敛）**：
- 第一轮：120 条候选中检出 3 组重复 URL，剔除 A-05、A-06、I-06；再按主题相关度剔除 17 条，共剔除 20 条，保留 100 篇。
- 第二轮：144 条新增候选中检出 5 组内部重复 URL，按「与 CUA 主线更贴合 / 保留带 star 证据的条目」剔除 `M-08`、`N-12（候补）`、`U-03`、`V-06`、`V-07`；另检出 6 组内部重复标题；连同按标题前缀归并的同类项，总计 7 组「同一成果的论文页 + 官方项目主页 / 仓库」：OSWorld（N-01 / T-01）、Windows Agent Arena（N-05 / T-06）、Spider2-V（N-09 / T-10）、The Agent Company（N-10 / T-11）、ScreenSpot-Pro（O-11 / T-07）、WebVoyager（P-03 / T-05）、AndroidWorld（Q-01 / T-03）。这些属**不同的一手资源**（论文摘要页与官方项目/数据集页各记录不同事实），均保留并互注，不视作重复；其余 4 组内部重复标题已随重复 URL 一并剔除。
- 跨轮重复：`N-01`（OSWorld, arXiv:2404.07972）与第一轮候选 `J-05` 同 URL，而 `J-05` 已在第一轮主题收敛时剔除，故总集中不重复；此处显式记录以免复核时误判。
- 第三轮：38 条补漏候选按前两轮已收录的 255 个 URL 预先排除，入集前再次程序化去重，剔除 0 条；其中 AA-13 / AA-14 是合并阶段从 simular-ai/Agent-S 官方 README 的 Updates / Citations 段落追出的两篇 Agent S3 / S4 配套论文，已逐页打开 arXiv 摘要页确认编号、标题、日期与摘要原文后补入，标题一律以 arXiv 页面为准（README 引用的长标题与页面标题不一致）。
- 合并结果：100 + 139 + 38 = **277 篇**，全部有可访问出处与页面依据。

**「高星 / 高评价」的硬证据**：
- 通过 GitHub 官方 REST API `https://api.github.com/repos/<owner>/<repo>` 于 2026-11-06T18:56:50+08:00 批量查询 56 个 CUA / GUI / VLM / 自动化相关仓库，成功取得 51 个仓库的 `stargazers_count`、`forks_count`、`language`、`license`、`pushed_at` 快照，存于 `star-evidence.json`。
- 另有 5 个仓库查询失败（GitHub API 限流 403 或 404），**未编造其 star 数**；总集中凡涉及这些仓库的条目，其影响力字段均不以 star 数作论据。
- 论文类的「高评价」证据只写页面明示的内容：会议录用信息（如 NeurIPS / ICLR / EMNLP / ACL）、官方 leaderboard 存在、官方组织署名、页面给出的具体数字；不写引用数、不写未经核实的获奖信息。
- 交叉校验：R 类条目「影响力」字段中由检索 Agent 独立取得的 star 数，与本脚本所用 API 快照可比对 17 个仓库，最大偏差 35 星（同一日内不同查询时刻的星标自然变动），无数量级或捏造偏差。

表：GitHub 官方 API 高星快照（按 star 降序，取成功查询的全部仓库）

| 仓库 | ★ | Fork | 语言 | 许可证 | 最近推送 | 总集内检索号 |
|---|---:|---:|---|---|---|---|
| ollama/ollama | 186,070 | 18,924 | Go | MIT | 2026-11-06 | —（背景证据，未单列条目） |
| ggml-org/llama.cpp | 133,536 | 25,202 | C++ | MIT | 2026-11-06 | —（背景证据，未单列条目） |
| browser-use/browser-use | 120,181 | 13,407 | Python | MIT | 2026-11-06 | R-01 |
| microsoft/playwright | 99,441 | 6,809 | TypeScript | Apache-2.0 | 2026-11-06 | —（背景证据，未单列条目） |
| vllm-project/vllm | 96,451 | 24,479 | Python | Apache-2.0 | 2026-11-06 | —（背景证据，未单列条目） |
| All-Hands-AI/OpenHands | 92,793 | 12,378 | TypeScript | MIT | 2026-11-06 | Z-05 |
| opencv/opencv | 91,473 | 57,082 | C++ | Apache-2.0 | 2026-11-06 | —（背景证据，未单列条目） |
| tesseract-ocr/tesseract | 77,379 | 10,897 | C++ | Apache-2.0 | 2026-11-02 | —（背景证据，未单列条目） |
| OpenInterpreter/open-interpreter | 68,813 | 5,935 | Rust | Apache-2.0 | 2026-11-04 | Z-06 |
| bytedance/UI-TARS-desktop | 39,555 | 4,025 | TypeScript | Apache-2.0 | 2026-10-09 | M-12 |
| SeleniumHQ/selenium | 34,577 | 8,726 | Java | Apache-2.0 | 2026-11-06 | —（背景证据，未单列条目） |
| trycua/cua | 31,855 | 2,372 | Rust | MIT | 2026-11-06 | R-02 |
| microsoft/OmniParser | 25,609 | 2,241 | Jupyter Notebook | CC-BY-4.0 | 2026-07-20 | Z-02 |
| haotian-liu/LLaVA | 25,075 | 2,771 | Python | Apache-2.0 | 2024-08-12 | —（背景证据，未单列条目） |
| Skyvern-AI/skyvern | 23,348 | 2,236 | Python | AGPL-3.0 | 2026-11-06 | Z-07 |
| appium/appium | 22,191 | 6,308 | TypeScript | Apache-2.0 | 2026-11-06 | —（背景证据，未单列条目） |
| QwenLM/Qwen2-VL | 20,170 | 1,885 | Jupyter Notebook | Apache-2.0 | 2026-01-30 | M-09 |
| QwenLM/Qwen2.5-VL | 20,170 | 1,885 | Jupyter Notebook | Apache-2.0 | 2026-01-30 | M-09 |
| anthropics/anthropic-quickstarts | 19,118 | 3,253 | Python | MIT | 2026-11-04 | Z-09 |
| vercel-labs/agent-desktop | 17,618 | 1,255 | Rust | Apache-2.0 | 2026-11-06 | R-04 |
| simular-ai/Agent-S | 12,892 | 1,504 | Python | Apache-2.0 | 2026-10-30 | R-06 |
| bytedance/UI-TARS | 11,681 | 888 | Python | Apache-2.0 | 2026-01-27 | M-07 |
| CursorTouch/Windows-MCP | 11,169 | 1,208 | Python | MIT | 2026-11-06 | R-07 |
| go-vgo/robotgo | 10,902 | 967 | Go | Apache-2.0 | 2026-11-04 | R-08 |
| OthersideAI/self-operating-computer | 10,305 | 1,411 | Python | MIT | 2026-10-19 | Z-08 |
| microsoft/UFO | 10,171 | 1,082 | Python | MIT | 2026-10-30 | R-09 |
| OpenGVLab/InternVL | 10,169 | 792 | Python | MIT | 2025-09-22 | —（背景证据，未单列条目） |
| X-PLUG/MobileAgent | 9,367 | 941 | Python | MIT | 2026-11-03 | —（背景证据，未单列条目） |
| TencentQQGYLab/AppAgent | 6,917 | 760 | Python | MIT | 2025-03-19 | —（背景证据，未单列条目） |
| THUDM/CogVLM | 6,744 | 452 | Python | Apache-2.0 | 2024-05-29 | —（背景证据，未单列条目） |
| lavague-ai/LaVague | 6,396 | 575 | Python | Apache-2.0 | 2025-01-21 | R-11 |
| pywinauto/pywinauto | 6,386 | 793 | Python | BSD-3-Clause | 2026-10-28 | —（背景证据，未单列条目） |
| microsoft/fara | 6,248 | 603 | Python | MIT | 2026-09-22 | R-12 |
| google-gemini/computer-use-preview | 3,267 | 410 | Python | Apache-2.0 | 2026-07-28 | M-10 |
| xlang-ai/OSWorld | 3,253 | 556 | Python | Apache-2.0 | 2026-11-02 | Z-01 |
| e2b-dev/open-computer-use | 2,405 | 269 | Python | Apache-2.0 | 2026-10-23 | —（背景证据，未单列条目） |
| showlab/computer_use_ootb | 1,979 | 196 | Python | Apache-2.0 | 2025-05-21 | —（背景证据，未单列条目） |
| showlab/ShowUI | 1,929 | 144 | Python | Apache-2.0 | 2026-04-24 | Z-03 |
| openai/openai-cua-sample-app | 1,922 | 440 | TypeScript | MIT | 2026-10-19 | Z-11 |
| OS-Copilot/OS-Copilot | 1,797 | 203 | Python | MIT | 2024-09-09 | Z-04 |
| web-arena-x/webarena | 1,642 | 248 | Python | Apache-2.0 | 2025-11-26 | —（背景证据，未单列条目） |
| microsoft/SoM | 1,571 | 111 | Python | MIT | 2024-08-19 | —（背景证据，未单列条目） |
| ServiceNow/BrowserGym | 1,429 | 216 | Python | NOASSERTION | 2026-10-28 | Z-10 |
| OSU-NLP-Group/Mind2Web | 1,036 | 123 | Jupyter Notebook | MIT | 2025-11-05 | T-04 |
| google-research/android_world | 1,005 | 204 | Python | Apache-2.0 | 2026-10-23 | —（背景证据，未单列条目） |
| microsoft/WindowsAgentArena | 915 | 107 | Python | MIT | 2026-10-26 | —（背景证据，未单列条目） |
| ServiceNow/AgentLab | 661 | 137 | Python | NOASSERTION | 2026-10-06 | —（背景证据，未单列条目） |
| njucckevin/SeeClick | 496 | 30 | HTML | Apache-2.0 | 2025-07-13 | T-09 |
| web-arena-x/visualwebarena | 490 | 81 | Python | MIT | 2024-11-09 | T-08 |
| OS-Copilot/OS-Atlas | 455 | 33 | Python | Apache-2.0 | 2025-04-20 | —（背景证据，未单列条目） |
| xlang-ai/OSWorld-V2 | 411 | 60 | Python | Apache-2.0 | 2026-10-23 | —（背景证据，未单列条目） |

查询失败未计入上表的仓库：`huggingface/smolagents`、`microsoft/onnxruntime`、`PyAutoGUI/PyAutoGUI`、`trycua/acu`、`ZJU-REAL/Awesome-GUI-Agents`。

**复跑方式**（中间材料与脚本，非交付物）：候选原文见 `.workbuddy-ai/research/raw-A.md` … `raw-X.md`、`raw-Y.md`、`raw-Z.md`、`raw-AA.md`；结构化候选见 `items.json` / `items-new.json` / `items-supp.json`；逐条状态码与标题相似度见 `verify-report.json` / `verify-report-new.json` / `verify-report-supp.json`；star 快照见 `star-evidence.json`。在 `.workbuddy-ai/research/` 下依次执行 `python verify.py check`、`python verify2.py check`、`python verify3.py check` 可重做核验，`python build2.py` 重新生成本总集。

## 三、分类索引
| 类 | 主题 | 篇数 | 编号 | 轮次 |
|---|---|---:|---|---|
| A | 主动式 / 常驻式智能体学术研究 | 8 | 001–008 | 一 |
| B | LLM 智能体基础架构与经典论文 | 9 | 009–017 | 一 |
| C | 国际云厂商 LLM API 官方文档 | 8 | 018–025 | 一 |
| D | 国内大模型平台官方 API 文档 | 9 | 026–034 | 一 |
| E | 智能体编排框架与 SDK 官方文档 | 9 | 035–043 | 一 |
| F | 家用机自托管编排 / 自动化平台官方文档 | 8 | 044–051 | 一 |
| G | 开放协议与工具调用标准 | 9 | 052–060 | 一 |
| H | 智能体记忆与长期状态 | 9 | 061–069 | 一 |
| I | 事件驱动、调度与常驻运行 | 8 | 070–077 | 一 |
| J | 智能体评测基准与成本 / 可靠性工程 | 6 | 078–083 | 一 |
| K | 家用硬件门槛与 API 成本一手资料 | 9 | 084–092 | 一 |
| L | 厂商工程指南、综述与主动任务产品证据 | 8 | 093–100 | 一 |
| M | 厂商官方 CUA 产品与技术文档 | 11 | 101–111 | 二 |
| N | CUA 系统架构学术论文 | 11 | 112–122 | 二 |
| O | GUI grounding 与屏幕视觉理解 | 12 | 123–134 | 二 |
| P | 浏览器 / Web 智能体 | 12 | 135–146 | 二 |
| Q | 移动端 / Android GUI 智能体 | 12 | 147–158 | 二 |
| R | 高星开源 CUA 实现（GitHub star 硬证据） | 12 | 159–170 | 二 |
| S | 桌面控制、无障碍与输入注入官方技术文档 | 12 | 171–182 | 二 |
| T | CUA 评测基准、数据集与公开榜单 | 12 | 183–194 | 二 |
| U | 视觉语言模型基座 | 11 | 195–205 | 二 |
| V | 长程规划、经验学习、失败恢复、人在回路 | 10 | 206–215 | 二 |
| W | 本地推理、量化与端侧部署 | 12 | 216–227 | 二 |
| X | 其他配套模块（语音 / 通知 / 可观测性 / 本地数据 / 状态持久化 / 桌面集成） | 12 | 228–239 | 二 |
| Y | 补漏：本地桌面 / 浏览器控制接口官方文档 | 12 | 240–251 | 三 |
| Z | 补漏：CUA 高星开源实现与官方示例仓库 | 12 | 252–263 | 三 |
| AA | 补漏：CUA 评测基准、数据集、公开榜单与关键方法论文 | 14 | 264–277 | 三 |
| **合计** | — | **277** | **001–277** | 三轮 |

## 四、CUA 专题文献地图（仅作资料定位，不是方案）
用户指定的重点是「能在本地计算机实际实现 CUA」的全量文献。按**资料类型**而非实施顺序，这些条目分布如下，便于按图索骥：

| 资料层次 | 对应类别 | 收录内容举例 |
|---|---|---|
| 厂商一手能力公告与 API 文档 | M | Anthropic computer use、OpenAI CUA / computer use、Gemini computer use、Microsoft Fara-7B、UI-TARS / UFO / Qwen-VL 官方仓库 |
| CUA 系统架构论文 | N、V | OSWorld、Agent S / S2、OS-Copilot、OS-ATLAS、UFO / UFO2、Windows Agent Arena、长程规划、经验学习、失败恢复、人在回路 |
| 屏幕理解与 GUI grounding | O、U | UI-TARS、CogAgent、SeeClick、OmniParser、Set-of-Mark、ScreenAI、Ferret-UI、Aguvis、ShowUI、Aria-UI、VLM 基座技术报告 |
| 浏览器 / 移动端智能体 | P、Q | Mind2Web、WebShop、WebVoyager、VisualWebArena、WorkArena、AndroidWorld、AitW、AppAgent、AutoDroid、Mobile-Agent 系列 |
| 本地动作落地的官方底层接口 | S、Y | Windows UI Automation / SendInput / 屏幕捕获、macOS AXUIElement / Quartz Event / ScreenCaptureKit、XTEST、Android UI Automator / AccessibilityService / adb、Playwright、CDP、WebDriver、OCR、模板匹配 |
| 高星开源实现 | R、Z | browser-use、trycua/cua、Agent-S、Windows-MCP、robotgo、OpenHands、Open Interpreter、Skyvern、OmniParser、Agent TARS 等，star 数见上表 |
| 评测基准 / 数据集 / 榜单 | T、AA | OSWorld 及 OSWorld 2.0、AndroidWorld、Windows Agent Arena、ScreenSpot-Pro、Spider2-V、WebArena 系、WorkArena、Mind2Web、The Agent Company |
| 本地推理与端侧部署 | W | vLLM / PagedAttention、GPTQ / AWQ / SmoothQuant、llama.cpp 量化、Ollama、MLX LM、SGLang、WebLLM、ONNX Runtime 量化 |
| 配套模块（与主动式 AI 共用） | A–L、X | 主动触发、记忆、调度、API 编排、开放协议、语音 I/O、通知、WebSocket、可观测性、本地检索与状态持久化、桌面集成 |

> 该表只说明「哪一类资料收在哪几类编号下」，不含组件选型、调用顺序、技术路线或任何实现建议。

## 五、文献总清单（001–277）

### A 类｜主动式 / 常驻式智能体学术研究（8 篇）

#### 001｜Foundations of Proactive Agents: Principles, Technical Layers, and Proactivity-Gym

- **检索号**：A-01　**类别**：A 主动式 / 常驻式智能体学术研究　**轮次**：第一轮
- **作者 / 机构**：Jio Oh、Seunghyun Do、Young-Jun Lee、Steven Euijong Whang、Dongyeop Kang（arXiv 预印本，cs.AI）
- **时间**：2026-09　**类型**：arXiv 预印本（主动式智能体基础研究/框架 + 评测平台）
- **出处**：<https://arxiv.org/abs/2609.37267>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Proactive LLM agents can turn idle compute into useful support before users ask.
- **要点**：给出 proactivity 的定义与 3T 联合原则（Task Capability、Temporal Allocation、Trust），并把设计空间拆成 task scope、anticipation horizon、activation trigger、processing timing、intervention depth 五个维度；另提出仿真评测平台 PROACTIVITY-GYM（多日场景、有状态环境、persona 条件模拟用户），30 人实验发现用户偏好 sleep-time assistance。
- **与主题关联**：它把主动式助理的核心归结为"空闲算力 + 触发时机 + 信任"的编排设计，本地无需大模型，按触发条件调度云 LLM API 即可实现。

#### 002｜Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance

- **检索号**：A-02　**类别**：A 主动式 / 常驻式智能体学术研究　**轮次**：第一轮
- **作者 / 机构**：Yaxi Lu、Shenzhi Yang、Cheng Qian 等（清华大学等，见检索结果；arXiv 预印本）
- **时间**：2024-10　**类型**：arXiv 预印本（cs.AI / cs.CL）
- **出处**：<https://arxiv.org/abs/2410.12361>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：developing proactive agents capable of anticipating and initiating tasks without explicit human instructions
- **要点**：针对多数 agent 仍是被动响应的问题，先从真实人类活动生成"主动任务预测"并由人工标注 accepted/rejected，训练 reward model 作为主动性自动评估器；再构建含 6,790 个事件的 ProactiveBench 数据集，微调后模型主动提供帮助的 F1 达 66.47%。
- **与主题关联**：主动预测由"观察事件 → 判断是否主动出手"的编排实现，家用机只需轻量事件源 + 云 API 即可承担该闭环。

#### 003｜Communication Policy Evolution for Proactive LLM Agents

- **检索号**：A-03　**类别**：A 主动式 / 常驻式智能体学术研究　**轮次**：第一轮
- **作者 / 机构**：Xinbei Ma、Jiyang Qiu、Yao Yao、Zhuosheng Zhang、Hai Zhao 等（arXiv 预印本，cs.AI）
- **时间**：2026-06　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2606.14314>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Building information asymmetry for proactive agents, we set up two complementary settings, User-Agent and Planner-Executor.
- **要点**：形式化"通信策略"，在文本与结构化 UI 两种通道下比较 User-Agent 与 Planner-Executor 设置，发现文本利于任务完成、结构化 UI 提升响应质量与 persona 一致性；提出 CPE 自进化框架，仅用 rollout + prompt 级演化（不改模型）即取得最佳任务成功率。
- **与主题关联**：主动式助理"何时、以何种方式"与用户沟通可在编排层用提示词演化实现，完全依赖调用云 LLM API 而非本地权重。

#### 004｜VisionClaw: Always-On AI Agents through Smart Glasses

- **检索号**：A-04　**类别**：A 主动式 / 常驻式智能体学术研究　**轮次**：第一轮
- **作者 / 机构**：Xiaoan Liu、DaeHo Lee、Eric J Gonzalez、Mar Gonzalez-Franco、Ryo Suzuki（arXiv 预印本，cs.HC）
- **时间**：2026-04　**类型**：arXiv 预印本（常驻式系统 + 用户研究）
- **出处**：<https://arxiv.org/abs/2604.03486>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：an always-on wearable AI agent that integrates live egocentric perception with agentic task execution
- **要点**：在 Meta Ray-Ban 智能眼镜上运行常驻式智能体，持续感知现实情境，并通过语音把任务委派给 OpenClaw AI agents（加购物车、从纸质文档生成笔记、收会议简报、从海报建日程、控 IoT）；实验室（N=12）与纵向部署（N=5）显示任务更"机会主义地"被发起、执行更多被委派而非手动控制。
- **与主题关联**：直接展示"常驻 + 实时感知 + 委派给云端 agent"的范式，家用机只承担轻感知/触发与 API 编排。

#### 005｜Personal LLM Agents: Insights and Survey about the Capability, Efficiency and Security

- **检索号**：A-07　**类别**：A 主动式 / 常驻式智能体学术研究　**轮次**：第一轮
- **作者 / 机构**：Yuanchun Li、Hao Wen、Weijun Wang、Xiangyu Li 等（综述；arXiv 预印本）
- **时间**：2024-01　**类型**：综述 / arXiv 预印本（cs.HC / cs.AI / cs.SE）
- **出处**：<https://arxiv.org/abs/2401.05459>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Personal LLM Agents, which are LLM-based agents that are deeply integrated with personal data and personal devices and used for personal assistance
- **要点**：系统讨论与个人数据、个人设备深度集成的 Personal LLM Agents，指出传统智能个人助理（IPA）受限于缺乏意图理解、任务规划、工具使用、个人数据管理等能力，而 LLM 可补足；综述其架构、能力、效率与安全挑战及代表方案，并汇集领域专家意见。
- **与主题关联**：直接给出"个人助理 = LLM + 意图理解 + 规划 + 工具 + 个人数据"的架构蓝图，支撑家用机以编排方式调用云 API 实现个人助理（此文为能力/架构综述，非攻击类主题）。

#### 006｜Lifelong Learning of Large Language Model based Agents: A Roadmap

- **检索号**：A-08　**类别**：A 主动式 / 常驻式智能体学术研究　**轮次**：第一轮
- **作者 / 机构**：Junhao Zheng、Chengming Shi、Xidi Cai、Qiuke Li、Duzhen Zhang、Qianli Ma 等（综述；已被 IEEE TPAMI 接收）
- **时间**：2025-01　**类型**：综述 / arXiv 预印本（期刊录用）
- **出处**：<https://arxiv.org/abs/2501.07278>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：This survey is the first to systematically summarize the potential techniques for incorporating lifelong learning into LLM-based agents.
- **要点**：首个系统梳理 LLM 智能体终身学习（continual/incremental learning）的综述，把智能体拆为感知（多模态输入整合）、记忆（存取演化知识）、行动（与动态环境交互）三模块，讨论持续适应、缓解灾难性遗忘、提升长期性能，并给出趋势、评测指标与应用场景路线图。
- **与主题关联**：常驻式助理需"持续在线、随环境演化"，其感知-记忆-行动闭环可由编排层 + 云 API 长期维持，不必本地训练大模型。

#### 007｜A Survey on Large Language Model based Autonomous Agents

- **检索号**：A-09　**类别**：A 主动式 / 常驻式智能体学术研究　**轮次**：第一轮
- **作者 / 机构**：Lei Wang、Chen Ma、Xueyang Feng、Wayne Xin Zhao、Ji-Rong Wen 等（中国人民大学等；综述）
- **时间**：2023-08（v7 2025-03）　**类型**：综述 / arXiv 预印本（cs.AI / cs.CL）
- **出处**：<https://arxiv.org/abs/2308.11432>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：we propose a unified framework that encompasses a majority of the previous work
- **要点**：从整体视角系统综述 LLM 自主智能体研究，先提出涵盖多数既有工作的统一构建框架，再梳理其在社科、自然科学、工程中的应用与常用评测策略，最后讨论挑战与未来方向，并维护持续更新的文献库。
- **与主题关联**：为"会规划、会调用工具的自主智能体"提供权威架构综述，说明能力来自编排框架而非本地模型规模。

#### 008｜From Reactive to Proactive: Assessing the Proactivity of Voice Agents via ProVoice-Bench

- **检索号**：A-10　**类别**：A 主动式 / 常驻式智能体学术研究　**轮次**：第一轮
- **作者 / 机构**：Ke Xu、Yuhao Wang、Yu Wang（arXiv 预印本；投稿 Interspeech 2026）
- **时间**：2026-04　**类型**：会议投稿 / 评测基准（arXiv 预印本，cs.AI / cs.CL / cs.SD）
- **出处**：<https://arxiv.org/abs/2604.15037>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：overlooking the complexities of proactive intervention and monitoring
- **要点**：指出现有基准偏重被动响应、忽视"主动干预与监测"的复杂性，提出首个面向主动语音智能体的评测框架 ProVoice-Bench（4 个任务、1,182 条高质量样本）；对 SOTA 多模态 LLM 的评测显示明显性能差距，尤其是 over-triggering（过度触发）与推理能力。
- **与主题关联**：把"事件触发的时机判断"作为主动式助理的关键可评测维度，说明常驻助理需在编排层解决"何时主动出手"，而非依赖本地模型。

### B 类｜LLM 智能体基础架构与经典论文（9 篇）

#### 009｜ReAct: Synergizing Reasoning and Acting in Language Models

- **检索号**：B-01　**类别**：B LLM 智能体基础架构与经典论文　**轮次**：第一轮
- **作者 / 机构**：Shunyu Yao、Jeffrey Zhao、Dian Yu 等（Princeton University、Google Research）
- **时间**：2022-10　**类型**：会议论文（ICLR 2023；arXiv 预印本 v3 标注为 ICLR camera ready 版）
- **出处**：<https://arxiv.org/abs/2210.03629>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：generate both reasoning traces and task-specific actions in an interleaved manner
- **要点**：提出让 LLM 交错地生成「推理轨迹」与「任务特定动作」，用推理来归纳、跟踪、更新行动计划并处理异常，用动作对接外部知识库或环境以补充信息。在 HotpotQA、FEVER 上通过与简单 Wikipedia API 交互缓解思维链的幻觉，在 ALFWorld、WebShop 上仅用一两个上下文示例即超过模仿学习与强化学习方法。
- **与主题关联**：确立「推理—行动」循环只需模型调用外部 API 即可闭环，家用机不必本地跑模型，编排云端 LLM 就能驱动会查证、会行动的助理。

#### 010｜Toolformer: Language Models Can Teach Themselves to Use Tools

- **检索号**：B-02　**类别**：B LLM 智能体基础架构与经典论文　**轮次**：第一轮
- **作者 / 机构**：Timo Schick、Jane Dwivedi-Yu、Roberto Dessì 等（Meta AI / FAIR、University of Washington 等）
- **时间**：2023-02　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2302.04761>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：LMs can teach themselves to use external tools via simple APIs
- **要点**：提出 Toolformer，以自监督方式让语言模型自己学会「调用哪些 API、何时调用、传什么参数、如何把结果并入后续生成」，每个 API 仅需少量示范。融入计算器、问答、两种搜索引擎、翻译系统和日历后，在多种下游任务上显著提升零样本表现且未牺牲核心语言建模能力。
- **与主题关联**：说明工具调用能力可由「模型 + 简单 API」构成，能力在云端、编排在本地，正是家用机靠 API 编织助理的底层机制。

#### 011｜Reflexion: Language Agents with Verbal Reinforcement Learning

- **检索号**：B-03　**类别**：B LLM 智能体基础架构与经典论文　**轮次**：第一轮
- **作者 / 机构**：Noah Shinn、Federico Cassano、Edward Berman 等（Northeastern University、Princeton University、MIT 等）
- **时间**：2023-03　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2303.11366>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer
- **要点**：提出不更新权重、而用「语言反馈」强化语言智能体的 Reflexion 框架，智能体对任务反馈作口头反思并把反思文本存入情景记忆缓冲，以改进后续试验的决策。在序列决策、编码与语言推理任务上明显优于基线，HumanEval 上 pass@1 达 91%，超过当时 GPT-4 的 80%。
- **与主题关联**：自我反思与经验记忆都可作为文本经 API 反复读写实现，无需本地训练或本地大模型，为常驻助理的「越用越聪明」提供轻量路径。

#### 012｜Tree of Thoughts: Deliberate Problem Solving with Large Language Models

- **检索号**：B-04　**类别**：B LLM 智能体基础架构与经典论文　**轮次**：第一轮
- **作者 / 机构**：Shunyu Yao、Dian Yu、Jeffrey Zhao、Thomas L. Griffiths 等（Princeton University、Google DeepMind）
- **时间**：2023-05　**类型**：会议论文（NeurIPS 2023；arXiv 预印本 v2 标注为 camera ready 版）
- **出处**：<https://arxiv.org/abs/2305.10601>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：enables exploration over coherent units of text (thoughts) that serve as intermediate steps toward problem solving
- **要点**：提出 Tree of Thoughts（ToT），把思维链推广为对连贯「思维单元」的树状搜索，允许模型考虑多条推理路径、自我评估选择并在需要时前瞻或回溯。在 24 点、创意写作、迷你填字三类需规划与搜索的任务上大幅提升解题能力，24 点上 GPT-4 思维链仅 4% 而 ToT 达 74%。
- **与主题关联**：把「规划」实现为对云端 LLM 的多路调用与自评选择，本地只做搜索编排，无需本地算力即可获得审慎规划能力。

#### 013｜Generative Agents: Interactive Simulacra of Human Behavior

- **检索号**：B-06　**类别**：B LLM 智能体基础架构与经典论文　**轮次**：第一轮
- **作者 / 机构**：Joon Sung Park、Joseph C. O'Brien、Carrie J. Cai、Percy Liang、Michael S. Bernstein 等（Stanford University、Google Research）
- **时间**：2023-04　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2304.03442>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：store a complete record of the agent's experiences using natural language, synthesize those memories over time into higher-level reflections, and retrieve them dynamically to plan behavior
- **要点**：提出可模拟可信人类行为的生成式智能体架构，用自然语言完整记录经历、把记忆逐步综合为更高层反思、并动态检索以规划行为。在类《模拟人生》沙盒中 25 个智能体仅凭一条「想办情人节派对」的设定，便自发传播邀请、结交、约会并协同准时到场；消融表明观察、规划、反思三者都关键。
- **与主题关联**：证明记忆、反思、规划与自主发起行为可由「LLM + 外部存储检索」支撑，家用机只需编排云端模型与本地记忆库即可让助理自主触发、带记忆、会规划。

#### 014｜MemGPT: Towards LLMs as Operating Systems

- **检索号**：B-07　**类别**：B LLM 智能体基础架构与经典论文　**轮次**：第一轮
- **作者 / 机构**：Charles Packer、Sarah Wooders、Kevin Lin、Ion Stoica、Joseph E. Gonzalez 等（UC Berkeley）
- **时间**：2023-10　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2310.08560>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：virtual context management, a technique drawing inspiration from hierarchical memory systems in traditional operating systems
- **要点**：受操作系统分层内存启发提出「虚拟上下文管理」，让系统在快慢存储间搬运数据以突破 LLM 有限上下文窗口，并用中断管理自身与用户之间的控制流。在文档分析上可处理远超底层 LLM 上下文长度的文档，在多会话聊天上可创建能记忆、反思、随长期交互动态演化的对话智能体。
- **与主题关联**：把长期记忆做成操作系统式的外置分层管理，本地只需调度上下文，云端 LLM 提供推理，支撑常驻个人助理跨会话不遗忘。

#### 015｜Cognitive Architectures for Language Agents

- **检索号**：B-08　**类别**：B LLM 智能体基础架构与经典论文　**轮次**：第一轮
- **作者 / 机构**：Theodore R. Sumers、Shunyu Yao、Karthik Narasimhan、Thomas L. Griffiths（Princeton University）
- **时间**：2023-09　**类型**：期刊论文（TMLR；arXiv 预印本 v3 标注为 TMLR camera ready 版）
- **出处**：<https://arxiv.org/abs/2309.02427>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：describes a language agent with modular memory components, a structured action space to interact with internal memory and external environments
- **要点**：借鉴认知科学与符号 AI 提出 CoALA 认知架构，用模块化记忆组件、与内部记忆及外部环境交互的结构化动作空间、以及通用的动作选择决策过程来刻画语言智能体。以此回顾并组织大量近期工作，并前瞻性指出通往更强智能体的方向，为把 LLM 放进经典 AI 脉络提供统一框架。
- **与主题关联**：给出「记忆 + 动作空间 + 决策循环」的通用蓝图，说明主动式助理是编排问题而非本地算力问题，家用机按此架构调用云端 LLM 即可搭建。

#### 016｜HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face

- **检索号**：B-09　**类别**：B LLM 智能体基础架构与经典论文　**轮次**：第一轮
- **作者 / 机构**：Yongliang Shen、Kaitao Song、Xu Tan、Dongsheng Li、Weiming Lu、Yueting Zhuang（浙江大学、Microsoft Research Asia）
- **时间**：2023-03　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2303.17580>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：LLMs could act as a controller to manage existing AI models to solve complicated AI tasks
- **要点**：主张以 LLM 作控制器、以语言为通用接口管理既有 AI 模型来解决复杂任务，提出 HuggingGPT：收到请求后由 ChatGPT 做任务规划，按 Hugging Face 模型功能描述选模型、执行各子任务并汇总结果。借助 ChatGPT 的语言能力与社区海量模型，可覆盖语言、视觉、语音等多模态多领域复杂任务。
- **与主题关联**：是「家用机当编排器、云端 LLM 当大脑、外部模型/工具当手脚」的直接范例，复杂能力全部经 API 调度获得。

#### 017｜MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework

- **检索号**：B-10　**类别**：B LLM 智能体基础架构与经典论文　**轮次**：第一轮
- **作者 / 机构**：Sirui Hong、Mingchen Zhuge、Jiaqi Chen、Jürgen Schmidhuber 等（DeepWisdom、KAUST 等）
- **时间**：2023-08　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2308.00352>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：encodes Standardized Operating Procedures (SOPs) into prompt sequences for more streamlined workflows
- **要点**：针对多智能体简单串联 LLM 易生级联幻觉的问题，提出把标准化操作流程（SOP）编码进提示序列的元编程框架，让具备类人领域专长的智能体验证中间结果、减少错误，并以流水线范式分配多样角色、把复杂任务拆解给多智能体协作。在协作式软件工程基准上生成比此前基于聊天的多智能体系统更连贯的解决方案。
- **与主题关联**：展示多智能体协作与任务分解可由提示词与 API 编排实现，家用机无需本地大模型即可组建分工协作的常驻助理团队。

### C 类｜国际云厂商 LLM API 官方文档（8 篇）

#### 018｜Structured model outputs | OpenAI API

- **检索号**：C-01　**类别**：C 国际云厂商 LLM API 官方文档　**轮次**：第一轮
- **作者 / 机构**：OpenAI
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://platform.openai.com/docs/guides/structured-outputs>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验；独立抓取二次确认「Structured model outputs | OpenAI API（直连 403，独立抓取可读正文）」
- **页面依据**：章节 "Structured Outputs vs JSON mode"、"When to use Structured Outputs via function calling vs via text.format"；请求参数 `text: { format: { type: "json_schema", "strict": true, "schema": ... } }` 与 `response_format: {type: "json_schema", ...}`；原文短语 "Reliable type-safety"
- **要点**：定义 Structured Outputs 能力，要求模型输出严格符合开发者提供的 JSON Schema，通过 `text.format`／`response_format` 的 `json_schema` 加 `strict: true` 开启，并列出支持模型与 JSON Schema 约束。页面明确区分结构化输出、JSON mode 与经由 function calling 的约束路径，说明其"无需校验或重试格式错误响应"的类型安全保证。
- **与主题关联**：家用机把助理的决策结果（待办、日程、动作指令）交给云端按 Schema 稳定产出，本地只做轻量解析与执行，无需本地模型即可获得可编排的结构化状态。

#### 019｜Tool use with Claude - Claude Platform Docs

- **检索号**：C-03　**类别**：C 国际云厂商 LLM API 官方文档　**轮次**：第一轮
- **作者 / 机构**：Anthropic
- **时间**：n.d.（官方文档）　**类型**：官方 API 文档
- **出处**：<https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验；站点重定向至 https://claude.com/app-unavailable-in-region；独立抓取二次确认「Tool use with Claude - Claude Platform Docs」
- **页面依据**：章节 "How tool use works"、"When Claude uses tools"、"Choose a tool"、"Pricing"；原文 "Tool use (also called function calling) lets Claude call functions that you define or that Anthropic provides."；参数与字段 `tools`、`input_schema`、`tool_choice={"type": "auto"}`、`stop_reason: "tool_use"`、`tool_use`、`tool_result`、`strict: true`
- **要点**：完整定义 Claude 的工具调用（function calling）机制，区分在应用侧执行的 client tools 与在 Anthropic 基础设施执行的 server tools（web_search、code_execution 等），并给出 `tool_use` → 本地执行 → `tool_result` 回传的 agentic loop 往返流程。页面还规定 `tool_choice` 的自动／强制行为、strict tool use 的 schema 强一致、以及工具调用按 `tools` 参数 token 与服务端用量计费的定价结构。
- **与主题关联**：这是"主动式代理"的核心一环——家用机只需注册本地函数、把云端返回的 `tool_use` 执行后回传，即可让助理主动查信息、跑脚本、操作系统，而无需本地跑模型。

#### 020｜Function calling with the Gemini API - Gemini API | Google AI Studio

- **检索号**：C-05　**类别**：C 国际云厂商 LLM API 官方文档　**轮次**：第一轮
- **作者 / 机构**：Google（Gemini API / Google AI Studio）
- **时间**：n.d.（官方文档）　**类型**：官方 API 文档
- **出处**：<https://ai.google.dev/gemini-api/docs/function-calling>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「Function calling with the Gemini API - Gemini API | Google AI Studio」
- **页面依据**：章节 "How function calling works"、"Function calling modes"、"Parallel function calling"、"Compositional function calling"、"Stream tool calls"、"Remote MCP (Model Context Protocol)"；原文 "Function calling lets you connect models to external tools and APIs."；参数 `tools`、`tool_choice`（`auto`／`any`／`none`／`validated`）、`previous_interaction_id`、`function_call`、`function_result`
- **要点**：定义 Gemini 的函数调用流程，通过 `tools` 传入函数声明、`generation_config`／`tool_choice` 控制调用模式，并支持并行调用、组合式多步调用与流式工具调用。页面还覆盖 Remote MCP 服务器接入、结构化输出与函数调用的配合以及函数声明的 JSON Schema 字段，给出从声明、调用、执行到结果回传的四步链路。
- **与主题关联**：家用机把操作系统、日历、家居设备封装成函数声明交给云端，模型自主决定调用顺序并串起多步任务，本机只负责执行回传，形成主动式代理的行动层。

#### 021｜Function Calling | Mistral Docs

- **检索号**：C-06　**类别**：C 国际云厂商 LLM API 官方文档　**轮次**：第一轮
- **作者 / 机构**：Mistral AI
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://docs.mistral.ai/capabilities/function_calling>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「Function Calling | Mistral Docs」
- **页面依据**：章节 "Five Steps"（Step 1–5）、"Full Example"；参数 `client.chat.complete(...)` 中的 `tools`、`tool_choice`（`auto`／`any`／`none`）、`parallel_tool_calls`；字段 `tool_calls`、`tool_call.function.arguments`、`tool_call_id`；原文 "allows Mistral models to connect to external local tools"
- **要点**：以"五步"流程定义 Mistral 的函数调用：开发者定义函数与系统提示、用户提问、模型生成函数参数、开发者执行函数、模型生成最终回答。页面规定 `tools` 中的 `function`／`parameters` JSON Schema、`tool_choice` 三种取值与 `parallel_tool_calls` 开关，以及 `response.choices[0].message.tool_calls` 的读取方式。
- **与主题关联**：提供又一家可替换的云端后端，家用机用同一套"声明工具—执行—回传"编排即可切换模型厂商，避免被单一供应商锁定，也无需本地算力。

#### 022｜Basic usage of tool use (function calling) | Cohere

- **检索号**：C-07　**类别**：C 国际云厂商 LLM API 官方文档　**轮次**：第一轮
- **作者 / 机构**：Cohere
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://docs.cohere.com/docs/tool-use>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：章节 "Tool use workflow"、"State management"、"Multi-step tool use (agents)"、"Parallel tool calling"；调用 `co.chat(model="command-a-plus-05-2026", messages=messages, tools=tools)`；字段 `tool_plan`、`tool_calls`、`tool_call_id`、citations；原文 "Tool use connects models to external tools like search engines and APIs."
- **要点**：以端到端示例定义 Cohere Chat endpoint 的工具使用：`tools` 定义函数 schema，模型先产出 `tool_plan` 与 `tool_calls`，应用执行后以 `role="tool"` 消息回传，并在 `messages` 中做状态管理以支撑多步代理。页面还说明带引用的响应生成、并行工具调用与 `Step 1`–`Step 4` 的显式工作流。
- **与主题关联**：文档把"多步工具使用（agents）"和状态管理写进 API 用法，家用机可据此让常驻助理跨轮次持续跟踪任务状态，而不必在本地维护大模型推理。

#### 023｜Tool Use Overview - GroqDocs

- **检索号**：C-08　**类别**：C 国际云厂商 LLM API 官方文档　**轮次**：第一轮
- **作者 / 机构**：Groq
- **时间**：n.d.（官方文档）　**类型**：官方 API 文档
- **出处**：<https://console.groq.com/docs/tool-use>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验；独立抓取二次确认「Tool Use Overview - GroqDocs」
- **页面依据**：章节 "How Tool Use Works"、"Groq Built-In Tools"、"Remote Tool Calling with MCP"、"Local Tool Calling (Function Calling)"、"Why Groq's Speed Matters"；原文 "Tool use (or function calling) is what transforms a language model from a conversational interface into an autonomous agent capable of taking action"；参数 `tools`、`tool_calls`、`tool_call_id`、`parallel tool use`
- **要点**：定义工具调用的四步循环（请求带 `tools` 定义→模型返回 `tool_calls`→执行并回传 `tool_result`→模型继续或结束），并对比三种模式：Groq 内置工具、经 MCP 的远端工具、本地函数调用，还列出支持模型的并行工具与 JSON mode 能力表。页面强调代理循环常需 2–10+ 次推理调用，而 Groq 的 300–1,000+ tokens/秒推理速度使多步代理体验接近瞬时。
- **与主题关联**：主动式代理是多轮推理密集负载，家用机把推理全部外包给高速云端即可获得"即时"响应，本地仅承担工具执行，正是"不本地跑大模型"的直接论据。

#### 024｜OpenRouter Quickstart Guide

- **检索号**：C-09　**类别**：C 国际云厂商 LLM API 官方文档　**轮次**：第一轮
- **作者 / 机构**：OpenRouter
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://openrouter.ai/docs/quickstart>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：章节 "Using the OpenRouter API"、"Using the Client SDKs"、"Using the Agent SDK"、"Using the OpenAI SDK"；原文 "OpenRouter gives you access to hundreds of AI models through a single API endpoint. It handles fallbacks automatically and picks the most cost-effective option for each request."；`/api/v1/responses`、`@openrouter/agent`、`callModel`、`@openrouter/sdk`、`GET /api/v1/models`、链接 "free models and rate limits" FAQ
- **要点**：定义通过单一 `POST /api/v1/responses` 端点访问数百个模型的接入方式，说明三种集成路径：原生 API、类型安全的 Client SDK、以及处理多轮循环／工具执行／状态管理的 Agent SDK（`callModel`）。页面还说明自动 fallback、按成本选路、OpenAI SDK 作为 drop-in 替换、可选的 `HTTP-Referer`／`X-OpenRouter-Title` 归属头，以及免费模型与速率限制 FAQ 入口。
- **与主题关联**：家用机只需一个 API Key 和一个端点即可在多家模型间自动切换与降级，Agent SDK 把工具循环与状态管理托管到云端侧能力，是"轻本地、重编排"最省事的落地形态。

#### 025｜Function calling patterns - Together AI docs

- **检索号**：C-10　**类别**：C 国际云厂商 LLM API 官方文档　**轮次**：第一轮
- **作者 / 机构**：Together AI
- **时间**：n.d.（官方文档）　**类型**：官方参考
- **出处**：<https://docs.together.ai/docs/function-calling>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验；独立抓取二次确认「Function calling patterns - Together AI docs」
- **页面依据**：章节 "Patterns"、"Supported models"、"Next steps"；原文 "Function calling lets LLMs respond with structured function names and arguments your application can execute."；参数 `tools`、`tool_calls`；模式条目 "Simple"、"Parallel"、"Multi-step"、"Multi-turn"、"Agentic patterns"
- **要点**：把函数调用归纳为 Simple／Multiple／Parallel／Parallel multiple／Multi-step／Multi-turn／Vision 七种模式，并给出各自适用场景与可运行示例入口，说明向 `tools` 参数传函数描述、模型返回 `tool_calls` 后由应用执行并可回传结果。页面还提供支持函数调用的 serverless 与专用端点模型目录指引。
- **与主题关联**：文档把"多步、多轮、人在回路"的代理模式直接列为标准用法，家用机按模式表选择编排方式即可让云端模型持续推进任务，无需本地承载模型推理。

### D 类｜国内大模型平台官方 API 文档（9 篇）

#### 026｜首次调用 API | DeepSeek API Docs

- **检索号**：D-01　**类别**：D 国内大模型平台官方 API 文档　**轮次**：第一轮
- **作者 / 机构**：深度求索 DeepSeek（DeepSeek API Docs / 开放平台）
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://platform.deepseek.com/api-docs/zh-cn/api/deepseek-api>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："DeepSeek API 使用与 OpenAI/Anthropic 兼容的 API 格式"、"您可以将 stream 设置为 true 来使用流式输出"、`https://api.deepseek.com/chat/completions`、`"model": "deepseek-flash"`、`"stream": false`
- **要点**：页面给出 curl/Python/Node 三种首次调用对话补全的样例，并说明 API 采用与 OpenAI/Anthropic 兼容的格式、只需替换 base_url 与 api_key。示例明确用 `stream` 参数在流式与非流式之间切换。
- **与主题关联**：家用机只需按 OpenAI 兼容格式发一个 HTTP 请求即可调用云端模型，无需本地部署权重。

#### 027｜DeepSeek API 创新采用硬盘缓存，价格再降一个数量级

- **检索号**：D-02　**类别**：D 国内大模型平台官方 API 文档　**轮次**：第一轮
- **作者 / 机构**：深度求索 DeepSeek（DeepSeek API Docs）
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://api-docs.deepseek.com/zh-cn/news/news0802>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："上下文硬盘缓存技术"、"缓存命中的部分，DeepSeek 收费 0.1元 每百万 tokens"、`prompt_cache_hit_tokens`、`prompt_cache_miss_tokens`、"对所有用户均不限流、不限并发"、"最高可以节省 90% 的费用"
- **要点**：官方说明上下文硬盘缓存自动生效、无需修改代码，重复前缀按缓存命中计费，并在 usage 中返回命中/未命中 token 数。文档同时给出定价、缓存命中率与并发限流说明。
- **与主题关联**：常驻助理的长系统提示与多轮历史由云端缓存承担，家用机既不存权重也不承担重复上下文的算力与成本。

#### 028｜如何通过Function Calling 实现工具调用-大模型服务平台百炼(Model Studio)-阿里云帮助中心

- **检索号**：D-03　**类别**：D 国内大模型平台官方 API 文档　**轮次**：第一轮
- **作者 / 机构**：阿里云 · 大模型服务平台百炼（Model Studio）/ 阿里云帮助中心
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://help.aliyun.com/zh/model-studio/qwen-function-calling>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Function Calling 允许模型调用外部工具（API、数据库、自定义函数等）"、"方式一：通过 tools 参数传入（推荐）"、`tool_calls`、`tool_choice`、`parallel_tool_calls`、`tool_call_id`、章节"流式输出"、"运行工具函数的过程由您的计算环境而非大模型来完成"
- **要点**：文档完整描述"定义工具→发起调用→应用端执行工具→回传结果→模型总结"的多步 Function Calling 流程，并列出 tools、tool_calls、tool_choice、parallel_tool_calls 等参数。还给出并行工具调用、强制工具调用、流式输出与 Responses API 工具调用等进阶用法。
- **与主题关联**：明确"工具在本地执行、模型在云端决策"，正是家用机只做编排、把推理交给云端的分工依据。

#### 029｜首次调用千问API-大模型服务平台百炼(Model Studio)-阿里云帮助中心

- **检索号**：D-04　**类别**：D 国内大模型平台官方 API 文档　**轮次**：第一轮
- **作者 / 机构**：阿里云 · 大模型服务平台百炼（Model Studio）/ 阿里云帮助中心
- **时间**：2026　**类型**：官方指南
- **出处**：<https://help.aliyun.com/zh/model-studio/product-overview/call-qwen-by-calling-api>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："阿里云百炼支持通过 API 调用大模型，涵盖 OpenAI 兼容接口、DashScope SDK 等接入方式"、`compatible-mode/v1/chat/completions`、`https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1`、"API 调用与操作系统版本无关，只要网络能连通即可正常使用"、`messages`、`model="qwen-plus"`
- **要点**：页面按账号、API Key、环境变量、SDK 安装的顺序引导完成首次 API 调用，并给出 Python/Node.js/curl/Go/PHP/C# 的 OpenAI 兼容 HTTP 示例。原文明确"API 调用与操作系统版本无关，只要网络能连通即可正常使用"。
- **与主题关联**：直接证明常驻助理对本地硬件无要求，只要一台能联网的家用机按兼容接口编排即可。

#### 030｜GLM-5 - 智谱AI开放文档

- **检索号**：D-05　**类别**：D 国内大模型平台官方 API 文档　**轮次**：第一轮
- **作者 / 机构**：智谱 AI（智谱AI开放文档 / bigmodel.cn 开放平台）
- **时间**：n.d.（官方文档）　**类型**：官方参考
- **出处**：<https://docs.bigmodel.cn/cn/guide/models/text/glm-5>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："面向 Agentic Engineering 打造"、"MCP 可灵活调用外部 MCP 工具与数据源"、"MCP-Atlas（工具调用和多步骤任务执行）"、`https://open.bigmodel.cn/api/paas/v4/chat/completions`、`"stream": true`"启用流式输出"、`thinking`、`max_tokens`
- **要点**：模型页列出 200K 上下文窗口与 Agent、工具调用、MCP 等能力，并给出 cURL、Python、Java 的基础调用与流式调用示例。示例展示 `chat/completions` 端点与 `stream: true` 的流式返回处理。
- **与主题关联**：云端模型原生具备长程 Agent 与工具调用能力，编排逻辑放在家用机即可驱动主动式助理。

#### 031｜如何在 Kimi API 中使用官方工具 - Kimi API 开放平台

- **检索号**：D-06　**类别**：D 国内大模型平台官方 API 文档　**轮次**：第一轮
- **作者 / 机构**：月之暗面 Moonshot AI（Kimi API 开放平台）
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://platform.moonshot.cn/docs/guide/use-official-tools>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Formula API 官方工具通道（OpenAI 协议，标准 `function` tool）"、`POST /v1/chat/completions`、`tools`、`tool_calls`、`finish_reason=tool_calls`、`tool_call_id`、章节"在 Chat Completions 中接入官方工具"
- **要点**：文档说明如何在 Chat Completions API 中通过标准 `function` tool 协议接入官方工具（联网搜索、记忆、Excel、日期、fetch 等），并给出四步调用链路与完整 Python 示例。工具由平台以 Formula 形式托管执行，本地仅负责拼接 messages 与回传 tool 结果。
- **与主题关联**：连工具执行都能托管到云端，家用机只需做请求编排与结果拼装，最适合轻量常驻助理。

#### 032｜混元 OpenAI 兼容接口相关调用示例（腾讯混元大模型 兼容接口 - Tencent Cloud）

- **检索号**：D-07　**类别**：D 国内大模型平台官方 API 文档　**轮次**：第一轮
- **作者 / 机构**：腾讯云 · 腾讯混元大模型（Tencent Cloud 文档中心）
- **时间**：2026　**类型**：官方 API 文档
- **出处**：<https://cloud.tencent.com/document/product/1729/111007>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验；独立抓取二次确认「腾讯混元大模型 混元 OpenAI 兼容接口相关调用示例_腾讯云」
- **页面依据**："混元 API 兼容了 OpenAI 的接口规范，这意味着您可以直接使用 OpenAI 官方提供的 SDK 来调用混元大模型"、`base_url：https://api.hunyuan.cloud.tencent.com/v1`、`https://api.hunyuan.cloud.tencent.com/v1/chat/completions`、章节"Function Calling"、`tools`、`tool_calls`、`finish_reason`
- **要点**：页面提供对话、多轮对话、图生文、Function Calling、Embedding 的 OpenAI 兼容调用示例，并强调仅替换 `base_url` 和 `api_key` 即可无缝迁移。还列出 `tools`、`tool_calls`、`tool_call_id` 等字段与"默认限制为5个并发"的配额说明。
- **与主题关联**：一套 OpenAI SDK 即可接入云端混元，家用机不用改应用架构就能编排对话与函数调用。

#### 033｜Create a Chat Completion

- **检索号**：D-08　**类别**：D 国内大模型平台官方 API 文档　**轮次**：第一轮
- **作者 / 机构**：硅基流动 SiliconFlow（SiliconFlow 文档中心）
- **时间**：n.d.（官方文档）　**类型**：官方 API 文档
- **出处**：<https://docs.siliconflow.cn/cn/api-reference/chat-completions/chat-completions>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`stream` "Server-Sent Events"、"data: [DONE]"、`response_format`、`{ "type": "json_schema", "json_schema": {...} }` "enables Structured Outputs"、`tools` "A list of tools the model may call"、`429` "Request was rejected due to rate limiting"、"TPM limit reached"、`prompt_cache_hit_tokens`、`https://api.siliconflow.cn/v1/chat/completions`
- **要点**：官方 Chat Completions API 参考列出 model、messages、stream、response_format（json_schema 结构化输出）、tools、reasoning_effort 等参数，并给出 OpenAI SDK（base_url 指向 `api.siliconflow.cn/v1`）与 Function Calling 流式示例。响应示例含 `prompt_cache_hit_tokens`、`prompt_cache_miss_tokens`，错误码含 429 限流。
- **与主题关联**：结构化输出、流式、工具调用与限流配额全部由云端 API 提供，家用机只处理编排与解析。

#### 034｜豆包助手 - 火山方舟 - 火山引擎

- **检索号**：D-09　**类别**：D 国内大模型平台官方 API 文档　**轮次**：第一轮
- **作者 / 机构**：火山引擎 · 火山方舟（字节跳动）
- **时间**：n.d.（官方文档）　**类型**：官方 API 文档
- **出处**：<https://www.volcengine.com/docs/82379/1978533>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验；站点重定向至 https://docs.volcengine.com/docs/ark/doubao-assistant?lang=zh；独立抓取二次确认「豆包助手 - 火山方舟 - 火山引擎（旧地址 200 并跳转新文档域）」
- **页面依据**："通过 Responses API，您可将豆包 App 同款 AI 能力…快速集成至自有应用"、`https://ark.cn-beijing.volces.com/api/v3/responses`、`"stream": true`、`tools`、`store`、`previous_response_id`、"Function Calling（函数调用）"、"单个账号调用频率上限为 2 QPS"
- **要点**：文档说明豆包助手 API 通过 Responses API 以 tools 方式提供日常沟通、深度沟通、联网搜索、边想边搜，含 stream、store、previous_response_id 等参数与 cURL/Python/Java/Go 示例。并给出按次计费、2 QPS 默认限流及与 Function Calling 的互斥说明。
- **与主题关联**：连搜索、角色设定与上下文保存都由云端工具托管，家用机只需编排 responses 请求即可获得常驻助理能力。

### E 类｜智能体编排框架与 SDK 官方文档（9 篇）

#### 035｜LangGraph overview - Docs by LangChain

- **检索号**：E-01　**类别**：E 智能体编排框架与 SDK 官方文档　**轮次**：第一轮
- **作者 / 机构**：LangChain, Inc.（LangGraph 团队）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://docs.langchain.com/oss/python/langgraph/overview>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Low-level orchestration framework and runtime for long-running, stateful agents；durable execution, streaming, human-in-the-loop, and persistence；Persistence: Checkpoint state and resume after failures or pauses.
- **要点**：以"共享 state + nodes + edges"的图定义工作流，把确定性节点与 LLM 驱动节点混排在同一图内；运行时原语提供 Persistence（Checkpoint state and resume after failures or pauses）、Human-in-the-loop（Pause execution, inspect or edit state, then continue）与 Memory（Short-term thread state and longer-term memory across sessions）。
- **与主题关联**：状态保存、中断恢复与长时循环都被做成编排层能力，家用机只需运行轻量图调度并把推理交给云端 LLM API。

#### 036｜Quickstart - OpenAI Agents SDK

- **检索号**：E-02　**类别**：E 智能体编排框架与 SDK 官方文档　**轮次**：第一轮
- **作者 / 机构**：OpenAI
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://openai.github.io/openai-agents-python/quickstart>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Give your agent tools；The runner handles executing individual agents, any handoffs, and any tool calls.；Full manual control and provider-agnostic history
- **要点**：用 Agent（instructions + name + model）与 Runner.run 组成最小智能体循环，通过 @tool 装饰器注册函数工具、通过 handoffs 列表在多个 specialist agent 之间转交；Quickstart 明确列出 session=... 由 SDK 保存历史以及 provider-agnostic history 的记忆策略。
- **与主题关联**：几行代码即可在本地跑"智能体循环 + 工具注册 + 多智能体转交"，模型推理全部由云端 API 承担。

#### 037｜Get started - Agent Development Kit (ADK)

- **检索号**：E-03　**类别**：E 智能体编排框架与 SDK 官方文档　**轮次**：第一轮
- **作者 / 机构**：Google（Agent Development Kit / google/adk-docs）
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://google.github.io/adk-docs/get-started/quickstart>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「Get started - Agent Development Kit (ADK)」
- **页面依据**：Agent Development Kit (ADK) is designed to empower developers to quickly build, manage, evaluate and deploy AI-powered agents.；Python Quickstart；Migrate existing agents and workflows to ADK with Agents CLI.
- **要点**：官方给出 Python / TypeScript / Go / Java / Kotlin 多语言 Quickstart 以及 Agents CLI Quickstart，均为 code-first 地创建、管理与部署 agent；页面还单列 Migrate to ADK，用于把既有 agents and workflows 迁入 ADK。
- **与主题关联**：ADK 把"定义 agent 与工作流"放在本地开发侧，部署与模型调用交给托管服务/API，家用机不承担算力。

#### 038｜AutoGen — AutoGen

- **检索号**：E-04　**类别**：E 智能体编排框架与 SDK 官方文档　**轮次**：第一轮
- **作者 / 机构**：Microsoft（AutoGen 团队 / microsoft/autogen）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://microsoft.github.io/autogen>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验；站点重定向至 https://microsoft.github.io/autogen/
- **页面依据**：A programming framework for building conversational single and multi-agent applications.；An event-driven programming framework for building scalable multi-agent AI systems.；Deterministic and dynamic agentic workflows for business processes.
- **要点**：分层提供 AgentChat（对话式单/多智能体）、Core（事件驱动、可分布式的多智能体运行时，用于 Deterministic and dynamic agentic workflows）与 Extensions（MCP 工具、代码执行器、gRPC 分布式 runtime 等）；首页示例以 OpenAIChatCompletionClient(model="gpt-4o") 把模型作为可替换客户端接入。
- **与主题关联**：本地只跑事件驱动的多智能体编排与工具调度，模型通过 model client 指向云端 LLM API。

#### 039｜Semantic Kernel documentation | Microsoft Learn

- **检索号**：E-05　**类别**：E 智能体编排框架与 SDK 官方文档　**轮次**：第一轮
- **作者 / 机构**：Microsoft（Microsoft Learn / Semantic Kernel 团队）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://learn.microsoft.com/en-us/semantic-kernel>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Concepts — Kernel、Plugins、Memory；Frameworks — Process Framework、Agent Framework；Learn to build robust, future-proof AI solutions that evolve with technological advancements.
- **要点**：以 Kernel 作为容器统一组织 AI 服务、Plugins 与 Memory，并在 Frameworks 下提供 Process Framework（有状态多步流程）与 Agent Framework 两类编排能力；文档自述其目标是 future-proof、可随模型技术演进的 AI 方案，即底层模型服务可替换。
- **与主题关联**：Kernel/Plugins/Memory 只是把云模型调用与本地函数封装成可组合编排单元，家用机是编排宿主而非推理硬件。

#### 040｜GitHub - crewAIInc/crewAI: Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. · GitHub

- **检索号**：E-06　**类别**：E 智能体编排框架与 SDK 官方文档　**轮次**：第一轮
- **作者 / 机构**：CrewAI Inc.（crewAIInc/crewAI）
- **时间**：n.d.（官方文档）　**类型**：官方 GitHub 仓库 README
- **出处**：<https://github.com/crewAIInc/crewAI>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Flows offer precise, event-driven control；with `@start`, `@listen`, or `@router` decorators；Crews provide autonomous agent collaboration；Understanding Flows and Crews
- **要点**：README 把能力拆成 Crews（Crews provide autonomous agent collaboration）与 Flows（Flows offer precise, event-driven control），Flow 用 @start / @listen / @router 装饰器组织事件驱动分支；并设 Using Crews and Flows Together、Connecting Your Crew to a Model、Can CrewAI automate human-in-the-loop workflows? 等章节。
- **与主题关联**：Crew/Flow 的状态机与事件回调都在本地进程内运行，而 Crew 所连接的模型可指向云端 LLM API。

#### 041｜Introduction | Developer Documentation（LlamaIndex Workflows）

- **检索号**：E-07　**类别**：E 智能体编排框架与 SDK 官方文档　**轮次**：第一轮
- **作者 / 机构**：LlamaIndex, Inc.（run-llama / LlamaIndex）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://developers.llamaindex.ai/python/llamaagents/workflows>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：A workflow is an event-driven, step-based way to control the execution flow of an application.；Loops are steps that return an event handled by an earlier step.；workflow runs can be interactive and stateful. In this case, to collect input from a human.
- **要点**：以 @step 与 Event 的输入/输出类型推断数据流并在运行前校验 event graph；原生提供 Loops（步骤返回由更早步骤处理的事件）、Branches and loops、有状态运行与 human-in-the-loop 输入收集，章节含 Defining Workflow Events、Workflow Entry Points、Workflow Exit Points、Validation、Examples。
- **与主题关联**：把循环、分支、状态与人机协同固化为本地工作流图，步骤里的 LLM 调用走云端 API 即可。

#### 042｜Pydantic AI | Pydantic Docs

- **检索号**：E-08　**类别**：E 智能体编排框架与 SDK 官方文档　**轮次**：第一轮
- **作者 / 机构**：Pydantic（PydanticAI 团队）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://ai.pydantic.dev>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Any model, one Python API.；typed dependency injection, typed tools；Agents, realtime voice, image generation, embeddings.
- **要点**：以一套 Python API 屏蔽不同模型供应商差异（Any model, one Python API），并用 Pydantic 类型系统实现 typed dependency injection 与 typed tools 的结构化校验；文档章节覆盖 What are you building?、Why Pydantic AI、Putting it together: a bank support agent、Instrumentation with Pydantic Logfire。
- **与主题关联**：本地只做类型化的工具/依赖编排与结果校验，模型可任意指向云端 LLM API。

#### 043｜smolagents/README.md at main · huggingface/smolagents · GitHub

- **检索号**：E-09　**类别**：E 智能体编排框架与 SDK 官方文档　**轮次**：第一轮
- **作者 / 机构**：Hugging Face（huggingface/smolagents）
- **时间**：n.d.（官方文档）　**类型**：官方 GitHub 仓库 README
- **出处**：<https://github.com/huggingface/smolagents/blob/main/README.md>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Model-agnostic: smolagents supports any LLM.；Our library is LLM-agnostic: you could switch the example above to any inference provider.；First-class support for Code Agents. Our CodeAgent writes its actions in code；LiteLLM to access 100+ LLMs
- **要点**：README 明确 Model-agnostic 与 Tool-agnostic：通过 InferenceClientModel（HF inference providers 网关）、LiteLLMModel（100+ LLMs）、OpenAIModel、AzureOpenAIModel、AmazonBedrockModel 等把模型作为可替换组件；CodeAgent 以 Python 代码片段作为动作来发起工具调用，主体逻辑集中在约 1,000 行的 agents.py。
- **与主题关联**：极简库在本地只负责"想代码 + 调工具"的循环，LLM 推理通过 model 对象指向任意云端 API 供应商。

### F 类｜家用机自托管编排 / 自动化平台官方文档（8 篇）

#### 044｜Schedule Trigger | Nodes | n8n Docs

- **检索号**：F-01　**类别**：F 家用机自托管编排 / 自动化平台官方文档　**轮次**：第一轮
- **作者 / 机构**：n8n 官方（n8n Docs）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Use the Schedule Trigger node to run workflows at fixed intervals and times. This works in a similar way to the Cron software utility in Unix-like systems."；章节 "Custom (Cron) interval"；"You must publish the workflow"
- **要点**：该节点按秒、分、时、日、周、月或自定义 Cron 表达式触发工作流，可在同一节点叠加多条 Trigger Rules 并设置停机后 missed execution 的补跑策略。使用定时触发必须保存并发布工作流，自托管实例默认时区为 `America/New York`，可通过环境变量调整。
- **与主题关联**：为自托管在家用机上的 n8n 提供纯时间驱动的主动触发，使常驻工作流能定时唤起云端 LLM API 而无需人工发起。

#### 045｜HTTP Request | Nodes | n8n Docs

- **检索号**：F-02　**类别**：F 家用机自托管编排 / 自动化平台官方文档　**轮次**：第一轮
- **作者 / 机构**：n8n 官方（n8n Docs）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："HTTP Request"；"make HTTP requests to query data from any app or service with a REST API"；"you're creating a REST API call"；章节 "Import curl command"
- **要点**：节点可配置 Method、URL、Send Query Parameters、Send Headers、Send Body（JSON / Form-Data / Raw 等）与 Pagination，并支持直接导入 curl 命令。官方 FAQ 专设 "How do I call an API without writing code?"，明确其定位是零代码构造 REST 调用。
- **与主题关联**：让常驻工作流主动向云端 LLM API 发起 HTTP/REST 请求，是"编排 + 云 API"取代本地模型的关键执行节点。

#### 046｜Automation triggers - Home Assistant

- **检索号**：F-03　**类别**：F 家用机自托管编排 / 自动化平台官方文档　**轮次**：第一轮
- **作者 / 机构**：Home Assistant 官方文档团队
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://www.home-assistant.io/docs/automation/trigger>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Automation triggers"；"A trigger is the part of an automation that makes the automation start when something specific happens"；"Types of triggers" 章节下的 "Time trigger"、"Time pattern trigger"、"State changed trigger"、"Webhook trigger"、"Numeric state crossed threshold trigger"、"MQTT trigger"、"Zone trigger"
- **要点**：官方把触发器定义为"当特定事情发生时启动自动化"的部分，并列出时间、时间模式、状态变化、数值越阈、Webhook、MQTT、Zone、Sun、Template 等十余种类型。文档同时说明多触发器并存、YAML 写法、Trigger ID 以及按不同触发器分支执行动作。
- **与主题关联**：把时间、家庭传感器状态、Webhook 与 MQTT 事件统一变成自动化起点，正好对应"主动式助理"所需的事件触发底座。

#### 047｜Deploy Dify with Docker Compose - Dify Docs

- **检索号**：F-04　**类别**：F 家用机自托管编排 / 自动化平台官方文档　**轮次**：第一轮
- **作者 / 机构**：Dify / LangGenius 官方（Dify Docs）
- **时间**：2026　**类型**：官方指南
- **出处**：<https://docs.dify.ai/en/self-host/deploy/quick-start/docker-compose>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Run Dify on one machine with Docker Compose"；"CPU: at least 2 cores"；"RAM: at least 4 GiB"；"docker compose up -d"
- **要点**：官方给出单机 Docker Compose 部署的最低硬件为 2 核 CPU、4 GiB 内存，并要求 Docker Compose 2.35.0 或更高版本。默认一键拉起 bundled PostgreSQL、Weaviate 等依赖服务，之后在 `http://localhost/install` 完成初始化。
- **与主题关联**：以官方最低配置证明工作流/agent 编排平台在普通家用机即可常驻自托管，而模型能力可由外部 API 提供。

#### 048｜Running Node-RED locally : Node-RED

- **检索号**：F-05　**类别**：F 家用机自托管编排 / 自动化平台官方文档　**轮次**：第一轮
- **作者 / 机构**：Node-RED 项目官方（Node-RED Docs）
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://nodered.org/docs/getting-started/local>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Running Node-RED locally"；"sudo npm install -g node-red"；"docker run -it -p 1880:1880 --name mynodered nodered/node-red"；"Server now running at http://127.0.0.1:1880/"
- **要点**：官方给出在 Windows / Linux / Raspberry Pi 上以 npm 全局安装或 Docker 一条命令启动的方式，仅需受支持的 Node.js 版本，启动后编辑器在 `localhost:1880` 常驻、流程存于 `flows.json`。文末导航指向 "Starting Node-RED on boot"，支持开机自启。
- **与主题关联**：提供极轻量的家用机常驻运行时，配合 inject / http in 等节点即可实现定时与 Webhook 触发并转发云端 API。

#### 049｜Overview of installing Docker Compose | Docker Docs

- **检索号**：F-06　**类别**：F 家用机自托管编排 / 自动化平台官方文档　**轮次**：第一轮
- **作者 / 机构**：Docker Inc. 官方（Docker Docs）
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://docs.docker.com/compose/install>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Overview of installing Docker Compose"；"The easiest and recommended way to get Docker Compose is to install Docker Desktop"；"Docker Desktop includes Docker Compose along with Docker Engine and Docker CLI which are Compose prerequisites"
- **要点**：官方推荐通过 Docker Desktop（Windows / Mac / Linux）获得 Compose，也可在 Linux 上单独安装 Compose plugin，独立 standalone 方式仅作向后兼容保留。Compose 与 Engine、CLI 一同构成运行多容器应用的前置条件。
- **与主题关联**：提供把 n8n、Dify、Huginn 等多个服务以容器方式长期常驻在同一台家用机上的统一部署底座。

#### 050｜GitHub - huginn/huginn: Create agents that monitor and act on your behalf. Your agents are standing by! · GitHub

- **检索号**：F-08　**类别**：F 家用机自托管编排 / 自动化平台官方文档　**轮次**：第一轮
- **作者 / 机构**：Huginn 项目官方（GitHub 组织 huginn）
- **时间**：n.d.（官方文档）　**类型**：官方仓库
- **出处**：<https://github.com/huginn/huginn>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Create agents that monitor and act on your behalf. Your agents are standing by!"；"Try it with Docker"；"Docker Compose on your own server"；"always-on worker"
- **要点**：官方仓库把系统定义为可自建、代用户监控并行动的常驻 agent，README 提供 "Try it with Docker"、"Docker Compose on your own server"、"Manual installation on any server" 等自托管路径。文档说明部署形态包含持续运行的后台 worker，用于周期性轮询与事件响应。
- **与主题关联**：几乎是"主动式常驻个人助理"的原型：事件驱动的常驻 agent 可轮询邮件/网页并在条件满足时主动触发动作，再转交云端 LLM 处理。

#### 051｜Self-host | Windmill（正文 H1：Self-host Windmill）

- **检索号**：F-09　**类别**：F 家用机自托管编排 / 自动化平台官方文档　**轮次**：第一轮
- **作者 / 机构**：Windmill Labs 官方（Windmill Docs）
- **时间**：n.d.（官方文档）　**类型**：官方指南
- **出处**：<https://www.windmill.dev/docs/advanced/self_host>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Self-host Windmill"；"Self-host Windmill on your own infrastructure."；"Using Docker and Caddy, Windmill can be deployed using 3 files:"；"docker compose up -d"；"Setup Windmill on localhost"
- **要点**：官方自托管页覆盖 Architecture、Docker、Helm chart、外部 PostgreSQL、Health endpoints、First time login 等章节，并给出在 localhost 用三个文件起服务的步骤。正文含 "Setup Windmill on localhost" 小节，明确支持单机本地部署。
- **与主题关联**：以脚本/工作流为单位的自托管编排器，可由定时与 Webhook 触发并调用任意 HTTP API，适合家用机常驻编排云端 LLM。

### G 类｜开放协议与工具调用标准（9 篇）

#### 052｜Specification - Model Context Protocol

- **检索号**：G-01　**类别**：G 开放协议与工具调用标准　**轮次**：第一轮
- **作者 / 机构**：Model Context Protocol 项目（Anthropic 发起，现由 Linux Foundation 旗下 Agentic AI Foundation 托管）
- **时间**：2026-07-28（/specification/latest 现行版；页面链接标注 2026-07-28）　**类型**：官方规范
- **出处**：<https://modelcontextprotocol.io/specification/latest>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：This specification defines the authoritative protocol requirements, based on the TypeScript schema in schema.ts；The protocol uses JSON-RPC 2.0 messages；Tools: Functions for the AI model to execute；Hosts / Clients / Servers；页面链接 https://modelcontextprotocol.io/specification/2026-07-28
- **要点**：定义 MCP 的权威协议要求，采用 JSON-RPC 2.0 在 Hosts、Clients、Servers 之间通信，服务端以 Resources、Prompts、Tools 三类能力暴露上下文与可执行函数。现行 2026-07-28 版改为无状态、按请求协商能力，并提供 Tasks、Skills over MCP、MCP Apps 等可选扩展。
- **与主题关联**：家用机只要实现 MCP 客户端，就能用统一协议把本地文件、数据库与云端 API 等外部工具/数据源接入云端 LLM 的编排链路，而不必本地跑模型。

#### 053｜Architecture overview - Model Context Protocol

- **检索号**：G-02　**类别**：G 开放协议与工具调用标准　**轮次**：第一轮
- **作者 / 机构**：Model Context Protocol 项目（Anthropic 发起，现由 Agentic AI Foundation 托管）
- **时间**：2026-07-28（文档版本，规范 URL 为 /docs/2026-07-28/learn/architecture）　**类型**：官方指南
- **出处**：<https://modelcontextprotocol.io/docs/learn/architecture>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：MCP follows a client-server architecture where an MCP host ... establishes connections to one or more MCP servers；MCP supports two transport mechanisms；Stdio transport: Uses standard input/output streams for direct process communication between local processes on the same machine；Streamable HTTP transport: Uses HTTP POST for client-to-server messages with optional Server-Sent Events；章节 Data layer / Transport layer / Primitives；tools/list；tools/call
- **要点**：说明 MCP 的分层架构（数据层 + 传输层）与 host/client/server 参与者，服务端原语 Tools、Resources、Prompts 通过 tools/list、tools/call 等方法被发现与执行。传输层规定两种机制：stdio 用于同机本地进程直连，Streamable HTTP（可配合 SSE）用于远程服务。
- **与主题关联**：直接给出家用机以 stdio 拉起本地 MCP server、以 Streamable HTTP 连接远程数据源的标准做法，是把外部工具接进编排器的实现依据。

#### 054｜GitHub - modelcontextprotocol/typescript-sdk: The official TypeScript SDK for Model Context Protocol servers and clients

- **检索号**：G-03　**类别**：G 开放协议与工具调用标准　**轮次**：第一轮
- **作者 / 机构**：Model Context Protocol 项目（官方 SDK 维护方）
- **时间**：2026（main 分支 v2 稳定线，实现 2026-07-28 MCP 规范；仓库持续更新）　**类型**：官方 SDK 仓库
- **出处**：<https://github.com/modelcontextprotocol/typescript-sdk>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：This is the `main` branch: v2 of the SDK ... implementing the 2026-07-28 MCP spec；This repository contains the TypeScript SDK implementation of the MCP specification；MCP server libraries (tools/resources/prompts, Streamable HTTP, stdio, auth helpers)；npm install @modelcontextprotocol/server；MCP TypeScript SDK
- **要点**：官方 TypeScript SDK 提供 MCP server/client 库，覆盖 tools/resources/prompts 原语、stdio 与 Streamable HTTP 两种传输，并附带 Express、Fastify、Hono、Node.js HTTP 等运行时适配中间件。仓库同时给出可运行示例与构建首个 server/client 的入门教程。
- **与主题关联**：家用机可直接用官方 SDK 起一个本地 MCP server 暴露工具、或写客户端连接现成 MCP server，把外部数据源挂到云端 LLM 编排上。

#### 055｜OpenAPI Specification v3.1.0

- **检索号**：G-04　**类别**：G 开放协议与工具调用标准　**轮次**：第一轮
- **作者 / 机构**：OpenAPI Initiative（编辑 Darrel Miller、Jeremy Whitlock、Marsh Gardiner、Mike Ralphson、Ron Ratovsky、Uri Sarid）
- **时间**：2021（Version 3.1.0，15 February 2021）　**类型**：官方规范
- **出处**：<https://spec.openapis.org/oas/v3.1.0.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：OpenAPI Specification v3.1.0；Version 3.1.0；15 February 2021；The source-of-truth for this specification is the HTML file referenced above as _This version_.；4.8.10 Operation Object；4.8.24 Schema Object；4.8.18 Callback Object；Copyright © 2021 the Linux Foundation
- **要点**：定义厂商中立、可移植的 HTTP API 描述格式，用 OpenAPI Document 描述 paths、operations、parameters、request/response、schema 与 callbacks 等对象，使机器可读地发现与调用 REST API。页面明确以该 HTML 文件为规范的权威来源，并给出版本、编辑者与修订历史。
- **与主题关联**：云端 LLM 的函数调用/工具描述可复用现成 OpenAPI 文档，把家用机能访问的 Web API 自动转成可编排的工具清单。

#### 056｜Specification — JSON Schema

- **检索号**：G-05　**类别**：G 开放协议与工具调用标准　**轮次**：第一轮
- **作者 / 机构**：JSON Schema 组织（json-schema.org / json-schema-org）
- **时间**：2020-12（The current version is 2020-12!）　**类型**：官方规范
- **出处**：<https://json-schema.org/specification>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：The current version is *2020-12*! The previous version was 2019-09.；The specification is split into two parts, Core and Validation.；JSON Schema Core defines the basic foundation of JSON Schema；The latest meta-schema is **2020-12**.；Core/Validation Dialect meta-schema
- **要点**：定义用于标注与校验 JSON 文档的声明式语言，规范拆分为 Core（基础）与 Validation（校验关键字）两部分，并提供 2020-12 元模式、单一词汇表元模式与推荐输出结构。页面还列出各 draft 之间的迁移说明与按词汇表拆分的元模式链接。
- **与主题关联**：LLM 工具调用的参数/返回值以及 MCP 工具的 inputSchema 都以 JSON Schema 描述，家用机编排器据此生成并校验结构化工具参数。

#### 057｜HTML Living Standard — 9.2 Server-sent events

- **检索号**：G-06　**类别**：G 开放协议与工具调用标准　**轮次**：第一轮
- **作者 / 机构**：WHATWG（Web Hypertext Application Technology Working Group）
- **时间**：n.d.（现行规范，Living Standard；页面标注 Last Updated 5 November 2026）　**类型**：标准文档
- **出处**：<https://html.spec.whatwg.org/multipage/server-sent-events.html>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验
- **页面依据**：HTML Living Standard — Last Updated 5 November 2026；9.2 Server-sent events；9.2.2 The `EventSource` interface；To enable servers to push data to web pages over HTTP or using dedicated server-push protocols, this specification introduces the `EventSource` interface.；This event stream format's MIME type is `text/event-stream`.；Clients will reconnect if the connection is closed
- **要点**：规定服务器经 HTTP 向客户端单向推送事件的标准机制，定义 EventSource 接口、text/event-stream MIME 类型、事件流解析与 UTF-8 解码、Last-Event-ID 头及断线重连行为。该标准以 Living Standard 形式持续更新，不设固定发布版本。
- **与主题关联**：为家用机常驻助理提供免轮询的长连接事件通道，MCP Streamable HTTP 的流式响应、云端 LLM 流式输出与工具进度通知都建立在这一格式之上。

#### 058｜CloudEvents - Version 1.0.2

- **检索号**：G-07　**类别**：G 开放协议与工具调用标准　**轮次**：第一轮
- **作者 / 机构**：CloudEvents 项目（CNCF Serverless Working Group）
- **时间**：1.0.2（Version 1.0.2；specversion 值为 1.0）　**类型**：官方规范
- **出处**：<https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **页面依据**：CloudEvents - Version 1.0.2；CloudEvents is a vendor-neutral specification for defining the format of event data.；Compliant event producers MUST use a value of 1.0 when referring to this version of the specification.；Context Attributes；REQUIRED Attributes: id, source, specversion, type；All implementations MUST support the JSON format.；Protocol Binding
- **要点**：定义跨服务、平台与系统描述事件数据的厂商中立通用格式，规定 id、source、specversion、type 等必需上下文属性与可选扩展属性，并要求实现支持 JSON 事件格式。规范同时定义 Event、Producer、Consumer、Event Format、Message、Protocol Binding 等术语与尺寸限制。
- **与主题关联**：家用机常驻助理接收外部 SaaS 与云服务的 webhook/事件推送时，可用统一信封格式解析、过滤与转发，不必为每个数据源编写专用适配器。

#### 059｜Agent2Agent (A2A) Protocol Specification（页面标题 Overview - A2A Protocol）

- **检索号**：G-08　**类别**：G 开放协议与工具调用标准　**轮次**：第一轮
- **作者 / 机构**：A2A Project（原由 Google 开发并捐赠 Linux Foundation，由 Technical Steering Committee 维护）
- **时间**：1.0.0（Latest Released Version 1.0.0）　**类型**：官方规范
- **出处**：<https://a2a-protocol.org/latest/specification>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「Overview - A2A Protocol」
- **页面依据**：Agent2Agent (A2A) Protocol Specification；Latest Released Version 1.0.0；Reuse existing, well-understood standards (HTTP, JSON-RPC 2.0, Server-Sent Events).；2.2. Core Concepts（Agent Card / Task / Message / Artifact）；3.1. Core Operations；4.4.1. AgentCard；Section 9: JSON-RPC Protocol Binding；Section 10: gRPC Protocol Binding；Section 11: HTTP+JSON/REST Protocol Binding
- **要点**：定义独立、彼此不透明 AI 智能体之间的互操作通信协议，规定 Agent Card 能力发现、Task 状态生命周期、Message/Artifact 数据模型以及 Send Message、Send Streaming Message、Get Task、Push Notification 等核心操作。协议复用 HTTP、JSON-RPC 2.0 与 SSE，并给出 JSON-RPC、gRPC、HTTP+JSON/REST 三种协议绑定。
- **与主题关联**：家用机上的编排器可作为 A2A 客户端发现并委派任务给远端专职智能体，与 MCP（接工具）形成分工，从而在单机上扩展能力而无需本地部署模型。

#### 060｜OpenTelemetry GenAI Semantic Conventions（仓库 open-telemetry/semantic-conventions-genai）

- **检索号**：G-10　**类别**：G 开放协议与工具调用标准　**轮次**：第一轮
- **作者 / 机构**：OpenTelemetry（CNCF；semantic-conventions-genai 仓库维护方）
- **时间**：n.d.（现行规范，开发中；README 中 Schema URL 标注 TODO，可见最近提交 Jun 4, 2026）　**类型**：官方规范
- **出处**：<https://github.com/open-telemetry/semantic-conventions-genai>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：OpenTelemetry GenAI Semantic Conventions；Semantic Conventions for Generative AI (GenAI), including spans, metrics, and events for GenAI clients, MCP (Model Context Protocol), and provider-specific conventions (OpenAI, etc.).；This repository extends the OpenTelemetry Semantic Conventions with GenAI-specific conventions；The human-readable version of the semantic conventions resides in the docs folder.；## Schema URL — TODO；另：原页面 https://opentelemetry.io/docs/specs/semconv/gen-ai/ 已标注 Moved: Generative AI semantic conventions 并指向本仓库
- **要点**：为 GenAI 客户端调用、MCP 交互与各模型厂商定义统一的 span、metric、event 语义属性（gen_ai.*、a2a.*），人类可读文档由 model 目录下的 YAML 定义生成。原 opentelemetry.io 的 GenAI 语义约定页已迁至本仓库，规范仍在推进（Schema URL 尚为 TODO）。
- **与主题关联**：使家用机常驻助理的云端 LLM 调用、工具执行与跨智能体委派可被统一追踪与计量，便于在单机上排查编排链路与成本。

### H 类｜智能体记忆与长期状态（9 篇）

#### 061｜Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

- **检索号**：H-01　**类别**：H 智能体记忆与长期状态　**轮次**：第一轮
- **作者 / 机构**：Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, Deshraj Yadav（Mem0 团队）
- **时间**：2025　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2504.19413>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：dynamically extracting, consolidating, and retrieving salient information from ongoing conversations
- **要点**：提出以记忆为中心的可扩展架构，从持续对话中动态抽取、整合与检索显著信息，并给出基于图的记忆变体。在 LOCOMO 基准上，相比全上下文方法 p95 延迟降低 91%、token 成本节省 90% 以上。
- **与主题关联**：家用机只需在本地持久化这些被抽取的结构化记忆片段并按需检索，生成与推理交由云端 LLM API 完成。

#### 062｜Memory blocks (core memory) | Letta Docs

- **检索号**：H-02　**类别**：H 智能体记忆与长期状态　**轮次**：第一轮
- **作者 / 机构**：Letta（Letta Docs 维护方）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://docs.letta.com/guides/core-concepts/memory/memory-blocks>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Memory blocks are structured sections of the agent’s context window
- **要点**：官方文档说明 memory blocks（core memory）是始终驻留在智能体上下文窗口中的结构化片段。智能体可自主读取并更新这些核心记忆块；本条为官方文档页，非 MemGPT 经典架构论文。
- **与主题关联**：家用机可用一个轻量本地文件/数据库维护常驻记忆块，每次调用云端 LLM 时把该块注入上下文即可保持长期状态。

#### 063｜Zep: A Temporal Knowledge Graph Architecture for Agent Memory

- **检索号**：H-03　**类别**：H 智能体记忆与长期状态　**轮次**：第一轮
- **作者 / 机构**：Preston Rasmussen, Pavlo Paliychuk, Travis Beauvais, Jack Ryan, Daniel Chalef（Zep AI）
- **时间**：2025　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2501.13956>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：a temporally-aware knowledge graph engine that dynamically synthesizes both unstructured conversational data and structured business data while maintaining historical relationships
- **要点**：提出面向 AI 智能体的时序知识图谱记忆层服务 Zep，其核心组件 Graphiti 动态整合对话数据与结构化数据并保留历史关系。论文在 DMR 与 LongMemEval 上报告优于静态 RAG 框架的表现。
- **与主题关联**：表明记忆可完全外置为独立的轻量服务或本地库，家用机无需承载任何模型权重即可维护带时间维度的长期状态。

#### 064｜Introduction - Chroma Docs

- **检索号**：H-04　**类别**：H 智能体记忆与长期状态　**轮次**：第一轮
- **作者 / 机构**：Chroma（chroma-core 开源项目，Apache 2.0）
- **时间**：n.d.（官方文档）　**类型**：官方文档
- **出处**：<https://docs.trychroma.com/docs/overview/introduction>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Chroma is the open-source data infrastructure for AI. It comes with everything you need to get started built-in.
- **要点**：官方介绍页说明 Chroma 内置 embeddings 与元数据存储、稠密/稀疏向量检索与元数据过滤。文档明确写出可本地运行、自托管或使用托管云。
- **与主题关联**：家用机可用它在本地持久化向量化的对话记忆，检索出的相关片段再交给云端 LLM 做编排与生成。

#### 065｜Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

- **检索号**：H-05　**类别**：H 智能体记忆与长期状态　**轮次**：第一轮
- **作者 / 机构**：Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela
- **时间**：2020　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2005.11401>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：models which combine pre-trained parametric and non-parametric memory for language generation
- **要点**：RAG 奠基论文，提出把参数化记忆（预训练 seq2seq 模型）与非参数化记忆（可检索的稠密向量索引）结合用于生成。其中非参数化记忆是 Wikipedia 的稠密向量索引，由预训练神经检索器访问。
- **与主题关联**：论证了"知识/记忆可外置为可检索索引"，家用机只需维护索引，生成环节可由云端 LLM 承担。

#### 066｜Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs

- **检索号**：H-06　**类别**：H 智能体记忆与长期状态　**轮次**：第一轮
- **作者 / 机构**：Yu. A. Malkov, D. A. Yashunin
- **时间**：2016　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/1603.09320>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：We present a new approach for the approximate K-nearest neighbor search based on navigable small world graphs with controllable hierarchy (Hierarchical NSW, HNSW).
- **要点**：提出 HNSW 分层可导航小世界图近似最近邻索引，为纯图结构、无需额外粗检索结构，并实现对数复杂度 scaling。该索引后被众多向量数据库用作底层实现。
- **与主题关联**：此类轻量索引让家用机在 CPU 与小内存上即可完成记忆的近似最近邻检索，无需本地运行大模型。

#### 067｜LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory

- **检索号**：H-07　**类别**：H 智能体记忆与长期状态　**轮次**：第一轮
- **作者 / 机构**：Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, Dong Yu
- **时间**：2024　**类型**：评测基准
- **出处**：<https://arxiv.org/abs/2410.10813>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention
- **要点**：提出评测聊天助手五项长期记忆能力的基准，并把长期记忆设计拆为索引、检索、阅读三阶段。论文给出会话分解、事实增强键扩展、时间感知查询扩展等优化，显著提升记忆召回与下游问答。
- **与主题关联**：为家用常驻助理的"记忆"提供可量化维度，以及可在本地轻量实现的索引/检索三阶段设计依据。

#### 068｜A-MEM: Agentic Memory for LLM Agents

- **检索号**：H-09　**类别**：H 智能体记忆与长期状态　**轮次**：第一轮
- **作者 / 机构**：Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, Yongfeng Zhang
- **时间**：2025　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2502.12110>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Following the basic principles of the Zettelkasten method, we designed our memory system to create interconnected knowledge networks through dynamic indexing and linking.
- **要点**：借鉴 Zettelkasten 方法，让新记忆以含上下文描述、关键词、标签的结构化笔记形式写入，并通过动态索引与链接形成互联知识网络，还能随新记忆触发对历史记忆的演化更新。
- **与主题关联**：这种"笔记 + 链接"的记忆组织完全可落在本地轻量数据库中，由云端 LLM 负责生成笔记与更新决策。

#### 069｜A Survey on the Memory Mechanism of Large Language Model based Agents

- **检索号**：H-10　**类别**：H 智能体记忆与长期状态　**轮次**：第一轮
- **作者 / 机构**：Zeyu Zhang, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Quanyu Dai, Jieming Zhu, Zhenhua Dong, Ji-Rong Wen
- **时间**：2024　**类型**：综述
- **出处**：<https://arxiv.org/abs/2404.13501>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：we propose a comprehensive survey on the memory mechanism of LLM-based agents
- **要点**：系统综述 LLM 智能体记忆机制，先讨论"记忆是什么、为何需要"，再梳理记忆模块的设计与评估方法。文中还汇总记忆发挥作用的智能体应用，并分析局限与未来方向。
- **与主题关联**：为家用常驻助理选择记忆的来源、写入与检索策略提供总览性文献依据，说明记忆模块可作为独立外置组件而非模型能力。

### I 类｜事件驱动、调度与常驻运行（8 篇）

#### 070｜crontab(5) — Linux manual page

- **检索号**：I-01　**类别**：I 事件驱动、调度与常驻运行　**轮次**：第一轮
- **作者 / 机构**：Linux man-pages project（man7.org）
- **时间**：n.d.（现行规范）　**类型**：官方手册
- **出处**：<https://man7.org/linux/man-pages/man5/crontab.5.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`crontab - files used to schedule the execution of programs`；`"run this command at this time on this date"`；`five time-and-date fields`；字段名 `minute` / `hour` / `day of month` / `month` / `day of week`；`@reboot`、`@daily`
- **要点**：NAME 段把 crontab 定义为"用于调度程序执行的文件"，正文中以五个时间日期字段（minute、hour、day of month、month、day of week）加待执行命令构成一条调度指令，由 cron(8) 守护进程读取执行。手册还定义 `@reboot`、`@hourly`、`@daily`、`@weekly`、`@monthly`、`@yearly` 等特殊时间别名及 `CRON_TZ` 等环境变量。
- **与主题关联**：为"由时间触发"提供最经典、可移植的规范性定义，是主动式助理按时刻唤醒执行的语义基线。

#### 071｜systemd.timer — Timer unit configuration

- **检索号**：I-02　**类别**：I 事件驱动、调度与常驻运行　**轮次**：第一轮
- **作者 / 机构**：systemd / freedesktop.org
- **时间**：n.d.（现行规范）　**类型**：官方手册
- **出处**：<https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验
- **页面依据**：`systemd.timer — Timer unit configuration`；`A unit configuration file whose name ends in ".timer" encodes information about a timer controlled and supervised by systemd, for timer-based activation.`；`OnCalendar=`、`OnBootSec=`、`OnUnitActiveSec=`、`OnClockChange=`、`Persistent=`、`AccuracySec=`
- **要点**：该手册说明以 `.timer` 结尾的单元文件编码由 systemd 常驻守护进程监督和控制的定时器信息，用于 `timer-based activation`。[Timer] 段提供日历触发 `OnCalendar=`、相对单调计时 `OnBootSec=` / `OnUnitActiveSec=`、以及 `Persistent=`（错过触发后补执行）等选项。
- **与主题关联**：说明常驻系统服务如何把"时间到达"转化为对服务单元的激活，是常驻助理被定时唤醒的官方机制。

#### 072｜Task Scheduler for developers - Win32 apps | Microsoft Learn

- **检索号**：I-03　**类别**：I 事件驱动、调度与常驻运行　**轮次**：第一轮
- **作者 / 机构**：Microsoft（Microsoft Learn / Win32 文档）
- **时间**：n.d.（现行规范）　**类型**：官方文档
- **出处**：<https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`The Task Scheduler enables you to automatically perform routine tasks on a chosen computer. The Task Scheduler does so by monitoring whatever criteria you choose (referred to as triggers) and then executing the tasks when those criteria are met.`；`When a specific system event occurs.`；`At a specific time.`；`When the computer enters an idle state.`；`When the system is booted.`；`When a user logs on.`
- **要点**：官方页说明任务计划程序通过监视用户选定的判定条件（称为 triggers）并在条件满足时执行任务，实现例行任务自动化。页面逐条列出可响应的触发条件，涵盖特定系统事件、特定时刻、每日/每周/每月计划、月度星期计划、计算机空闲、任务注册、系统启动、用户登录与终端会话状态变化。
- **与主题关联**：在消费级 Windows 主机上提供"无需用户提问、由时间或系统事件自动启动"的官方触发语义。

#### 073｜apscheduler.triggers.cron — APScheduler 3.11.3.post3 documentation

- **检索号**：I-04　**类别**：I 事件驱动、调度与常驻运行　**轮次**：第一轮
- **作者 / 机构**：APScheduler 项目（官方 readthedocs 文档）
- **时间**：n.d.（现行规范）　**类型**：官方文档
- **出处**：<https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`Triggers when current time matches all specified time constraints, similarly to how the UNIX cron scheduler works.`；`You can specify a variety of different expressions on each field, and when determining the next execution time, it finds the earliest possible time that satisfies the conditions in every field.`；参数 `year`、`month`、`day`、`day_of_week`、`hour`、`minute`、`second`、`start_date`、`end_date`、`jitter`
- **要点**：官方 API 文档定义 CronTrigger：当当前时间满足所有指定时间约束时触发作业，行为与 UNIX cron 一致，并可在每个字段上写表达式以求出下一次满足全部条件的最早时间。参数列表包含 year/month/day/hour/minute/second 以及 `start_date`、`end_date`、`timezone`、`jitter`。
- **与主题关联**：把 cron 风格的时间触发语义嵌入常驻 Python 进程，便于助理在同一进程内编排定时任务而无需依赖系统 crontab。

#### 074｜MQTT Version 3.1.1 OASIS Standard

- **检索号**：I-05　**类别**：I 事件驱动、调度与常驻运行　**轮次**：第一轮
- **作者 / 机构**：OASIS Open（MQTT Technical Committee）
- **时间**：2014　**类型**：官方标准
- **出处**：<https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`MQTT Version 3.1.1`；`OASIS Standard`；`29 October 2014`；`MQTT is a Client Server publish/subscribe messaging transport protocol.`；`Use of the publish/subscribe message pattern which provides one-to-many message distribution and decoupling of applications.`；`The Server sends a copy of the Application Message to each Client that has a matching Subscription.`
- **要点**：OASIS 标准把 MQTT 定义为轻量、开放的客户端-服务器发布/订阅消息传输协议，以 Topic Name 与 Topic Filter 实现一对多分发和应用解耦。服务器职责被描述为把匹配订阅的 Application Message 副本发送给每个订阅客户端，并提供三级 QoS。
- **与主题关联**：为传感器、设备与外部消息提供"发布即到达、订阅方被动接收"的标准事件通道，是主动触发的核心传输语义。

#### 075｜Creating webhooks - GitHub Docs

- **检索号**：I-07　**类别**：I 事件驱动、调度与常驻运行　**轮次**：第一轮
- **作者 / 机构**：GitHub, Inc.（GitHub Docs）
- **时间**：n.d.（现行规范）　**类型**：官方文档
- **出处**：<https://docs.github.com/en/webhooks/using-webhooks/creating-webhooks>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`You can create webhooks to subscribe to specific events that occur on GitHub.`；`"Which events would you like to trigger this webhook?"`；`"Payload URL", type the URL where you'd like to receive payloads`；`GitHub will send you a simple ping event to let you know you've set up the webhook correctly`；`application/json will deliver the JSON payload directly as the body of the POST request`
- **要点**：官方文档说明可创建 webhook 订阅 GitHub 上发生的特定事件，配置 Payload URL 作为接收端点，并在"Which events would you like to trigger this webhook?"中选择触发事件，交付以 POST 请求发送 JSON 载荷。创建完成后 GitHub 会先发送 `ping` 事件验证端点连通。
- **与主题关联**：给出"外部系统事件发生即主动向常驻端点推送通知"的官方 webhook 触发范式。

#### 076｜RFC 2177: IMAP4 IDLE command

- **检索号**：I-08　**类别**：I 事件驱动、调度与常驻运行　**轮次**：第一轮
- **作者 / 机构**：IETF / RFC Editor（B. Leiba, IBM T.J. Watson Research Center）
- **时间**：1997　**类型**：RFC
- **出处**：<https://www.rfc-editor.org/rfc/rfc2177>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`RFC 2177: IMAP4 IDLE command`；`IMAP4 IDLE command`；`June 1997`；`Category: Standards Track`；`This document specifies the syntax of an IDLE command, which will allow a client to tell the server that it's ready to accept such real-time updates.`；`as long as an IDLE command is active, the server is now free to send untagged EXISTS, EXPUNGE, and other messages at any time`
- **要点**：该 Standards Track RFC 指出 IMAP4 原本要求客户端轮询邮箱变化（新邮件、删除），而 IDLE 命令允许客户端声明已准备好接收服务器实时更新。IDLE 期间服务器可随时发送未请求的 untagged `EXISTS`、`EXPUNGE` 等响应，并建议客户端至少每 29 分钟重新发起 IDLE 以免被判为 inactive。
- **与主题关联**：为"新邮件到达即触发"提供标准化的服务器主动通知机制，是外部消息触发的规范依据。

#### 077｜RFC 4287 - The Atom Syndication Format

- **检索号**：I-09　**类别**：I 事件驱动、调度与常驻运行　**轮次**：第一轮
- **作者 / 机构**：IETF / RFC Editor（M. Nottingham, Ed.; R. Sayre, Ed.）
- **时间**：2005　**类型**：RFC
- **出处**：<https://datatracker.ietf.org/doc/html/rfc4287>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：`RFC 4287 - The Atom Syndication Format`；`The Atom Syndication Format`；`December 2005`；`This document specifies Atom, an XML-based Web content and metadata syndication format.`；`The primary use case that Atom addresses is the syndication of Web content such as weblogs and news headlines to Web sites as well as directly to user agents.`；`atom:updated`
- **要点**：该 RFC 把 Atom 定义为基于 XML 的 Web 内容与元数据联合（syndication）格式，feed 由多条 entry 组成，主要用例是将博客与新闻标题联合发布到站点及用户代理。`atom:updated` 元素标识条目或 feed 最近一次被发布者认为有实质修改的时刻，处理器可据 `latest atom:updated timestamp` 识别新内容。
- **与主题关联**：为"内容源出现新条目即触发"提供可比对的标准数据结构与更新时间语义。

### J 类｜智能体评测基准与成本 / 可靠性工程（6 篇）

#### 078｜AgentBench: Evaluating LLMs as Agents

- **检索号**：J-01　**类别**：J 智能体评测基准与成本 / 可靠性工程　**轮次**：第一轮
- **作者 / 机构**：Xiao Liu、Hao Yu、Hanchen Zhang 等（THUDM / 清华大学，摘要注明数据与评测包发布于 github.com/THUDM/AgentBench；ICLR 2024）
- **时间**：2023　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2308.03688>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：「We present AgentBench, a multi-dimensional benchmark that consists of 8 distinct environments to assess LLM-as-Agent's reasoning and decision-making abilities.」
- **要点**：以 8 个不同的交互环境系统评测 LLM 作为智能体的推理与决策能力，覆盖 API 商业模型与开源模型。结果显示顶级商业 LLM 在复杂环境中表现强，但与参数量不超过 70B 的开源模型存在显著差距；作者归纳失败主因为长期推理、决策与指令遵循能力不足。
- **与主题关联**：直接证明「调用商业 API 的智能体」在多维度任务上明显强于家用机可本地承载的小参数开源模型，为「家用机 + 云端 API 编排」提供能力侧证据，同时指出长程推理与指令遵循是当前边界。

#### 079｜GAIA: a benchmark for General AI Assistants

- **检索号**：J-02　**类别**：J 智能体评测基准与成本 / 可靠性工程　**轮次**：第一轮
- **作者 / 机构**：Grégoire Mialon、Clémentine Fourrier、Craig Swift、Thomas Wolf、Yann LeCun、Thomas Scialom（Meta AI / Hugging Face 等）
- **时间**：2023　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2311.12983>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：「GAIA proposes real-world questions that require a set of fundamental abilities such as reasoning, multi-modality handling, web browsing, and generally tool-use proficiency.」
- **要点**：构建 466 道真实世界问题，考察推理、多模态处理、网页浏览与工具使用等通用助手基础能力，答案仅公开 300 题以外的部分以支撑榜单。量化结论是人类作答正确率 92%，而带插件的 GPT-4 仅 15%。
- **与主题关联**：说明常驻个人助理的瓶颈在于「编排工具与浏览」而非模型参数规模，正是云端 API 编排可发力的方向，同时量化了当前能力天花板。

#### 080｜τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

- **检索号**：J-03　**类别**：J 智能体评测基准与成本 / 可靠性工程　**轮次**：第一轮
- **作者 / 机构**：Shunyu Yao、Noah Shinn、Pedram Razavi、Karthik Narasimhan（Sierra）
- **时间**：2024　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2406.12045>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：「We also propose a new metric (pass^k) to evaluate the reliability of agent behavior over multiple trials.」
- **要点**：模拟「LM 驱动的用户」与「配备领域 API 工具及政策指南的智能体」之间的动态多轮对话，以对话结束时的数据库状态与标注目标状态比对来评测功能正确性，并提出 pass^k 度量多次试验下行为可靠性。实验显示即便 gpt-4o 这类先进函数调用智能体，任务成功率仍不足 50%，零售域 pass^8 低于 25%。
- **与主题关联**：直接量化「干得稳不稳」——云端最强模型在重复运行下的一致性依然很差，是常驻助理可靠性边界的关键证据。

#### 081｜WebArena: A Realistic Web Environment for Building Autonomous Agents

- **检索号**：J-04　**类别**：J 智能体评测基准与成本 / 可靠性工程　**轮次**：第一轮
- **作者 / 机构**：Shuyan Zhou、Frank F. Xu、Hao Zhu、Graham Neubig 等（Carnegie Mellon University；ICLR 2024）
- **时间**：2023　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2307.13854>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：「our best GPT-4-based agent only achieves an end-to-end task success rate of 14.41%, significantly lower than the human performance of 78.24%.」
- **要点**：搭建电商、社交论坛、协作软件开发、内容管理四类功能完整、可复现的真实网站环境，并发布以「任务完成的功能正确性」为目标的长时程基准任务。最佳 GPT-4 智能体端到端成功率仅 14.41%，远低于人类 78.24%。
- **与主题关联**：说明「云端 API + 网页工具编排」已能跑通真实日常任务，但成功率仍低，给出家用机做常驻 Web 助理的可行性下限与改进空间。

#### 082｜Berkeley Function Calling Leaderboard（Blog 8: Berkeley Function-Calling Leaderboard）

- **检索号**：J-07　**类别**：J 智能体评测基准与成本 / 可靠性工程　**轮次**：第一轮
- **作者 / 机构**：Fanjia Yan、Huanzhi Mao、Charlie Cheng-Jie Ji、Ion Stoica、Joseph E. Gonzalez、Tianjun Zhang、Shishir G. Patil（UC Berkeley，页面含 people.eecs.berkeley.edu 作者主页链接）
- **时间**：2024　**类型**：官方基准站点
- **出处**：<https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：「It consists of 2k question-function-answer pairs with multiple languages (python, java, javascript, restAPI), diverse application domains and complex use cases.」
- **要点**：首个系统评测 LLM 函数与工具调用能力的公开榜单，含 2,000 组 question-function-answer 对，覆盖 Python、Java、JavaScript、REST API、SQL 多语言，并含单次调用、并行调用、多函数选择与函数相关性检测等复杂场景；页面标注 Last updated: 2024-08-19、引用年份 year={2024}。
- **与主题关联**：函数调用/工具编排正是「家用机只做编排、把推理交给云端 API」的核心能力，该榜单可直接用于云端模型选型。

#### 083｜FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance

- **检索号**：J-08　**类别**：J 智能体评测基准与成本 / 可靠性工程　**轮次**：第一轮
- **作者 / 机构**：Lingjiao Chen、Matei Zaharia、James Zou（Stanford / UC Berkeley）
- **时间**：2023　**类型**：arXiv 论文
- **出处**：<https://arxiv.org/abs/2305.05176>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：「FrugalGPT can match the performance of the best individual LLM (e.g. GPT-4) with up to 98% cost reduction or improve the accuracy over GPT-4 by 4% with the same cost.」
- **要点**：梳理查询 GPT-4、ChatGPT、J1-Jumbo 等 API 的定价（费用可差两个数量级），归纳提示适配、LLM 近似、LLM 级联三类降本策略，并提出按查询学习选用不同 LLM 组合的级联方法。实验可在匹配 GPT-4 表现的同时降低最多 98% 成本，或在同等成本下把准确率提高 4%。
- **与主题关联**：直接论证「成本能否承受」——通过 API 级联与按需选模，常驻助理的长期调用开销可被压缩一到两个数量级。

### K 类｜家用硬件门槛与 API 成本一手资料（9 篇）

#### 084｜Business Pricing | OpenAI（正文 H1：Pricing）

- **检索号**：K-01　**类别**：K 家用硬件门槛与 API 成本一手资料　**轮次**：第一轮
- **作者 / 机构**：OpenAI
- **时间**：n.d.（现行定价页）　**类型**：官方定价页
- **出处**：<https://openai.com/api/pricing>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验；独立抓取二次确认「Business Pricing | OpenAI（Pricing）」
- **页面依据**："Input:$10.00 / 1M tokens"、"Cached input:$1.00 / 1M tokens"、"Output:$50.00 / 1M tokens"；"StandardBatch -50%Data residency +10%"；"Pricing above reflects standard processing rates for context lengths under 272K."
- **要点**：页面按每百万 token 明码标价，GPT-6 Astra 为输入 $10.00 / 1M、缓存输入 $1.00 / 1M、输出 $50.00 / 1M，最便宜的 GPT-6 Luna 为输入 $0.10 / 1M、缓存输入 $0.01 / 1M、输出 $0.50 / 1M。页面同时列出 Standard、Batch（-50%）、Data residency（+10%）三种处理模式的计费维度，并注明上述价格适用于 272K 以下上下文。
- **与主题关联**：把"输入/缓存输入/输出"三类 token 单价与批处理折扣公开，常驻助理的月度云端开销可直接按用量核算，家用机无需为本地算力付费。

#### 085｜Models & Pricing | DeepSeek API Docs

- **检索号**：K-02　**类别**：K 家用硬件门槛与 API 成本一手资料　**轮次**：第一轮
- **作者 / 机构**：深度求索 DeepSeek（DeepSeek API Docs）
- **时间**：n.d.（现行定价页）　**类型**：官方定价页
- **出处**：<https://api-docs.deepseek.com/quick_start/pricing>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**："Model prices are listed in units of per 1M tokens."；"1M INPUT TOKENS (CACHE HIT) OFF-PEAK$0.003 ... PEAK$0.006"；"1M OUTPUT TOKENS OFF-PEAK$0.6 ... PEAK$1.2"；"Off-peak rates are half of the peak rates."；"CONTEXT LENGTH1M"；"Concurrency Limit(3)2500500"
- **要点**：官方按每百万 tokens 计价，deepseek-flash 的缓存命中/未命中输入与输出在低谷时段为 $0.003 / $0.15 / $0.6，高峰时段为 $0.006 / $0.3 / $1.2，并明确"Off-peak rates are half of the peak rates"。页面还列出上下文长度 1M、最大输出 384K、并发限制 2500（flash）/ 500（v4-pro），以及 Search 与 Fetch 每 1000 次成功请求各 $0.75。
- **与主题关联**：低谷价与缓存命中价把定时轮询、批量编排的边际成本压到极低，家用机按量调用即可，成本可逐项对照价目表计算。

#### 086｜Pricing - Claude Platform Docs

- **检索号**：K-03　**类别**：K 家用硬件门槛与 API 成本一手资料　**轮次**：第一轮
- **作者 / 机构**：Anthropic（Claude Platform Docs）
- **时间**：n.d.（现行定价页）　**类型**：官方定价页
- **出处**：<https://docs.anthropic.com/en/docs/about-claude/pricing>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验；站点重定向至 https://claude.com/app-unavailable-in-region
- **页面依据**："All prices are in USD."；"Claude Haiku 5.5 ... $0.10 / MTok ... $0.50 / MTok"；"The Batch API allows asynchronous processing of large volumes of requests with a 50 percent discount on both input and output tokens."；"Batch API and prompt caching discounts can be combined."
- **要点**：页面以 $/MTok 列出各档模型输入/输出价，Claude Haiku 5.5 为输入 $0.10 / MTok、输出 $0.50 / MTok，Claude Sonnet 5.5 为 $2 / $10、Claude Opus 5.5 为 $4 / $20。官方写明 Batch API 对输入与输出 token 均给 50% 折扣，prompt caching 缓存读取按 0.1x 基准输入价计费，且两种折扣可以叠加。
- **与主题关联**：缓存与批处理可叠加折扣，使长期常驻助理的重复系统提示成本被摊薄，成本项全部发生在云端而非本机。

#### 087｜Rate limits | OpenAI API

- **检索号**：K-04　**类别**：K 家用硬件门槛与 API 成本一手资料　**轮次**：第一轮
- **作者 / 机构**：OpenAI
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://platform.openai.com/docs/guides/rate-limits>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验；独立抓取二次确认「Rate limits | OpenAI API（直连 403，独立抓取可读正文）」
- **页面依据**："Rate limits use metrics such as RPM (requests per minute), RPD (requests per day), TPM (tokens per minute), TPD (tokens per day), IPM (images per minute)"；"The three paid usage tiers are Build, Launch, and Grow."；表格 "BuildAstra, Sol, Terra5,0001,000,000"；"Free ... $100 / month"、"Build $5 in total credit purchases $500 / month"
- **要点**：文档定义 RPM、RPD、TPM、TPD、IPM 等限额维度，并给出付费层级资格与月度额度：Free $100 / month、Build（累计 $5）$500 / month、Launch（$100）$5,000 / month、Grow（$500）$200,000 / month。标准限额表列出 Build 层 Astra/Sol/Terra 为 5,000 RPM 与 1,000,000 TPM，Grow 层 Luna 为 30,000 RPM 与 180,000,000 TPM。
- **与主题关联**：吞吐上限由账号 usage tier 与云端配额决定，与家用机 CPU/内存无关，常驻助理只需按限额节奏发请求。

#### 088｜Batch API | OpenAI API

- **检索号**：K-05　**类别**：K 家用硬件门槛与 API 成本一手资料　**轮次**：第一轮
- **作者 / 机构**：OpenAI
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://platform.openai.com/docs/guides/batch>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验
- **页面依据**："Better cost efficiency: 50% cost discount compared to synchronous APIs"；"Each batch completes within 24 hours (and often more quickly)"；`"completion_window": "24h"`；"A single batch may include up to 50,000 requests, and a batch input file can be up to 200 MB in size."；"using the Batch API will not consume tokens from your standard per-model rate limits"
- **要点**：Batch API 相对同步调用给 50% 成本折扣、承诺 24 小时内完成，单个 batch 最多 50,000 个请求 / 200 MB 输入文件，每小时最多创建 2,000 个 batch，结果文件在完成后 30 天自动删除。文档还说明批处理使用独立限额池，不占用同步请求的 per-model rate limits，并写明 "You will be charged for tokens consumed from any completed requests."。
- **与主题关联**：夜间离线整理、批量摘要用半价窗口提交即可，家用机无需长时间高负载运行，也无需为突发吞吐升级硬件。

#### 089｜Understanding and counting tokens | OpenAI Help Center

- **检索号**：K-06　**类别**：K 家用硬件门槛与 API 成本一手资料　**轮次**：第一轮
- **作者 / 机构**：OpenAI（OpenAI Help Center）
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验
- **页面依据**："1 token is approximately 4 characters."；"100 tokens are approximately 75 words."；"Use the Tokenizer to see how text is divided into tokens."、"For programmatic plain-text tokenization, use tiktoken."；"Counting input tokens with the Responses input-token counting API ... is free and does not consume your model's normal inference quota."
- **要点**：官方给出英文文本的经验换算（1 token ≈ 4 字符、100 tokens ≈ 75 词），并区分输入、输出、缓存输入与推理 token 四类计费口径。页面说明可用 Tokenizer 页面或 tiktoken 库精确计数，而 Responses input-token counting API 免费且"does not consume your model's normal inference quota"。
- **与主题关联**：发请求前即可用官方工具把文本换算成 token 并估算费用，家用机只需运行极轻量的计数逻辑，无需本地模型。

#### 090｜Getting started with the Realtime API | OpenAI API

- **检索号**：K-07　**类别**：K 家用硬件门槛与 API 成本一手资料　**轮次**：第一轮
- **作者 / 机构**：OpenAI
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://platform.openai.com/docs/guides/realtime>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验
- **页面依据**："Build a speech-to-speech voice agent with the Realtime API."；"The model works directly with audio, maintains conversation state, and can call tools."；"The session connects over WebRTC in the browser or WebSocket on the server."；示例 `model: "gpt-realtime-2.1"`
- **要点**：官方把 Realtime API 定义为直接处理音频、维持会话状态并可调用工具的 speech-to-speech 接口，浏览器端经 WebRTC、服务端经 WebSocket 建立会话，示例模型为 gpt-realtime-2.1。文档另列出打断（barge-in）、低首音频延迟、VAD 自动轮次检测与 Realtime MCP 工具等能力入口。
- **与主题关联**：语音输入与合成全部由云端实时端点承担，家用机只需麦克风、扬声器和网络，不必本地部署 STT/TTS 模型。

#### 091｜Buy a Raspberry Pi 5 – Raspberry Pi

- **检索号**：K-08　**类别**：K 家用硬件门槛与 API 成本一手资料　**轮次**：第一轮
- **作者 / 机构**：Raspberry Pi Ltd（Raspberry Pi 官方）
- **时间**：n.d.　**类型**：官方规格书
- **出处**：<https://www.raspberrypi.com/products/raspberry-pi-5>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验；独立抓取二次确认「Buy a Raspberry Pi 5 – Raspberry Pi（直连 403，独立抓取读回官方 Specification 表）」
- **页面依据**："Broadcom BCM2712 2.4GHz quad-core 64-bit Arm Cortex-A76 CPU"；"LPDDR4X-4267 SDRAM (1GB, 2GB, 4GB, 8GB, and 16GB)"；"5V/5A DC power via USB-C, with Power Delivery support"；"Raspberry Pi 5 16GB is available now for $305."
- **要点**：官方规格表列出 BCM2712 2.4GHz 四核 Cortex-A76（512KB 每核 L2、2MB 共享 L3）、LPDDR4X-4267 内存 1GB/2GB/4GB/8GB/16GB、2 × USB 3.0（5Gbps）、PCIe 2.0 x1 与 5V/5A USB-C 供电，配套官方 27W USB-C 电源。页面标明 16GB 版本售价 $305，并称产品"will remain in production until at least January 2036"。
- **与主题关联**：以单板机官方规格、5V/5A 供电与整机价格界定最低硬件门槛，证明编排云端 API 的常驻助理可运行在几十瓦级、数十美元级设备上。

#### 092｜Resource constraints | Docker Docs

- **检索号**：K-09　**类别**：K 家用硬件门槛与 API 成本一手资料　**轮次**：第一轮
- **作者 / 机构**：Docker Inc.（Docker Docs）
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://docs.docker.com/engine/containers/resource_constraints>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「Resource constraints | Docker Docs」
- **页面依据**："By default, a container has no resource constraints and can use as much of a given resource as the host's kernel scheduler allows."；"`-m` or `--memory=` The maximum amount of memory the container can use. If you set this option, the minimum allowed value is `6m` (6 megabytes)."；"So if `--memory=\"300m\"` and `--memory-swap=\"1g\"`, the container can use 300m of memory and 700m (1g - 300m) swap."
- **要点**：官方说明容器默认无资源约束，可用 `-m/--memory` 设硬性内存上限（最小 6m）、`--memory-swap` 设内存加交换总量、`--memory-swappiness` 取 0 到 100。示例 `--memory="300m"` 配 `--memory-swap="1g"` 表示 300m 内存加 700m swap，另说明硬限与软限的区别及 OOM 风险。
- **与主题关联**：编排服务可被显式约束在很小的内存配额内长期常驻，家用机无需为"本地跑大模型"预留大内存或显存。

### L 类｜厂商工程指南、综述与主动任务产品证据（8 篇）

#### 093｜Building effective agents

- **检索号**：L-01　**类别**：L 厂商工程指南、综述与主动任务产品证据　**轮次**：第一轮
- **作者 / 机构**：Erik Schluntz、Barry Zhang（Anthropic）
- **时间**：2024-12　**类型**：官方工程指南
- **出处**：<https://www.anthropic.com/engineering/building-effective-agents>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns.
- **要点**：基于与数十个团队合作的经验，主张成功落地几乎不依赖复杂框架，而是用「简单、可组合的模式」把 LLM 调用、工具与工作流串起来。文中区分 workflow 与 agent，并建议优先用最简方案、只在必要时增加自主性。
- **与主题关联**：它把智能体能力定位为「编排模式」而非本地重资产，家用机只需调度云端 LLM API 与工具即可复现同类系统。

#### 094｜A practical guide to building agents

- **检索号**：L-02　**类别**：L 厂商工程指南、综述与主动任务产品证据　**轮次**：第一轮
- **作者 / 机构**：OpenAI
- **时间**：2025-04　**类型**：白皮书
- **出处**：<https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf>
- **核验**：直连 200 · PDF 无 HTML 标题，已确认响应类型与文件大小；独立抓取二次确认「A practical guide to building agents（官方 PDF，直连 200，Content-Type: application/pdf）」
- **页面依据**：Agents are systems that independently accomplish tasks on your behalf.
- **要点**：面向产品与工程团队给出首个智能体的设计基础，明确 agent 是「由 LLM 管理流程执行、动态选择工具」的系统，并给出编排模式、单 agent 与多 agent 及护栏的最佳实践。全篇围绕调用模型与工具构建逻辑，不涉及本地训练或本地部署大模型。
- **与主题关联**：把「智能体」定义为对 LLM 与工具的编排层，正好支撑家用机通过 API 调用云端模型完成编排、无需本地跑大模型。

#### 095｜Agents

- **检索号**：L-03　**类别**：L 厂商工程指南、综述与主动任务产品证据　**轮次**：第一轮
- **作者 / 机构**：Julia Wiesinger、Patrick Marlow、Vladimir Vuskovic（Google，Kaggle 白皮书）
- **时间**：n.d.　**类型**：白皮书
- **出处**：<https://www.kaggle.com/whitepaper-agents>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验；独立抓取二次确认「Agents | Kaggle（作者 Julia Wiesinger, Patrick Marlow, Vladimir Vuskovic）」
- **页面依据**：This combination of reasoning, logic, and access to external information that are all connected to a Generative AI model invokes the concept of an agent, or a program that extends beyond the standalone capabilities of a Generative AI model.
- **要点**：系统讲生成式 AI Agent 的基础构件与认知架构，强调模型通过工具访问实时信息、发起 API 调用（发邮件、完成事务等）来扩展自身能力。白皮书给出扩展、函数、数据存储等工具形态与编排方式。
- **与主题关联**：明确指出 Agent 是「模型 + 工具/API 调用」的扩展程序，能力来自云端模型与外部接口，而非本地算力。

#### 096｜Introducing ambient agents

- **检索号**：L-04　**类别**：L 厂商工程指南、综述与主动任务产品证据　**轮次**：第一轮
- **作者 / 机构**：Harrison Chase（LangChain）
- **时间**：2025-01　**类型**：官方博文
- **出处**：<https://blog.langchain.com/introducing-ambient-agents>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Ambient agents listen to an event stream and act on it accordingly, potentially acting on multiple events at a time
- **要点**：提出「ambient agents」范式：不再由用户每次发起聊天，而是监听事件流、在后台常驻并主动响应，可同时跑多个 agent；配套 LangGraph 提供持久化、human-in-the-loop、长期记忆与内置 cron jobs。文中还给出已落地的邮件助理参考实现（Agent Inbox）。
- **与主题关联**：这是「常驻、主动、定时触发」助理的直接工程范式，且明确指出许多 ambient agents 靠 schedule/cron 运行，家用机做轻量编排即可承载。

#### 097｜Agentic Design Patterns Part 3, Tool Use

- **检索号**：L-05　**类别**：L 厂商工程指南、综述与主动任务产品证据　**轮次**：第一轮
- **作者 / 机构**：Andrew Ng（DeepLearning.AI, The Batch）
- **时间**：2024-04　**类型**：官方博文
- **出处**：<https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **页面依据**：Tool Use, in which an LLM is given functions it can request to call for gathering information, taking action, or manipulating data, is a key design pattern of AI agentic workflows.
- **要点**：吴恩达在 The Batch 系列信件中系统阐述 agentic workflow 的四种设计模式（Reflection、Tool Use、Planning、Multi-agent collaboration），本篇专讲 Tool Use：让 LLM 请求调用搜索、代码执行、邮件与日历等外部函数。他强调 agentic workflow 是「多次提示 LLM 逐步迭代」而非一次性零样本输出。
- **与主题关联**：权威论述把价值放在「工作流编排 + 工具/API 调用」上，说明能力增量来自编排层，家用机调用云端 LLM 即可实现。

#### 098｜Introducing smolagents: simple agents that write actions in code.

- **检索号**：L-06　**类别**：L 厂商工程指南、综述与主动任务产品证据　**轮次**：第一轮
- **作者 / 机构**：Hugging Face
- **时间**：2024-12　**类型**：官方博文
- **出处**：<https://huggingface.co/blog/smolagents>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「Introducing smolagents: simple agents that write actions in code.」
- **页面依据**：For the `model`, you can use any LLM, either open models using our `HfApiModel` class, that leverages Hugging Face's free inference API (as shown in the leopard example above), or you can use `LiteLLMModel` to leverage litellm and pick from a list of 100+ different cloud LLMs.
- **要点**：发布极简 agent 库 smolagents，核心逻辑仅约千行代码、抽象压到最低；模型层可任意替换，既可用 HF 免费推理 API，也可经 LiteLLM 接入 100+ 云端 LLM。它以「代码即动作」的 CodeAgent 让轻量客户端驱动智能体行为。
- **与主题关联**：直接证明智能体框架可以极轻、模型可以完全云端化，家用消费级电脑只需跑编排逻辑而不必本地加载大模型。

#### 099｜Scheduled tasks in ChatGPT | OpenAI Help Center

- **检索号**：L-07　**类别**：L 厂商工程指南、综述与主动任务产品证据　**轮次**：第一轮
- **作者 / 机构**：OpenAI Help Center
- **时间**：n.d.　**类型**：官方帮助文档
- **出处**：<https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验；独立抓取二次确认「Scheduled tasks in ChatGPT | OpenAI Help Center」
- **页面依据**：ChatGPT can run one-time or recurring tasks, monitor for changes, and respond to supported events when available.
- **要点**：官方文档确认 ChatGPT 已上线「Scheduled tasks」：可创建一次性或周期性任务、监测变化、按支持的应用事件（Gmail/Slack/GitHub）触发，并在后台执行模型处理、通过推送或邮件通知用户。文档还列出不同套餐的活跃任务上限与每小时执行频率。
- **与主题关联**：这是云端产品已落地的「定时/主动执行」证据，说明主动式个人助理的运行与算力在云侧，用户端只需配置与接收结果。

#### 100｜Schedules in Gemini Apps - Computer - Gemini Apps Help

- **检索号**：L-08　**类别**：L 厂商工程指南、综述与主动任务产品证据　**轮次**：第一轮
- **作者 / 机构**：Google（Gemini Apps Help）
- **时间**：n.d.　**类型**：官方帮助文档
- **出处**：<https://support.google.com/gemini/answer/16316416>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「Schedules in Gemini Apps - Computer - Gemini Apps Help」
- **页面依据**：You can make Gemini a part of your daily, weekly, and monthly routines by scheduling recurring actions.
- **要点**：官方帮助文档确认 Gemini Apps 支持 Schedules（定时主动动作）：可设置每日、每周、每月的重复任务（新闻摘要、日历与邮件日报、市场报告等），Gemini 在后台提前准备内容并按设定时间投递与通知，用户最多可保留 10 个活跃计划。文档还说明计划可暂停、编辑并在 Scheduled 页统一管理。
- **与主题关联**：与 ChatGPT Tasks 并列，构成厂商级「已落地定时主动任务」产品证据，证明常驻主动助理由云端服务承载，家用机不必本地运行大模型。

### M 类｜厂商官方 CUA 产品与技术文档（11 篇）

#### 101｜Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku（页面 title：Computer use, Claude 3.5 Sonnet, and Claude 3.5 Haiku \ Anthropic）

- **检索号**：M-01　**类别**：M 厂商官方 CUA 产品与技术文档　**轮次**：第二轮
- **作者 / 机构**：Anthropic
- **时间**：2024-10　**类型**：官方公告
- **出处**：<https://www.anthropic.com/news/3-5-models-and-computer-use>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：厂商官方（Anthropic 官网公告），页面标注 "Oct 22, 2024"；页面给出 OSWorld screenshot-only 14.9%（对比次优系统 7.8%）、增加步数后 22.0%；页面称 "Claude 3.5 Sonnet is the first frontier AI model to offer computer use in public beta"。
- **页面依据**："computer use"、"Available today on the API"、"Claude 3.5 Sonnet is the first frontier AI model to offer computer use in public beta"、"On OSWorld ... Claude 3.5 Sonnet scored 14.9%"
- **要点**：宣布 computer use 公测，开发者可经 Anthropic API、Amazon Bedrock、Google Cloud Vertex AI 让 Claude 看屏幕、移动光标、点击按钮、输入文字，把自然语言指令翻译为计算机命令。页面说明该能力仍属实验性，滚动/拖拽/缩放有困难，并建议从低风险任务起步。
- **与主题关联**：提供可在本地自建沙箱环境中经 API 驱动的通用桌面 computer use 能力，是本地 PC 实现 CUA 的开创性一手依据。

#### 102｜Computer-Using Agent | OpenAI（正文 H1：Computer-Using Agent）

- **检索号**：M-02　**类别**：M 厂商官方 CUA 产品与技术文档　**轮次**：第二轮
- **作者 / 机构**：OpenAI
- **时间**：2025-01　**类型**：官方技术报告
- **出处**：<https://openai.com/index/computer-using-agent>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验；独立抓取二次确认「Computer-Using Agent | OpenAI（页面标注 January 23, 2025）」
- **影响力**：厂商官方（OpenAI 官方研究页），页面标注 "January 23, 2025"；页面 Evaluations 表列出 OpenAI CUA 的 OSWorld 38.1%、WebArena 58.1%、WebVoyager 87.0% 为当时 SOTA，并列出 OSWorld 人类 72.4%。
- **页面依据**："Computer-Using Agent (CUA)"、"the same universal interface of screen, mouse, and keyboard"、"OSWorld 38.1%"、"an iterative loop that integrates perception, reasoning, and action"
- **要点**：介绍 CUA 模型以 screen、mouse、keyboard 通用接口操作 GUI，通过截图感知、链式推理、产出 click/scroll/type 动作的迭代循环工作，无需 OS 或 Web 专用 API。页面给出多项基准成绩，并写明仍处早期、文本编辑不精确等限制。
- **与主题关联**：定义"看屏幕—推理—输出鼠标键盘动作"的闭环，是本地 PC 上以截图驱动实现 CUA 的核心模型依据。

#### 103｜Computer use | OpenAI API（正文 H1：Computer use）

- **检索号**：M-03　**类别**：M 厂商官方 CUA 产品与技术文档　**轮次**：第二轮
- **作者 / 机构**：OpenAI
- **时间**：n.d.　**类型**：官方 API 文档
- **出处**：<https://platform.openai.com/docs/guides/tools-computer-use>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验；独立抓取二次确认「Computer use | OpenAI API（原文 "Computer use lets a model operate a browser or desktop interface."）」
- **影响力**：厂商官方（OpenAI Platform 官方 API 文档）；页面未标注发布日期（未核实）；页面未给出基准成绩（未核实）；为 Responses API `computer` 工具的权威接口定义，含 "Migration from computer-use-preview" 章节。
- **页面依据**："Enable `computer` in the `tools` array"、"computer_call"、"computer_call_output"、"computer_screenshot"、"ComputerToolset"、"Migration from computer-use-preview"
- **要点**：文档说明在 Responses API 的 `tools` 数组启用 `{"type": "computer"}`，应用侧以 driver 执行 `computer_call` 中的动作、用 `computer_call_output` 回传截图构成 agent loop；并提供 `ComputerToolset`/`BrowserToolset` SDK 与代码执行（PyAutoGUI、Playwright）路径。约束含隔离环境、截图坐标换算、会话保持、人类审批与步数/成本上限。
- **与主题关联**：给出本地程序可直接调用的 `computer` 工具循环与截图/动作回传协议，是本地 PC 落地 CUA 的接口规范。

#### 104｜Computer use tool - Claude Platform Docs（正文 H1：Computer use tool）

- **检索号**：M-04　**类别**：M 厂商官方 CUA 产品与技术文档　**轮次**：第二轮
- **作者 / 机构**：Anthropic
- **时间**：n.d.　**类型**：官方 API 文档
- **出处**：<https://docs.anthropic.com/en/docs/build-with-claude/computer-use>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验；站点重定向至 https://claude.com/app-unavailable-in-region；独立抓取二次确认「Computer use tool - Claude Platform Docs（独立抓取未出现地区重定向）」
- **影响力**：厂商官方（Claude Platform Docs 官方工具参考）；页面未标注发布日期（未核实）；页面未给出基准成绩（未核实）；官方定义 `computer_toolset_20260801`、`computer_20251124`、`computer_20250124` 工具版本与 17 个 member tools。
- **页面依据**："computer use tool"、"computer_toolset_20260801"、"screenshot"、"left_click"、`"toolset_name": "computer"`、"Messages API"
- **要点**：文档说明在 Messages API 的 `tools` 数组声明 `{"type": "computer_toolset_20260801"}` 即获得 screenshot、left_click、type、zoom 等成员工具，应用侧在自有沙箱环境顺序执行 `tool_use` 并以 `tool_result` 回传构成 agent loop。页面给出坐标按截图像素空间、截图尺寸/缩放限制、批处理失败中止等约束，并要求容器化隔离环境。
- **与主题关联**：提供客户端本地执行 computer use 动作的完整工具集与循环协议，直接支撑在本地 PC/容器中搭建 CUA。

#### 105｜Computer use - Gemini API | Google AI Studio（正文 H1：Computer use）

- **检索号**：M-05　**类别**：M 厂商官方 CUA 产品与技术文档　**轮次**：第二轮
- **作者 / 机构**：Google（Google AI Studio / Gemini API）
- **时间**：n.d.　**类型**：官方 API 文档
- **出处**：<https://ai.google.dev/gemini-api/docs/computer-use>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「Computer use - Gemini API | Google AI Studio」
- **影响力**：厂商官方（Google 官方 Gemini API 文档）；页面未标注发布日期（未核实）；页面明确未发现公开基准成绩（未核实）；为 `computer_use` 工具的权威接口定义，支持 browser / mobile / desktop 三种环境。
- **页面依据**："computer_use"、"function_call"、"function_result"、"ENVIRONMENT_DESKTOP"、"excluded_predefined_functions"、"normalized 1000x1000 coordinates"
- **要点**：页面定义经 Interactions API 以 `tools=[{"type":"computer_use","environment":"browser"}]` 构建 CUA，模型基于截图产出 `function_call`（click、type、navigate 等），应用侧用 Playwright 执行并回传 `function_result` 截图形成循环。支持三环境、1000×1000 归一化坐标换算、自定义函数与安全确认（`safety_decision`、`require_confirmation`）。
- **与主题关联**：给出本地用 Playwright 执行 UI 动作并回传截图的官方循环，可直接用于本地 PC 的浏览器/桌面 CUA。

#### 106｜Fara-7B: An Efficient Agentic Model for Computer Use - Microsoft Research

- **检索号**：M-06　**类别**：M 厂商官方 CUA 产品与技术文档　**轮次**：第二轮
- **作者 / 机构**：Microsoft Research
- **时间**：2025-11　**类型**：官方技术报告
- **出处**：<https://www.microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：厂商官方（Microsoft Research 官方发布博客），页面 "Published November 24, 2025"；Table 1 给出 Fara-7B 的 WebVoyager 73.5、Online-Mind2Web 34.1、DeepShop 26.2、WebTailBench 38.4；页面说明以 MIT license 发布于 Microsoft Foundry 与 Hugging Face。
- **页面依据**："Fara-7B"、"run CUA models directly on devices"、"none of its context needs to leave your personal device"、"click(x,y)"、"Copilot+ PCs powered by Windows 11"
- **要点**：发布 7B 的 on-device CUA 模型，仅凭浏览器截图预测单步动作（click(x,y)、type()、web_search()、visit_url()），上下文与数据不出本地设备，可在 Windows 11 Copilot+ PC 借助 NPU 全本地运行。页面给出四个 web 基准成绩、约 16 步平均完成，以及沙箱运行、Critical Point 用户确认等约束。
- **与主题关联**：直接给出"模型在设备端本地运行、无需云端上下文"的 CUA 实现路径，是本地 PC 实现 CUA 最贴合的官方依据。

#### 107｜GitHub - bytedance/UI-TARS: Pioneering Automated GUI Interaction with Native Agents · GitHub

- **检索号**：M-07　**类别**：M 厂商官方 CUA 产品与技术文档　**轮次**：第二轮
- **作者 / 机构**：ByteDance（bytedance / ByteDance-Seed）
- **时间**：2025-04　**类型**：官方模型卡
- **出处**：<https://github.com/bytedance/UI-TARS>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：厂商官方（ByteDance 官方开源仓库）；页面 Updates 记 "2025.04.16 we open-sourced the UI-TARS-1.5-7B"、"2025.09.04 ... release the UI-TARS-2"；Apache License 2.0；页面给出 OSworld (100 steps) 42.5、Windows Agent Arena (50 steps) 42.1、ScreenSpot-V2 94.2 等成绩。
- **页面依据**："UI-TARS-1.5"、"OSworld (100 steps) 42.5"、"COMPUTER_USE"、"parsing_response_to_pyautogui_code"、"Apache License 2.0"
- **要点**：官方仓库发布开源多模态 GUI agent UI-TARS，提供 COMPUTER_USE / MOBILE_USE / GROUNDING 三套 prompt 模板，可把带 Thought/Action 的输出解析为 pyautogui 代码，在 Windows/Linux/macOS 桌面执行点击、拖拽、快捷键、滚动等动作。页面列出多基准成绩、部署与坐标处理说明，并指向可在本地设备运行的 UI-TARS-desktop。
- **与主题关联**：提供可本地部署的模型权重、动作解析与桌面 prompt 模板，是本地 PC 上自建 CUA 的开源一手依据。

#### 108｜GitHub - QwenLM/Qwen3-VL: Qwen3-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud. · GitHub

- **检索号**：M-09　**类别**：M 厂商官方 CUA 产品与技术文档　**轮次**：第二轮
- **作者 / 机构**：Qwen team, Alibaba Cloud（QwenLM）
- **时间**：2025-09　**类型**：官方模型卡
- **出处**：<https://github.com/QwenLM/Qwen3-VL>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「GitHub - QwenLM/Qwen3-VL（独立抓取确认仓库存在，README / Cookbook 含 Visual Agent、Computer-Use Agent 段落）」
- **影响力**：厂商官方（Qwen 团队官方模型仓库）；页面 News 记 2025.09.23 发布 Qwen3-VL-235B-A22B-Instruct/Thinking、2025.11.27 发布 Qwen3-VL paper；页面未给出可读的基准成绩数字（Performance 为图片，未核实）。
- **页面依据**："Visual Agent"、"Computer-Use Agent"、"Operates PC/mobile GUIs—recognizes elements, understands functions, invokes tools, completes tasks"、"computer_use.ipynb"
- **要点**：官方模型仓库把 Qwen3-VL 定位为具备 Visual Agent 能力的多模态模型，明确列出 `Computer-Use Agent`（"Locate and think for controlling computers and Web"）与 Mobile Agent，并提供 computer_use.ipynb cookbook。页面列出 2B 至 235B-A22B 的 Dense/MoE、Instruct/Thinking 版本与 vLLM/SGLang 部署方式。
- **与主题关联**：提供可本地部署的开源视觉模型及其 computer-use cookbook，是本地 PC 以视觉模型驱动 GUI 操作的模型侧依据。

#### 109｜GitHub - google-gemini/computer-use-preview · GitHub（README H1：Computer Use Preview）

- **检索号**：M-10　**类别**：M 厂商官方 CUA 产品与技术文档　**轮次**：第二轮
- **作者 / 机构**：Google（google-gemini / Google DeepMind）
- **时间**：2025-10　**类型**：官方 API 文档
- **出处**：<https://github.com/google-gemini/computer-use-preview>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：厂商官方（Google 官方参考实现仓库，Gemini API computer use 文档 "What's next" 中列为 Reference implementation）；页面 Initial commit 为 "Oct 7, 2025"；页面未给出基准成绩（未核实）。
- **页面依据**："gemini-2.5-computer-use-preview-10-2025"、"python main.py --query"、`--env="playwright"`、"Runs the browser locally using Playwright"
- **要点**：官方参考实现给出用 Gemini Developer API 或 Vertex AI 运行 Gemini Computer Use 的 Quick Start：`python main.py --query ... --env=playwright` 在本地用 Playwright 驱动 Chrome，也支持 browserbase 远程后端。README 列出可用模型（含 `gemini-2.5-computer-use-preview-10-2025`）、CLI 参数与 Playwright 下拉框已知问题。
- **与主题关联**：提供可在本地命令行直接跑通 Gemini computer use 的参考实现，是本地 PC 复现 CUA 的可执行一手入口。

#### 110｜Qwen2.5 VL! Qwen2.5 VL! Qwen2.5 VL! | Qwen

- **检索号**：M-11　**类别**：M 厂商官方 CUA 产品与技术文档　**轮次**：第二轮
- **作者 / 机构**：Qwen Team（Alibaba Cloud / Qwen）
- **时间**：2025-01　**类型**：官方公告
- **出处**：<https://qwenlm.github.io/blog/qwen2.5-vl>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：厂商官方（Qwen 官方博客），页面标注 "January 26, 2025"；页面未给出具体基准分数（仅称 Qwen2.5-VL-7B-Instruct 在若干任务上优于 GPT-4o-mini，未核实具体数字）。
- **页面依据**："Being agentic"、"capable of computer use and phone use"、"Superior Computer and Mobile Agent"、"visual agent"
- **要点**：官方发布博客把 "Being agentic" 列为 Qwen2.5-VL 关键特性，说明模型可直接作为 visual agent 推理并动态调用工具，具备 computer use 与 phone use 能力，并设 "Superior Computer and Mobile Agent" 章节展示移动端订票等示例。开源 3B/7B/72B 权重于 Hugging Face 与 ModelScope。
- **与主题关联**：官方确认 Qwen2.5-VL 的 computer/phone use 定位并开放权重，为本地 PC 以该视觉模型驱动 GUI 操作提供早期一手依据。

#### 111｜GitHub - bytedance/UI-TARS-desktop: The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra · GitHub

- **检索号**：M-12　**类别**：M 厂商官方 CUA 产品与技术文档　**轮次**：第二轮
- **作者 / 机构**：ByteDance（bytedance）
- **时间**：n.d.　**类型**：官方模型卡
- **出处**：<https://github.com/bytedance/UI-TARS-desktop>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「GitHub - bytedance/UI-TARS-desktop: The Open-Source Multimodal AI Agent Stack · GitHub」
- **影响力**：厂商官方（ByteDance 官方开源仓库）；页面未标注单一发布日期（未核实）；Apache License 2.0；页面未给出基准成绩（未核实）。
- **页面依据**："UI-TARS Desktop is a native GUI agent for your local computer"、"Precise mouse and keyboard control"、"Screenshot and visual recognition support"、"Private and secure - fully local processing"
- **要点**：官方桌面应用仓库提供基于 UI-TARS 模型的本地 GUI Agent，支持截图视觉识别、精确鼠标键盘控制、Windows/MacOS/Browser 跨平台，以及本地与远程 computer/browser operator。页面说明 "fully local processing"，并提供 Agent TARS CLI、MCP 集成与本地/远程 operator 文档。
- **与主题关联**：把 CUA 直接封装为本地 PC 可运行的桌面应用（本地+远程 operator），是"本地计算机实现 CUA"最贴近成品形态的官方依据。

### N 类｜CUA 系统架构学术论文（11 篇）

#### 112｜OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

- **检索号**：N-01　**类别**：N CUA 系统架构学术论文　**轮次**：第二轮
- **作者 / 机构**：Tianbao Xie、Danyang Zhang、Jixuan Chen 等（香港大学 / Salesforce Research 等；arXiv 页未列机构，据项目公开信息）
- **时间**：2024-04　**类型**：会议论文（NeurIPS 2024，据 xlang-ai/OSWorld 仓库标题标注；此处登记 arXiv abs 页）
- **出处**：<https://arxiv.org/abs/2404.07972>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：NeurIPS 2024（GitHub 仓库 xlang-ai/OSWorld 标题「[NeurIPS 2024]」标注）；页面量化成绩：369 个真实计算机任务，最佳模型成功率 12.24%，人类 72.36%
- **页面依据**：the first-of-its-kind scalable, real computer environment for multimodal agents, supporting task setup, execution-based evaluation, and interactive learning across various operating systems such as Ubuntu, Windows, and macOS
- **要点**：以虚拟机快照复位初始状态、通过鼠标键盘级动作与自定义执行脚本评估，跨 Ubuntu / Windows / macOS 的真实桌面应用、文件 I/O 与多应用工作流执行开放式任务；369 个任务上最佳 LLM/VLM 智能体仅 12.24% 成功，人类可达 72.36%。
- **与主题关联**：提供本地真实 OS 上「任务设定—执行—可复现评测」的完整环境范式，是家用机 CUA 落地最先要对齐的基准与执行层接口。

#### 113｜Agent S: An Open Agentic Framework that Uses Computers Like a Human

- **检索号**：N-02　**类别**：N CUA 系统架构学术论文　**轮次**：第二轮
- **作者 / 机构**：Saaket Agashe、Jiuzhou Han、Shuyu Gan 等（simular-ai/Agent-S 团队）
- **时间**：2024-10　**类型**：会议论文（ICLR 2025，据 simular-ai/Agent-S 仓库 BibTeX 标注；此处登记 arXiv abs 页）
- **出处**：<https://arxiv.org/abs/2410.08164>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：ICLR 2025（simular-ai/Agent-S 仓库 BibTeX 中 booktitle={International Conference on Learning Representations (ICLR)}, year={2025}）；页面量化成绩：OSWorld 成功率较基线 +9.37%（83.6% 相对提升）
- **页面依据**：Agent S introduces experience-augmented hierarchical planning ... it employs an Agent-Computer Interface (ACI) to better elicit the reasoning and control capabilities of GUI agents
- **要点**：用「经验增强分层规划 + Agent-Computer Interface」把外部知识检索与内部经验复用组织成多层级任务规划，在真实 OS 的 GUI 上完成多步长时程操作；OSWorld 上成功率绝对提升 9.37%（相对 83.6%）并刷新 SOTA，且泛化到新发布的 WindowsAgentArena。
- **与主题关联**：其 ACI 动作抽象与分层规划/经验检索，是把云端 LLM 输出稳定转换为本地可执行 GUI 动作的核心架构参考。

#### 114｜OS-Copilot: Towards Generalist Computer Agents with Self-Improvement

- **检索号**：N-03　**类别**：N CUA 系统架构学术论文　**轮次**：第二轮
- **作者 / 机构**：Zhiyong Wu、Chengcheng Han、Zichen Ding 等（OS-Copilot / FRIDAY 团队）
- **时间**：2024-02　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2402.07456>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：会议/期刊：未核实；arXiv 预印本 2024-02；页面量化成绩：GAIA 基准上较此前方法提升 35%
- **页面依据**：a framework to build generalist agents capable of interfacing with comprehensive elements in an operating system (OS), including the web, code terminals, files, multimedia, and various third-party applications
- **要点**：以统一接口把网页、代码终端、文件、多媒体与第三方应用纳入 OS 级操作，并通过自我指导学习为陌生应用生成课程、积累可复用技能，实现 FRIDAY 在真实桌面上的自我改进；在 GAIA 上比此前方法高 35%，并给出在 Excel、PowerPoint 上以最少监督学会控制与自我改进的量化证据。
- **与主题关联**：给出「本地 OS 全要素接口 + 技能库自我改进」的实现骨架，适合家用机上长期运行的主动式助理。

#### 115｜OS-ATLAS: A Foundation Action Model for Generalist GUI Agents

- **检索号**：N-04　**类别**：N CUA 系统架构学术论文　**轮次**：第二轮
- **作者 / 机构**：Zhiyong Wu、Zhenyu Wu、Fangzhi Xu 等（OS-Atlas 团队）
- **时间**：2024-10　**类型**：会议论文（ICLR 2025 Spotlight，据检索结果中知乎专栏「[ICLR'25 Spotlight] OS-Atlas」标注；此处登记 arXiv abs 页）
- **出处**：<https://arxiv.org/abs/2410.23218>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：ICLR 2025 Spotlight（检索结果中知乎专栏标题「[ICLR'25 Spotlight] OS-Atlas」标注）；页面量化成绩：开源跨平台 GUI grounding 语料含超过 1300 万 GUI 元素（over 13 million），覆盖 Windows / Linux / MacOS / Android / Web
- **页面依据**：releasing the largest open-source cross-platform GUI grounding corpus to date, which contains over 13 million GUI elements
- **要点**：把 GUI grounding 与动作/规划统一为可微调的基座动作模型，合成跨 Windows、Linux、macOS、Android、Web 的开源 grounding 数据并驱动桌面端动作执行；在覆盖移动端、桌面端、网页的 6 个基准上显著超越此前 SOTA 开源模型。
- **与主题关联**：为本地 CUA 提供可端侧部署的 grounding 基座模型与跨平台数据配方，降低对云端闭源 VLM 的依赖。

#### 116｜Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale

- **检索号**：N-05　**类别**：N CUA 系统架构学术论文　**轮次**：第二轮
- **作者 / 机构**：Rogerio Bonatti、Dan Zhao、Francesco Bonacci 等（微软 / Microsoft Research）
- **时间**：2024-09　**类型**：arXiv 预印本（微软研究院官方出版物页收录）
- **出处**：<https://arxiv.org/abs/2409.08264>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：会议/期刊：未核实；arXiv 预印本 2024-09；页面量化成绩：150+ Windows 任务，Navi 成功率 19.5% vs 人类 74.5%，Azure 并行全量评测最短约 20 分钟
- **页面依据**：agents can operate freely within a real Windows OS and use the same wide range of applications, tools, and web browsers available to human users when solving tasks
- **要点**：改造 OSWorld 框架在真实 Windows 上提供 150+ 跨领域任务，并把多步顺序评测并行化到 Azure，同时给出多模态智能体 Navi 作基线；Navi 成功率 19.5%，未辅助人类 74.5%，全量评测最短 20 分钟。
- **与主题关联**：直接给出 Windows 本地桌面上的可规模化评测与并行执行方案，是家用 Windows 机实现 CUA 的工程参照。

#### 117｜UFO: A UI-Focused Agent for Windows OS Interaction

- **检索号**：N-06　**类别**：N CUA 系统架构学术论文　**轮次**：第二轮
- **作者 / 机构**：Chaoyun Zhang、Liqun Li、Shilin He 等（微软研究院 / Microsoft Research）
- **时间**：2024-02　**类型**：arXiv 预印本（微软研究院官方出版物页收录）
- **出处**：<https://arxiv.org/abs/2402.07939>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：会议/期刊：未核实；arXiv 预印本 2024-02（v5 2024-05）；页面量化成绩：在 9 个常用 Windows 应用上测试；摘要自称首个 Windows OS 专用 UI 智能体
- **页面依据**：To the best of our knowledge, UFO stands as the first UI agent specifically tailored for task completion within the Windows OS environment
- **要点**：双智能体框架读取 Windows 应用 GUI 与控件信息，经 control interaction 模块完成免人工干预的动作 grounding，可跨单个及多个应用连续操作；在 9 个常用 Windows 应用的日常场景上给出定量指标与真实案例评测。
- **与主题关联**：提供 Windows 原生控件树 + 视觉融合的操作通道，是本地 Windows CUA 最早、最直接的完整系统实现。

#### 118｜UFO2: The Desktop AgentOS

- **检索号**：N-07　**类别**：N CUA 系统架构学术论文　**轮次**：第二轮
- **作者 / 机构**：Chaoyun Zhang、He Huang、Chiming Ni 等（微软 / Microsoft，源码 github.com/microsoft/UFO）
- **时间**：2025-04　**类型**：arXiv 预印本（微软官方开源项目配套论文）
- **出处**：<https://arxiv.org/abs/2504.14603>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：会议/期刊：未核实；arXiv 预印本 2025-04；页面量化成绩：在 20+ 真实 Windows 应用上评测（over 20 real-world Windows applications）
- **页面依据**：We present UFO2, a multiagent AgentOS for Windows desktops that elevates CUAs into practical, system-level automation
- **要点**：以集中式 HostAgent 分解协调、应用专用 AppAgent 结合原生 API 与统一 GUI–API 动作层，并用 Windows UIA + 视觉混合控件检测、推测式多动作规划、画中画隔离虚拟桌面在真实 Windows 上执行；在 20+ 真实 Windows 应用上的鲁棒性与执行准确率显著优于此前 CUA。
- **与主题关联**：把 CUA 提升为系统级 AgentOS（深度 OS 集成、API/GUI 混合动作、用户与智能体并发互不干扰），是本地桌面实现最完整的系统架构样板。

#### 119｜Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents

- **检索号**：N-08　**类别**：N CUA 系统架构学术论文　**轮次**：第二轮
- **作者 / 机构**：Saaket Agashe、Kyle Wong、Vincent Tu 等（simular-ai/Agent-S 团队）
- **时间**：2025-04　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2504.00906>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：会议/期刊：未核实；arXiv 预印本 2025-04；页面量化成绩：OSWorld 15 步 / 50 步设置相对提升 18.9% / 32.7%，WindowsAgentArena 提升 52.8%，AndroidWorld 16.52%
- **页面依据**：a novel compositional framework that delegates cognitive responsibilities across various generalist and specialist models
- **要点**：用 Mixture-of-Grounding 精确 GUI 定位与主动分层规划（多时间尺度动态修正计划）把通用模型与专家模型组合，在真实桌面 GUI 上执行长时程任务；OSWorld 15/50 步相对 Claude Computer Use、UI-TARS 等基线提升 18.9%/32.7%，WindowsAgentArena 提升 52.8%。
- **与主题关联**：给出本地多模型分工 + 精确 grounding + 长时程重规划的 CUA 编排架构，并附可复现的 SOTA 量化数字。

#### 120｜Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?

- **检索号**：N-09　**类别**：N CUA 系统架构学术论文　**轮次**：第二轮
- **作者 / 机构**：Ruisheng Cao、Fangyu Lei、Haoyuan Wu 等（香港大学、上海交通大学、Google Cloud AI Research、Google DeepMind、Salesforce Research 等）
- **时间**：2024-07　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2407.10956>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：会议/期刊：未核实；arXiv 预印本 2024-07；页面量化成绩：494 个真实任务、20 个企业级应用，最佳模型 14.0% 成功率（含逐步引导 16.2%，远程云工作区 10.6%）
- **页面依据**：494 real-world tasks in authentic computer environments and incorporating 20 enterprise-level professional applications
- **要点**：基于 OSWorld 式可执行虚拟机环境，让智能体观察实时截图与无障碍树、写代码并操作 BigQuery / dbt / Airbyte 等 20 个企业软件 GUI，完成端到端数据工作流；494 个任务上最佳 VLM（GPT-4V）仅 14.0% 成功，含 oracle 逐步引导也只到 16.2%。
- **与主题关联**：展示本地真实桌面中「代码 + GUI + 云账号」混合长流程的落地形态与失败边界，是主动式 AI 编织多应用任务的压力测试。

#### 121｜TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks

- **检索号**：N-10　**类别**：N CUA 系统架构学术论文　**轮次**：第二轮
- **作者 / 机构**：Frank F. Xu、Yufan Song、Boxuan Li 等（TheAgentCompany 团队，作者含 Graham Neubig、Shuyan Zhou）
- **时间**：2024-12　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2412.14161>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：会议/期刊：未核实；arXiv 预印本 2024-12（v3 2025-09）；页面量化成绩：最强智能体可自主完成 30% 任务
- **页面依据**：an extensible benchmark for evaluating AI agents that interact with the world in similar ways to those of a digital worker: by browsing the Web, writing code, running programs, and communicating with other coworkers
- **要点**：搭建自包含的小型软件公司环境（内部网站、代码仓、数据与同事），让智能体以浏览网页、写代码、运行程序、与他人沟通的方式在真实工具链中完成职业任务；最强基线自主完成 30% 任务，更困难的长时程任务仍明显超出当前系统。
- **与主题关联**：提供本地可自托管的「数字员工」工作环境与跨工具长任务链，是家用机长期主动式 CUA 的场景模板。

#### 122｜OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks

- **检索号**：N-11（候补）　**类别**：N CUA 系统架构学术论文　**轮次**：第二轮
- **作者 / 机构**：Mengqi Yuan、Zilong Zhou、Xinzhuang Xiong 等（XLANG / OSWorld 团队，作者含 Tianbao Xie、Tao Yu、Xin Eric Wang）
- **时间**：2026-06　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2606.29537>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：会议/期刊：未核实；arXiv 预印本 2026-06（v2 2026-07）；页面量化成绩：108 个长时程工作流、平均 318 次工具调用（OSWorld 1.0 约 30 次），Claude Opus 4.8 完成 20.6%（部分得分 54.8%），GPT-5.5 约 13%
- **页面依据**：108 long-horizon computer-use workflows ... takes human users a median of about 1.6 hours to complete and requires an average of 318 tool calls
- **要点**：以真实输入工件、有状态用户画像与流式/动态交互构建 108 个端到端工作流（人类中位约 1.6 小时、平均 318 次工具调用），在真实桌面 OS 上评测前沿智能体的长时程执行；500 步预算下最佳 Claude Opus 4.8 仅完成 20.6%（部分得分 54.8%）。
- **与主题关联**：把 OSWorld 系列推进到长时程真实工作流（对应 OSWorld-V2 / Long-Horizon Computer Use），直接刻画本地 CUA 在数百步任务中的状态跟踪、约束保持与验证缺口。

### O 类｜GUI grounding 与屏幕视觉理解（12 篇）

#### 123｜UI-TARS: Pioneering Automated GUI Interaction with Native Agents

- **检索号**：O-01　**类别**：O GUI grounding 与屏幕视觉理解　**轮次**：第二轮
- **作者 / 机构**：Yujia Qin、Yining Ye、Junjie Fang 等（ByteDance / ByteDance-Seed；GitHub bytedance/UI-TARS、Hugging Face 命名空间 ByteDance-Seed、seed-tars.com）
- **时间**：2025-01　**类型**：官方技术报告
- **出处**：<https://arxiv.org/abs/2501.12326>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv:2501.12326（2025-01）；摘要给出 OSWorld 24.6（50 steps）与 22.7（15 steps），对比 Claude 的 22.0 与 14.9；AndroidWorld 46.6，对比 GPT-4o 的 34.5；并称在 10+ GUI agent benchmarks 上取得 SOTA（数字均来自 arXiv abs 页）
- **页面依据**：UI-TARS achieves SOTA performance in 10+ GUI agent benchmarks evaluating perception, grounding, and GUI task execution.
- **要点**：UI-TARS 是端到端原生 GUI 智能体，仅以截图为输入，通过大规模 GUI 截图数据做上下文感知的元素理解与精确 captioning，并用统一动作空间（Unified Action Modeling）标准化跨平台动作、借助大规模动作轨迹实现精确 grounding 与交互。摘要报告 OSWorld 24.6（50 步）/ 22.7（15 步）、AndroidWorld 46.6，均超过 Claude 与 GPT-4o 的对应分数。
- **与主题关联**：它把「截图 → 统一动作空间 → 鼠标/键盘坐标」做成单一可本地部署模型，使 CUA 无需 HTML/AXTree 即可把自然语言指令直接落到屏幕像素坐标。

#### 124｜CogAgent: A Visual Language Model for GUI Agents

- **检索号**：O-02　**类别**：O GUI grounding 与屏幕视觉理解　**轮次**：第二轮
- **作者 / 机构**：Wenyi Hong、Weihan Wang、Qingsong Lv 等（清华大学 KEG / 智谱 AI Zhipu AI；项目页 github.com/THUDM/CogAgent）
- **时间**：2023-12（CVPR 2024）　**类型**：会议论文
- **出处**：<https://arxiv.org/abs/2312.08914>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：CVPR 2024 (Highlight)（arXiv Comments 字段原文「CVPR 2024 (Highlight), 27 pages, 19 figures」）；摘要给出 18-billion-parameter 模型、1120×1120 输入分辨率，并称在 5 个 text-rich 与 4 个通用 VQA 基准上取得 SOTA
- **页面依据**：By utilizing both low-resolution and high-resolution image encoders, CogAgent supports input at a resolution of 1120*1120, enabling it to recognize tiny page elements and text.
- **要点**：CogAgent 用低分辨率与高分辨率双图像编码器，把 1120×1120 高分辨率屏幕送入 VLM，从而识别页面上的微小元素和文字，并仅凭截图在 Mind2Web、AITW 上超过消费 HTML 文本的 LLM 方法。摘要给出 18B 参数与 1120×1120 输入，并列出 VQAv2、Text-VQA、ST-VQA、ChartQA、DocVQA、MM-Vet、POPE 等 9 个 VQA 基准上的 SOTA。
- **与主题关联**：高分辨率双编码器让本地 PC 截图中的小图标与小字可被辨认，为 CUA 把语言指令定位到具体像素区域提供视觉底座。

#### 125｜SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents

- **检索号**：O-03　**类别**：O GUI grounding 与屏幕视觉理解　**轮次**：第二轮
- **作者 / 机构**：Kanzhi Cheng、Qiushi Sun、Yougang Chu 等（南京大学；项目页 github.com/njucckevin/SeeClick）
- **时间**：2024-01（ACL 2024）　**类型**：会议论文
- **出处**：<https://arxiv.org/abs/2401.10935>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv HTML 正文 Table 1 给出 ScreenSpot click accuracy 平均 53.4%（Mobile Text 78.0%、Desktop Text 72.2%、Web Text 55.7%），正文另有「surpasses the strong visual baseline Pix2Act while utilizing merely 0.3% training data」；GitHub 项目页 news 标注「seeclick is accepted by acl 2024」；并创建了首个 ScreenSpot 基准
- **页面依据**：we have discovered a key challenge in developing visual GUI agents: GUI grounding -- the capacity to accurately locate screen elements based on instructions.
- **要点**：SeeClick 首次把「按指令精确定位屏幕元素」的 GUI grounding 形式化为视觉 GUI 智能体的核心能力，通过 GUI grounding 预训练与自动化构造 grounding 数据，仅靠截图完成定位。arXiv HTML Table 1 报告其在自建 ScreenSpot 上 click accuracy 平均 53.4%，且仅用 Pix2Act 0.3% 训练数据即超越后者。
- **与主题关联**：它定义了「语言指令 → 屏幕元素坐标」这一 CUA 必备能力并给出 ScreenSpot 评测，使本地 PC 上的智能体可被训练为直接输出可点击的像素位置。

#### 126｜OmniParser for Pure Vision Based GUI Agent

- **检索号**：O-04　**类别**：O GUI grounding 与屏幕视觉理解　**轮次**：第二轮
- **作者 / 机构**：Yadong Lu、Jianwei Yang、Yelong Shen、Ahmed Awadallah（Microsoft Research / Microsoft Gen AI）
- **时间**：2024-08　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2408.00203>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv HTML 正文 Table 2 给出 ScreenSpot Average 73.0%（OmniParser w. LS + ID），对比 GPT-4V 基线 16.2%；正文另报告微调的可交互区域检测（ID）模型相对原始 Grounding DINO 再提升 4.3% overall accuracy（数字均来自 arXiv 正文页）
- **页面依据**：a comprehensive method for parsing user interface screenshots into structured elements, which significantly enhances the ability of GPT-4V to generate actions that can be accurately grounded in the corresponding regions of the interface.
- **要点**：OmniParser 用微调的可交互图标检测模型把截图解析为带边界框的结构化元素，再用 caption 模型赋予功能语义，从而让 GPT-4V 生成的动作准确落到对应屏幕区域。正文 Table 2 显示 ScreenSpot 平均准确率 73.0%（GPT-4V 仅 16.2%），其中 Mobile Text 93.9%、Desktop Text 91.3%。
- **与主题关联**：它把任意截图转成带框/编号的可交互元素列表，本地 PC 上的 CUA 只需选择元素即可换算成点击坐标，无需依赖后台 DOM/AXTree。

#### 127｜Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding in GPT-4V

- **检索号**：O-05　**类别**：O GUI grounding 与屏幕视觉理解　**轮次**：第二轮
- **作者 / 机构**：Jianwei Yang、Hao Zhang、Feng Li、Xueyan Zou、Chunyuan Li、Jianfeng Gao（Microsoft；项目页 github.com/microsoft/SoM）
- **时间**：2023-10　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2310.11441>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv:2310.11441（2023-10，Microsoft；GitHub microsoft/SoM 仓库标注「[arXiv 2023]」）；摘要称 zero-shot 的 GPT-4V+SoM 在 RefCOCOg 上超过 fully-finetuned 的 SOTA referring expression comprehension 与 segmentation 模型；页面未给出具体分数，量化数值未核实
- **页面依据**：we employ off-the-shelf interactive segmentation models, such as SEEM/SAM, to partition an image into regions at different levels of granularity, and overlay these regions with a set of marks e.g., alphanumerics, masks, boxes.
- **要点**：SoM 用 SAM/SEEM 把图像切成不同粒度的区域并叠加字母数字、掩码、框等标记，使 GPT-4V 能回答需要视觉 grounding 的问题；摘要报告其在 RefCOCOg 上 zero-shot 超过 fully-finetuned SOTA 模型。该「先打标记再按编号指代」的范式被后续 GUI/CUA 工作（OmniParser、OSWorld 中的 SoM 基线等）直接沿用。
- **与主题关联**：它提供把屏幕分区编号、再让模型以编号指代目标位置的通用机制，使本地 PC CUA 可以把语言指令解析为带标记区域并还原成像素坐标。

#### 128｜ScreenAI: A Vision-Language Model for UI and Infographics Understanding

- **检索号**：O-06　**类别**：O GUI grounding 与屏幕视觉理解　**轮次**：第二轮
- **作者 / 机构**：Gilles Baechler、Srinivas Sunkara、Maria Wang 等（Google DeepMind；PDF 作者行标注 google deepmind）
- **时间**：2024-02（IJCAI 2024）　**类型**：会议论文
- **出处**：<https://arxiv.org/abs/2402.04615>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：IJCAI 2024（arXiv Comments 字段原文「Accepted to International Joint Conference on Artificial Intelligence (IJCAI), 2024」）；摘要给出仅 5B 参数即在 Multi-page DocVQA、WebSRC、MoTIF、Widget Captioning 上取得 new state-of-the-art，并在 Chart QA、DocVQA、InfographicVQA 上取得 best-in-class
- **页面依据**：At the heart of this mixture is a novel screen annotation task in which the model has to identify the type and location of UI elements.
- **要点**：ScreenAI 在 PaLI 架构上引入 pix2struct 的灵活 patching 策略，以「识别 UI 元素的类型与位置」的 screen annotation 任务为核心预训练，再把生成的文本标注用于大规模构建 QA、导航与摘要数据。摘要报告仅 5B 参数即在 WebSRC、MoTIF、Widget Captioning 等 UI 任务上取得新 SOTA。
- **与主题关联**：其 screen annotation 任务直接输出元素类型与位置，是把屏幕语言描述转成可定位区域、进而落到本地 PC 像素坐标的关键预训练范式。

#### 129｜Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs

- **检索号**：O-07　**类别**：O GUI grounding 与屏幕视觉理解　**轮次**：第二轮
- **作者 / 机构**：Keen You、Haotian Zhang、Eldon Schoop、Floris Weers 等（Apple；arXiv HTML 作者行 Affiliation: Apple）
- **时间**：2024-04　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2404.05719>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv HTML 正文 Table 2 给出 Ferret-UI-anyres 在 iPhone / Android grounding 任务（Grd-i / Grd-A）为 81.4 / 83.8，对比 GPT-4V 的 70.3 / 4.7；grounded conversation 输出框准确率 Ferret-UI 91.7%（GPT-4V 93.4%）；摘要另称 surpasses GPT-4V on all the elementary UI tasks
- **页面依据**：we present Ferret-UI, a new MLLM tailored for enhanced understanding of mobile UI screens, equipped with referring, grounding, and reasoning capabilities.
- **要点**：Ferret-UI 在 Ferret 之上加入「any resolution」，按屏幕长宽比把细长 UI 截成两个子图分别编码以放大小图标/小字，并用带区域标注的指令数据训练 referring 与 grounding。正文 Table 2 显示其 Android grounding 达 83.8，远高于 GPT-4V 的 4.7；grounded conversation 输出框准确率 91.7%。
- **与主题关联**：any-resolution 切图加区域标注训练让模型从细长、密集的屏幕中精确回归元素框，为本地 PC 上高分辨率桌面截图的像素级定位提供可迁移方案。

#### 130｜Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction

- **检索号**：O-08　**类别**：O GUI grounding 与屏幕视觉理解　**轮次**：第二轮
- **作者 / 机构**：Yiheng Xu、Zekun Wang、Junli Wang、Dunjie Lu、Tianbao Xie、Tao Yu 等（University of Hong Kong / Salesforce Research）
- **时间**：2024-12（ICML 2025）　**类型**：会议论文
- **出处**：<https://arxiv.org/abs/2412.04454>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：ICML 2025（arXiv Comments 字段原文「ICML 2025」）；arXiv 正文 Table 1 给出 ScreenSpot 平均准确率 Aguvis-72B 89.2、Aguvis-7B 84.4（对比 SeeClick 53.4、GPT-4o 18.3），正文 Remark 给出 OSWorld 任务成功率 17.04%（对比 GPT-4o+SoM 4.59%、Claude Computer-Use 14.9）
- **页面依据**：we construct Aguvis Data Collection, a large-scale dataset with multimodal grounding and reasoning annotations, and develop a two-stage training pipeline that separates GUI grounding from planning and reasoning.
- **要点**：Aguvis 构建带 grounding 与推理标注的大规模数据集，用两阶段训练把 GUI grounding 与规划/推理解耦，配合 inner monologue 实现首个不依赖闭源模型的纯视觉自主 GUI 智能体。正文 Table 1 报告 Aguvis-72B 在 ScreenSpot 平均 89.2、Aguvis-7B 84.4，OSWorld 任务成功率 17.04%。
- **与主题关联**：把 grounding 作为独立可训练阶段，使本地 PC 上的 CUA 能先把语言指令精确落到元素坐标，再复用同一模型做跨桌面应用的规划与执行。

#### 131｜ShowUI: One Vision-Language-Action Model for GUI Visual Agent

- **检索号**：O-09　**类别**：O GUI grounding 与屏幕视觉理解　**轮次**：第二轮
- **作者 / 机构**：Kevin Qinghong Lin、Linjie Li、Difei Gao、Zhengyuan Yang 等（Show Lab @ National University of Singapore / Microsoft；GitHub 项目页）
- **时间**：2024-11（CVPR 2025）　**类型**：会议论文
- **出处**：<https://arxiv.org/abs/2411.17465>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：CVPR 2025（GitHub showlab/ShowUI 仓库标题「[CVPR 2025]」、更新日志原文「ShowUI has been accepted to CVPR 2025」）；摘要给出 2B 模型、256K 数据、zero-shot screenshot grounding 75.1% 准确率，以及 UI-guided token selection 减少 33% 冗余视觉 token、加速 1.4x（数字来自 arXiv abs 页）
- **页面依据**：UI-Guided Visual Token Selection to reduce computational costs by formulating screenshots as an UI connected graph, adaptively identifying their redundant relationship and serve as the criteria for token selection during self-attention blocks
- **要点**：ShowUI 把截图建模为 UI 连通图，据此在自注意力中做 UI 引导的视觉 token 选择、去掉冗余 patch，再以交错的视觉-语言-动作流统一导航与 grounding 训练。摘要报告 2B 模型用 256K 数据取得 75.1% zero-shot screenshot grounding，并减少 33% 冗余视觉 token、加速 1.4x。
- **与主题关联**：轻量 2B 模型与 token 剪枝让高分辨率桌面截图可在本地实时编码，输出的动作可直接换算成 PC 屏幕上的点击坐标。

#### 132｜Aria-UI: Visual Grounding for GUI Instructions

- **检索号**：O-10　**类别**：O GUI grounding 与屏幕视觉理解　**轮次**：第二轮
- **作者 / 机构**：Yuhao Yang、Yue Wang、Dongxu Li、Ziyang Luo、Junnan Li 等（The University of Hong Kong / Alibaba Group / Salesforce AI Research / Australian National University）
- **时间**：2024-12（ACL 2025）　**类型**：会议论文
- **出处**：<https://arxiv.org/abs/2412.16256>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：ACL 2025（arXiv Comments 字段原文「ACL 2025」）；arXiv 正文 Table 2 给出 ScreenSpot 平均 element accuracy 82.4%（对比 GPT-4o 18.1%、SeeClick 55.8%、UGround 74.1%），Table 6 给出 OSWorld 平均任务成功率 15.15%（数字来自 arXiv 正文页）
- **页面依据**：we introduce Aria-UI, a large multimodal model specifically designed for GUI grounding. Aria-UI adopts a pure-vision approach, eschewing reliance on auxiliary inputs.
- **要点**：Aria-UI 是专为 GUI grounding 设计的纯视觉多模态模型，用可扩展数据管线合成多样化指令样本，并引入文本与图文交错的动作历史以处理动态上下文。正文 Table 2 报告 ScreenSpot 平均 82.4%（GPT-4o 仅 18.1%），Table 6 报告 OSWorld 任务成功率 15.15%。
- **与主题关联**：纯视觉、不依赖 HTML/AXTree，直接把规划器给出的语言指令映射为屏幕元素框，是本地 PC 上「截图即输入、坐标即输出」的 CUA 典型 grounding 模块。

#### 133｜ScreenSpot-Pro: GUI Grounding for Professional High-Resolution Computer Use

- **检索号**：O-11（候补）　**类别**：O GUI grounding 与屏幕视觉理解　**轮次**：第二轮
- **作者 / 机构**：Kaixin Li、Ziyang Meng、Hongzhan Lin、Ziyang Luo、Yuchen Tian、Jing Ma、Zhiyong Huang、Tat-Seng Chua（National University of Singapore / East China Normal University / Hong Kong Baptist University 等）
- **时间**：2025-04（ACM MM 2025）　**类型**：会议论文
- **出处**：<https://arxiv.org/abs/2504.07981>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：ACM Multimedia 2025（百度学术条目给出「MM 25: ACM International Conference on Multimedia - 2025」、DOI 10.1145/3746027.3755688、pp. 8778–8786）；arXiv 摘要给出覆盖 23 个应用、5 个行业、3 个操作系统，现有最佳模型仅 18.9%，所提 ScreenSeekeR 免训练达 48.1%（数字来自 arXiv abs 页）
- **页面依据**：we introduce ScreenSpot-Pro, a new benchmark designed to rigorously evaluate the grounding capabilities of MLLMs in high-resolution professional settings.
- **要点**：ScreenSpot-Pro 针对专业软件的高分辨率屏幕、小目标与复杂界面构建 grounding 基准，覆盖 23 个应用、5 个行业、3 个操作系统，并配有专家标注；摘要指出现有最佳模型仅 18.9%，并据此提出用强规划器的 GUI 知识引导级联搜索的 ScreenSeekeR，免训练达到 48.1%。
- **与主题关联**：它专门刻画 Windows/macOS/Linux 桌面专业软件上的像素级定位难度，为本地 PC CUA 的 grounding 能力提供可核验的评测标尺与「缩小搜索区域」的定位思路。

#### 134｜UI-R1: Enhancing Efficient Action Prediction of GUI Agents by Reinforcement Learning

- **检索号**：O-12（候补）　**类别**：O GUI grounding 与屏幕视觉理解　**轮次**：第二轮
- **作者 / 机构**：Zhengxi Lu、Yuxiang Chai、Yaxuan Guo、Hongsheng Li 等（vivo AI Lab / 香港中文大学）
- **时间**：2025-03　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2503.21620>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv:2503.21620；摘要给出仅 136 个高质量任务、覆盖 5 类移动端常见动作，UI-R1-3B 相对基座 Qwen2.5-VL-3B 在 ScreenSpot 平均准确率 +22.1%、ScreenSpot-Pro +6.0%、ANDROIDCONTROL +12.7%（数字均来自 arXiv abs 页）
- **页面依据**：UI-R1 introduces a novel rule-based action reward, enabling model optimization via policy-based algorithms such as Group Relative Policy Optimization (GRPO).
- **要点**：UI-R1 首次把 DeepSeek-R1 式基于规则奖励的强化学习引入 GUI 动作预测，用 136 个任务的小样本集与 GRPO 优化，使 3B 模型同时提升 grounding 与动作预测，并可与用 76K 样本 SFT 的 OS-Atlas-7B 竞争。摘要给出相对基座在 ScreenSpot +22.1%、ScreenSpot-Pro +6.0%、ANDROIDCONTROL +12.7% 的平均准确率增益。
- **与主题关联**：以规则奖励直接优化「预测坐标是否命中元素」，让本地 PC 上的小模型 CUA 能用极少数据把语言指令更准地落到像素坐标。

### P 类｜浏览器 / Web 智能体（12 篇）

#### 135｜Mind2Web: Towards a Generalist Agent for the Web

- **检索号**：P-01　**类别**：P 浏览器 / Web 智能体　**轮次**：第二轮
- **作者 / 机构**：Xiang Deng、Yu Gu、Boyuan Zheng、Huan Sun、Yu Su 等（Ohio State University，OSU NLP Group；项目页 osu-nlp-group.github.io/Mind2Web）
- **时间**：2023　**类型**：会议论文（NeurIPS 2023 Spotlight）
- **出处**：<https://arxiv.org/abs/2306.06070>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：NeurIPS'23 Spotlight（arXiv Comments 字段原文「NeurIPS'23 Spotlight」）；首个面向任意真实网站的通用 Web Agent 数据集，2,000+ 任务、137 个网站、31 个领域（摘要）
- **页面依据**：We introduce Mind2Web, the first dataset for developing and evaluating generalist agents for the web
- **要点**：从 137 个真实网站、31 个领域收集 2,000+ 开放式任务及众包动作序列，用小型 LM 先过滤原始 HTML 再交 LLM 生成动作，以支持跨网站、跨域泛化。摘要给出「over 2,000 open-ended tasks collected from 137 websites spanning 31 domains」，并说明该方案在未见过的网站乃至整个领域上仍有一定效果但距真正通用仍有差距。
- **与主题关联**：确立「真实 DOM/HTML → LLM → 动作」的通用网页操控范式，是本地 PC 上浏览器型 CUA 训练与评测的基础数据集。

#### 136｜WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents

- **检索号**：P-02　**类别**：P 浏览器 / Web 智能体　**轮次**：第二轮
- **作者 / 机构**：Shunyu Yao、Howard Chen、John Yang、Karthik Narasimhan 等（Princeton University，Department of Computer Science；PDF 署名）
- **时间**：2022　**类型**：会议论文（NeurIPS 2022，v3 为 camera ready）
- **出处**：<https://arxiv.org/abs/2207.01206>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：NeurIPS 2022（arXiv Comments「v3 is NeurIPS camera ready version」）；1.18 million 真实商品、12,087 条众包指令，最佳模型 29% 成功率 vs 规则启发式 9.6% vs 人类专家 59%（摘要）
- **页面依据**：a simulated e-commerce website environment with 1.18 million real-world products and 12,087 crowd-sourced text instructions
- **要点**：构建含 118 万真实商品与 12,087 条文本指令的模拟电商环境，智能体须跨多类型网页搜索、定制并下单，用可自动计算的奖励替代人工评判。收集 1,600+ 人类示范并训练 RL/模仿学习/预训练模型，最佳模型任务成功率 29%，且展示到 amazon、ebay 的非平凡 sim-to-real 迁移。
- **与主题关联**：定义了「多页面点击/输入 + 自动奖励」的网页交互闭环，是本地浏览器 CUA 决策与语言接地最经典的可复现基准。

#### 137｜WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models

- **检索号**：P-03　**类别**：P 浏览器 / Web 智能体　**轮次**：第二轮
- **作者 / 机构**：Hongliang He、Wenlin Yao、Kaixin Ma、Dong Yu 等（腾讯 AI Lab 为公开作者隶属；arXiv abs 页未显式标注机构）
- **时间**：2024　**类型**：会议论文（ACL 2024 主会）
- **出处**：<https://arxiv.org/abs/2401.13919>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：ACL 2024 主会（arXiv Comments「Accepted to ACL 2024 (main)」）；15 个真实网站任务上 59.1% 任务成功率，GPT-4V 自动评测与人类判断一致率 85.3%（摘要）
- **页面依据**：We show that WebVoyager achieves a 59.1% task success rate on our benchmark
- **要点**：以大型多模态模型端到端操控真实网站，从 15 个热门网站编译真实任务，并首次用 GPT-4V 的多模态理解对开放式 Web Agent 做自动评测。59.1% 成功率显著超过 GPT-4 (All Tools) 与纯文本 WebVoyager，自动指标与人类判断一致率达 85.3%。
- **与主题关联**：验证「截图 + 文本」多模态闭环在真实网站上端到端执行，直接对应本地 PC 上驱动真实浏览器的 CUA 形态。

#### 138｜A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis

- **检索号**：P-04　**类别**：P 浏览器 / Web 智能体　**轮次**：第二轮
- **作者 / 机构**：Izzeddin Gur、Hiroki Furuta、Austin Huang、Aleksandra Faust 等（Google DeepMind / University of Tokyo 为公开作者隶属；arXiv abs 页未显式标注机构）
- **时间**：2023　**类型**：会议论文（ICLR 2024 Oral）
- **出处**：<https://arxiv.org/abs/2307.12856>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：ICLR 2024 Oral（arXiv Comments「Accepted to ICLR 2024 (Oral)」）；真实网站成功率提升「over 50%」，HTML-T5 在 MiniWoB 上比此前方法高 18.7% 成功率，并在 Mind2Web 取得 SoTA（摘要）
- **页面依据**：we introduce WebAgent, an LLM-driven agent that learns from self-experience to complete tasks on real websites following natural language instructions
- **要点**：将指令分解为规范子指令、把长 HTML 文档摘要成任务相关片段，并用 Flan-U-PaLM 生成 Python 程序在真实网站执行；HTML-T5 以局部/全局注意力处理长 HTML。模块式配方使真实网站成功率提升超 50%，MiniWoB 上高出 18.7%，Mind2Web 离线规划评测达 SoTA。
- **与主题关联**：给出「规划 + 长上下文压缩 + 程序化动作」的可执行 Web Agent 架构，适合在本地浏览器上把自然语言转成具体操作。

#### 139｜VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks

- **检索号**：P-05　**类别**：P 浏览器 / Web 智能体　**轮次**：第二轮
- **作者 / 机构**：Jing Yu Koh、Robert Lo、Graham Neubig、Ruslan Salakhutdinov、Daniel Fried 等（Carnegie Mellon University 为公开作者隶属；arXiv abs 页未显式标注机构）
- **时间**：2024　**类型**：会议论文（ACL 2024）
- **出处**：<https://arxiv.org/abs/2401.13649>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：ACL 2024 主会（arXiv Comments「Accepted to ACL 2024」）；代码、基线模型与数据公开于项目页 jykoh.com/vwa；具体成功率数值未在 abs 页给出，未核实
- **页面依据**：we introduce VisualWebArena, a benchmark designed to assess the performance of multimodal web agents on realistic visually grounded tasks
- **要点**：构建以视觉为基础的真实网页任务基准，要求智能体处理图文输入、理解自然语言指令并在网站上执行动作。系统评测多种 SOTA LLM 与多模态智能体，揭示纯文本智能体的局限及多模态语言智能体的能力缺口（摘要未列具体成功率数值）。
- **与主题关联**：强调「截图 + 视觉定位」对网页操作的必要性，是本地 PC 上基于屏幕/视觉的浏览器 CUA 的关键评测依据。

#### 140｜WebLINX: Real-World Website Navigation with Multi-Turn Dialogue

- **检索号**：P-06　**类别**：P 浏览器 / Web 智能体　**轮次**：第二轮
- **作者 / 机构**：Xing Han Lù、Zdeněk Kasner、Siva Reddy 等（McGill University / Mila；项目页 mcgill-nlp.github.io/weblinx）
- **时间**：2024　**类型**：arXiv 预印本（v1 2024-02，v2 2024-09）
- **出处**：<https://arxiv.org/abs/2402.05930>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：基准规模 100K interactions、2,300 条专家示范、覆盖 150+ 真实网站（摘要）；实验发现小型微调解码器超过包括 GPT-4V 在内的最佳零样本 LLM（摘要）
- **页面依据**：a large-scale benchmark of 100K interactions across 2300 expert demonstrations of conversational web navigation
- **要点**：提出「对话式网页导航」，以检索式模型高效裁剪 HTML 页面、结合截图与动作历史复现人类浏览行为。覆盖 150+ 真实网站、100K 交互与 2,300 条专家示范；结果显示微调小模型优于零样本 GPT-4V，但所有微调模型对未见网站泛化仍困难。
- **与主题关联**：把浏览器操控建模为「多轮人机对话 + DOM 裁剪」，支撑本地 PC 上可交互、可监督的浏览器型 CUA。

#### 141｜Reinforcement Learning on Web Interfaces Using Workflow-Guided Exploration

- **检索号**：P-07　**类别**：P 浏览器 / Web 智能体　**轮次**：第二轮
- **作者 / 机构**：Evan Zheran Liu、Kelvin Guu、Panupong Pasupat、Tianlin Shi、Percy Liang 等（Stanford University；项目页 stanfordnlp.github.io/wge）
- **时间**：2018　**类型**：会议论文（ICLR 2018）
- **出处**：<https://arxiv.org/abs/1802.08802>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：ICLR 2018（arXiv Comments「International Conference on Learning Representations (ICLR), 2018」）；MiniWoB++ 官方 Farama 文档载「over 100 web interaction environments」；工作流引导探索较行为克隆样本效率提升「more than 100x」（摘要）
- **页面依据**：MiniWoB++ is an extension of the OpenAI MiniWoB benchmark, and was introduced in the paper Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration（官方文档 https://miniwob.farama.org/）；workflow-guided exploration improves sample efficiency over behavioral cloning by more than 100x（arXiv 摘要）
- **要点**：从示教诱导高层「工作流」约束稀疏奖励下的探索，训练可处理半结构化网页的神经策略，评估于 World of Bits / MiniWoB++ 任务集。官方 Farama 文档确认 MiniWoB++ 含 100+ 网页交互环境，基于 Selenium WebDriver 与 Gymnasium API，可在本地直接运行。
- **与主题关联**：提供本地可运行的浏览器微任务沙盒（Selenium/Gymnasium），是训练与调试本地 PC 网页操控策略的基础环境，也是后续众多 CUA 工作的底层基准。

#### 142｜WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?

- **检索号**：P-08　**类别**：P 浏览器 / Web 智能体　**轮次**：第二轮
- **作者 / 机构**：Alexandre Drouin、Maxime Gasse、Massimo Caccia、Alexandre Lacoste 等（ServiceNow Research / Mila；GitHub ServiceNow/WorkArena）
- **时间**：2024　**类型**：会议论文（ICML 2024）
- **出处**：<https://arxiv.org/abs/2403.07718>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：ICML 2024（来源：ServiceNow/WorkArena GitHub 页标注 [ICML 2024]；arXiv Comments 字段标「preprint」）；基于 ServiceNow 平台的 33 个任务（摘要），并同时引入 BrowserGym 环境（摘要）
- **页面依据**：we propose WorkArena, a remote-hosted benchmark of 33 tasks based on the widely-used ServiceNow platform. We also introduce BrowserGym, an environment for the design and evaluation of such agents
- **要点**：以企业知识工作者日常任务为对象，构建 33 个基于 ServiceNow 平台的浏览器任务，并提出 BrowserGym 环境提供丰富动作与多模态观测（其生态扩展见 arXiv:2412.05467《The BrowserGym Ecosystem for Web Agent Research》，已核验，含 AgentLab 框架）。评测显示当前智能体距完全自动化仍有明显差距，且开源与闭源 LLM 性能差异显著。
- **与主题关联**：把「本地浏览器 + 企业软件网页」定义为可复现的动作/观测空间与任务集，是办公 PC 上浏览器型 CUA 及其评测框架（BrowserGym/AgentLab）的源头。

#### 143｜WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks

- **检索号**：P-09　**类别**：P 浏览器 / Web 智能体　**轮次**：第二轮
- **作者 / 机构**：Léo Boisvert、Megh Thakkar、Maxime Gasse、Alexandre Drouin 等（ServiceNow Research / Mila；GitHub ServiceNow/WorkArena）
- **时间**：2024　**类型**：会议论文（NeurIPS 2024）
- **出处**：<https://arxiv.org/abs/2407.05291>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：NeurIPS 2024（来源：ServiceNow/WorkArena GitHub 页标注 [NeurIPS 2024]；arXiv:2508.13024 引文标「Advances in Neural Information Processing Systems 37 (2024), 5996–6051」）；682 个任务（摘要）
- **页面依据**：we propose WorkArena++, a novel benchmark consisting of 682 tasks corresponding to realistic workflows routinely performed by knowledge workers
- **要点**：构建 682 个对应真实知识工作流的组合式任务，专门评测规划、解题、逻辑/算术推理、检索与上下文理解；同时提供可轻松生成数千条 ground-truth 观察/动作轨迹的机制用于微调。实验覆盖 SOTA LLM、VLM 及人类工作者。
- **与主题关联**：以「多步组合任务 + 可自动生成动作轨迹」刻画本地 PC 上浏览器型 CUA 的规划与执行能力，并可直接产出训练数据。

#### 144｜AgentOccam: A Simple Yet Strong Baseline for LLM-Based Web Agents

- **检索号**：P-10　**类别**：P 浏览器 / Web 智能体　**轮次**：第二轮
- **作者 / 机构**：Ke Yang、Yao Liu、Sapana Chaudhary、Rasool Fakoor、Huzefa Rangwala 等（arXiv abs 页未标注机构）
- **时间**：2024　**类型**：arXiv 预印本（v1 2024-10，v2 2025-05）
- **出处**：<https://arxiv.org/abs/2410.13825>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：WebArena 上超越此前 SOTA 9.8 个绝对点（+29.4%）、超越同期工作 5.9 点（+15.8%），较同类朴素 Web Agent 成功率提升 26.6 点（+161%）（摘要）
- **页面依据**：our agent AgentOccam surpasses the previous state-of-the-art and concurrent work by 9.8 (+29.4%) and 5.9 (+15.8%) absolute points respectively
- **要点**：不增加复杂智能体策略，仅通过裁剪非必要动作、精简并重排网页观察、引入 branch/prune 两个规划动作来对齐 LLM 的观察/动作空间。在 WebArena 的 812 个任务、5 个网站上取得上述提升，且不使用上下文示例、在线搜索、专用提示模板或智能体角色。
- **与主题关联**：说明「观察/动作空间对齐」这一轻量工程手段即可大幅提升网页操控成功率，对本地 PC 上以纯 LLM 驱动浏览器的实现最具直接借鉴价值。

#### 145｜Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents

- **检索号**：P-11　**类别**：P 浏览器 / Web 智能体　**轮次**：第二轮
- **作者 / 机构**：Yu Gu、Kai Zhang、Yuting Ning、Boyuan Zheng、Huan Sun、Yu Su 等（Ohio State University, OSU NLP Group 为公开作者隶属；arXiv abs 页未显式标注机构）
- **时间**：2024　**类型**：arXiv 预印本（v1 2024-11，v2 2025-04）
- **出处**：<https://arxiv.org/abs/2411.06559>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：摘要给出在 VisualWebArena 沙盒中以 4-5 倍效率达到与树搜索相当的效果，并在 Online-Mind2Web、Mind2Web-Live 真实网站有效；训练的世界模型 Dreamer-7B 表现与 GPT-4o 相当；会议/录用信息未在页面给出，未核实
- **页面依据**：It is competitive, while being 4-5 times more efficient, with tree search in sandbox environments (VisualWebArena)
- **要点**：（候补）用 LLM 同时充当世界模型与价值函数，在提交动作前先模拟并评估候选动作结果，规避真实网站上不可逆动作无法回溯的问题，并训练专用世界模型 Dreamer-7B。在 VisualWebArena 上以 4-5 倍效率达到与树搜索相当的效果，Dreamer-7B 表现接近 GPT-4o。
- **与主题关联**：（候补）为本地浏览器 CUA 提供「先在模型里推演、再落到真实网页」的高效规划范式，减少真实 PC 操作中的不可逆误动作。

#### 146｜Human Quickstart - Browser Use（Browser Use 官方文档）

- **检索号**：P-12　**类别**：P 浏览器 / Web 智能体　**轮次**：第二轮
- **作者 / 机构**：Browser Use 开源组织（github.com/browser-use/browser-use；Magnus Müller、Gregor Zunic 创建）
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://docs.browser-use.com/open-source/quickstart>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：GitHub 仓库 browser-use/browser-use stargazers_count = 120,180、forks_count = 13,407、MIT License（来源：GitHub REST API https://api.github.com/repos/browser-use/browser-use，updated_at 2026-11-06T10:25:24Z，核验日期 2026-11-06）
- **页面依据**：Install and run your first AI browser agent in minutes（出处页原文）；For a local agent, use the open-source library（官方文档 cloud/quickstart 页原文）
- **要点**：（候补）给出在本地安装 browser-use 与 Chromium、配置 LLM API key、以 `Agent(task=..., llm=...)` 直接驱动本地浏览器的最小可运行流程，并支持自定义浏览器、多种 LLM 及 `@sandbox` 生产部署。仓库自述为「The open-source browser agent.」，MIT 许可。
- **与主题关联**：（候补）是本地 PC 上「云端 LLM API + 本机浏览器」这一浏览器型 CUA 最直接的官方实现文档，对应主动式 AI 在本机落地的工程入口。

### Q 类｜移动端 / Android GUI 智能体（12 篇）

#### 147｜AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents

- **检索号**：Q-01　**类别**：Q 移动端 / Android GUI 智能体　**轮次**：第二轮
- **作者 / 机构**：Christopher Rawles、Sarah Clinckemaillie、Yifan Chang、Jonathan Waltz、Oriana Riva 等（Google DeepMind、Google；官方项目页标注 "1 Google DeepMind 2 Google"）
- **时间**：2024-05（v1 2024-05-23；ICLR 2025）　**类型**：会议论文（ICLR 2025 Poster）+ 官方仓库
- **出处**：<https://arxiv.org/abs/2405.14573>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：ICLR 2025 Poster（iclr.cc 页面标注 "2025 Poster"，访问 2026-11-06）；arXiv abs 与官方项目页给出 "116 programmatic tasks across 20 real-world Android apps" 及最佳 agent "30.6%"（访问 2026-11-06）
- **页面依据**："We present AndroidWorld, a fully functional Android environment that provides reward signals for 116 programmatic tasks across 20 real-world Android apps."；"Our best agent can complete 30.6% of AndroidWorld's tasks, leaving ample room for future work."；项目页 "📝 116 diverse tasks across 20 real-world apps"
- **要点**：构建可动态参数化、以设备系统状态给出奖励信号的 Android 环境，116 个任务覆盖 20 个真实 app，每个任务含初始化、成功判定与清理逻辑。基线 M3A 仅完成 30.6% 任务，且把桌面 web agent 迁移到 Android 后效果更差，说明跨平台通用 agent 仍未解决。
- **与主题关联**：为家用机通过 adb / 模拟器控制 Android 提供可复现任务集与系统状态级成功判定，是本地 CUA 控制移动端的标准评测底座。

#### 148｜Android in the Wild: A Large-Scale Dataset for Android Device Control

- **检索号**：Q-02　**类别**：Q 移动端 / Android GUI 智能体　**轮次**：第二轮
- **作者 / 机构**：Christopher Rawles、Alice Li、Daniel Rodriguez、Oriana Riva、Timothy Lillicrap（Google Research；数据集托管于 google-research/google-research 仓库）
- **时间**：2023-07　**类型**：arXiv 预印本（数据集论文）
- **出处**：<https://arxiv.org/abs/2307.10088>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv abs 页给出 "715k episodes spanning 30k unique instructions"、four versions of Android (v10-13)、eight device types（访问 2026-11-06）；被后续 AndroidWorld、AndroidControl 等作为对照数据集
- **页面依据**："It consists of 715k episodes spanning 30k unique instructions, four versions of Android (v10-13),and eight device types (Pixel 2 XL to Pixel 6) with varying screen resolutions."；"We present a dataset for device-control research, Android in the Wild (AITW), which is orders of magnitude larger than current datasets."
- **要点**：发布数量级远超以往的设备控制数据集，含屏幕、动作与对应自然语言指令，动作空间为精确手势（如横向滚动）而非 UI 元素级操作。论文给出两个基线 agent 在数据集上的表现，并按新指令、新应用、新平台版本组织鲁棒性分析。
- **与主题关联**：为本地 CUA 训练/微调「看截图 → 出 adb 手势」策略提供大规模真人演示数据，覆盖多机型与多 Android 版本。

#### 149｜On the Effects of Data Scale on UI Control Agents（v1 原题 On the Effects of Data Scale on Computer Control Agents）

- **检索号**：Q-03　**类别**：Q 移动端 / Android GUI 智能体　**轮次**：第二轮
- **作者 / 机构**：Wei Li、William Bishop、Alice Li、Chris Rawles、Folawiyo Campbell-Ajala、Divya Tyamagundlu、Oriana Riva（Google DeepMind / Google；据 arXiv PDF 首页 "1 Google DeepMind 2 Google"）
- **时间**：2024-06　**类型**：会议论文（NeurIPS 2024 Datasets and Benchmarks Track）
- **出处**：<https://arxiv.org/abs/2406.03679>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv abs 页 Comments 字段 "NeurIPS 2024 (Datasets and Benchmarks)"；同页给出 "15,283 demonstrations"、"14,548 unique tasks over 833 Android apps"（访问 2026-11-06）
- **页面依据**："we collect and release a new dataset, AndroidControl, consisting of 15,283 demonstrations of everyday tasks with Android apps."；"AndroidControl is the most diverse computer control dataset to date, including 14,548 unique tasks over 833 Android apps"；"Comments: NeurIPS 2024 (Datasets and Benchmarks)"
- **要点**：发布同时含高层与低层人工指令的 AndroidControl 数据集（15,283 条演示、14,548 个唯一任务、833 个 app），用其研究微调数据规模对域内/域外性能的影响。结论是域内随数据增加可持续提升，域外尤其高层任务仅靠加数据不足以稳健。
- **与主题关联**：给出「高低层指令 → 可执行动作」的成对监督数据，可用于家用机侧本地 agent 的指令分解与动作映射训练。

#### 150｜Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration

- **检索号**：Q-04　**类别**：Q 移动端 / Android GUI 智能体　**轮次**：第二轮
- **作者 / 机构**：Junyang Wang、Haiyang Xu、Haitao Jia、Xi Zhang、Ming Yan、Weizhou Shen、Ji Zhang、Fei Huang、Jitao Sang（阿里巴巴集团通义实验室 Tongyi Lab；官方仓库 X-PLUG/MobileAgent）
- **时间**：2024-06　**类型**：arXiv 预印本（官方仓库 README 标注该版本为 NeurIPS 2024）
- **出处**：<https://arxiv.org/abs/2406.01014>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv abs 页给出 "over a 30% improvement in task completion compared to the single-agent architecture of Mobile-Agent"（访问 2026-11-06）；官方仓库页显示 "9.4k stars"（GitHub X-PLUG/MobileAgent，访问 2026-11-06）；仓库 README 标注 "Mobile-Agent-v2 (NeurIPS 2024)"
- **页面依据**："Experimental results indicate that Mobile-Agent-v2 achieves over a 30% improvement in task completion compared to the single-agent architecture of Mobile-Agent."；"The code is open-sourced at this https URL (https://github.com/X-PLUG/MobileAgent)."
- **要点**：用 planning / decision / reflection 三智能体加随任务进度更新的记忆单元，缓解长 token 序列与图文交错输入导致的任务进度导航、焦点内容导航难题。相较单智能体 Mobile-Agent 任务完成率提升超过 30%，代码开源于 X-PLUG/MobileAgent。
- **与主题关联**：多智能体分工（规划/决策/反思）可迁移到家用机侧编排本机手机/模拟器的长程操作，减少上下文丢失导致的误操作。

#### 151｜AppAgent: Multimodal Agents as Smartphone Users

- **检索号**：Q-05　**类别**：Q 移动端 / Android GUI 智能体　**轮次**：第二轮
- **作者 / 机构**：Chi Zhang、Zhao Yang、Jiaxuan Liu、Yucheng Han、Xin Chen、Zebiao Huang、Bin Fu、Gang Yu（Tencent；官方项目页标注 "Tencent"）
- **时间**：2023-12　**类型**：会议论文（CHI 2025）
- **出处**：<https://arxiv.org/abs/2312.13771>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv abs 页 Comments "Accepted to CHI 2025, project page is this https URL"；同页给出 "50 tasks in 10 different applications"（访问 2026-11-06）
- **页面依据**："we conducted extensive testing over 50 tasks in 10 different applications"；"This novel approach bypasses the need for system back-end access"；项目页 "2023.12.26: Andriod emulator is supported for AppAgent!"；项目页 "CHI 2025" 与 "Tencent"
- **要点**：以简化动作空间（tap / swipe）模仿人类操作，通过自主探索或观察人类演示生成 app 知识库，再据此执行跨 app 高层任务，不依赖系统后端访问。在 10 个应用的 50 个任务上验证；官方项目页注明支持 Android emulator 与「网格叠加任意点按/滑动」。
- **与主题关联**：是 adb 驱动 GUI 智能体的标志性工作，其「纯前端手势 + 免 XML/后端」路线与模拟器支持，直接对应家用机在本机控制手机/模拟器的实现路径。

#### 152｜AutoDroid: LLM-powered Task Automation in Android

- **检索号**：Q-06　**类别**：Q 移动端 / Android GUI 智能体　**轮次**：第二轮
- **作者 / 机构**：Hao Wen、Yuanchun Li、Guohong Liu、Shanhui Zhao、Tao Yu、Toby Jia-Jun Li、Shiqi Jiang、Yunhao Liu、Yaqin Zhang、Yunxin Liu（Tsinghua University、University of Notre Dame、Microsoft Research Asia；官方项目页标注）
- **时间**：2023-08（v1），2024-03（v4）　**类型**：会议论文（MobiCom 2024）
- **出处**：<https://arxiv.org/abs/2308.15272>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv abs 页 Comments "Published in MobiCom 2024"；同页与官方项目页给出 "158 common tasks"、"an accuracy of 90.9%"、"a success rate of 71.3%"（访问 2026-11-06）
- **页面依据**："The results demonstrated that AutoDroid is able to precisely generate actions with an accuracy of 90.9%, and complete tasks with a success rate of 71.3%, outperforming the GPT-4-powered baselines by 36.4% and 39.7%."；"Published in MobiCom 2024; Original title: \"Empowering LLM to use Smartphone for Intelligent Task Automation\""
- **要点**：通过自动化动态分析获得 app 领域知识，构建功能感知的 UI 表示、探索式记忆注入与多粒度查询优化，接入 GPT-4/3.5 与端侧 Vicuna。在含 158 个常见任务的基准上动作生成准确率 90.9%、任务成功率 71.3%，相对 GPT-4 基线分别高 36.4% 与 39.7%。
- **与主题关联**：其 UI 转换图/记忆注入与端侧小模型推理，是家用机以 uiautomator / UI 层级驱动本地 Android 任务自动化的可复用工程范式。

#### 153｜Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception

- **检索号**：Q-07　**类别**：Q 移动端 / Android GUI 智能体　**轮次**：第二轮
- **作者 / 机构**：Junyang Wang、Haiyang Xu、Jiabo Ye、Ming Yan、Weizhou Shen、Ji Zhang、Fei Huang、Jitao Sang（阿里巴巴集团通义实验室 Tongyi Lab；官方仓库 X-PLUG/MobileAgent）
- **时间**：2024-01　**类型**：会议论文（ICLR 2024 Workshop in Large Language Model (LLM) Agents）
- **出处**：<https://arxiv.org/abs/2401.16158>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv abs 页 Comments "Accepted by ICLR 2024 Workshop in Large Language Model (LLM) Agents"；官方仓库 X-PLUG/MobileAgent 显示 "9.4k stars"（GitHub，访问 2026-11-06）；论文引入 Mobile-Eval 基准
- **页面依据**："Different from previous solutions that rely on XML files of Apps or mobile system metadata, Mobile-Agent allows for greater adaptability across diverse mobile operating environments in a vision-centric way"；"To assess the performance of Mobile-Agent, we introduced Mobile-Eval, a benchmark for evaluating mobile device operations."
- **要点**：纯视觉方案，先用视觉感知工具定位界面图标/文本元素，再自主规划分解任务并逐步导航 App，不依赖 XML 或系统元数据；论文同时提出 Mobile-Eval 基准评估移动设备操作。同系列延伸工作 Mobile-Agent-E（arXiv 2501.11733，已打开正文）引入自进化模块 Tips/Shortcuts 与 Mobile-Eval-E 基准，摘要报告 "a 22% absolute improvement over previous state-of-the-art approaches"；因同系列限 2 条，此处仅核验不单列。
- **与主题关联**：纯截图驱动、免系统元数据的路线最适合家用机经 adb 截图控制异构手机/模拟器，Mobile-Eval 也提供可直接复用的评测任务集。

#### 154｜Large Language Model-Brained GUI Agents: A Survey

- **检索号**：Q-08　**类别**：Q 移动端 / Android GUI 智能体　**轮次**：第二轮
- **作者 / 机构**：Chaoyun Zhang、Shilin He、Jiaxu Qian、Bowen Li、Liqun Li、Si Qin、Yu Kang、Minghua Ma、Guyue Liu、Qingwei Lin、Saravan Rajmohan、Dongmei Zhang、Qi Zhang（微软；页面给出检索页 https://aka.ms/gui-agent 与论文库仓库）
- **时间**：2024-11（v1），2025-05（v12）　**类型**：arXiv 预印本（综述）
- **出处**：<https://arxiv.org/abs/2411.18279>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv abs 页显示 12 次修订（v1 2024-11-27 至 v12 2025-05-06，访问 2026-11-06）；摘要明确覆盖 web navigation、mobile app interactions 与 desktop automation 三大平台，并配套持续更新的 GitHub 论文库
- **页面依据**："Their applications span across web navigation, mobile app interactions, and desktop automation"；"this paper presents a comprehensive survey of LLM-brained GUI agents, exploring their historical evolution, core components, and advanced techniques."
- **要点**：系统梳理 LLM 驱动 GUI agent 的框架、训练数据收集与利用、大动作模型、评测指标与基准，并给出研究空白与路线图；配套仓库长期维护论文清单。检索中 UI-Vision 作为 GUI grounding 基准被 2025–2026 多篇工作与 ScreenSpot-Pro 并列引用（如 arXiv 2606.25760v2），但未定位到其独立 arXiv abs / 会议页 / 官方仓库，故不单列，标记为「未核实」。
- **与主题关联**：为家用机侧 CUA 提供跨平台（桌面 + 移动）方法学与基准清单，便于把移动端 agent 与本地计算机控制统一到同一套框架。

#### 155｜GUIOdyssey: A Comprehensive Dataset for Cross-App GUI Navigation on Mobile Devices

- **检索号**：Q-09　**类别**：Q 移动端 / Android GUI 智能体　**轮次**：第二轮
- **作者 / 机构**：Quanfeng Lu、Wenqi Shao、Zitao Liu、Lingxiao Du、Fanqing Meng、Boxuan Li、Botong Chen、Siyuan Huang、Kaipeng Zhang、Ping Luo（机构未在 abs 页逐字列出）
- **时间**：2024-06（v1），2025-08（v2）　**类型**：会议论文（ICCV 2025）
- **出处**：<https://arxiv.org/abs/2406.08451>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv abs 页 Comments "22 pages, 14 figures, ICCV 2025, a cross-app GUI navigation dataset"；同页给出 "8,334 episodes with an average of 15.3 steps per episode, covering 6 mobile devices, 212 distinct apps, and 1,357 app combinations"（访问 2026-11-06）
- **页面依据**："GUIOdyssey comprises 8,334 episodes with an average of 15.3 steps per episode, covering 6 mobile devices, 212 distinct apps, and 1,357 app combinations."；"we develop OdysseyAgent, an exploratory multimodal agent for long-step cross-app navigation equipped with a history resampler module"
- **要点**：针对跨 App 长程导航发布 8,334 条轨迹（平均 15.3 步、212 个 app、1,357 种 app 组合），每步附详细语义推理标注，并提出带历史重采样模块的 OdysseyAgent。域内/域外实验显示历史动作、截图与上下文信息可显著提升复杂跨 App 任务表现。
- **与主题关联**：为家用机在本地编排「跨多个手机 App 的长程任务」提供带推理标注的训练与评测数据。

#### 156｜MobileAgentBench: An Efficient and User-Friendly Benchmark for Mobile LLM Agents

- **检索号**：Q-10　**类别**：Q 移动端 / Android GUI 智能体　**轮次**：第二轮
- **作者 / 机构**：Luyuan Wang（Carnegie Mellon University）、Yongyu Deng（University of Michigan）、Yiwei Zha / Guodong Mao / Tianchen Min（Northeastern University）、Qinmin Wang、Wei Chen、Shoufa Chen 等（据 arXiv PDF 首页机构标注）
- **时间**：2024-06　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2406.08184>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv abs 页给出 "100 tasks across 10 open-source apps, categorized by multiple levels of difficulty"（访问 2026-11-06）；是较早专门面向移动 LLM agent 的公开基准
- **页面依据**："We initially define 100 tasks across 10 open-source apps, categorized by multiple levels of difficulty."；"we evaluate several existing mobile agents, including AppAgent and MobileAgent, to thoroughly and systematically compare their performance."；"All materials are accessible on our project webpage: this https URL (https://MobileAgentBench.github.io)"
- **要点**：面向移动 LLM agent 定义 100 个任务、覆盖 10 个开源 app 并按难度分级，以程序化方式降低穷举状态带来的手工测试负担。对 AppAgent、MobileAgent 等已有 agent 做系统横向比较，材料全部在项目页开放。
- **与主题关联**：提供可在本地模拟器/真机复现的轻量移动 agent 评测集，便于家用机侧 CUA 的回归测试与横向对比。

#### 157｜Mobilerun（原 DroidRun）官方仓库 — README 首句 "Mobilerun is an open-source framework for mobile app testing, QA, and running AI agents on real Android and iOS devices."

- **检索号**：Q-11　**类别**：Q 移动端 / Android GUI 智能体　**轮次**：第二轮
- **作者 / 机构**：Droidrun 团队（GitHub 组织 droidrun，德国，droidrun.ai；仓库标注 MIT License）
- **时间**：2025（官方仓库页未标注创建年份，按 2025 年起出现的公开文档推断，未核实）　**类型**：官方仓库（候补条目）
- **出处**：<https://github.com/droidrun/droidrun>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验；站点重定向至 https://github.com/droidrun/mobilerun；独立抓取二次确认「GitHub - droidrun/mobilerun（droidrun 仓库改名，直连 301 到新地址）」
- **影响力**：GitHub 仓库页显示 "10.0k stars" 与 "MIT License"（访问 2026-11-06）；项目页自述 "It scores 100% on AndroidWorld and 98.34% on iOSWorld"（厂商自述基准，非第三方评测，访问 2026-11-06）；GitHub 组织页显示 260 followers（检索结果 2026-10-25）
- **页面依据**："Android Real Device ✅ `adb` or the Portal app / Android Emulator ✅ Running emulator (`adb`)"；"Before starting, make sure you have ADB installed and an Android device with Developer options and USB debugging enabled."；"Combine accessibility trees with screenshots for visual understanding"；"It scores 100% on AndroidWorld and 98.34% on iOSWorld"
- **要点**：通过 ADB 或 Portal App 的 accessibility service 驱动真机与模拟器，把 UI trees / a11y tree、截图、点按滑动、文本输入与多步规划封装为 LLM 可调用的 CLI / Python API，并支持纯视觉模式。仓库页给出 10.0k stars 与 MIT 许可，自述在 AndroidWorld 达 100%、iOSWorld 98.34%。
- **与主题关联**：几乎是「家用机通过本机 adb 控制手机/模拟器」的开箱即用工程实现，可直接作为本地 CUA 执行层的参照。

#### 158｜MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research

- **检索号**：Q-12　**类别**：Q 移动端 / Android GUI 智能体　**轮次**：第二轮
- **作者 / 机构**：Dingbang Wu、Rui Hao、Haiyang Wang、Shuzhe Wu、Han Xiao、Zhenghong Li、Bojiang Zhou、Zheng Ju、Zichen Liu、Lue Fan、Zhaoxiang Zhang（机构全称未在 abs 页逐字列出，页面以上标编号标注）
- **时间**：2026-05　**类型**：会议论文（EMNLP 2026 Main Conference）（候补条目）
- **出处**：<https://arxiv.org/abs/2605.26114>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv abs 页 Comments "EMNLP 2026 Main Conference"；同页给出 "416 parameterized task templates, including 256 test and 160 train templates, over 28 apps"、"gains +12.8 percentage points on the 256-task test set"、"real-device execution retains 95.1% of the simulation-side training gain"（访问 2026-11-06）
- **页面依据**："We present MobileGym, a browser-hosted, lightweight, fully controllable environment for everyday mobile use, targeting interaction fidelity without replicating proprietary backends."；"a single server can host hundreds of parallel instances, with about 400 MB memory per instance and about 3 s cold start."；项目页 "28 Apps simulated"、"416 Parameterized task templates"
- **要点**：以结构化 JSON 状态实现浏览器托管的移动模拟环境，提供确定性状态判定与低成本并行在线 RL，MobileGym-Bench 含 28 个 app、416 个任务模板（256 测试 / 160 训练）。GRPO 微调 Qwen3-VL-4B 在 256 任务测试集提升 +12.8 个百分点，59 个真机任务子集上保留 95.1% 的仿真训练增益。
- **与主题关联**：把「本机模拟器 + 可重置状态 + 并行 rollout」做成轻量可验证平台，正是家用机侧离线训练与评测移动端 CUA 所需的基础设施。

### R 类｜高星开源 CUA 实现（GitHub star 硬证据）（12 篇）

#### 159｜browser-use/browser-use

- **检索号**：R-01　**类别**：R 高星开源 CUA 实现（GitHub star 硬证据）　**轮次**：第二轮
- **作者 / 机构**：Browser Use（组织 browser-use）
- **时间**：2024　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/browser-use/browser-use>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★120,179（GitHub 官方 API / 搜索 API，2026-11-06 查询）+ 核心能力："Open-source Python library for AI browser agents"，可在本地驱动 Chrome 执行 "all 31 browser actions"（官方描述与 README 可核验）
- **页面依据**："control a local browser"
- **要点**：在本地 PC 上以 Python 库/CLI 连接本地或 CDP 远程浏览器，把 LLM 任务转成浏览器点击、输入与导航，支持复用系统 Chrome profile 与 "Bash is included" 的本地辅助处理。README 明示最低 `Python >= 3.11`、Chrome，且 `Bash requires a Linux or macOS host`、Windows 需 "use WSL on Windows"，语言为 Python/TypeScript。
- **与主题关联**：本地浏览器控制型 CUA 的头部高星实现，给出 agent 到本地浏览器动作的完整落地链路。

#### 160｜trycua/cua

- **检索号**：R-02　**类别**：R 高星开源 CUA 实现（GitHub star 硬证据）　**轮次**：第二轮
- **作者 / 机构**：Cua AI, Inc. / trycua（组织）
- **时间**：2025　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/trycua/cua>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★31,855（GitHub 官方 API / 搜索 API，2026-11-06 查询）+ 核心能力："Scale computer-use 2.0 with open-source drivers, cross-OS sandboxes, and benchmarks for training, evaluation, and data generation"（官方仓库描述，可核验）
- **页面依据**："Give AI agents computers they can use."
- **要点**：在本地 PC 上提供 Cua Driver（在 macOS/Windows/Linux "inspect and operate native desktop apps and browsers"，经 CLI/MCP/typed SDK 注入输入、读 UI 且可不移动指针不抢焦点）、Cua Spaces 完整桌面、Lume 本地 Apple Silicon VM、gVisor 沙箱与 `cua sb screenshot dev` 截图。README 明示 SDK 为 Python（`pip install cua`）、TypeScript（`@trycua/cua`）、Rust（`cua-sdk`），Cua Bench 需 "With Python 3.12 or 3.13 and uv installed"，Spaces 需 "Install on macOS 26 or later"。
- **与主题关联**：把"给 agent 一台能用的电脑"做成开源驱动 + 跨 OS 沙箱 + 基准的本地 CUA 基础设施。

#### 161｜Fosowl/agenticSeek

- **检索号**：R-03　**类别**：R 高星开源 CUA 实现（GitHub star 硬证据）　**轮次**：第二轮
- **作者 / 机构**：Fosowl（个人开发者，README 明示 "not a startup or affiliated with any organization"）
- **时间**：2025　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/Fosowl/agenticSeek>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★27,631（GitHub 官方 API / 搜索 API，2026-11-06 查询）+ 核心能力："Fully Local Manus AI. No APIs, No $200 monthly bills."，100% 本地、零云依赖的自主 agent（官方描述，可核验）
- **页面依据**："Everything runs on your machine — no cloud, no data sharing."
- **要点**：在本地 PC 上跑一个语音启用的自主 agent，自行浏览网页/搜索/填表、写并运行代码、读写本地文件，且 "runs entirely on your hardware"、"zero cloud dependency"。README 要求 "Python 3.10.x"、"Docker Engine & Docker Compose"，本地 LLM 建议 Ollama/LM Studio，最低需 "a GPU capable of running Magistral, Qwen or Deepseek 14B is required"（如 "12 GB VRAM (e.g. RTX 3060)"），支持 Linux/macOS/Windows。
- **与主题关联**：证明 CUA 类自主 agent 可完全离线跑在用户自有硬件上，是"本地计算机实际实现"的典型。

#### 162｜vercel-labs/agent-desktop

- **检索号**：R-04　**类别**：R 高星开源 CUA 实现（GitHub star 硬证据）　**轮次**：第二轮
- **作者 / 机构**：Vercel Labs（组织）
- **时间**：2026　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/vercel-labs/agent-desktop>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★17,583（GitHub 官方 API / 搜索 API，2026-11-06 查询）+ 核心能力："Computer use CLI for AI agents"，无需截图/像素匹配、基于 OS 无障碍树的桌面 computer use（官方描述与 README 可核验）
- **页面依据**："see and operate desktop apps on macOS, Windows, and Linux through the OS accessibility tree"
- **要点**：在本地 PC 上把桌面应用的无障碍树读成带 ref 的 JSON，agent 对 ref 执行 click/type 再重新读取 UI 验证，默认 headless（不移动指针、不抢焦点），另提供 snapshot/screenshot、键盘鼠标命令、MCP server 与 C 库。README 明示平台为 "macOS 13 or later"、"Windows 10 1809 or later"、"Ubuntu 24.04 or later"（分别用 AX API / UI Automation / AT-SPI），安装 "npm install -g agent-desktop"（Bun/Yarn/pnpm 亦可），核心为 Rust（cargo）。
- **与主题关联**：以无障碍树替代截图的本地桌面 CUA 实现，直接给出跨平台的 OS 级驱动层。

#### 163｜browseros-ai/BrowserOS

- **检索号**：R-05　**类别**：R 高星开源 CUA 实现（GitHub star 硬证据）　**轮次**：第二轮
- **作者 / 机构**：BrowserOS AI / Felafax, Inc.（组织）
- **时间**：2025　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/browseros-ai/BrowserOS>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★14,264（GitHub 官方 API / 搜索 API，2026-11-06 查询）+ 核心能力："The open-source Agentic browser; alternative to ChatGPT Atlas, Perplexity Comet, Dia."（官方描述，可核验）
- **页面依据**："BrowserOS neo runs on your machine, on 127.0.0.1."
- **要点**：在本地 PC 上以 Chromium fork 运行本地优先（README 明确 "Not a cloud browser"）的 agentic 浏览器，复用用户已登录账号让 agent 自动化真实网页工作，会话/截图/历史存 `~/.browserclaw/` 且可回放逐步动作视频。README 明示 "BrowserOS neo runs on macOS, Windows, and Linux"、"Linux builds are x64"、"System requirements match Google Chrome"，技术栈为 Chromium fork（C++/Python）与 agent 平台（TypeScript/Rust），构建 "requires ~100GB of disk"，安装 `brew install --cask browseros-neo`。
- **与主题关联**：把"浏览器即 CUA 运行环境"做成可本地安装的开源桌面浏览器。

#### 164｜simular-ai/Agent-S

- **检索号**：R-06　**类别**：R 高星开源 CUA 实现（GitHub star 硬证据）　**轮次**：第二轮
- **作者 / 机构**：Simular AI（组织）
- **时间**：2024　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/simular-ai/Agent-S>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★12,891（GitHub 官方 API / 搜索 API，2026-11-06 查询）+ 会议背书：Agent S 论文 "accepted to ICLR 2025!" 且获 ICLR 2025 Agentic AI for Science Workshop "Best Paper Award"，Agent S2 "accepted to COLM 2025"、Agent S3 "accepted to TMLR 2026"（README Updates 可核验）
- **页面依据**："An open-source computer use agent that can operate a real GUI like a human"
- **要点**：在本地 PC 上 "looks at the screen and completes the task by clicking, typing, and scrolling in ordinary desktop and web apps"，提供 `gui-agents` Python 库与 S/S2/S2.5/S3/S4 多版本 agent-computer interface。README 明示 "It runs on macOS, Windows, and Linux"、本地运行见 "On your own computer: follow the Agent S3 README"；最低 Python 版本 README 未明示（未核实）。
- **与主题关联**：学术会议背书的开源 CUA 框架，明确给出本地三平台 GUI 操作实现。

#### 165｜CursorTouch/Windows-MCP

- **检索号**：R-07　**类别**：R 高星开源 CUA 实现（GitHub star 硬证据）　**轮次**：第二轮
- **作者 / 机构**：CursorTouch（组织）
- **时间**：2025　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/CursorTouch/Windows-MCP>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★11,166（GitHub 官方 API / 搜索 API，2026-11-06 查询）+ 核心能力："MCP Server for Computer Use in Windows"，把 Windows 桌面能力以 MCP 工具暴露给 LLM（官方描述，可核验）
- **页面依据**："Windows-MCP runs directly on your Windows machine and exposes its tools to the connected MCP client."
- **要点**：在本地 Windows PC 上提供截图优先的桌面捕获、按需构建的 a11y/UI 树、Click/Type/Shortcut/Move 输入注入，以及 App 启动、PowerShell、FileSystem、Registry 等系统工具（"Rich Toolset for UI Automation"）。README 明示 "Platform: Windows 10 and 11"、"The current package requires Python 3.14+"，安装/启动用 `uvx windows-mcp serve`（uv 包管理器）。
- **与主题关联**：Windows 本地 CUA 的 MCP 化实现，覆盖截图、无障碍树与输入注入全链路。

#### 166｜go-vgo/robotgo

- **检索号**：R-08　**类别**：R 高星开源 CUA 实现（GitHub star 硬证据）　**轮次**：第二轮
- **作者 / 机构**：go-vgo（组织，维护者 @vcaesar）
- **时间**：2016　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/go-vgo/robotgo>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★10,902（GitHub 官方 API / 搜索 API，2026-11-06 查询）+ 核心能力："Go Native cross-platform RPA, GUI automation, Auto test and Computer use"（官方描述，可核验）
- **页面依据**："Control the mouse, keyboard, read the screen, process, Window Handle, image and bitmap and global event listener."
- **要点**：在本地 PC 上以 Go 原生库提供鼠标/键盘控制、屏幕读取与截图（"read the screen" / "Screen capture"）、bitmap、窗口句柄与全局事件监听等底层桌面自动化原语。README 明示 "Go 1.26+"、安装 `go get github.com/go-vgo/robotgo`，Cgo 后端需 C 编译器与平台库（Linux `sudo apt install gcc libc6-dev libx11-dev xorg-dev libxtst-dev`、libpng），并写明 "RobotGo supports Mac, Windows, and Linux; and robotgo supports arm64 and x86-amd64"。
- **与主题关联**：CUA 底层输入注入/屏幕捕获驱动的长期高星实现，被上层 agent 复用。

#### 167｜microsoft/UFO

- **检索号**：R-09　**类别**：R 高星开源 CUA 实现（GitHub star 硬证据）　**轮次**：第二轮
- **作者 / 机构**：Microsoft（Microsoft Research，组织）
- **时间**：2024　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/microsoft/UFO>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★10,171（GitHub 官方 API / 搜索 API，2026-11-06 查询）+ 论文背书：原版 "UFO: A UI-Focused Agent for Windows OS Interaction"（arXiv:2402.07939，2024-02）、UFO² "UFO2: The Desktop AgentOS"（arXiv:2504.14603）（README 发布记录可核验）
- **页面依据**："Deep OS Integration Windows UIA, Win32, WinCOM native control"
- **要点**：在本地 Windows PC 上以 GUI Agent 深度集成 Windows UIA/Win32/WinCOM 控件，采用 "Hybrid GUI + API actions"（GUI 点击 + API 调用）、"Visual + UIA Detection" 与 HostAgent + AppAgents 多 agent 协作完成跨应用任务。README 明示安装 `pip install -r requirements.txt`（Python），需配置 LLM（"OpenAI Configuration" / "Azure OpenAI Configuration"，`API_KEY`、`API_MODEL: "gpt-4o"`），原版定位 "GUI Agent for Windows" / "Windows Desktop"。
- **与主题关联**：微软官方的 Windows 桌面 CUA 研究实现，给出 UIA 控件级与 GUI 混合动作的本地方案。

#### 168｜steel-dev/steel-browser

- **检索号**：R-10　**类别**：R 高星开源 CUA 实现（GitHub star 硬证据）　**轮次**：第二轮
- **作者 / 机构**：Steel / steel-dev（组织，steel.dev）
- **时间**：2024　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/steel-dev/steel-browser>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★7,930（GitHub 官方 API / 搜索 API，2026-11-06 查询）+ 核心能力："Open Source Browser API for AI Agents & Apps"，"batteries-included browser sandbox"（官方描述，可核验）
- **页面依据**："Steel Browser is a batteries-included browser sandbox that lets you automate the web without worrying about infrastructure."
- **要点**：在本地 PC 上自托管一个浏览器沙箱/API，提供 Sessions、Playwright/Puppeteer/Selenium 接入、反检测（"Includes stealth plugins and fingerprint management"）与会话调试 UI。README 明示 `docker run -p 3000:3000 -p 9223:9223 ghcr.io/steel-dev/steel-browser`（或 `docker compose up`）、本地 "npm install" / "npm run dev"，服务 "port 3000"、UI "port 5173"，技术栈 Node.js/TypeScript，支持 Linux/MacOS/Windows 的 Chrome 可执行文件。
- **与主题关联**：为本地 CUA 提供可自托管的浏览器沙箱与会话/驱动基础设施。

#### 169｜lavague-ai/LaVague（候补）

- **检索号**：R-11　**类别**：R 高星开源 CUA 实现（GitHub star 硬证据）　**轮次**：第二轮
- **作者 / 机构**：LaVague AI / lavague-ai（组织）
- **时间**：2024　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/lavague-ai/LaVague>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★6,396（GitHub 官方 API / 搜索 API，2026-11-06 查询）+ 核心能力："Large Action Model framework to develop AI Web Agents"（官方描述，可核验）
- **页面依据**："An Action Engine which 'compiles' these instructions into action code, e.g., Selenium or Playwright & executes them"
- **要点**：在本地 PC 上由 World Model 读当前网页与目标生成指令，Action Engine 把指令编译为 Selenium/Playwright 动作代码并执行，支持 "A Selenium Webdriver"、"A Playwright webdriver"、"A Chrome extension driver" 三种驱动。README 明示 `pip install lavague`（Python），示例需在本地环境设置 "OPENAI_API_KEY"（默认 `gpt4-o`，可自定义）。
- **与主题关联**：以"大动作模型 + 编译成浏览器驱动代码"实现本地 Web CUA 的候补高星方案。

#### 170｜microsoft/fara（候补）

- **检索号**：R-12　**类别**：R 高星开源 CUA 实现（GitHub star 硬证据）　**轮次**：第二轮
- **作者 / 机构**：Microsoft（Microsoft Research，组织）
- **时间**：2025　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/microsoft/fara>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★6,248（GitHub 官方 API / 搜索 API，2026-11-06 查询）+ 论文背书："Fara1.5 – A family of frontier computer use agent models"，配套论文 arXiv:2606.20785 与 Fara-7B arXiv:2511.19663（README 可核验）
- **页面依据**："taking actions like scrolling, typing, and clicking on directly predicted coordinates"
- **要点**：在本地 PC 上以原生 CUA 模型（4B/9B/27B）跑 observe-think-act 循环，输入浏览器截图即输出鼠标/键盘坐标动作（"with no accessibility trees or separate parsing models"），并保存逐步截图轨迹到 `--output_folder`。README 明示 `pip install -e .[vllm]`、`python3 -m playwright install`（Python），"The following instructions are for Linux systems"、Windows "we highly recommend using WSL2"，可 vLLM 自托管或 Microsoft Foundry/OpenAI 兼容 endpoint，且 "context length is set to at least 15000 tokens"。
- **与主题关联**：微软官方的纯视觉 CUA 模型本地推理实现，配套 "sandboxed browser environment"，列为候补。

### S 类｜桌面控制、无障碍与输入注入官方技术文档（12 篇）

#### 171｜UI Automation - Win32 apps | Microsoft Learn

- **检索号**：S-01　**类别**：S 桌面控制、无障碍与输入注入官方技术文档　**轮次**：第二轮
- **作者 / 机构**：Microsoft（Microsoft Learn / Win32 apps 文档）
- **时间**：n.d.　**类型**：官方 API 文档
- **出处**：<https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Microsoft 官方无障碍框架文档；UI Automation 把桌面 UI 元素以树形/属性方式暴露给客户端，是 Windows 上「拿到控件树」并读取元素属性的第一手接口，也是 Windows 桌面自动化（含 pywinauto 的 uia 后端）所对接的底层框架。
- **页面依据**："Microsoft UI Automation is an accessibility framework that enables Windows applications to provide and consume programmatic information about user interfaces (UIs). It provides programmatic access to most UI elements on the desktop."；"UI Automation also allows automated test scripts to interact with the UI."；章节 "UI Automation Client Programmer's Guide"、"UI Automation Fundamentals"、"Reference"
- **要点**：官方定义 UI Automation 为无障碍框架，向客户端提供桌面上绝大多数 UI 元素的编程访问，并明确允许 automated test scripts 与 UI 交互；页面给出 Fundamentals、Provider/Client Programmer's Guide、Reference、Samples 等分册入口。文档面向熟悉 COM 对象/接口、Unicode 与 Windows API 的 C/C++ 开发者（托管代码另见 .NET Framework 的 Accessibility 指南），运行时要求覆盖 Windows XP、Vista、7、10 及 Windows Server 2003–2019（XP/Server 2003 另需 .NET Framework 3.0）。
- **与主题关联**：提供 Windows 本地 CUA 的「控件树 / UI 语义」层——读取结构化元素信息并驱动界面。

#### 172｜AXUIElementCopyAttributeValues(_:_:_:_:_:) | Apple Developer Documentation

- **检索号**：S-02　**类别**：S 桌面控制、无障碍与输入注入官方技术文档　**轮次**：第二轮
- **作者 / 机构**：Apple Inc.（Apple Developer Documentation / ApplicationServices）
- **时间**：n.d.　**类型**：官方 API 文档
- **出处**：<https://developer.apple.com/documentation/applicationservices/1462060-axuielementcopyattributevalues>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Apple 官方 macOS Accessibility（AXUIElement）API 文档；AXUIElement 体系是 macOS 上读取窗口/控件层级与属性并触发动作的一手接口，是 macOS CUA「控件树」能力的基础。
- **页面依据**："Returns an array of attribute values for the accessibility object's attribute, starting at the specified index."；"macOS 10.2+"；"func AXUIElementCopyAttributeValues("；"-> AXError"；"The AXUIElementRef representing the accessibility object."；"kAXErrorNotImplemented"、"kAXErrorCannotComplete"
- **要点**：该函数按索引分批读取某个无障碍对象（AXUIElement）的指定 CFString 属性值数组，页面给出完整函数签名、参数说明、返回 AXError 及 kAXErrorIllegalArgument / kAXErrorNoValue / kAXErrorInvalidUIElement / kAXErrorCannotComplete / kAXErrorNotImplemented 等错误码，并说明适用于「含大量子元素的表视图」这类大数组的分批读取。页面标注 macOS 10.2+，且 kAXErrorNotImplemented（进程未完全支持 accessibility API）与 kAXErrorCannotComplete（消息传递失败）表明能力受目标进程对无障碍接口支持程度的限制。
- **与主题关联**：提供 macOS 本地 CUA 的「控件树 / 属性读取」层——从 AXUIElement 取得结构化界面信息。

#### 173｜SendInput function (winuser.h) - Win32 apps | Microsoft Learn

- **检索号**：S-03　**类别**：S 桌面控制、无障碍与输入注入官方技术文档　**轮次**：第二轮
- **作者 / 机构**：Microsoft（Microsoft Learn / Win32 API）
- **时间**：n.d.　**类型**：官方 API 文档
- **出处**：<https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendinput>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Microsoft 官方 Win32 输入合成 API；SendInput 把键盘/鼠标事件串行插入系统输入流，是 Windows 上「注入鼠标键盘」的标准系统调用，为上层桌面自动化封装提供底层原语。
- **页面依据**："Synthesizes keystrokes, mouse motions, and button clicks."；"UINT SendInput(UINT cInputs, LPINPUT pInputs, int cbSize)"；"an array of INPUT structures"；"This function is subject to UIPI. Applications are permitted to inject input only into applications that are at an equal or lesser integrity level."；"Minimum supported client Windows 2000 Professional"
- **要点**：通过 INPUT 结构数组一次提交多个键击、鼠标移动与按键事件，事件串行插入键盘/鼠标输入流且不与用户、keybd_event / mouse_event 或其他 SendInput 调用产生的事件交错；页面附有 Win+D 组合键的 C++ 示例与 INPUT_KEYBOARD / KEYEVENTF_KEYUP 用法。明确限制：受 UIPI 约束，只能向完整性级别相等或更低的进程注入输入，UIPI 阻断时返回值与 GetLastError 都不会提示；不重置键盘当前状态；最低支持 Windows 2000 Professional，头文件 winuser.h、库 User32.lib、DLL User32.dll。
- **与主题关联**：提供 Windows 本地 CUA 的「输入注入 / 动作执行」层——把决策落成真实键鼠事件。

#### 174｜Quartz Event Services | Apple Developer Documentation

- **检索号**：S-04　**类别**：S 桌面控制、无障碍与输入注入官方技术文档　**轮次**：第二轮
- **作者 / 机构**：Apple Inc.（Apple Developer Documentation / Core Graphics）
- **时间**：n.d.　**类型**：官方 API 文档
- **出处**：<https://developer.apple.com/documentation/coregraphics/quartz-event-services>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Apple 官方 Core Graphics 事件服务文档；CGEvent 与 event taps 是 macOS 上构造并投递键盘、鼠标等低层输入事件的一手接口（文档原文指出其输入合成能力与 Win32 SendInput 类似），是 macOS CUA「注入鼠标键盘」的基础。
- **页面依据**："Provides features for managing event taps—filters for observing and altering the stream of low-level user input events in macOS."；"class CGEvent — Defines an opaque type that represents a low-level hardware event."；"func post(tap: CGEventTapLocation) — Posts a Quartz event into the event stream at a specified location."；"init?(keyboardEventSource: CGEventSource?, virtualKey: CGKeyCode, keyDown: Bool) — Returns a new Quartz keyboard event."；"Introduced in OS X version 10.4, event taps provide functionality similar to the Win32 functions SetWinEventHook ... and SendInput."
- **要点**：该 API Collection 覆盖 CGEvent（低层硬件事件的不透明类型）、键盘/鼠标事件构造、post(tap:) 投递、tapCreate 事件点击创建与 CGEventTapLocation 等，既能监听/过滤系统输入流，也能构造并注入键鼠事件（分区含 Working With Events / Event Taps / Event Sources、Data Types、Constants、Deprecated Functions）。文档说明 event taps 自 OS X 10.4 引入，作用类似 Win32 的 SetWinEventHook 与 SendInput；并指出 CGRemoteOperation.h 中的旧式事件函数仍受支持但不推荐用于新开发。
- **与主题关联**：提供 macOS 本地 CUA 的「事件合成 / 输入注入」层，同时可兼做输入流观测。

#### 175｜XTEST Extension Protocol

- **检索号**：S-05　**类别**：S 桌面控制、无障碍与输入注入官方技术文档　**轮次**：第二轮
- **作者 / 机构**：X Consortium（标准制定）/ X.Org Foundation（X11R7.7 文档集发布）；文档作者 Kieron Drake, UniSoft Ltd.
- **时间**：n.d.　**类型**：标准文档
- **出处**：<https://www.x.org/releases/X11R7.7/doc/xextproto/xtest.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：X Consortium 标准、由 X.Org 随 X Window System 文档集发布；XTEST 的 XTestFakeInput 请求是 X11 / Linux 桌面合成键鼠事件（按键按下/释放、指针移动、按钮按下/释放）的协议级依据，是 X11 上「注入鼠标键盘」的底层标准。
- **页面依据**："XTEST Extension Protocol"；"X Consortium Standard"；"Kieron Drake, UniSoft Ltd."；"X Version 11, Release 7.7"、"Version 2.2"；"XTestFakeInput"；"limited synthesis of input device events, almost as if a cooperative user had moved the pointing device or pressed a key or button"；"The name of this extension is \"XTEST\"."
- **要点**：规范定义 FAKE_EVENT_TYPE（KeyPress / KeyRelease / MotionNotify / ButtonPress / ButtonRelease）与 XTestFakeInput 请求，可注入物理键码、相对或绝对指针坐标与鼠标按钮，并规定被模拟事件会像真实设备动作一样触发事件传播、被动 grab 激活（但 motion 可能不写入 motion history）。明确这是面向 X Server 测试的「最小集」扩展，不用于用户动作的一般录制/回放；同时给出 XTestGetVersion、XTestCompareCursor、XTestGrabControl 请求及第 6 章协议编码，客户端操作一节链接到 XTEST Extension Library（libXtst）文档。
- **与主题关联**：提供 X11 / Linux 本地 CUA 的「输入注入」协议层——键鼠事件合成的标准定义。

#### 176｜Screen capture - Windows apps | Microsoft Learn

- **检索号**：S-06　**类别**：S 桌面控制、无障碍与输入注入官方技术文档　**轮次**：第二轮
- **作者 / 机构**：Microsoft（Microsoft Learn / Windows App SDK 与 UWP 文档）
- **时间**：n.d.　**类型**：官方 API 文档
- **出处**：<https://learn.microsoft.com/en-us/windows/apps/develop/media-authoring-processing/screen-capture>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Microsoft 官方 Windows.Graphics.Capture 文档；该命名空间是 Windows 上获取显示器/应用窗口帧以生成截图或视频流的现代官方 API，是 Windows CUA「看屏幕」的一手依据。
- **页面依据**："The Windows.Graphics.Capture namespace provides APIs to acquire frames from a display or application window, to create video streams or snapshots"；"GraphicsCapturePicker"、"GraphicsCaptureItem"、"Direct3D11CaptureFramePool"、"GraphicsCaptureSession.StartCapture"、"Direct3D11CaptureFramePool.FrameArrived"；"a yellow notification border is drawn by the system around the actively captured item"；"This article describes capturing a single image of the display or application window."
- **要点**：通过 GraphicsCapturePicker 让用户选取显示器或应用窗口得到 GraphicsCaptureItem，再用 Direct3D11CaptureFramePool（指定 D3D 设备、DXGI_FORMAT_B8G8R8A8_UNORM 像素格式与帧尺寸）配合 GraphicsCaptureSession.StartCapture 获取 Direct3D11CaptureFrame（含 ContentSize / Surface / SystemRelativeTime），页面给出 FrameArrived 事件、TryGetNextFrame 拉取及保存为 PNG 的示例。明确限制：需先以 GraphicsCaptureSession.IsSupported() 检查支持性，捕获需用户显式同意且系统会在被捕获项周围绘制黄色通知边框，API 仅支持 Windows 桌面设备与 Windows Mixed Reality 沉浸式头显；WinUI 3 下 picker 需用 InitializeWithWindow 传入 HWND。
- **与主题关联**：提供 Windows 本地 CUA 的「屏幕感知」层——拿到屏幕/窗口的像素帧。

#### 177｜Write automated tests with UI Automator | Test your app on Android | Android Developers

- **检索号**：S-07　**类别**：S 桌面控制、无障碍与输入注入官方技术文档　**轮次**：第二轮
- **作者 / 机构**：Google / Android Developers
- **时间**：n.d.　**类型**：官方 API 文档
- **出处**：<https://developer.android.com/training/testing/other-components/ui-automator>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「Write automated tests with UI Automator | Test your app on Android | Android Developers」
- **影响力**：Google 官方 Android UI Automator 框架文档；该框架提供跨应用查看 UI 层级、按文本/资源 ID 定位控件并点击/输入的能力，是 Android 本地 CUA「控件树 + 控件级操作」的一手接口，能力建立在无障碍树之上。
- **页面依据**："The UI Automator testing framework provides a set of APIs to build UI tests that interact with user apps and system apps."；"UI Automator 2.4 introduces a streamlined, Kotlin-friendly Domain Specific Language (DSL)"；"Direct interaction with accessibility window nodes for multi-window testing scenarios."；"waitForStable() works by waiting until no changes are detected in the accessibility tree"；"device.findObject(By.text(\"Click Me\"))"；"androidx.test.uiautomator:uiautomator:2.4.0-alpha05"
- **要点**：官方指南给出 UI Automator 2.4 的现代 Kotlin DSL 写法、Gradle 依赖配置（androidx.test.uiautomator）以及与旧版 UiDevice / By.text / By.res 写法的迁移对照表，可直接与用户应用和系统应用交互。页面明确其能力依赖无障碍体系：可直接操作 accessibility window nodes（多窗口场景），waitForStable() 通过检测 accessibility tree 在一段时间内无变化来判断界面稳定。
- **与主题关联**：提供 Android 本地 CUA 的「控件树读取 + 控件级操作」层。

#### 178｜Create an accessibility service | Android Developers

- **检索号**：S-08　**类别**：S 桌面控制、无障碍与输入注入官方技术文档　**轮次**：第二轮
- **作者 / 机构**：Google / Android Developers
- **时间**：n.d.　**类型**：官方 API 文档
- **出处**：<https://developer.android.com/guide/topics/ui/accessibility/service>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「Create an accessibility service | Android Developers」
- **影响力**：Google 官方 AccessibilityService 指南；无障碍服务可在系统级读取窗口内容/无障碍树、对节点执行动作并派发手势，是 Android 上「拿到控件树 + 注入操作」的 OS 级机制，与 UI Automator 同属 Android 无障碍能力体系。
- **页面依据**："To create an accessibility service, you must extend the AccessibilityService class and declare the service in your app's manifest."；"Your service interacts primarily with AccessibilityNodeInfo objects, which represent UI elements like buttons, lists, and text."；"To perform an action, call performAction() on an AccessibilityNodeInfo object."；"node.performAction(AccessibilityNodeInfo.ACTION_CLICK)"；"android:canPerformGestures" / "dispatchGesture()"；"android:canRetrieveWindowContent : Must be true if your service needs to inspect the UI hierarchy (for example, to read text from the screen)."
- **要点**：需继承 AccessibilityService 并在 manifest 声明（含 BIND_ACCESSIBILITY_SERVICE 权限），服务主要与代表按钮/列表/文本的 AccessibilityNodeInfo 交互，可遍历无障碍树并调用 performAction()（如 ACTION_CLICK）执行控件动作。通过 android:canRetrieveWindowContent 允许检视 UI 层级/读取屏幕文字，通过 android:canPerformGestures=true 启用 dispatchGesture() 派发点按/滑动等手势；页面同时警示无障碍服务是专用辅助工具而非常规做法。
- **与主题关联**：提供 Android 本地 CUA 的「系统级控件树 + 动作/手势注入」层。

#### 179｜Getting Started Guide

- **检索号**：S-09　**类别**：S 桌面控制、无障碍与输入注入官方技术文档　**轮次**：第二轮
- **作者 / 机构**：pywinauto 项目（Read the Docs 官方文档；源码仓库 github.com/pywinauto/pywinauto）
- **时间**：n.d.　**类型**：官方手册
- **出处**：<https://pywinauto.readthedocs.io/en/latest/getting_started.html>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验
- **影响力**：pywinauto 项目官方入门手册；它把 Windows 的 Win32 API 与 MS UI Automation 两套无障碍后端封装成 Application / Desktop / WindowSpecification，是 Windows 桌面 CUA 常用的「控件树 + 输入」Python 实现层。GitHub star 数：未核实。
- **页面依据**："Getting Started Guide"；"**Win32 API** (backend=\"win32\") - a default backend for now"；"**MS UI Automation** (backend=\"uia\")"、"WinForms, WPF, Store apps, Qt5, browsers"；"app = Application(backend=\"uia\").start('notepad.exe')"；"your entry point is a Desktop object"；章节 "Entry Points for Automation"、"Window Specification"、"Attribute Resolution Magic"
- **要点**：明确两套 backend：win32（当前默认）与 uia，uia 适用于 WinForms、WPF、Store apps、Qt5、浏览器（Chrome 需 --force-renderer-accessibility 启动参数）；自动化入口为 Application（单进程）与 Desktop（需跨进程边界时，如 Win10 计算器）。另给出 GUI Objects Inspection / Spy Tools、Window Specification、Attribute Resolution Magic 等章节，说明用控件属性与 best match 机制定位窗口和控件；Application 与 Desktop 对象都与 backend 绑定。
- **与主题关联**：提供 Windows 本地 CUA 的「开箱即用实现层」——把 UIA/Win32 控件树与输入封装为 Python API。

#### 180｜Cheat Sheet — PyAutoGUI documentation

- **检索号**：S-10　**类别**：S 桌面控制、无障碍与输入注入官方技术文档　**轮次**：第二轮
- **作者 / 机构**：PyAutoGUI 项目（Read the Docs 官方文档）
- **时间**：n.d.　**类型**：官方手册
- **出处**：<https://pyautogui.readthedocs.io/en/latest/quickstart.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：PyAutoGUI 项目官方速查手册；它把 screenshot、鼠标移动/点击/拖拽、键盘输入以及基于模板图的 locateOnScreen 图像定位统一为跨平台 API，是「看屏幕 + 注入键鼠」的经典 Python 实现层。GitHub star 数：未核实。
- **页面依据**："PyAutoGUI is cross-platform GUI automation module that works on Python 2 & 3. You can control the mouse and keyboard as well as perform basic image recognition to automate tasks on your computer."；"PyAutoGUI works on Windows/Mac/Linux"；"pyautogui.screenshot() # returns a Pillow/PIL Image object"；"pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')"；"pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)"；"pyautogui.locateOnScreen('looksLikeThis.png')"
- **要点**：覆盖 General / Mouse / Keyboard / Message Box / Screenshot 函数：position()、size()、moveTo/moveRel、click/dragTo/scroll/mouseDown/mouseUp、typewrite/hotkey/keyDown/keyUp、screenshot()、locateOnScreen()/locateAllOnScreen()/locateCenterOnScreen()，并带 FAILSAFE（鼠标移到左上角抛出 FailSafeException 中止）与 PAUSE（每次调用后暂停）保护。明确平台与限制：Windows/Mac/Linux、Python 2&3，图像功能基于 Pillow/PIL，Linux 上截图需安装 scrot，locate 系列函数较慢（可能耗时 1–2 秒），Mac 上拖拽不能瞬时完成。
- **与主题关联**：提供跨平台本地 CUA 的「看屏幕 + 键鼠注入 + 图像定位」一体化实现层。

#### 181｜Command Line Usage | tessdoc

- **检索号**：S-11　**类别**：S 桌面控制、无障碍与输入注入官方技术文档　**轮次**：第二轮
- **作者 / 机构**：Tesseract OCR 项目（tessdoc 官方文档，tesseract-ocr.github.io / github.com/tesseract-ocr/tessdoc）
- **时间**：n.d.　**类型**：官方手册
- **出处**：<https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Tesseract OCR 项目官方命令行手册；Tesseract 把屏幕/截图图像转为带坐标的文字（TSV/HOCR 输出含词级 bbox），是无控件树场景下 CUA「看屏幕 → 读出文字与位置」的常用 OCR 引擎。GitHub star 数：未核实。
- **页面依据**："Command Line Usage | tessdoc"；"Simplest Invocation to OCR an image — tesseract imagename outputbase"；"Use --oem 1 for LSTM/neural network, --oem 0 for Legacy Tesseract"；"tesseract imagename outputbase -l eng --psm 3"；"Use 'tsv' config file by adding tsv at the end of the command to get the TSV output"；"level   page_num   block_num   par_num   line_num   word_num   left   top   width   height   conf   text"
- **要点**：给出 tesseract 命令行用法：-l 指定语言（可 eng+deu 多语言）、--psm 页分割模式（如 --psm 3 全自动、--psm 6 单一文本块）、--oem 引擎（LSTM/legacy），输出格式含 text、pdf、hocr、tsv，其中 TSV 逐词给出 left/top/width/height/conf/text，HOCR 给出带 bbox 的词级 XML。另说明 --tessdata-dir 与 TESSDATA_PREFIX 指定训练数据、quiet 抑制分辨率提示，并提示多语言顺序会影响识别结果与耗时；页面基于 Tesseract 5（LSTM 引擎）。
- **与主题关联**：提供本地 CUA 的「屏幕文字感知」层——把截图转成可定位的文本及其坐标。

#### 182｜OpenCV: Template Matching

- **检索号**：S-12　**类别**：S 桌面控制、无障碍与输入注入官方技术文档　**轮次**：第二轮
- **作者 / 机构**：OpenCV 项目（docs.opencv.org 官方教程文档）
- **时间**：n.d.　**类型**：官方手册
- **出处**：<https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：OpenCV 官方模板匹配教程；cv.matchTemplate + cv.minMaxLoc 用模板图在屏幕截图中定位控件/图标，是纯视觉 CUA（无控件树时）实现「看屏幕 → 定位点击目标」的基础方法。GitHub star 数：未核实。
- **页面依据**："OpenCV: Template Matching"；"Template Matching is a method for searching and finding the location of a template image in a larger image."；"cv.matchTemplate()" — "Compares a template against overlapped image regions."；"cv.minMaxLoc()" — "Finds the global minimum and maximum in an array."；"TM_CCOEFF"、"TM_CCOEFF_NORMED"、"TM_SQDIFF_NORMED"；"threshold = 0.8"
- **要点**：说明 matchTemplate 以类似 2D 卷积的方式在大图上滑动模板并输出匹配度灰度图（输出尺寸 W-w+1, H-h+1），配合 minMaxLoc 取最大/最小值位置作为目标矩形左上角；列出 TM_CCOEFF / TM_CCORR / TM_SQDIFF 及其归一化共 6 种比较方法（TM_SQDIFF 类取最小值为最佳匹配）。给出多目标匹配示例：以 TM_CCOEFF_NORMED 配合 threshold=0.8 找出图中所有金币位置；该页为 OpenCV 4.x（当前 4.13.0）Python 教程。
- **与主题关联**：提供本地 CUA 的「屏幕图像定位」层——用模板匹配得到可点击的屏幕坐标。

### T 类｜CUA 评测基准、数据集与公开榜单（12 篇）

#### 183｜OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

- **检索号**：T-01　**类别**：T CUA 评测基准、数据集与公开榜单　**轮次**：第二轮
- **作者 / 机构**：The University of Hong Kong、Salesforce Research、Carnegie Mellon University、University of Waterloo（页面作者单位）；官方仓库由 xlang-ai 维护
- **时间**：2024　**类型**：官方榜单
- **出处**：<https://os-world.github.io>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：主办机构：页面作者单位为 "1The University of Hong Kong, 2Salesforce Research, 3Carnegie Mellon University, 4University of Waterloo"，并声明 "These are official results evaluated by our team under unified settings and environment."；会议：本页未标注会议，官方仓库标题标 "[NeurIPS 2024]"（github.com/xlang-ai/OSWorld，2026-11-06 打开）；公开榜单成绩：字段 "Success Rate (Avg±Std)"，Rank 1 为 "86.0%"（claude-fable-5）、榜末 Rank 68 为 "3.0%"，摘要另给人类 "over 72.36%" 与当时最佳模型 "12.24% success"；GitHub star 数：xlang-ai/OSWorld 3253 stars（来源 api.github.com/repos/xlang-ai/OSWorld，查询日期 2026-11-06）
- **页面依据**："We also create a benchmark of 369 real-world computer tasks in OSWorld with reliable, reproducible setup and evaluation scripts."；"Rank Model & Date Approach & Details Success Rate (Avg±Std)"；"OSWorld contains a total of 369 tasks (and an additional 43 tasks on Windows for analysis)."
- **要点**：369 个真实计算机任务（8 个 Google Drive 任务可排除后按 361 个评测，另有 43 个 Windows 分析任务），环境跨 "across various operating systems such as Ubuntu, Windows, and macOS" 且含 "# Exec.-based Eval. Func. 134" 个执行式评估函数，指标为 "Success Rate (Avg±Std)"。官方榜单区间 3.0%–86.0%，页面摘要为人类 "over 72.36%"、当时最佳模型 "12.24% success"。
- **与主题关联**：在真实桌面 OS 上用执行式脚本按最终状态判分，直接衡量本地 CUA 能否真正完成跨应用电脑任务而非只做文本推理。

#### 184｜OSWorld 2.0（OSWorld-V2 官方项目主页与 Leaderboard）

- **检索号**：T-02　**类别**：T CUA 评测基准、数据集与公开榜单　**轮次**：第二轮
- **作者 / 机构**：XLANG Lab, University of Hong Kong（页面第一作者单位 "1[XLANG Lab, University of Hong Kong](https://xlang.ai/)"），另列 UCSD、Columbia、UCSB、Mila、Alibaba Qwen、OSU、Simular 等 12 家单位；页面未明示维护方
- **时间**：2026　**类型**：官方榜单
- **出处**：<https://osworld-v2.xlang.ai>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验
- **影响力**：主办机构：页面作者单位首位 "XLANG Lab, University of Hong Kong"，仓库/数据集/站点线索为 "xlang-ai" / "xlangai" / "osworld-v2.xlang.ai"；会议：页面未标注，未核实；公开榜单成绩："Last update time: 2026-10-15"，Rank 1 "Claude Opus 5"（Anthropic）为 "44.33%" binary accuracy 与 "77.67%" Partial，摘要主结果为 "Claude Opus 4.8 ... completes only 20.6% of tasks at a 54.8% partial score"；GitHub star 数：xlang-ai/OSWorld-V2 411 stars（来源 api.github.com/repos/xlang-ai/OSWorld-V2，查询日期 2026-11-06）
- **页面依据**："We introduce OSWorld 2.0, a benchmark of 108 long-horizon computer-use workflows spanning everyday and professional tasks."；"Under our primary binary-completion metric at 500 steps"；"Last update time: 2026-10-15"；"31 Self-hosted websites"
- **要点**：108 个长时程计算机工作流、31 个 "Self-hosted websites"、"69.6% Tasks >1h"，人类中位耗时约 1.6 小时、平均 "27.25 Avg. scoring checkpoints"，主指标为 "primary binary-completion metric at 500 steps" 并辅以 "Partial reward"。覆盖 7 个专业域 21 个子类与动态/流式交互场景，榜单榜首 44.33%。
- **与主题关联**：把任务拉长到以小时计的端到端办公流程并含中途状态变化，检验本地 CUA 在长链路状态跟踪下是否仍真正可用。

#### 185｜AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents | AndroidWorld

- **检索号**：T-03　**类别**：T CUA 评测基准、数据集与公开榜单　**轮次**：第二轮
- **作者 / 机构**：Google DeepMind、Google（页面作者标注 "1 Google DeepMind 2 Google"）
- **时间**：2024　**类型**：官方数据集页
- **出处**：<https://google-research.github.io/android_world>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：主办机构：页面作者标注 "1 Google DeepMind 2 Google"，代码仓库为 google-research/android_world（README 附 "*This is not an officially supported Google product.*"）；会议：页面未标注，未核实；公开榜单成绩：页面给出 "M3A can complete 30.6% of AndroidWorld's tasks"（排行榜为外部 Google Sheets 链接，本页无排名表）；GitHub star 数：google-research/android_world 1005 stars（来源 api.github.com/repos/google-research/android_world，查询日期 2026-11-06）
- **页面依据**："a fully functional Android environment that provides reward signals for 116 programmatic tasks across 20 real-world Android apps"；"M3A can complete 30.6% of AndroidWorld's tasks"；"📝 116 diverse tasks across 20 real-world apps"
- **要点**：116 个程序化任务覆盖 20 个真实 Android 应用，运行于 "It runs on a live Android emulator"，"Durable reward signals" 由设备系统状态导出并可动态实例化出 "millions of unique task variations"。轻量占用 "2 GB memory, 8 GB disk"，M3A 基线成功率 30.6%。
- **与主题关联**：在可动态构造、以设备系统状态判分的真实移动环境里测本地 GUI 代理的成功率与鲁棒性。

#### 186｜[NeurIPS'23 Spotlight] Mind2Web: Towards a Generalist Agent for the Web（官方仓库）

- **检索号**：T-04　**类别**：T CUA 评测基准、数据集与公开榜单　**轮次**：第二轮
- **作者 / 机构**：The Ohio State University（OSU-NLP-Group；联系人 Xiang Deng, Huan Sun, Yu Su）
- **时间**：2023　**类型**：官方仓库
- **出处**：<https://github.com/OSU-NLP-Group/Mind2Web>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：主办机构：页面 "The Ohio State University"，仓库组织 "OSU-NLP-Group"；会议：页面标题 "[NeurIPS'23 Spotlight]"；公开榜单成绩：仓库未设排行榜，给出候选生成 "Recall@50 ~ 85%" 及论文口径 "macro average accuracy, which is the one we reported in the paper"；GitHub star 数：1036 stars（来源 api.github.com/repos/OSU-NLP-Group/Mind2Web，查询日期 2026-11-06）
- **页面依据**："over 2,000 open-ended tasks collected from 137 websites spanning 31 domains"；"macro average accuracy"；"use of real-world websites instead of simulated and simplified ones"
- **要点**：2000+ 开放式任务、137 个真实网站、31 个域，附众包动作序列，动作空间为 CLICK/TYPE/SELECT；数据划分 train 1,009 / Cross Task 252 / Cross Website 177 / Cross Domain 912，指标为 "macro average accuracy"（另有 "micro average accuracy" 与 "Recall@50 ~ 85%"）。
- **与主题关联**：以真实网站快照与动作序列评测跨站/跨域泛化，衡量本地 CUA 面对未见网页时的元素定位与动作预测能力。

#### 187｜WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models（官方仓库）

- **检索号**：T-05　**类别**：T CUA 评测基准、数据集与公开榜单　**轮次**：第二轮
- **作者 / 机构**：维护者 GitHub 用户 MinorJerry；README Disclaimer 声明 "This is not an officially supported Tencent product."（Citation 作者 He, Yao, Ma, Yu, Dai, Zhang, Lan, Yu）
- **时间**：2024　**类型**：官方仓库
- **出处**：<https://github.com/MinorJerry/WebVoyager>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：主办机构：仓库未明示机构（Disclaimer 提及 Tencent 但声明非官方支持），未核实；会议：页面未标注，Citation 为 "arXiv preprint arXiv:2401.13919"，未核实；公开榜单成绩：本仓库无榜单；第三方公开聚合榜单 leaderboard.steel.dev 的 WebVoyager 页显示 "643 tasks across 15 popular real-world websites"、榜首 "browser-control (Fable 5) 99.19%"（来源 https://leaderboard.steel.dev/ ，2026-11-06 打开，非官方榜单，数字来自该页）；GitHub star 数：1129 stars（来源 api.github.com/repos/MinorJerry/WebVoyager，查询日期 2026-11-06）
- **页面依据**："we utilize a semi-automated approach to generate and filter 643 task queries, covering 15 websites, with each website containing 40+ queries"；"We propose an automated evaluation protocol using GPT-4V."；"We build an online web browsing environment using Selenium."
- **要点**：643 个任务查询覆盖 15 个真实网站（每站 40+ 查询），环境为 Selenium 构建的在线真实网页浏览，数据集在 "data/WebVoyager_data.jsonl" 并另附从 GAIA 抽取的 90 个网页任务。指标为 GPT-4V 自动评测（"GPT-4V Based Auto Evaluation"）辅以人工评测，"--max_iter 15" 步内未完成即判失败。
- **与主题关联**：在实时真实网站上做端到端多模态浏览评测，检验本地 CUA 面对网页改版、弹窗与时效信息时能否真正完成用户指令。

#### 188｜Windows Agent Arena: Evaluating Multi-modal OS Agents at Scale

- **检索号**：T-06　**类别**：T CUA 评测基准、数据集与公开榜单　**轮次**：第二轮
- **作者 / 机构**：Microsoft（页面机构栏 "Microsoft"；合作者 Carnegie Mellon University、Columbia University）
- **时间**：2024　**类型**：官方榜单
- **出处**：<https://microsoft.github.io/WindowsAgentArena>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：主办机构：页面作者机构 "Microsoft"（另有 "Carnegie Mellon University"、"Columbia University"），BibTeX 写 "institution = {Microsoft}, year = {2024}"；会议：页面未标注（BibTeX 为技术报告 @article），未核实；公开榜单成绩：页面 Results 段给出 "Navi ... can achieve a success rate of 19.5%, compared to 74.5% for human performance"，本页为基线结果而非持续更新排名表；GitHub star 数：microsoft/WindowsAgentArena 915 stars（来源 api.github.com/repos/microsoft/WindowsAgentArena，查询日期 2026-11-06）
- **页面依据**："Our initial release consists of 154 diverse tasks spanning applications"；"Navi, showing it can achieve a success rate of 19.5%, compared to 74.5% for human performance"；"a full benchmark evaluation in as little as 20 minutes"
- **要点**：154 个 Windows 11 真实 OS 任务，覆盖 LibreOffice Calc/Writer、Edge/Chrome、VS Code、VLC、Notepad/Clock/Paint 与 File Explorer/Settings，"Task evaluation is deterministic" 用自定义脚本在每集末尾给 reward。Azure 并行可在 "as little as 20 minutes" 跑完全量，Navi 19.5% vs 人类 74.5%。
- **与主题关联**：专注 Windows 真实桌面环境，直接检验本地 CUA 在日常 Windows 应用与系统设置中的可用性。

#### 189｜ScreenSpot-Pro: GUI Grounding for Professional High-Resolution Computer Use（Hugging Face 官方数据集页）

- **检索号**：T-07　**类别**：T CUA 评测基准、数据集与公开榜单　**轮次**：第二轮
- **作者 / 机构**：数据集由 Hugging Face 用户 "likaixin" 维护；Citation 作者 Kaixin Li、Ziyang Meng、Hongzhan Lin、Ziyang Luo、Yuchen Tian、Jing Ma、Zhiyong Huang、Tat-Seng Chua
- **时间**：2025　**类型**：官方数据集页
- **出处**：<https://huggingface.co/datasets/likaixin/ScreenSpot-Pro>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「likaixin/ScreenSpot-Pro · Datasets at Hugging Face（含官方 leaderboard 与 citation）」
- **影响力**：主办机构：页面数据集所有者 "likaixin"，Citation 为 "@misc{screenspotpro, ... year = {2025}, note = {Preprint}}"，具体机构未标注，未核实；会议：页面未标注会议，未核实；公开榜单成绩：页面 leaderboard "SCORE" 榜首 "beipo-ai/NorthCUA-Pro 93.3"、"beipo-ai/NorthCUA-Mini 92.4"、"meta-models/Muse-Glimmer-30B 75.4"；同源官方榜单 https://gui-agent.github.io/grounding-leaderboard/ 榜首为 "85.1%"（原文 "Micro-average numbers are reported."，2026-11-06 打开，与 HF 榜口径/时间不同）；GitHub star 数：likaixin2000/ScreenSpot-Pro-GUI-Grounding 398 stars（来源 api.github.com/repos/likaixin2000/ScreenSpot-Pro-GUI-Grounding，查询日期 2026-11-06），HF 页面 "Like 70"
- **页面依据**："ScreenSpot-Pro: GUI Grounding for Professional High-Resolution Computer Use"；"Size: 1K<n<10K"；"Data Details" 表头 "Category Abbr. Application Edition & Version OS Icons Texts"
- **要点**：数据集规模标注 "1K<n<10K"，Data Details 表覆盖 Development and Programming、Creative、CAD and Engineering、Scientific and Analytical、Office Suite、Operating System Commons 共 6 类 23 款专业软件（VS Code、Photoshop、AutoCAD、MATLAB、Word、Windows 11 等）。环境跨 macOS / Windows / Linux（Ubuntu 24.04），每条样本含 Icons/Texts 标注与 bbox，指标为 leaderboard 的 Overall "SCORE"（最高 93.3）。
- **与主题关联**：GUI grounding（按指令在截图中定位元素）是本地 CUA 点击操作的底层能力，该页量化代理在专业高分屏软件中的定位准确度。

#### 190｜GitHub - web-arena-x/visualwebarena: VisualWebArena is a benchmark for multimodal agents. · GitHub

- **检索号**：T-08　**类别**：T CUA 评测基准、数据集与公开榜单　**轮次**：第二轮
- **作者 / 机构**：GitHub 组织 "web-arena-x"（README 未列作者单位，未核实）
- **时间**：2024　**类型**：官方仓库
- **出处**：<https://github.com/web-arena-x/visualwebarena>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：主办机构：GitHub 组织 "web-arena-x"（README 未列作者单位，未核实）；会议：README 把本文标为 "arXiv preprint arXiv:2401.13649"，其引用的 WebArena 条目为 "journal={ICLR}"，本文会议未标注，未核实；公开榜单成绩：README 未给模型榜单分数，仅 "with a human success rate of ~89%"（基于 "We collected human trajectories on 233 tasks"）；GitHub star 数：490 stars（来源 api.github.com/repos/web-arena-x/visualwebarena，查询日期 2026-11-06）
- **页面依据**："full set of 910 VWA tasks"；"It builds off the reproducible, execution based evaluation introduced in WebArena."；"with a human success rate of ~89%"
- **要点**：910 个视觉接地任务，自托管环境含 CLASSIFIEDS / SHOPPING / REDDIT / WIKIPEDIA / HOMEPAGE（并可复用 WebArena 的 CMS、GitLab、map），采用 "execution based evaluation" 与 Set-of-Marks 标注。另有 233 个任务的人类轨迹，人类成功率 "~89%"。
- **与主题关联**：要求代理读页面截图而非仅读 DOM 文本，检验本地 CUA 在真实视觉网页上的多模态理解与执行式完成度。

#### 191｜SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents（ScreenSpot 官方发布仓库）

- **检索号**：T-09　**类别**：T CUA 评测基准、数据集与公开榜单　**轮次**：第二轮
- **作者 / 机构**：GitHub 用户 "njucckevin"（Citation 作者 Kanzhi Cheng、Qiushi Sun、Yougang Chu 等；页面未明示机构，未核实）
- **时间**：2024　**类型**：官方仓库
- **出处**：<https://github.com/njucckevin/SeeClick>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：主办机构：GitHub 用户 "njucckevin"（页面未明示机构，未核实）；会议："SeeClick is accepted by ACL 2024."，Citation 为 "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)"；公开榜单成绩：页面 "Evaluation Results" 表 Average 列给出 "SeeClick 9.6B ... 53.4%"、"CogAgent 18B ... 47.4%"、"GPT-4V ... 16.2%"；GitHub star 数：496 stars（来源 api.github.com/repos/njucckevin/SeeClick，查询日期 2026-11-06）
- **页面依据**："ScreenSpot is an evaluation benchmark for GUI grounding, comprising over 1200 instructions from iOS, Android, macOS, Windows and Web environments"；"SeeClick is accepted by ACL 2024."
- **要点**：ScreenSpot 含 "over 1200 instructions"，覆盖 iOS、Android、macOS、Windows、Web 五类环境，样本含 instruction / bbox / data_type（icon 或 text）与平台标注，可从南大云盘或 Google Drive 下载图像与标注。指标为 Mobile/Desktop/Web 各 Text、Icon/Widget 子项及 Average 定位准确率（SeeClick 53.4%、GPT-4V 16.2%）。
- **与主题关联**：作为最早被广泛采用的 GUI grounding 基准，衡量本地 CUA 把自然语言指令落到多平台界面具体坐标的基础能力。

#### 192｜Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?

- **检索号**：T-10　**类别**：T CUA 评测基准、数据集与公开榜单　**轮次**：第二轮
- **作者 / 机构**：The University of Hong Kong、Shanghai Jiao Tong University、Google Cloud AI Research、Google Deepmind、Salesforce Research、Yale University、Sea AI Lab、University of Waterloo（页面 1–8 单位）
- **时间**：2024　**类型**：官方榜单
- **出处**：<https://spider2-v.github.io>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：主办机构：页面作者单位以 "1The University of Hong Kong"、"2Shanghai Jiao Tong University" 为首（共 8 家）；会议：本页未标注，官方仓库标题标 "[NeurIPS 2024]"（github.com/xlang-ai/Spider2-V，2026-11-06 打开）；公开榜单成绩：页面 Benchmarking 表 Rank 1 "Learn-by-interact"（Google Cloud）"16.6"、Rank 2 "GPT-4V (1106)" "14.0"、Rank 3 "GPT-4o (0513)" "13.8"，摘要给出 "14.0% success"；GitHub star 数：xlang-ai/Spider2-V 153 stars（来源 api.github.com/repos/xlang-ai/Spider2-V，查询日期 2026-11-06）
- **页面依据**："featuring 494 real-world tasks in authentic computer environments and incorporating 20 enterprise-level professional applications"；"existing state-of-the-art LLM/VLM-based agents do not reliably automate full data workflows (14.0% success)"；"The interactive environment is a computer desktop of Ubuntu operating system."
- **要点**：494 个真实任务覆盖 20 个企业级数据应用（BigQuery、dbt、Airbyte 等），环境为 Ubuntu 桌面（pyautogui 或 JSON 动作、screenshot 或 a11ytree 观察，改编自 OSWorld），含 "# Exec. Eval. Func. 151" 个执行式评估函数。指标为任务成功率，榜单榜首 16.6、GPT-4V 14.0、逐步指引下 16.2%。
- **与主题关联**：在真实 Ubuntu 桌面上混合 GUI 与代码完成数据工程流程，检验本地 CUA 处理专业软件长流程的可用上限。

#### 193｜The Agent Company — Benchmarking LLM Agents on Consequential Real World Tasks（官方 Leaderboard）

- **检索号**：T-11　**类别**：T CUA 评测基准、数据集与公开榜单　**轮次**：第二轮
- **作者 / 机构**：Carnegie Mellon University、Duke University（页面 "1Carnegie Mellon University 2Independent 3Duke University"）
- **时间**：2024　**类型**：官方榜单
- **出处**：<https://the-agent-company.com>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验
- **影响力**：主办机构：页面作者单位 "1Carnegie Mellon University 2Independent 3Duke University"；会议：页面未标注（仓库 README 引文为 arXiv:2412.14161），未核实；公开榜单成绩："Total of 175" 任务，榜首 "TTE-MatrixAgent + Deepseek-V3.2 42.9%" %Resolved / "52.4%" %Score（2025-11-10），榜尾 "1.1%" / "4.2%"，且 "The leaderboard is updated once a week on Monday."；GitHub star 数：TheAgentCompany/TheAgentCompany 812 stars（来源 api.github.com/repos/TheAgentCompany/TheAgentCompany，查询日期 2026-11-06）
- **页面依据**："The % Resolved metric refers to the percentage of Agent Company Tasks (Total of 175) that were resolved by the model."；"The % Score is a weighted metric combining the sub checkpoint resolution rate and resolution rate (50% each)."；"% Resolved  % Score  Avg Steps  Avg Costs ($)"
- **要点**：175 个任务运行在自托管模拟软件公司环境（GitLab、Plane、ownCloud、RocketChat，含 Software Engineer / Product Manager / Data Scientist / HR / Financial Staff / Administrator 角色），指标为 "% Resolved" 与 "% Score"（子检查点与完成状态各占 50%）并报告 Avg Steps / Avg Costs。榜首 42.9% / 52.4%，每周一更新。（候补）
- **与主题关联**：要求代理像数字员工一样在本地自托管服务里写代码、浏览并与同事沟通后按结果评分，检验本地 CUA 承担真实工作职责的能力。（候补）

#### 194｜GitHub - ServiceNow/WorkArena: WorkArena: How Capable are Web Agents at Solving Common Knowledge Work Tasks? · GitHub

- **检索号**：T-12　**类别**：T CUA 评测基准、数据集与公开榜单　**轮次**：第二轮
- **作者 / 机构**：ServiceNow（README 指向 "ServiceNow platform"；仓库归 GitHub 组织 ServiceNow）
- **时间**：2024　**类型**：官方仓库
- **出处**：<https://github.com/ServiceNow/WorkArena>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：主办机构：GitHub 组织 "ServiceNow"，README 明列 "ServiceNow platform" 与 "ServiceNow instances"；会议：README 明列 "[ICML 2024] WorkArena" 与 "[NeurIPS 2024] WorkArena++"；公开榜单成绩：README 未给数值成绩，指向 "unified leaderboard"（https://huggingface.co/spaces/ServiceNow/browsergym-leaderboard）并称 "this benchmark is not solved"，未核实具体分数；GitHub star 数：280 stars（来源 api.github.com/repos/ServiceNow/WorkArena，查询日期 2026-11-06）
- **页面依据**："WorkArena-L1 includes 19,912 unique instances drawn from 33 tasks"；"WorkArena++ contains 682 tasks, each one sampling among thousands of potential configurations."；"WorkArena is a suite of browser-based tasks"
- **要点**：WorkArena-L1 含 19,912 个实例 / 33 个原子任务，WorkArena++ 含 682 个组合式任务；环境为 ServiceNow 平台上的 "browser-based tasks"（BrowserGym / AgentLab / Playwright，含 Knowledge Bases、Forms、Service Catalogs、Lists、Menus、Dashboards 组件）。判定为 env.task.validate 的 "reward == 1" 成功信号，正式评估走 "unified leaderboard"。（候补）
- **与主题关联**：在真实企业 SaaS 界面上测知识工作自动化，衡量本地 CUA 处理表单、列表、服务目录等企业 UI 的实用程度。（候补）

### U 类｜视觉语言模型基座（11 篇）

#### 195｜GPT-4 Technical Report

- **检索号**：U-01　**类别**：U 视觉语言模型基座　**轮次**：第二轮
- **作者 / 机构**：OpenAI
- **时间**：2023-03　**类型**：官方技术报告（arXiv 预印本）
- **出处**：<https://arxiv.org/abs/2303.08774>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv:2303.08774，2023-03-15 首发、2024-03-04 修订至 v6；页面给出 "passing a simulated bar exam with a score around the top 10% of test takers" 与 "predict some aspects of GPT-4's performance based on models trained with no more than 1/1,000th the compute of GPT-4"，Comments 标注 "100 pages"；该报告是 GPT-4V 视觉能力的技术来源。GitHub star 数：未核实（闭源模型，无官方代码仓库；所引页面未披露，核验日 2026-11-06）。
- **页面依据**："a large-scale, multimodal model which can accept image and text inputs and produce text outputs"
- **要点**：页面明确模型可接受 image 与 text 输入并输出文本，为 GPT-4V 系列截图理解奠定多模态范式；页面未给出视觉输入分辨率、坐标/grounding 机制与参数量（报告明确不公开架构与规模），仅说明为 Transformer 下一 token 预训练加后训练对齐。
- **与主题关联**：作为闭源旗舰只能经云端 API 充当 CUA 的截图语义理解基座，页面未记载坐标定位能力且无法本地部署。

#### 196｜Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context

- **检索号**：U-02　**类别**：U 视觉语言模型基座　**轮次**：第二轮
- **作者 / 机构**：Gemini Team, Google
- **时间**：2024-03　**类型**：官方技术报告
- **出处**：<https://arxiv.org/abs/2403.05530>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv:2403.05530，2024-03-08 首发、2024-12-16 修订至 v5；页面给出 "near-perfect retrieval (>99%) up to at least 10M tokens"、"26 to 75% time savings across 10 different job categories"，并对比 "Claude 3.0 (200k) and GPT-4 Turbo (128k)"。GitHub star 数：未核实（闭源模型，无官方代码仓库；所引页面未披露，核验日 2026-11-06）。
- **页面依据**："capable of recalling and reasoning over fine-grained information from millions of tokens of context, including multiple long documents and hours of video and audio"
- **要点**：视觉输入以长视频与多文档多模态长上下文为主（页面写明 "hours of video and audio" 与跨模态 needle 检索）；页面未披露屏幕坐标/grounding 细节与参数量，仅给出 Gemini 1.5 Pro 与 "a more lightweight variant designed for efficiency"（Gemini 1.5 Flash）两档规模。
- **与主题关联**：可经 Google 云端 API 一次性读入整段录屏或多帧截图的 CUA 操作轨迹做感知与检索，但为闭源模型、不能本地部署。

#### 197｜Improved Baselines with Visual Instruction Tuning

- **检索号**：U-04　**类别**：U 视觉语言模型基座　**轮次**：第二轮
- **作者 / 机构**：Haotian Liu, Chunyuan Li, Yuheng Li, Yong Jae Lee（LLaVA-1.5；arXiv 页面未逐条标注机构）
- **时间**：2023-10　**类型**：会议论文（CVPR 2024 highlight）
- **出处**：<https://arxiv.org/abs/2310.03744>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Comments 标注 "Camera ready, CVPR 2024 (highlight)"；页面给出 "state-of-the-art across 11 benchmarks"、"merely 1.2M publicly available data"、"~1 day on a single 8-A100 node" 与 "final 13B checkpoint"。GitHub star 数：25,075（来源：GitHub REST API 经本会话本地核验记录 star-evidence.json，仓库 haotian-liu/LLaVA，queried_at 2026-11-06 18:56 +08:00）。
- **页面依据**："the fully-connected vision-language cross-modal connector in LLaVA is surprisingly powerful and data-efficient"
- **要点**：视觉输入为单张图像，使用 "CLIP-ViT-L-336px with an MLP projection"（336px 分辨率），页面明确 13B checkpoint；训练仅需 1.2M 公开数据与单台 8×A100 约 1 天，本地复现门槛低，但页面未涉及屏幕坐标或 grounding 输出。
- **与主题关联**：开源权重、13B 且训练成本极低，适合作为本地 CUA 的通用截图理解基座，但缺页面记载的坐标定位能力，需另补 grounding 才能点选控件。

#### 198｜Qwen2.5-VL Technical Report

- **检索号**：U-05　**类别**：U 视觉语言模型基座　**轮次**：第二轮
- **作者 / 机构**：Shuai Bai 等，Qwen 团队（阿里巴巴；arXiv 页面以作者列表呈现）
- **时间**：2025-02　**类型**：官方技术报告
- **出处**：<https://arxiv.org/abs/2502.13923>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv:2502.13923，2025-02-19 提交；页面给出 "available in three sizes"、"Qwen2.5-VL-72B"、"videos of extended durations (up to hours) with second-level event localization"，并称 72B "matches state-of-the-art models like GPT-4o and Claude 3.5 Sonnet"。GitHub star 数：未核实（本地 star 核验记录中 QwenLM/Qwen2.5-VL 与 Qwen2-VL 条目发生仓库重定向错位、stars 与 forks 与 Qwen3-VL 完全相同，故不予引用；核验日 2026-11-06）。
- **页面依据**："A standout feature of Qwen2.5-VL is its ability to localize objects using bounding boxes or points accurately."
- **要点**：通过 "training a native dynamic-resolution Vision Transformer (ViT) from scratch and incorporating Window Attention" 支持原生动态分辨率、不依赖传统归一化，可用 bounding boxes 或 points 精确定位物体并做 "second-level event localization"；页面写明三档尺寸（含 72B 旗舰）并覆盖 "from edge AI to high-performance computing"，摘要未给屏幕坐标归一化格式。
- **与主题关联**：摘要明确 "as an interactive visual agent capable of reasoning, tool usage, and task execution in real-world scenarios such as operating computers and mobile devices"，是开源可本地部署（含边缘档）的 CUA 截图感知 + 坐标定位基座首选。

#### 199｜Qwen3-VL Technical Report

- **检索号**：U-06　**类别**：U 视觉语言模型基座　**轮次**：第二轮
- **作者 / 机构**：Shuai Bai 等，Qwen 团队（阿里巴巴；arXiv 页面以作者列表呈现）
- **时间**：2025-11　**类型**：官方技术报告
- **出处**：<https://arxiv.org/abs/2511.21631>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv:2511.21631，2025-11-26 提交、2025-11-27 修订至 v2，Comments 标注 "42 pages"；页面给出 "up to 256K tokens"、dense "2B/4B/8B/32B" 与 MoE "30B-A3B/235B-A22B"，并称在 MMMU、MathVista、MathVision 等评测领先。GitHub star 数：未核实（本地 star 核验记录中 Qwen 系列仓库条目发生重定向错位，不予引用；核验日 2026-11-06）。
- **页面依据**："We envision Qwen3-VL serving as a foundational engine for image-grounded reasoning, agentic decision-making, and multimodal code intelligence in real-world workflows."
- **要点**：视觉输入为文本/图像/视频交错的 256K 上下文，采用 "enhanced interleaved-MRoPE"、"DeepStack" 与 "text-based time alignment" 强化时空建模（agent 能力见依据句）；页面给出 dense 与 MoE 两套规模及 "diverse latency-quality trade-offs"，但摘要未给出屏幕坐标或 GUI grounding 的具体输出格式。
- **与主题关联**：官方定位含 agentic decision-making（GUI/agent 能力说明），2B 起的 dense 版本可本地部署、大 MoE 版本可云端调用，适合作为 CUA 长上下文截图/录屏感知基座。

#### 200｜Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling

- **检索号**：U-07　**类别**：U 视觉语言模型基座　**轮次**：第二轮
- **作者 / 机构**：Zhe Chen 等（InternVL 2.5 / OpenGVLab；arXiv 页面未逐条标注机构，摘要指向 HuggingFace 演示 OpenGVLab/InternVL）
- **时间**：2024-12　**类型**：官方技术报告（Comments: "Technical Report"）
- **出处**：<https://arxiv.org/abs/2412.05271>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv:2412.05271，2024-12-06 提交、2025-09-26 修订至 v5；页面给出 "the first open-source MLLMs to surpass 70% on the MMMU benchmark, achieving a 3.7-point improvement through Chain-of-Thought (CoT) reasoning"，并称 "rivaling leading commercial models such as GPT-4o and Claude-3.5-Sonnet"。GitHub star 数：10,169（来源：GitHub REST API 经本会话本地核验记录 star-evidence.json，仓库 OpenGVLab/InternVL，queried_at 2026-11-06 18:56 +08:00）。
- **页面依据**："our model is the first open-source MLLMs to surpass 70% on the MMMU benchmark, achieving a 3.7-point improvement through Chain-of-Thought (CoT) reasoning"
- **要点**：评测覆盖 "visual grounding"、"multi-image / video understanding"、"document understanding" 等，并系统考察 vision encoders、语言模型、数据规模与 test-time 配置的缩放关系；页面仅说明沿用 InternVL 2.0 "core model architecture" 并强化训练/测试策略与数据质量，摘要未披露具体输入分辨率、坐标格式与参数量。
- **与主题关联**：开源 MLLM 系列且评测含 visual grounding 与多图/视频理解，可本地部署并扩展为 CUA 的屏幕视觉感知基座。

#### 201｜Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Vision-Language Models

- **检索号**：U-08　**类别**：U 视觉语言模型基座　**轮次**：第二轮
- **作者 / 机构**：Matt Deitke 等（Allen Institute for AI / University of Washington；页面给出发布页 molmo.allenai.org）
- **时间**：2024-09　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2409.17146>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv:2409.17146，2024-09-25 提交、2024-12-05 修订至 v2；页面给出 "Our best-in-class 72B model"、"second only to GPT-4o based on both academic benchmarks and on a large human evaluation"，并称超越 "Claude 3.5 Sonnet, and Gemini 1.5 Pro and Flash"。GitHub star 数：未核实（所引页面未披露；本会话本地 star 核验记录未含该仓库，核验日 2026-11-06）。
- **页面依据**："an innovative 2D pointing dataset, all collected without the use of external VLMs"
- **要点**：PixMo 含 "innovative 2D pointing dataset"，使模型具备 2D 点指/坐标式 grounding 能力；页面明确 72B 最佳模型并声明 "Our model weights, new datasets, and source code are available"，可完整本地复现，摘要未给输入分辨率。
- **与主题关联**：开放权重加 2D pointing（可映射为屏幕点击坐标），是本地部署 CUA 感知/定位基座的高相关选择。

#### 202｜PaliGemma: A versatile 3B VLM for transfer

- **检索号**：U-09　**类别**：U 视觉语言模型基座　**轮次**：第二轮
- **作者 / 机构**：Lucas Beyer 等（Google；arXiv 页面以作者列表呈现）
- **时间**：2024-07　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2407.07726>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv:2407.07726，2024-07-10 提交、2024-10-10 修订至 v2（Comments: "v2 adds Appendix H and I and a few citations"）；页面给出 "almost 40 diverse tasks including standard VLM benchmarks ... remote-sensing and segmentation"，标题标注 3B。GitHub star 数：未核实（所引页面未披露；本会话本地 star 核验记录未含该仓库，核验日 2026-11-06）。
- **页面依据**："PaliGemma is an open Vision-Language Model (VLM) that is based on the SigLIP-So400m vision encoder and the Gemma-2B language model."
- **要点**：以 SigLIP-So400m 视觉编码器 + Gemma-2B 语言模型构成 3B 开放 VLM，评测覆盖近 40 类任务并含 segmentation 等稠密预测；页面摘要未给出输入分辨率、屏幕坐标或 grounding 输出格式，也未给部署硬件要求，仅强调 "effective to transfer" 的基座定位。
- **与主题关联**：3B 开放权重、体量小，适合在消费级本地硬件上微调为 CUA 截图编码器，但页面未记载坐标 grounding，需配合专用定位模块。

#### 203｜Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding

- **检索号**：U-10　**类别**：U 视觉语言模型基座　**轮次**：第二轮
- **作者 / 机构**：Kenton Lee, Mandar Joshi 等（Google Research；arXiv 页面未逐条标注机构）
- **时间**：2022-10　**类型**：会议论文（ICML 2023；Comments: "Accepted at ICML"）
- **出处**：<https://arxiv.org/abs/2210.03347>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv:2210.03347，2022-10-07 提交、2023-06-15 修订至 v2；Comments 标注 "Accepted at ICML"；页面给出 "achieve state-of-the-art results in six out of nine tasks across four domains: documents, illustrations, user interfaces, and natural images"。GitHub star 数：未核实（所引页面未披露；本会话本地 star 核验记录未含该仓库，核验日 2026-11-06）。
- **页面依据**："we introduce a variable-resolution input representation and a more flexible integration of language and vision inputs, where language prompts such as questions are rendered directly on top of the input image"
- **要点**：预训练目标为 "parse masked screenshots of web pages into simplified HTML"，提出 variable-resolution 输入表示并把问题文本直接渲染到输入图像上；页面摘要未给参数量、部署要求或屏幕坐标输出，但明确覆盖 "user interfaces" 域。
- **与主题关联**：奠定「截图→结构化界面表示」的视觉语言预训练范式，可作为本地 CUA 屏幕解析模块的技术源头（非通用大模型基座）。

#### 204｜SmolVLM: Redefining small and efficient multimodal models

- **检索号**：U-11　**类别**：U 视觉语言模型基座　**轮次**：第二轮
- **作者 / 机构**：Andrés Marafioti 等（Hugging Face；arXiv 页面以作者列表呈现）
- **时间**：2025-04　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2504.05299>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：候补条目。arXiv:2504.05299，2025-04-07 提交；页面给出 "SmolVLM-256M, uses less than 1GB GPU memory during inference and outperforms the 300-times larger Idefics-80B model"、"18-month development gap"、"largest model, at 2.2B parameters, rivals state-of-the-art VLMs consuming twice the GPU memory"。GitHub star 数：未核实（所引页面未披露；本会话本地 star 核验记录未含该仓库，核验日 2026-11-06）。
- **页面依据**："Our smallest model, SmolVLM-256M, uses less than 1GB GPU memory during inference"
- **要点**：页面强调 "aggressive yet efficient tokenization" 并支持图像与视频理解，最小 256M 推理显存 <1GB、最大 2.2B，明确面向 "mobile and edge devices" / "on-device applications"；摘要未给出输入分辨率、坐标或 grounding 能力说明。
- **与主题关联**：显存 <1GB 的开源小模型是本地/边缘 CUA 截图编码最现实的候选，但页面未记载坐标 grounding，须配合专用 GUI 定位模块使用。

#### 205｜A Survey on Multimodal Large Language Models

- **检索号**：U-12　**类别**：U 视觉语言模型基座　**轮次**：第二轮
- **作者 / 机构**：Shukang Yin, Chaoyou Fu 等（arXiv 页面未逐条标注机构）
- **时间**：2023-06　**类型**：arXiv 预印本（期刊综述）
- **出处**：<https://arxiv.org/abs/2306.13549>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：候补条目。arXiv:2306.13549，2023-06-23 首发、2024-11-29 修订至 v4；Comments 标注 "Accepted for publication in National Science Review"，页面列出相关 DOI 10.1093/nsr/nwae403；摘要给出扩展技术 "Multimodal ICL (M-ICL), Multimodal CoT (M-CoT), and LLM-Aided Visual Reasoning (LAVR)"；页面本身未给出量化成绩数字。GitHub star 数：未核实（页面仅给出 GitHub 论文列表链接 https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models，未给计数；核验日 2026-11-06）。
- **页面依据**："Multimodal Large Language Model (MLLM) represented by GPT-4V has been a new rising research hotspot, which uses powerful Large Language Models (LLMs) as a brain to perform multimodal tasks"
- **要点**：综述系统梳理 MLLM 的 "architecture, training strategy and data, as well as evaluation"，并讨论扩展到 "more granularity, modalities, languages, and scenarios" 及 M-ICL / M-CoT / LAVR；属综述性质，页面未给出具体视觉输入分辨率、坐标/grounding 机制、参数量或部署要求。
- **与主题关联**：不直接充当感知基座，但为 CUA 在云端 API 与本地开源 VLM 之间的选型提供架构、训练与评测的背景框架。

### V 类｜长程规划、经验学习、失败恢复、人在回路（10 篇）

#### 206｜Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models

- **检索号**：V-01　**类别**：V 长程规划、经验学习、失败恢复、人在回路　**轮次**：第二轮
- **作者 / 机构**：Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang；University of Illinois Urbana-Champaign / Lapis Labs（arXiv HTML 首页 affiliation 原文）
- **时间**：2023-10（v1）/ 2024-06（v3）　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2310.04406>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv:2310.04406，v1 2023-10-06、v3 2024-06-06；arXiv 摘要页报告 GPT-4 在 HumanEval 上 pass@1 达 92.7%、GPT-3.5 在 WebShop 平均得分 75.9（"comparable to gradient-based fine-tuning"）。检索结果显示该文收录于 ICML 2024（PMLR），但 arXiv 页面本身未标注会议，故会议信息标注为「检索结果确认」
- **页面依据**：「the first general framework that synergizes the capabilities of LMs in reasoning, acting, and planning」「LATS achieves state-of-the-art pass@1 accuracy (92.7%) for programming on HumanEval with GPT-4」
- **要点**：把蒙特卡洛树搜索引入 LM 智能体，配合 LM 驱动的价值函数与自我反思（self-reflections）做审慎探索，并用外部环境反馈形成自适应解题闭环。页面给出可核实量化结果：HumanEval pass@1 92.7%（GPT-4）、WebShop 平均分 75.9（GPT-3.5，与梯度微调相当）。
- **与主题关联**：为本地 CUA 提供「多步候选动作搜索 + 反思回溯」的长任务规划骨架，出错时可在树中转向而非一条道走到黑。

#### 207｜ExpeL: LLM Agents Are Experiential Learners

- **检索号**：V-02　**类别**：V 长程规划、经验学习、失败恢复、人在回路　**轮次**：第二轮
- **作者 / 机构**：Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, Gao Huang；Department of Automation / Department of Computer Science, BNRist, Tsinghua University（arXiv HTML 首页 affiliation 原文）
- **时间**：2023-08（v1）/ 2024-12（v3）　**类型**：会议论文（AAAI-24）
- **出处**：<https://arxiv.org/abs/2308.10144>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv comments 明确「Accepted by the 38th Annual AAAI Conference on Artificial Intelligence (AAAI-24)」；摘要只给定性结论「a consistent enhancement in its performance as it accumulates experiences」，具体提升幅度页面未给出，标注为「未核实」
- **页面依据**：「Accepted by the 38th Annual AAAI Conference on Artificial Intelligence (AAAI-24)」「Our agent autonomously gathers experiences and extracts knowledge using natural language from a collection of training tasks.」
- **要点**：ExpeL 无需更新模型参数，自主收集训练任务经验并用自然语言抽取可复用 insights，推理时召回 insights 与相似过往轨迹辅助决策；页面称性能随经验累积「consistent enhancement」，并观察到涌现能力与迁移学习潜力。具体百分比未在页面给出（未核实）。
- **与主题关联**：让本地 CUA 把每一次桌面任务轨迹沉淀为可检索经验，长任务链越跑越稳、失败后可复用教训而非从零重试。

#### 208｜Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents

- **检索号**：V-03　**类别**：V 长程规划、经验学习、失败恢复、人在回路　**轮次**：第二轮
- **作者 / 机构**：Pranav Putta, Edmund Mills, Naman Garg, Sumeet Motwani, Chelsea Finn, Divyansh Garg, Rafael Rafailov；The AGI Company (MultiOn) / Stanford University（arXiv HTML 首页 affiliation 原文）
- **时间**：2024-08　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2408.07199>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv 摘要页报告真实预订场景 Llama-3 70B zero-shot 成功率从 18.6% 提升到 81.7%（"a 340% relative increase"），开启在线搜索后进一步到 95.4%；仅一天数据采集
- **页面依据**：「combines guided Monte Carlo Tree Search (MCTS) search with a self-critique mechanism and iterative fine-tuning」「boosts Llama-3 70B model's zero-shot performance from 18.6% to 81.7% success rate (a 340% relative increase)」
- **要点**：用引导式 MCTS 搜索 + 自我批评 + DPO 离线偏好迭代微调，使智能体同时从成功与失败轨迹学习，缓解 compounding errors；WebShop 上超过行为克隆与强化微调基线，配备在线搜索后超过平均人类表现。
- **与主题关联**：为本地 CUA 提供「先搜索多步动作、再自我批评纠错」的长链决策与失败学习闭环，直接提升真实桌面的多步任务完成率。

#### 209｜Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control

- **检索号**：V-04　**类别**：V 长程规划、经验学习、失败恢复、人在回路　**轮次**：第二轮
- **作者 / 机构**：Longtao Zheng, Rundong Wang, Xinrun Wang, Bo An；NTU, Singapore（arXiv HTML 首页 affiliation 原文）
- **时间**：2023-06（v1）/ 2024-01（v3）　**类型**：会议论文（ICLR 2024）
- **出处**：<https://arxiv.org/abs/2306.07863>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv comments 明确「ICLR 2024」并给出项目页 https://ltzheng.github.io/Synapse；摘要页报告 MiniWoB++ 64 任务平均成功率 99.2%（"a 10% relative improvement"），Mind2Web 平均步成功率较先前 SOTA 提示方案相对提升 56%
- **页面依据**：「trajectory-as-exemplar prompting, which prompts the LLM with complete trajectories of the abstracted states and actions」「Synapse achieves a 99.2% average success rate (a 10% relative improvement) across 64 tasks using demonstrations from only 48 tasks.」
- **要点**：三件套——状态抽象（滤除任务无关信息以塞进更多示例）、完整轨迹作为示例提示、示例嵌入记忆的相似度检索，专攻长程任务与 novel task 泛化；是首个在 MiniWoB++ 解决 book-flight 任务的 ICL 方法，Mind2Web 步级成功率相对提升 56%。
- **与主题关联**：直接面向 computer control，用过往完整操作轨迹做示例，让本地 CUA 在长任务链上复用经验并泛化到没做过的新任务。

#### 210｜Agent Workflow Memory

- **检索号**：V-05　**类别**：V 长程规划、经验学习、失败恢复、人在回路　**轮次**：第二轮
- **作者 / 机构**：Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, Graham Neubig；Carnegie Mellon University / Massachusetts Institute of Technology（arXiv HTML 首页 affiliation 原文）
- **时间**：2024-09　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2409.07429>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv 摘要页报告在 Mind2Web 与 WebArena 上相对成功率分别提升 24.6% 与 51.1%，且减少 WebArena 成功任务所需步数；跨任务/网站/领域泛化随训练-测试分布差距扩大超出基线 8.9 至 14.0 个绝对点
- **页面依据**：「AWM substantially improves the baseline results by 24.6% and 51.1% relative success rate on Mind2Web and WebArena while reducing the number of steps taken to solve WebArena tasks successfully.」
- **要点**：从过往经验中归纳常被复用的例程（workflows），并选择性注入以指导后续生成，支持离线预先归纳与在线即时归纳两种模式；实验覆盖 Mind2Web 与 WebArena 共 1000+ 任务、200+ 领域。
- **与主题关联**：把长任务中反复出现的子流程固化成工作流，本地 CUA 可直接调用，缩短任务链、减少步数并降低长链出错概率。

#### 211｜A Survey on (M)LLM-Based GUI Agents

- **检索号**：V-08　**类别**：V 长程规划、经验学习、失败恢复、人在回路　**轮次**：第二轮
- **作者 / 机构**：Fei Tang, Haolei Xu, Hang Zhang, Siqi Chen, Xingyu Wu, Yongliang Shen, Wenqi Zhang, Guiyang Hou, Zeqi Tan, Yuchen Yan, Kaitao Song, Jian Shao, Weiming Lu, Jun Xiao, Yueting Zhuang；Zhejiang University / Microsoft Research Asia（arXiv HTML 首页 affiliation 原文）
- **时间**：2025-03（v1）/ 2025-06（v2）　**类型**：综述
- **出处**：<https://arxiv.org/abs/2504.13865>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv:2504.13865，v1 2025-03-27、v2 2025-06-04，主分类 cs.HC；页面明确把 planning 列为四大组件之一并点名 long-horizon planning 为核心挑战。页面未给出引用数或量化提升，标注为「未核实」
- **页面依据**：「(3) planning frameworks that leverage advanced reasoning methodologies for task decomposition and execution」「including accurate element localization, effective knowledge retrieval, long-horizon planning, and safety-aware execution control」
- **要点**：系统梳理 GUI agent 的 four fundamental components（感知、探索/知识库构建、规划、交互），其中探索机制明确包含 historical experience，规划章节覆盖任务分解与执行；并批评现有评测基准在 long-horizon planning 上的局限。摘要未给量化结果（未核实）。
- **与主题关联**：为本地 CUA 的规划与经验模块提供完整技术地图，并给出长程规划、知识检索等挑战清单，便于定位失败恢复与人在回路的缺口。

#### 212｜Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks

- **检索号**：V-09　**类别**：V 长程规划、经验学习、失败恢复、人在回路　**轮次**：第二轮
- **作者 / 机构**：Zhenhailong Wang, Haiyang Xu, Junyang Wang, Xi Zhang, Ming Yan, Ji Zhang, Fei Huang, Heng Ji；University of Illinois Urbana-Champaign / Alibaba Group（arXiv HTML 首页 affiliation 原文）
- **时间**：2025-01　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2501.11733>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv 摘要页报告「a 22% absolute improvement over previous state-of-the-art approaches across three foundation model backbones」；给出项目页 https://x-plug.github.io/MobileAgent，并配套 Mobile-Eval-E 长程多 App 基准
- **页面依据**：「a hierarchical multi-agent framework capable of self-evolution through past experience」「a novel self-evolution module which maintains a persistent long-term memory comprising Tips and Shortcuts」「Mobile-Agent-E achieves a 22% absolute improvement over previous state-of-the-art approaches across three foundation model backbones.」
- **要点**：层次多代理框架，Manager 拆子目标，Perceptor/Operator/Action Reflector/Notetaker 分别负责感知、执行、错误校验与信息聚合；持久长期记忆含 Tips（经验教训）与 Shortcuts（可复用原子操作序列），实现自我进化，绝对提升 22%。
- **与主题关联**：self-evolving 让本地 CUA 把教训与可复用操作序列沉淀下来，并由专门 Action Reflector 在长任务链中即时校验、纠错。

#### 213｜CUA-Recovery: Benchmarking Error Recovery in Long-Horizon Computer-Use Agents

- **检索号**：V-10　**类别**：V 长程规划、经验学习、失败恢复、人在回路　**轮次**：第二轮
- **作者 / 机构**：Xu Hu, Haoming Li, Yuxiang Wang, Jinxin Yang, Kangshuo Li, Licheng Wang, Dingyi Kang, Jiayu Song, Tianhao Wang, Zhanhua Hu, Xu Yang, Qiannan Li, Bingzhe Li, Feng Chen；University of Texas at Dallas / University of Manchester / Rice University / University of Texas at Austin / University of California, Davis / Independent Researcher（arXiv HTML 首页 affiliation 原文）
- **时间**：2026-10　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2610.27645>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv 摘要页给出测试集 2,250 个人工核验错误状态 / 100 任务、训练集 8.6K 轨迹 / 377 任务；六个代理、六种接管深度下 EAR 最高仅 44.0%、Pass@3 最高 25.5%；微调 Qwen3.5-35B-A3B 后 EAR 19.9%→35.2%、Rubric 5.0%→16.1%，MyPCBench +15.3、Odysseys +10.8（Pass@3）
- **页面依据**：「undetected errors can silently corrupt persistent state and cause cascading failures in subsequent actions」「Across six agents and six takeover depths, Error Awareness Rate (EAR) reaches at most 44.0% and Pass@3 at most 25.5%.」
- **要点**：用 ReRail 在持久桌面环境把 MyPCBench 任务合成为长程工作流、收集多策略「经验证器确认」的真实失败并转成可验证恢复轨迹，构建 CUA-Recovery 测试/训练集；评测显示现有代理既难察觉继承错误也难完成任务，而微调训练轨迹可同时提升恢复与从干净起点完成任务的能力。
- **与主题关联**：专门度量并训练本地 CUA 在长程跨应用任务中的「出错能发现、人能接管（takeover depths）、能恢复」能力，是失败恢复最贴合的一条。

#### 214｜LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks

- **检索号**：V-11（候补）　**类别**：V 长程规划、经验学习、失败恢复、人在回路　**轮次**：第二轮
- **作者 / 机构**：Ziyu Ma, Hailang Huang, Shun Zou, Yong Wang, Shidong Yang, Yiming Hu, Fei Wei, XiangXiang Chu；AMAP-ML（GitHub 组织 AMAP-ML，阿里巴巴高德机器学习团队；机构归属据组织名，未在页面逐字标注）
- **时间**：2026-08　**类型**：官方仓库（附 arXiv 技术报告）
- **出处**：<https://github.com/AMAP-ML/LongHorizon-Harness>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub 官方 API https://api.github.com/repos/AMAP-ML/LongHorizon-Harness 于 2026-11-06 查询显示 stargazers_count = 1852、forks_count = 195、created_at 2026-08-04；arXiv 摘要页报告 Qwen3.7-Plus 在 WeaveBench 从 51.8% 提升到 80.7%
- **页面依据**：「Plan → act → verify → checkpoint or recover → repeat — until the work is actually done.」（README 原文）「LongHorizon-Harness improves Qwen 3.7-Plus from 51.8% to 80.7% on WeaveBench」（arXiv 摘要原文）
- **要点**：把长程执行重述为「任务状态管理」问题，Manage-Execute-Audit（MEA）循环用显式外置状态、全新上下文执行器与只读审计器核验环境结果，仅用独立核验过的事实更新状态，失败证据回灌下一轮；跨模型与 harness 一致提升：Terminal-Bench 2.1 69.7%→77.2%、OSWorld 2.0 2.8%→8.3%，Claude Opus 4.7 在 OSWorld2.0 子集 20.0%→34.3%。
- **与主题关联**：给出本地 CUA 跑几十小时的工程骨架——状态外置、逐步核验、失败可恢复、进度可保存，直接对应 long-horizon computer use harness。

#### 215｜DeskCraft: Benchmarking Desktop Agents on Professional Workflows and Human-in-the-Loop Collaboration

- **检索号**：V-12（候补）　**类别**：V 长程规划、经验学习、失败恢复、人在回路　**轮次**：第二轮
- **作者 / 机构**：Wenkai Wang, Tao Xiong, Jingchen Ni, Yunpeng Bao, Xiyun Li, Tianqi Liu, Hongcan Guo, Zilong Huang, Shengyu Zhang；Zhejiang University / Tsinghua University / Tencent / The University of Hong Kong（arXiv HTML 首页 affiliation 原文）
- **时间**：2026-06　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2606.03103>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv 摘要页报告在 538 个任务上评测 18 个专有与开源代理，GPT-5.4 标准任务 31.6%、交互任务 27.6%；长程任务要求「over 50 execution steps」；代码/数据将开源于 https://github.com/mrwwk/DeskCraft
- **页面依据**：「Mid-turn interaction captures both agent-initiated clarification under uncertainty and user-initiated interruption during execution」「We evaluate 18 proprietary and open source agents on 538 tasks and find that GPT-5.4 reaches 31.6% on standard tasks and 27.6% on interactive tasks.」
- **要点**：面向专业创意/工程桌面软件（设计、视频、音频、3D）的长程基准，把人机协作形式化为 mid-turn（代理不确定时主动澄清、用户执行中打断）与 post-turn（用户完成后反馈纠正）交互协议；进一步分析揭示长程工作流交付与主动澄清的持续失败。
- **与主题关联**：定义本地 CUA 的「人能接管」点——执行中可打断、不确定时主动问、完成后可反馈纠正，是人在回路 HCI 的直接依据。

### W 类｜本地推理、量化与端侧部署（12 篇）

#### 216｜Efficient Memory Management for Large Language Model Serving with PagedAttention

- **检索号**：W-01　**类别**：W 本地推理、量化与端侧部署　**轮次**：第二轮
- **作者 / 机构**：Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, Ion Stoica（vLLM 团队）
- **时间**：2023　**类型**：会议论文
- **出处**：<https://arxiv.org/abs/2309.06180>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：SOSP 2023（arXiv Comments 原文标注）；摘要给出「2-4×」吞吐提升；项目仓库 vllm-project/vllm 96,451 stars（GitHub REST API，2026-11-06）
- **页面依据**：「vLLM improves the throughput of popular LLMs by 2-4× with the same level of latency」「near-zero waste in KV cache memory」
- **要点**：PagedAttention 借操作系统虚拟内存分页思想把每个请求的 KV cache 切成固定大小块按需分配，消除碎片与重复拷贝，使 KV cache 显存浪费接近零。摘要实测同延迟下吞吐提升 2-4×，且序列越长、模型越大、解码算法越复杂收益越明显。
- **与主题关联**：它给出「KV cache 可分页复用」的边界，说明家用机显存吃紧时瓶颈不只在权重、更在长上下文缓存。

#### 217｜GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers

- **检索号**：W-02　**类别**：W 本地推理、量化与端侧部署　**轮次**：第二轮
- **作者 / 机构**：Elias Frantar, Saleh Ashkboos, Torsten Hoefler, Dan Alistarh
- **时间**：2023　**类型**：会议论文
- **出处**：<https://arxiv.org/abs/2210.17323>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：ICLR 2023（arXiv Comments 原文标注）；3 或 4 bits/weight；175B 模型约 4 GPU hours 完成量化；首次在单 GPU 跑 175B；端到端约 3.25×（A100）/ 4.5×（A6000）加速（均为摘要原文）
- **页面依据**：「reducing the bitwidth down to 3 or 4 bits per weight」「execute an 175 billion-parameter model inside a single GPU for generative inference」「around 3.25x when using high-end GPUs (NVIDIA A100) and 4.5x when using more cost-effective ones (NVIDIA A6000)」
- **要点**：基于近似二阶信息的一次性（one-shot）训练后权重量化，把权压到 3-4 bit 且无需重训，175B 模型约 4 GPU 小时即可量化完成。量化后可在单张 GPU 上做生成推理，高端卡 3.25×、性价比卡 4.5× 端到端加速，2-bit/三值极端档仍保有合理精度。
- **与主题关联**：它把「单张消费级/工作站 GPU 能否跑大模型」的边界从「多卡 FP16」压到「单卡 3-4 bit」，是家用机显存预算的一手标尺。

#### 218｜AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration

- **检索号**：W-03　**类别**：W 本地推理、量化与端侧部署　**轮次**：第二轮
- **作者 / 机构**：Ji Lin, Jiaming Tang, Haotian Tang, Shang Yang, Wei-Ming Chen, Wei-Chen Wang, Guangxuan Xiao, Xingyu Dang, Chuang Gan, Song Han（MIT HAN Lab 等）
- **时间**：2024　**类型**：会议论文
- **出处**：<https://arxiv.org/abs/2306.00978>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：MLSys 2024 Best Paper Award（arXiv Comments 原文）；保护 1% 显著权重；TinyChat 比 Hugging Face FP16 实现「more than 3x speedup」；70B Llama-2 可部署到移动 GPU
- **页面依据**：「MLSys 2024 Best Paper Award」「Protecting only 1% salient weights can greatly reduce quantization error」「TinyChat offers more than 3x speedup over the Huggingface FP16 implementation on both desktop and mobile GPUs」
- **要点**：激活感知的 weight-only 低比特量化，按激活分布（而非权重本身）识别约 1% 显著权重通道并用数学等价缩放保护它们，避免混合精度带来的硬件低效，且不依赖反向传播/重建。配套 TinyChat 以 kernel fusion 与 platform-aware weight packing 在桌面与移动 GPU 上比 HF FP16 快 3 倍以上，并使 70B Llama-2 在移动 GPU 上部署成为可能。
- **与主题关联**：它证明 4-bit 权重加融合内核可把 70B 级模型放进桌面/移动 GPU，界定了家用机「端侧大模型」的规模上限。

#### 219｜SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models

- **检索号**：W-04　**类别**：W 本地推理、量化与端侧部署　**轮次**：第二轮
- **作者 / 机构**：Guangxuan Xiao, Ji Lin, Mickael Seznec, Hao Wu, Julien Demouth, Song Han
- **时间**：2023　**类型**：会议论文
- **出处**：<https://arxiv.org/abs/2211.10438>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：ICML 2023（arXiv Comments 原文标注）；W8A8；up to 1.56× speedup、2× memory reduction；单节点服务 530B 模型
- **页面依据**：「enable 8-bit weight, 8-bit activation (W8A8) quantization for LLMs」「up to 1.56x speedup and 2x memory reduction」「SmoothQuant enables serving 530B LLM within a single node」
- **要点**：训练后、无需重训、数学等价的逐通道缩放把量化难度从含异常值的激活迁移到易量化的权重，使 LLM 所有矩阵乘都能用 INT8 的 W8A8。摘要给出最高 1.56× 加速与 2× 显存减半，并把 530B 模型压进单节点。
- **与主题关联**：W8A8 把权重与激活同时减半，直接给出「显存减半 / 单节点」的量化边界，是判断家用机是否必须降到 4-bit 的一手依据。

#### 220｜Ollama documentation

- **检索号**：W-05　**类别**：W 本地推理、量化与端侧部署　**轮次**：第二轮
- **作者 / 机构**：Ollama（官方维护方，仓库 ollama/ollama）
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://docs.ollama.com>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：官方仓库 ollama/ollama 186,070 stars（GitHub REST API，2026-11-06）；同站官方 GPU 文档 docs.ollama.com/gpu.md 列出消费级显卡（RTX 4060/4090/5090、GTX 750 Ti 等）与 compute capability 5.0+ / 驱动 550+ 要求
- **页面依据**：「Choose cloud models or run models on your computer.」（本条出处页）、「Ollama supports Nvidia GPUs with compute capability 5.0+ and driver version 550 and newer.」「The Ollama scheduler leverages available VRAM data reported by the GPU libraries to make optimal scheduling decisions.」（同站官方 gpu.md 页，亦已打开）
- **要点**：Ollama 把模型下载、GGUF 量化加载与本地服务封装成同一套 API，并按 GPU 库上报的可用 VRAM 做调度（显存不足时可回退 CPU / CPU+GPU 混合）。官方硬件文档列出从 GTX 750 Ti（compute capability 5.0）到 RTX 5090 的消费级卡支持范围，以及 Metal / Vulkan / ROCm 后端。
- **与主题关联**：它把「云端模型」与「本机模型」做成同一接口，并用官方消费级显卡清单界定家用机哪些 GPU 能被本地推理直接利用。

#### 221｜quantize（llama.cpp 量化工具说明页 tools/quantize/README.md）

- **检索号**：W-06　**类别**：W 本地推理、量化与端侧部署　**轮次**：第二轮
- **作者 / 机构**：ggml-org（llama.cpp 维护组织）
- **时间**：n.d.　**类型**：官方仓库
- **出处**：<https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：仓库 ggml-org/llama.cpp 133,537 stars（GitHub REST API，2026-11-06）；官方量化表给出 Llama 3.1 8B 原始 32.1 GB → Q4_K_M 4.9 GB、70B 280.9 → 43.1 GB、405B 1,625.1 → 249.1 GB；Q4_K_M 4.8944 bits/weight / 4.58 GiB、F16 16.0005 bpw / 14.96 GiB（Llama-3.1-8B）
- **页面依据**：「Quantization reduces the precision of model weights (e.g., from 32-bit floats to 4-bit integers), which shrinks the model's size and can speed up inference.」「At the moment, memory and disk requirements are the same.」（表格：8B 32.1 GB → 4.9 GB Q4_K_M）。（说明：本条选用 tools/quantize/README.md 而非仓库主 README，以避开原清单已剔除的 K-10「llama.cpp README」URL 重复）
- **要点**：`llama-quantize` 把 F32/BF16 的 GGUF 转成 1.5-8 bit 整数权重（IQ1_S 至 Q8_0、Q4_K_M 等 k-quants/i-quants），官方表格显示 Llama 3.1 8B 从 32.1 GB 压到 4.9 GB、70B 从 280.9 GB 压到 43.1 GB，并逐档给出 bits/weight、体积与生成 t/s。页面同时说明「memory and disk requirements are the same」，即跑大模型需等量内存/磁盘。
- **与主题关联**：这张官方显存/磁盘表直接划出家用机边界——8B Q4_K_M 约 4.9 GB 可进 8GB 卡，而 70B Q4_K_M 43.1 GB 仍超出 24GB 消费卡，需卸载或改用云端/多机。

#### 222｜Fast Inference from Transformers via Speculative Decoding

- **检索号**：W-07　**类别**：W 本地推理、量化与端侧部署　**轮次**：第二轮
- **作者 / 机构**：Yaniv Leviathan, Matan Kalman, Yossi Matias
- **时间**：2023　**类型**：会议论文
- **出处**：<https://arxiv.org/abs/2211.17192>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：ICML 2023 Oral（arXiv Comments 原文标注）；T5-XXL 上 2X-3X acceleration，且「identical outputs」
- **页面依据**：「We demonstrate it on T5-XXL and show a 2X-3X acceleration compared to the standard T5X implementation, with identical outputs.」「by computing several tokens in parallel」
- **要点**：用更小的近似模型并行草拟多个 token，再由大模型一次前向批量验证，把原本 K 次串行解码变成分块并行；配合新型采样方法保证输出分布完全不变，无需重训或改架构。T5-XXL 实测 2X-3X 加速且输出与标准解码一致。
- **与主题关联**：它说明即使不做量化，家用机也能靠「小模型草稿 + 大模型校验」把自回归延迟压低 2-3 倍，是纯算法侧的算力门槛下压手段。

#### 223｜SGLang: Efficient Execution of Structured Language Model Programs

- **检索号**：W-08　**类别**：W 本地推理、量化与端侧部署　**轮次**：第二轮
- **作者 / 机构**：Lianmin Zheng, Liangsheng Yin, Zhiqiang Xie, Chuyue Sun, Jeff Huang, Cody Hao Yu, Shiyi Cao, Christos Kozyrakis, Ion Stoica, Joseph E. Gonzalez, Clark Barrett, Ying Sheng
- **时间**：2024　**类型**：arXiv 预印本
- **出处**：<https://arxiv.org/abs/2312.07104>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv 预印本 2312.07104（v1 2023-12-12、v2 2024-06-06）；摘要给出「up to 6.4x higher throughput」；arXiv abs 页未标注会议（会议信息未核实）
- **页面依据**：「SGLang achieves up to 6.4x higher throughput compared to state-of-the-art inference systems」「RadixAttention for KV cache reuse and compressed finite state machines for faster structured output decoding」
- **要点**：RadixAttention 用基数树在多轮/多请求间复用相同前缀的 KV cache，配合压缩有限状态机加速结构化输出解码，避免重复 prefill。摘要实测在 agent 控制、逻辑推理、JSON 解码、RAG、多轮对话等工作负载上吞吐最高 6.4×。
- **与主题关联**：CUA 的多步调用与长系统提示会产生大量可复用前缀，这条给出「缓存复用能把家用机有限显存下的有效吞吐放大多少」的上界。

#### 224｜Run LLMs with MLX（MLX LM）

- **检索号**：W-09　**类别**：W 本地推理、量化与端侧部署　**轮次**：第二轮
- **作者 / 机构**：ml-explore（Apple MLX 官方组织）
- **时间**：n.d.　**类型**：官方仓库
- **出处**：<https://github.com/ml-explore/mlx-lm>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：7,571 stars（GitHub REST API，2026-11-06；仓库页面显示 7.6k）；README 给出 4-bit 量化命令与结果（仓库 created_at 2025-03-11，GitHub REST API）
- **页面依据**：「MLX LM is a Python package for generating text and fine-tuning large language models on Apple silicon with MLX.」「This will generate a 4-bit quantized Mistral 7B and upload it to the repo」「Support for quantizing and uploading models to the Hugging Face Hub.」
- **要点**：基于 Apple MLX 框架在 Apple Silicon 统一内存上做文本生成与微调，`mlx_lm.convert --model ... -q` 一键产出 4-bit 量化模型（示例 Mistral 7B），并支持量化模型上传 Hugging Face Hub 与 `mx.distributed` 分布式推理。
- **与主题关联**：统一内存让 CPU/GPU 共享同一池高速 RAM，这条界定「Mac 家用机不靠独立大显存也能跑多大模型」的可行边界。

#### 225｜Quantize ONNX Models

- **检索号**：W-10　**类别**：W 本地推理、量化与端侧部署　**轮次**：第二轮
- **作者 / 机构**：Microsoft / ONNX Runtime 官方
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：官方量化文档；「8 bit linear quantization」、32-bit → 8-bit；「4 bit integer types」block-wise weight-only（block_size=128、opset 21、ONNX Runtime 1.20）；页面未给出加速倍数或显存百分比（未核实具体倍数）
- **页面依据**：「Quantization in ONNX Runtime refers to 8 bit linear quantization of an ONNX model.」「ONNX Runtime can quantize certain operators in a model to 4 bit integer types. Block-wise weight-only quantization is applied to the operators.」「The performance gain from quantization has two aspects: compute and memory.」
- **要点**：提供 dynamic / static / QAT 三类量化 API，把 FP32 权重压到 8-bit（U8/S8 组合，默认 S8S8 with QDQ），并支持 MatMul 的 4-bit block-wise weight-only（MatMulNBits，block_size=128、需 ONNX opset 21 / ONNX Runtime 1.20），收益来自 compute 与 memory 两方面。文档同时提醒旧硬件缺少 int8 指令时反而更慢，GPU 需 Tensor Core int8（如 T4/A100）才受益。
- **与主题关联**：它把「量化收益依赖 CPU VNNI / GPU Tensor Core」写成官方条件，直接界定家用机老卡能否靠 ONNX Runtime 量化获益。

#### 226｜High-performance In-browser LLM Inference Engine（WebLLM）

- **检索号**：W-11　**类别**：W 本地推理、量化与端侧部署　**轮次**：第二轮
- **作者 / 机构**：mlc-ai（由 CMU Catalyst、UW SAMPL、SJTU、OctoML 与 MLC community 成员发起）
- **时间**：n.d.　**类型**：官方仓库
- **出处**：<https://github.com/mlc-ai/web-llm>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：19,356 stars（GitHub REST API，2026-11-06）；WebGPU；模型 ID 含 q4f32_1 / q4f16_1 等 4-bit 权重变体；README 给出「M3 Max Llama 2 7B q4f32_1, decoding 128 tokens with a 12-token prompt」实机基准（仓库 created_at 2023-04-13，GitHub REST API）
- **页面依据**：「Everything runs inside the browser with no server support and is accelerated with WebGPU.」「High-Performance In-Browser LLM Inference Engine.」「fully compatible with OpenAI API」
- **要点**：借 MLC/TVM 编译栈把 4-bit 量化权重（q4f32_1、q4f16_1、q4f32_0 等变体）编译为浏览器可执行的 WebGPU 内核，全部推理在浏览器内完成、无需服务器，且提供 OpenAI 兼容 API。README 含 M3 Max 上 Llama 2 7B q4f32_1 解码 128 tokens 的实机基准。
- **与主题关联**：它把「本地推理」下推到任意装了浏览器的家用机（无需独立显卡、权重留在本机），是零部署成本端侧路线的边界样本。

#### 227｜SmolVLM - small yet mighty Vision Language Model

- **检索号**：W-12　**类别**：W 本地推理、量化与端侧部署　**轮次**：第二轮
- **作者 / 机构**：Hugging Face / HuggingFaceTB（博客引用区列 Andrés Marafioti 等 17 位作者）
- **时间**：2024　**类型**：官方文档（Hugging Face 官方技术博客 / 端侧报告）
- **出处**：<https://huggingface.co/blog/smolvlm>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「SmolVLM - small yet mighty Vision Language Model（Published November 26, 2024）」
- **影响力**：Published November 26, 2024；2B VLM；官方表格「Min GPU RAM required (GB) 5.02」；prefill 3.3-4.5× / generation 7.5-16× faster（对比 Qwen2-VL）；单图 1.2k tokens（Qwen2-VL 16k）；微调在 L4 上约 16 GB VRAM
- **页面依据**：「This blog post introduces SmolVLM, a 2B VLM, SOTA for its memory footprint.」「Min GPU RAM required (GB)」表中 SmolVLM 为 5.02、「This allows it to run efficiently on-device, such as a laptop!」「SmolVLM encodes each 384x384 image patch to 81 tokens.」
- **要点**：以 SmolLM2 1.7B 作语言骨干并用 pixel shuffle 把每张 384×384 图像压成 81 tokens（单图测试 prompt 仅 1.2k tokens，Qwen2-VL 需 16k），把 2B VLM 的推理最小显存压到 5.02 GB。官方实测 prefill 吞吐快 3.3-4.5×、生成吞吐快 7.5-16×，并称可在 laptop 等端侧设备高效运行。
- **与主题关联**：CUA 需视觉理解屏幕，这条给出「带视觉的端侧模型在笔记本/消费卡上约 5 GB 显存即可跑」的一手边界。

### X 类｜其他配套模块（语音 / 通知 / 可观测性 / 本地数据 / 状态持久化 / 桌面集成）（12 篇）

#### 228｜Robust Speech Recognition via Large-Scale Weak Supervision（openai/whisper）

- **检索号**：X-01　**类别**：X 其他配套模块（语音 / 通知 / 可观测性 / 本地数据 / 状态持久化 / 桌面集成）　**轮次**：第二轮
- **作者 / 机构**：OpenAI
- **时间**：2022　**类型**：官方仓库
- **出处**：<https://github.com/openai/whisper>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：OpenAI 官方仓库 openai/whisper，README 顶部 [Paper] 链接指向 arXiv:2212.04356；该论文《Robust Speech Recognition via Large-Scale Weak Supervision》2022-12-06 提交，摘要给出 "680,000 hours of multilingual and multitask supervision"；README 列出 "There are six model sizes" 及 A100 实测相对速度 "~10x"（tiny）/"~8x"（turbo）；GitHub star 数：未核实（所引 GitHub 页面未返回 star 计数，核验日 2026-11-06）。
- **页面依据**："Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification."
- **要点**：把本地麦克风或音频流转写为文本，是常驻助理「听」的入口，同时支持语音翻译与语种识别。六种模型尺寸与相对速度表允许按家用 PC 的显存、延迟预算取舍，turbo 为 large-v3 的优化版。
- **与主题关联**：补齐语音 I/O 中的本地语音识别（ASR）环节。

#### 229｜SQLite FTS5 Extension

- **检索号**：X-02　**类别**：X 其他配套模块（语音 / 通知 / 可观测性 / 本地数据 / 状态持久化 / 桌面集成）　**轮次**：第二轮
- **作者 / 机构**：SQLite（sqlite.org）
- **时间**：2015　**类型**：官方文档
- **出处**：<https://www.sqlite.org/fts5.html>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：SQLite 官方文档；页面原文 "As of version 3.9.0 (2015-10-14), FTS5 is included as part of the SQLite amalgamation."，说明自 3.9.0 起随 SQLite 主发行版内置；页面另载 "Prior to SQLite version 3.20.0 (2017-08-01), the fts5() worked slightly differently." 与默认 unicode61 tokenizer；性能基准/GitHub star 数：未核实（页面未披露，核验日 2026-11-06）。
- **页面依据**："FTS5 is an SQLite virtual table module that provides full-text search functionality to database applications."
- **要点**：为常驻助理的本地笔记、会话日志、文档提供零独立服务进程的倒排索引全文检索。以虚拟表形式直接用 SQL 查询，便于把长期记忆与本地知识落地到单文件数据库。
- **与主题关联**：补齐本地数据/知识库中的全文检索与本地记忆存取环节。

#### 230｜Notifications API Standard

- **检索号**：X-03　**类别**：X 其他配套模块（语音 / 通知 / 可观测性 / 本地数据 / 状态持久化 / 桌面集成）　**轮次**：第二轮
- **作者 / 机构**：WHATWG（Apple, Google, Mozilla, Microsoft）
- **时间**：n.d.　**类型**：官方规范
- **出处**：<https://notifications.spec.whatwg.org>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：WHATWG Living Standard（官方规范）；状态行 "Living Standard — Last Updated 19 October 2026"（核验日 2026-11-06 可见）；版权行 "Copyright © WHATWG (Apple, Google, Mozilla, Microsoft)"，由四大浏览器厂商共同维护；引用数/star 数：未核实（标准文档未披露，核验日 2026-11-06）。
- **页面依据**："This standard defines an API to display notifications to the end user, typically outside the top-level browsing context's viewport."
- **要点**：定义浏览器在页面视口之外向用户弹出通知的标准接口，是助理主动打断用户、发起确认的规范化通道。配合动作按钮可承载「批准/拒绝」的人在回路决策，而不必自建 UI。
- **与主题关联**：补齐通知与人在回路中的主动触达与确认入口。

#### 231｜Web Speech API - Web APIs | MDN

- **检索号**：X-04　**类别**：X 其他配套模块（语音 / 通知 / 可观测性 / 本地数据 / 状态持久化 / 桌面集成）　**轮次**：第二轮
- **作者 / 机构**：MDN Web Docs（Mozilla）；规范为 W3C/WHATWG Web Speech API
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：MDN 官方 Web API 文档；Specifications 段引用 Web Speech API 规范（webaudio.github.io/web-speech-api/#speechreco-section 与 #tts-section）；页面列出 SpeechRecognition 与 SpeechSynthesis 两套接口，并记载 on-device speech recognition 与 Permissions-Policy 指令 on-device-speech-recognition；发布日期/star 数：未核实（页面未披露，核验日 2026-11-06）。
- **页面依据**："The Web Speech API enables you to incorporate voice data into web apps. The Web Speech API has two parts: SpeechSynthesis (Text-to-Speech), and SpeechRecognition (Asynchronous Speech Recognition.)"
- **要点**：一套浏览器原生接口同时覆盖语音识别（SpeechRecognition）与语音合成（SpeechSynthesis），即助理的「听」与「说」两端。页面明确支持 on-device 本地识别，可免于自行部署模型就完成语音 I/O。
- **与主题关联**：补齐语音 I/O 中的浏览器端语音输入与朗读输出环节。

#### 232｜Temporal Platform Documentation（Build applications that never fail）

- **检索号**：X-05　**类别**：X 其他配套模块（语音 / 通知 / 可观测性 / 本地数据 / 状态持久化 / 桌面集成）　**轮次**：第二轮
- **作者 / 机构**：Temporal（Temporal Technologies，开源 Durable Execution 平台）
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://docs.temporal.io>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Temporal 官方文档首页；页面原文 "Temporal delivers crash-proof execution by guaranteeing that applications resume exactly where they left off after crashes, network failures, or infrastructure outages, whether that happens seconds, days, or even years later."，并明确把 "AI agents" 列入 "mission-critical processes ... never fail or disappear"；版本/star 数：未核实（页面未披露，核验日 2026-11-06）。
- **页面依据**："Temporal is an open-source platform for building reliable applications."
- **要点**：把长任务编排成可重放的 Workflow，崩溃、断网或主机重启后从中断点精确恢复，而非从头再跑。文档明确点名 AI agents，适合常驻助理跨天、跨重启的持续任务与定时调度状态。
- **与主题关联**：补齐状态与长任务中的持久化执行与故障恢复环节。

#### 233｜From Local to Global: A Graph RAG Approach to Query-Focused Summarization

- **检索号**：X-06　**类别**：X 其他配套模块（语音 / 通知 / 可观测性 / 本地数据 / 状态持久化 / 桌面集成）　**轮次**：第二轮
- **作者 / 机构**：arXiv（作者 Darren Edge、Ha Trinh、Newman Cheng、Jonathan Larson 等）；配套官方仓库 microsoft/graphrag（Microsoft）
- **时间**：2024　**类型**：论文
- **出处**：<https://arxiv.org/abs/2404.16130>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：arXiv:2404.16130 [cs.CL]（另标 cs.AI、cs.IR），2024-04-24 提交 v1、2025-02-19 修订至 v2；摘要给出 "For a class of global sensemaking questions over datasets in the 1 million token range" 与 "GraphRAG leads to substantial improvements over a conventional RAG baseline for both the comprehensiveness and diversity of generated answers"；配套仓库 microsoft/graphrag 的 README 提及 "Microsoft Research Blog Post."；被引数/star 数：未核实（所引页面未披露，核验日 2026-11-06）。
- **页面依据**："we propose GraphRAG, a graph-based approach to question answering over private text corpora that scales with both the generality of user questions and the quantity of source text."
- **要点**：用 LLM 从私有文档两阶段构建实体知识图谱并预生成社区摘要，再逐社区生成部分答案后汇总，专门回答「整个语料的主要主题」这类全局问题。使常驻助理能对本地长期积累的笔记与文档做跨文档归纳，而非仅返回零散片段。
- **与主题关联**：补齐本地数据/知识库中的图谱化索引与全局问答环节。

#### 234｜RFC 6455: The WebSocket Protocol

- **检索号**：X-07　**类别**：X 其他配套模块（语音 / 通知 / 可观测性 / 本地数据 / 状态持久化 / 桌面集成）　**轮次**：第二轮
- **作者 / 机构**：IETF（Internet Engineering Task Force）；作者 I. Fette (Google, Inc.)、A. Melnikov (Isode Ltd.)
- **时间**：2011　**类型**：官方规范
- **出处**：<https://www.rfc-editor.org/rfc/rfc6455>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：RFC Editor 官方发布的 IETF 标准，编号 6455，日期 December 2011，原文 "Request for Comments: 6455"；作者署名 Google, Inc. 与 Isode Ltd.；引用数/star 数：未核实（标准文档无此项，核验日 2026-11-06）。
- **页面依据**："The WebSocket Protocol enables two-way communication between a client running untrusted code in a controlled environment to a remote host that has opted-in to communications from that code."
- **要点**：定义单 TCP 连接上的全双工双向通信，使本地常驻助理进程能把主动事件与流式 LLM 输出实时推送给桌面前端、托盘 UI 或手机。是「local HTTP/WebSocket 服务」这一桌面集成方式的权威协议依据。
- **与主题关联**：补齐桌面集成中的本地实时双向通信通道。

#### 235｜Tauri 2.0 | Tauri

- **检索号**：X-08　**类别**：X 其他配套模块（语音 / 通知 / 可观测性 / 本地数据 / 状态持久化 / 桌面集成）　**轮次**：第二轮
- **作者 / 机构**：Tauri（Tauri Team / tauri-apps）
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://tauri.app>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Tauri 官方站点（Tauri 2.0）；页面给出明确体积数字 "By using the OS's native web renderer, the size of a Tauri app can be as small as 600 KB."，并载 "Build your app for Linux, macOS, Windows, Android and iOS - all from a single codebase"；GitHub star 数：未核实（所引页面未披露，核验日 2026-11-06）。
- **页面依据**："Create small, fast, secure, cross-platform applications"
- **要点**：用系统原生 WebView 渲染前端、Rust 编写应用逻辑，打包体积可小至 600 KB，适合长期常驻、低内存占用的本地助理外壳。Rust 后端可直接对接系统托盘、全局快捷键与本地文件，避免 Electron 式整包 Chromium 开销。
- **与主题关联**：补齐桌面集成中的轻量常驻应用外壳环节。

#### 236｜AI Observability & Evaluation（GitHub - Arize-ai/phoenix）

- **检索号**：X-09　**类别**：X 其他配套模块（语音 / 通知 / 可观测性 / 本地数据 / 状态持久化 / 桌面集成）　**轮次**：第二轮
- **作者 / 机构**：Arize AI, Inc.（GitHub owner: Arize-ai）
- **时间**：2025　**类型**：官方仓库
- **出处**：<https://github.com/Arize-ai/phoenix>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：GitHub 仓库页显示 "12.2k stars"、"1.3k forks"（来源：github.com/Arize-ai/phoenix 页面，打开核验日 2026-11-06）；README 载 "Phoenix is built on top of OpenTelemetry and is vendor, language, and framework agnostic."，并指向 OpenInference 自动 instrumentation 项目；版权行 "Copyright 2025 Arize AI, Inc. All Rights Reserved."；另有官方站点 phoenix.arize.com 标注 "Run locally or self-host in your environment"。
- **页面依据**："Arize Phoenix is Arize's open-source AI observability platform designed for experimentation, evaluation, and troubleshooting."
- **要点**：基于 OpenTelemetry/OpenInference 采集 LLM 应用的 trace 与 span，可定位检索、工具调用、多步链路在哪一步出错或退化。支持本地/自托管运行，让常驻助理的自主决策链可回放、可评测而不必把数据送出本机。
- **与主题关联**：补齐可观测性中的链路追踪与评测环节。

#### 237｜Open Source AI Engineering Platform - Langfuse（Langfuse Overview）

- **检索号**：X-10　**类别**：X 其他配套模块（语音 / 通知 / 可观测性 / 本地数据 / 状态持久化 / 桌面集成）　**轮次**：第二轮
- **作者 / 机构**：Langfuse（GitHub: langfuse/langfuse）
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://langfuse.com/docs>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Langfuse 官方文档；页面自述 "100+ library/framework integrations"，并载 "Langfuse provides comprehensive tracing capabilities" 与 "Langfuse provides flexible evaluation tools"；文档称其为 "an open-source AI engineering platform"；GitHub star 数/发布日期：未核实（所引页面未披露，核验日 2026-11-06）。
- **页面依据**："Langfuse provides comprehensive tracing capabilities that help you understand exactly what's happening in your application."
- **要点**：记录每次 LLM/agent 调用的 trace、prompt 版本、评测与运行指标，覆盖从开发到生产的完整生命周期。使常驻助理长期运行中的行为、延迟与成本可观测、可对比、可迭代。
- **与主题关联**：补齐可观测性中的 trace/评测与持续迭代环节。

#### 238｜Durable Functions overview

- **检索号**：X-11　**类别**：X 其他配套模块（语音 / 通知 / 可观测性 / 本地数据 / 状态持久化 / 桌面集成）　**轮次**：第二轮
- **作者 / 机构**：Microsoft（Microsoft Learn / Azure Functions）
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验；站点重定向至 https://learn.microsoft.com/en-us/azure/durable-task/durable-functions/durable-functions-overview；独立抓取二次确认「Durable Functions Overview: Stateful Serverless Workflows | Microsoft Learn（微软文档改版重定向）」
- **影响力**：Microsoft Learn 官方文档；页面原文 "The Durable Functions runtime manages state, checkpoints, retries, and recovery so your workflows can run reliably for long periods."；Supported languages 表列出 .NET (C#)、JavaScript、TypeScript、Python、PowerShell、Java 六种语言；star 数/发布日期：未核实（页面未披露，核验日 2026-11-06）。
- **页面依据**："Durable Functions is an extension of Azure Functions that lets you build stateful workflows in a serverless environment by writing orchestrator, activity, and entity functions in code."
- **要点**：以 orchestrator/activity/entity 函数编写有状态工作流，运行时自动持久化状态、做检查点、重试与恢复，适合助理跨小时乃至跨天的长任务。本条列为候补：与 X-05 Temporal 同属持久化编排，是绑定 Azure 生态时的托管替代选型。
- **与主题关联**：补齐状态与长任务中的有状态编排与检查点环节（候选方案）。

#### 239｜App notifications overview

- **检索号**：X-12　**类别**：X 其他配套模块（语音 / 通知 / 可观测性 / 本地数据 / 状态持久化 / 桌面集成）　**轮次**：第二轮
- **作者 / 机构**：Microsoft（Microsoft Learn / Windows App SDK）
- **时间**：n.d.　**类型**：官方文档
- **出处**：<https://learn.microsoft.com/en-us/windows/apps/develop/notifications/app-notifications>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验；站点重定向至 https://learn.microsoft.com/en-us/windows/apps/develop/notifications/app-notifications/；独立抓取二次确认「App Notifications Overview for Windows Apps - Windows apps | Microsoft Learn」
- **影响力**：Microsoft Learn 官方文档；页面载 "The Windows App SDK provides APIs for sending and managing app notifications, and for responding to user interaction with notifications."，并列出 WPF、WinForms、Console、UWP 等多框架接入文档；star 数/发布日期：未核实（页面未披露，核验日 2026-11-06）。
- **页面依据**："App notifications are UI popups that appear outside of your app's window, delivering timely information or actions to the user. Notifications can be purely informational, can launch your app when clicked, or can trigger a background action without bringing your app to the foreground."
- **要点**：Windows 原生 toast 通知在应用窗口之外弹出，点击可拉起应用或触发后台动作，是常驻助理在 PC 上主动提醒与「需要你确认」的最直接通道。本条列为候补：与 X-03 W3C Notifications API 同属通知触达，是桌面原生实现而非浏览器标准。
- **与主题关联**：补齐通知与人在回路中的桌面原生触达与确认环节（候选方案）。

### Y 类｜补漏：本地桌面 / 浏览器控制接口官方文档（12 篇）

#### 240｜Installation | Playwright

- **检索号**：Y-01　**类别**：Y 补漏：本地桌面 / 浏览器控制接口官方文档　**轮次**：第三轮
- **作者 / 机构**：Microsoft / Playwright 项目（playwright.dev 官方文档）
- **时间**：n.d.　**类型**：官方技术文档
- **出处**：<https://playwright.dev/docs/intro>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Playwright 项目官方入门页；页面原文明确其 bundles test runner / assertions / isolation / parallelization，并跨 Chromium、WebKit、Firefox 三引擎与 Windows、Linux、macOS 三平台，是浏览器自动化的主流入口之一，也是把「看页面 + 点控件 + 输入」落到本地浏览器的常用实现层。
- **页面依据**："Playwright Test is an end-to-end test framework for modern web apps."；"Playwright supports Chromium, WebKit and Firefox on Windows, Linux and macOS, locally or in CI, headless or headed, with native mobile emulation for Chrome (Android) and Mobile Safari."；"npm init playwright@latest"；"By default tests run headless in parallel across Chromium, Firefox and WebKit"
- **要点**：官方安装与入门页，说明 Playwright 会下载所需浏览器二进制并生成 playwright.config.ts / tests / example.spec.ts 脚手架，集中配置目标浏览器、超时、重试、projects 与 reporters。给出 `npx playwright test` 运行、`--headed`、`--ui`、`--project=chromium` 等参数，以及 System requirements 中列出的 Node.js 与操作系统版本。页面表明测试默认 headless 并行执行，并可用 Codegen 生成测试、用 trace viewer 回放。
- **与主题关联**：提供本地 CUA 的「浏览器自动化入口层」——在本机启动并驱动浏览器执行页面级操作。

#### 241｜DevTools Protocol Viewer

- **检索号**：Y-02　**类别**：Y 补漏：本地桌面 / 浏览器控制接口官方文档　**轮次**：第三轮
- **作者 / 机构**：Chrome DevTools 团队 / Chromium 项目（chromedevtools.github.io 官方协议站点）
- **时间**：n.d.　**类型**：官方技术文档
- **出处**：<https://chromedevtools.github.io/devtools-protocol>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Chrome DevTools Protocol 官方协议查看器；页面原文说明其为 JSON-based protocol、供 debug and automation clients 使用，且 Puppeteer 官方首页明确声明其通过 DevTools Protocol 控制 Chrome / Firefox，是浏览器底层控制接口被上层自动化框架直接依赖的一手规范入口。
- **页面依据**："JSON-based protocol"；"debug and automation clients"；"Instrumentation is divided into domains"；"commands and events"
- **要点**：官方协议查看器把调试与自动化能力按 domain 划分，每个 domain 由 commands 与 events 组成，供客户端通过 JSON 消息与浏览器内核交互。页面提供各 domain 的 Reference、tot（最新）、各 Chrome 版本快照以及 Protocol 更新说明的入口。这是不经过 WebDriver、直接对浏览器实例发指令的底层接口。
- **与主题关联**：提供本地 CUA 的「浏览器内核指令层」——以命令 / 事件方式读取页面状态并驱动浏览器。

#### 242｜Puppeteer

- **检索号**：Y-03　**类别**：Y 补漏：本地桌面 / 浏览器控制接口官方文档　**轮次**：第三轮
- **作者 / 机构**：Chrome DevTools 团队 / Puppeteer 项目（pptr.dev 官方文档）
- **时间**：n.d.　**类型**：官方技术文档
- **出处**：<https://pptr.dev>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Puppeteer 项目官方首页；页面原文说明其提供 high-level API 通过 DevTools Protocol 或 WebDriver BiDi 控制 Chrome / Firefox，默认 headless 运行，是本地把 CDP 封装成可调用浏览器动作的主流实现层；页面标注 Version: 25.16.0。
- **页面依据**："Puppeteer is a JavaScript library which provides a high-level API to control Chrome or Firefox over the DevTools Protocol or WebDriver BiDi."；"Puppeteer runs in the headless (no visible UI) by default"；"npm i puppeteer # Downloads compatible Chrome during installation."；"const browser = await puppeteer.launch();"
- **要点**：官方首页给出 puppeteer / puppeteer-core 安装方式、浏览器下载说明（`npx puppeteer browsers install`）与完整示例：`puppeteer.launch()`、`browser.newPage()`、`page.goto()`、`page.setViewport()`、`page.keyboard.press('/')`、`page.locator().fill()`、`page.locator().click()` 等。示例展示了以可访问名称定位输入框并键入、等待并点击搜索结果、读取元素文本的完整交互链，另提供 Get started / API / FAQ 等文档入口。
- **与主题关联**：提供本地 CUA 的「浏览器动作执行层」——把页面导航、键盘、定位与点击封装为可编程 API。

#### 243｜WebDriver

- **检索号**：Y-04　**类别**：Y 补漏：本地桌面 / 浏览器控制接口官方文档　**轮次**：第三轮
- **作者 / 机构**：World Wide Web Consortium（W3C）
- **时间**：2018-06　**类型**：官方技术文档
- **出处**：<https://www.w3.org/TR/webdriver1>
- **核验**：直连 403（站点反爬 / 地区限制）· 检索时已打开正文核验；独立抓取二次确认「WebDriver — W3C Recommendation 05 June 2018（直连 403，独立抓取读回 W3C 状态行）」
- **影响力**：W3C Recommendation（页面状态原文 "W3C Recommendation 05 June 2018"）；作为浏览器远程控制的标准化线协议，Selenium 官方首页原文说明其提供 "the infrastructure for implementations of the W3C WebDriver specification"，是跨浏览器自动化的事实标准依据。
- **页面依据**："W3C Recommendation 05 June 2018"；"WebDriver is a remote control interface"；"introspection and control of user agents"；"platform- and language-neutral wire protocol"；"discover and manipulate DOM elements"；"control the behavior of a user agent"
- **要点**：W3C 正式推荐标准定义 WebDriver 为平台与语言无关（platform- and language-neutral）的 wire protocol，用于用户代理的自省与控制，可发现并操作 web document 中的 DOM 元素、控制 user agent 行为。规范覆盖会话、命令、能力协商、元素定位与交互等，是各浏览器厂商实现 driver 与各语言绑定互操作的共同依据。
- **与主题关联**：提供本地 CUA 的「浏览器控制标准化协议层」——让同一套指令可作用于不同浏览器。

#### 244｜Android Debug Bridge (adb)  |  Android Studio  |  Android Developers

- **检索号**：Y-05　**类别**：Y 补漏：本地桌面 / 浏览器控制接口官方文档　**轮次**：第三轮
- **作者 / 机构**：Google / Android Developers（Android Studio 官方工具文档）
- **时间**：n.d.　**类型**：官方技术文档
- **出处**：<https://developer.android.com/tools/adb>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「Android Debug Bridge (adb) | Android Studio | Android Developers」
- **影响力**：Google 官方 adb 文档；页面原文称其为 versatile command-line tool，用于 communicate with a device，是 Android 设备侧执行 shell、安装 / 调试应用与端口转发的一手工具，也是 Chrome 远程调试文档所引用的 CDP socket 转发手段。
- **页面依据**："versatile command-line tool"；"communicate with a device"；"installing and debugging apps"；"access to a Unix shell"；"client-server program"
- **要点**：官方说明 adb 是 client-server program，含 client、daemon（adbd）与 server 三部分，可通过 USB 或 Wi-Fi 与设备通信。能力覆盖在设备上运行命令（Unix shell）、安装与调试应用、文件传输、端口转发（forward）以及查看设备状态等，是主机侧驱动设备界面与底层服务的命令行通道。
- **与主题关联**：提供本地 CUA 的「设备侧命令 / 端口通道层」——从 PC 向设备下发 shell 与转发调试端口。

#### 245｜ScreenCaptureKit | Apple Developer Documentation

- **检索号**：Y-06　**类别**：Y 补漏：本地桌面 / 浏览器控制接口官方文档　**轮次**：第三轮
- **作者 / 机构**：Apple Inc.（Apple Developer Documentation / ScreenCaptureKit）
- **时间**：n.d.　**类型**：官方技术文档
- **出处**：<https://developer.apple.com/documentation/screencapturekit>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Apple 官方 ScreenCaptureKit 框架文档；页面原文 "ScreenCaptureKit replaces ReplayKit for screen streaming and mirroring"，并标注 macOS 12.3+，是 macOS 上以高性能方式获取显示器、应用与窗口画面帧的现代官方屏幕捕获接口。
- **页面依据**："Stream screen content and audio to your app with fine-grained control over what you capture."；"Use ScreenCaptureKit to capture high-performance video and audio across iOS, iPadOS, macOS, tvOS, and visionOS."；"ScreenCaptureKit replaces ReplayKit for screen streaming and mirroring."；"macOS 12.3+"；"class SCStream"、"class SCContentFilter"、"class SCScreenshotManager"
- **要点**：官方框架页说明其以 CMSampleBuffer 交付屏幕与音频，并允许细粒度选择要捕获的内容。Topics 列出 Essentials、Shareable content（SCShareableContent / SCDisplay / SCRunningApplication / SCWindow）、Content capture（SCStream、SCStreamConfiguration、SCContentFilter、SCScreenshotManager）、Output processing（SCStreamOutput）与 System content-sharing picker（SCContentSharingPicker）等分组；页面说明捕获前需申请 screen recording 权限并在 Info 中配置 NSScreenCaptureUsageDescription。
- **与主题关联**：提供 macOS 本地 CUA 的「屏幕感知层」——按显示器 / 应用 / 窗口粒度取得画面帧。

#### 246｜Desktop Duplication API - Win32 apps | Microsoft Learn

- **检索号**：Y-07　**类别**：Y 补漏：本地桌面 / 浏览器控制接口官方文档　**轮次**：第三轮
- **作者 / 机构**：Microsoft（Microsoft Learn / Win32 apps 与 DirectX 文档）
- **时间**：n.d.　**类型**：官方技术文档
- **出处**：<https://learn.microsoft.com/en-us/windows/win32/direct3ddxgi/desktop-dup-api>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Microsoft 官方 DXGI Desktop Duplication API 文档；页面原文说明其提供 frame-by-frame updates to the desktop 并利用 the full power of the GPU，是 Windows 上在 Windows.Graphics.Capture 之外获取桌面图像的另一套官方底层接口，为远程协作与屏幕流场景提供依据。
- **页面依据**："remote access to a desktop image for collaboration scenarios"；"frame-by-frame updates to the desktop"；"the full power of the GPU"；"current desktop image"；"dirty regions"、"move regions"、"mouse pointer shape"
- **要点**：官方说明该 API 自 Windows 8 起提供，通过 IDXGIOutputDuplication 逐帧取得桌面图像，给出桌面更新的 dirty regions（脏矩形）与 move regions（移动区域），并暴露鼠标指针形状与位置信息；每帧由 GPU 直接提供，应用程序据此增量合成当前桌面画面。页面同时说明其与图形适配器 / 输出（DXGI output）的对应关系与帧获取循环。
- **与主题关联**：提供 Windows 本地 CUA 的「屏幕帧获取层」——以 GPU 逐帧方式拿到桌面像素与变化区域。

#### 247｜README.md · main · GNOME / at-spi2-core · GitLab

- **检索号**：Y-08　**类别**：Y 补漏：本地桌面 / 浏览器控制接口官方文档　**轮次**：第三轮
- **作者 / 机构**：GNOME 项目 / GNOME Foundation（gitlab.gnome.org 官方仓库文档）
- **时间**：n.d.　**类型**：官方技术文档
- **出处**：<https://gitlab.gnome.org/GNOME/at-spi2-core/-/blob/main/README.md>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：GNOME 官方 at-spi2-core 仓库文档；页面原文说明该仓库包含 AT-SPI（Assistive Technology Service Provider Interface）的 DBus interface definitions，即 "the core of an accessibility stack for free software systems"，并列出 ATK 与 libatspi 官方参考文档入口，是 Linux 桌面无障碍 / 控件树能力的第一手依据。
- **页面依据**："This repository contains the DBus interface definitions for AT-SPI (Assistive Technology Service Provider Interface) — the core of an accessibility stack for free software systems."；"`registryd` - Daemon that keeps track of accessible applications in the user's session, and lets them talk to each other and to assistive technologies (ATs) like screen readers."；"ATK library to make applications and GUI toolkits accessible"；"Versions 1.x of AT-SPI were based on CORBA for inter-process communication (IPC)"；"During the GNOME 2 and 3 release series, CORBA was phased out in favor of DBus"
- **要点**：README 说明仓库组成：`xml` 为 DBus introspection 格式的无障碍接口定义，`bus` 为会话无障碍总线启动器，`registryd` 跟踪会话中可访问应用并让其与屏幕阅读器等 AT 通信，`atk` 为供应用 / GUI toolkit 实现可访问性的 GObject API，`atspi` 为 C 语言绑定，`atk-adaptor` 负责 ATK 与 atspi 之间的转换。Documentation 一节给出 ATK 与 libatspi 参考文档、开发指南（devel-docs）入口；历史说明 AT-SPI 1.x 曾基于 CORBA，GNOME 2/3 时期改为 DBus。
- **与主题关联**：提供 Linux 本地 CUA 的「无障碍控件树 / 应用暴露层」——以 DBus 接口暴露应用界面结构供外部程序读取与操作。

#### 248｜mouse_event function (winuser.h) - Win32 apps | Microsoft Learn

- **检索号**：Y-09　**类别**：Y 补漏：本地桌面 / 浏览器控制接口官方文档　**轮次**：第三轮
- **作者 / 机构**：Microsoft（Microsoft Learn / Win32 API）
- **时间**：n.d.　**类型**：官方技术文档
- **出处**：<https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Microsoft 官方 Win32 输入合成 API 文档；页面原文 "The mouse_event function synthesizes mouse motion and button clicks."，是 SendInput 之外 Windows 上合成鼠标移动与按键的原生接口（页面注明已被 SendInput 取代），为桌面自动化动作执行提供底层原语。
- **页面依据**："The mouse_event function synthesizes mouse motion and button clicks."；"This function has been superseded. Use SendInput instead."；"MOUSEEVENTF_ABSOLUTE"、"MOUSEEVENTF_LEFTDOWN"、"MOUSEEVENTF_MOVE"；"If the MOUSEEVENTF_ABSOLUTE value is specified, dx and dy contain normalized absolute coordinates between 0 and 65,535."；"Minimum supported client Windows 2000 Professional"
- **要点**：官方给出 `VOID mouse_event(DWORD dwFlags, DWORD dx, DWORD dy, DWORD dwData, ULONG_PTR dwExtraInfo)` 完整签名与 dwFlags 取值（MOUSEEVENTF_MOVE / LEFTDOWN / LEFTUP / RIGHTDOWN / RIGHTUP / WHEEL / HWHEEL / XDOWN / XUP / ABSOLUTE 等）。说明 MOUSEEVENTF_ABSOLUTE 时 dx/dy 为 0–65,535 的归一化绝对坐标并映射到显示表面，未设置时为相对 mickey 位移且受鼠标加速与速度设置影响；滚轮位移以 WHEEL_DELTA=120 为一个刻度，最低支持 Windows 2000 Professional，库 User32.lib、DLL User32.dll。
- **与主题关联**：提供 Windows 本地 CUA 的「鼠标事件合成层」——把决策落成真实指针移动与点击。

#### 249｜Recognizing Text in Images | Apple Developer Documentation

- **检索号**：Y-10　**类别**：Y 补漏：本地桌面 / 浏览器控制接口官方文档　**轮次**：第三轮
- **作者 / 机构**：Apple Inc.（Apple Developer Documentation / Vision framework）
- **时间**：n.d.　**类型**：官方技术文档
- **出处**：<https://developer.apple.com/documentation/vision/recognizing-text-in-images>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Apple 官方 Vision 框架文字识别指南；页面原文说明所有 Vision 处理都在用户设备上完成（all of Vision's processing happens on the user's device），并给出 VNRecognizeTextRequest 的 fast / accurate 两条识别路径，是本地（离线、不依赖云端）把屏幕 / 图像解析成带坐标文字的官方 OCR 能力文档，与 Tesseract、OpenCV 模板匹配属不同实现。
- **页面依据**："Add text-recognition features to your app using the Vision framework."；"The fast path uses the framework's character-detection capabilities to find individual characters, and then uses a small machine learning model to recognize individual characters and words. This approach is similar to traditional optical character recognition (OCR)."；"Vision provides its text-recognition capabilities through VNRecognizeTextRequest, an image-based request type that finds and extracts text in images."；"Each observation provides the recognized text string, along with a confidence score"；"VNRecognizedTextObservation"
- **要点**：官方说明用 VNImageRequestHandler 执行 VNRecognizeTextRequest（默认 accurate 路径，可设 recognitionLevel 为 fast），结果以 VNRecognizedTextObservation 数组返回，含识别文本字符串、置信度与归一化坐标的 bounding rectangles，可用 VNImageRectForNormalizedRect 转换为图像坐标。页面还给出 supportedRecognitionLanguages(for:revision:) 查询支持语言、recognitionLanguages 指定中英文（zh-Hant / zh-Hans）、customWords 与语言校正等优化项。
- **与主题关联**：提供本地 CUA 的「屏幕文字解析层」——在设备端把图像转成可定位的文本与坐标。

#### 250｜Introduction | Electron

- **检索号**：Y-11　**类别**：Y 补漏：本地桌面 / 浏览器控制接口官方文档　**轮次**：第三轮
- **作者 / 机构**：Electron 项目 / OpenJS Foundation（electronjs.org 官方文档）
- **时间**：n.d.　**类型**：官方技术文档
- **出处**：<https://www.electronjs.org/docs/latest>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：Electron 项目官方文档首页；页面原文说明其把 Chromium 与 Node.js 嵌入二进制、以单一 JavaScript 代码库构建 Windows / macOS / Linux 跨平台桌面应用，是桌面应用集成 Web 与原生能力的官方一手说明（Tauri 已另收录）。
- **页面依据**："Electron is a framework for building desktop applications using JavaScript, HTML, and CSS."；"By embedding Chromium and Node.js into its binary, Electron allows you to maintain one JavaScript codebase and create cross-platform apps that work on Windows, macOS, and Linux"；"Electron Fiddle is a sandbox app written with Electron and supported by Electron's maintainers."
- **要点**：官方首页给出 quick-start 示例（app / BrowserWindow / preload.js / index.html，含 `win.loadFile('index.html')` 与 `app.whenReady()`），并列出文档分类：Tutorial、Processes in Electron、Best Practices、Examples、Development、Distribution、Testing And Debugging、References 等。说明 Fiddle 可与文档示例联动（Open in Fiddle），示例标注 docs/fiddles/quick-start (45.2.3)。
- **与主题关联**：提供本地 CUA 的「桌面应用集成层」——理解可被自动化驱动的桌面应用（Chromium + Node）运行形态。

#### 251｜Remote debug Android devices  |  Chrome DevTools  |  Chrome for Developers

- **检索号**：Y-12　**类别**：Y 补漏：本地桌面 / 浏览器控制接口官方文档　**轮次**：第三轮
- **作者 / 机构**：Google / Chrome for Developers（Chrome DevTools 官方文档）
- **时间**：n.d.　**类型**：官方技术文档
- **出处**：<https://developer.chrome.com/docs/devtools/remote-debugging>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「Remote debug Android devices | Chrome DevTools | Chrome for Developers」
- **影响力**：Google Chrome DevTools 官方远程调试指南；页面原文给出 `adb forward tcp:9222 localabstract:chrome_devtools_remote` 及 `http://localhost:9222/json`、`http://localhost:9222/json/version` 的 CDP endpoint 发现方式，是把本地浏览器 / 设备调试端口与 CDP 客户端连接起来的官方依据。
- **页面依据**："Remote debug live content on an Android device from your Windows, Mac, or Linux computer."；"Forward the CDP socket on the device to your machine's local port, for example, 9222."；"adb forward tcp:9222 localabstract:chrome_devtools_remote"；"http://localhost:9222/json lists your page targets."；"http://localhost:9222/json/version exposes the browser target endpoint"
- **要点**：官方指南说明在开发机 Chrome 打开 `chrome://inspect#devices` 发现设备、Inspect 打开 DevTools 实例，并可用 Toggle Screencast 把设备画面投到开发机（点击转为 tap、键盘击键发到设备）。"Debug manually through Android Debug Bridge (adb)" 一节给出直接连接 CDP 的方法：启用 USB debugging 后 `adb devices -l` 确认设备，用 adb forward 把设备 CDP socket 转发到本机 9222 端口，随后 `http://localhost:9222/json` 列出 page targets、`http://localhost:9222/json/version` 暴露 browser target endpoint。
- **与主题关联**：提供本地 CUA 的「CDP 连接 / 调试端口层」——建立本机到浏览器调试目标的连接与目标发现入口。

### Z 类｜补漏：CUA 高星开源实现与官方示例仓库（12 篇）

#### 252｜xlang-ai/OSWorld

- **检索号**：Z-01　**类别**：Z 补漏：CUA 高星开源实现与官方示例仓库　**轮次**：第三轮
- **作者 / 机构**：xlang-ai（GitHub 组织，OSWorld 官方评测仓库）
- **时间**：2023　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/xlang-ai/OSWorld>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★3,253（GitHub REST API stargazers_count，2026-11-06 查询）+ 学术背书：仓库描述明示 "[NeurIPS 2024] OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments"，homepage 为 os-world.github.io，许可证 Apache-2.0（均可核验）
- **页面依据**："Suppose you are operating on a system that has not been virtualized (e.g. your desktop, laptop, bare metal machine)"
- **要点**：README 给出在真实桌面环境（Ubuntu/Windows VM 或本机）跑多模态 agent 的评测环境：`pip install -r requirements.txt`、`python quickstart.py`，`provider_name` 可为 `vmware`/`docker`、`os_type` 为 "Ubuntu or Windows"，并要求 "Please ensure that the version of Python is >= 3.10"。运行前提写明需 "Install VMware Workstation Pro ... and configure the vmrun command"（Apple 芯片用 VMware Fusion，亦支持 VirtualBox），且 "We recommend running the VM with KVM support"（`egrep -c '(vmx|svm)' /proc/cpuinfo`），macOS 主机 "generally do not support KVM"。只描述页面已有事实。
- **与主题关联**：为本地 PC 上的 CUA 提供可复现的真实 OS 评测环境与虚拟机运行前提。

#### 253｜microsoft/OmniParser

- **检索号**：Z-02　**类别**：Z 补漏：CUA 高星开源实现与官方示例仓库　**轮次**：第三轮
- **作者 / 机构**：Microsoft（组织 microsoft）
- **时间**：2024　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/microsoft/OmniParser>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★25,609（GitHub REST API stargazers_count，2026-11-06 查询）+ 学术/工程背书：README 给出技术报告 arXiv:2408.00203（"OmniParser for Pure Vision Based GUI Agent"），明示 "[2024/09] OmniParser achieves the best performance on Windows Agent Arena!" 与 "[2024/10] OmniParser was the #1 trending model on huggingface model hub"，许可证 CC-BY-4.0（均可核验）
- **页面依据**："OmniParser is a comprehensive method for parsing user interface screenshots into structured and easy-to-understand elements, which significantly enhances the ability of GPT-4V to generate actions that can be accurately grounded in the corresponding regions of the interface."
- **要点**：把 UI 截图解析成结构化、易理解的元素（可交互区域检测 + icon 功能描述），供 GPT-4V 等模型把动作准确落到界面区域。本地运行 README 给出 `conda create -n "omni" python==3.12`、`pip install -r requirements.txt`、`huggingface-cli download microsoft/OmniParser-v2.0 ... --local-dir weights`、`python gradio_demo.py`。另提供 OmniTool "Control a Windows 11 VM with OmniParser + your vision model of choice"，支持 OpenAI、DeepSeek、Qwen2.5VL 或 Anthropic Computer Use。
- **与主题关联**：本地 PC 上纯视觉 CUA 的屏幕解析层，可本地下载权重运行并驱动 Windows VM。

#### 254｜showlab/ShowUI

- **检索号**：Z-03　**类别**：Z 补漏：CUA 高星开源实现与官方示例仓库　**轮次**：第三轮
- **作者 / 机构**：Show Lab @ National University of Singapore, Microsoft（README 明示）
- **时间**：2024　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/showlab/ShowUI>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★1,929（GitHub REST API stargazers_count，2026-11-06 查询）+ 学术背书：仓库描述标注 "[CVPR 2025]"，README 明示 "ShowUI has been accepted to CVPR 2025"、"ShowUI received Outstanding Paper Award at NeurIPS2024 Open-World Agents workshop"，配套论文 arXiv:2411.17465，许可证 Apache-2.0（均可核验）
- **页面依据**："Open-source, End-to-end, Lightweight, Vision-Language-Action model for GUI Agent & Computer Use."
- **要点**：端到端 VLA 模型（ShowUI-2B），输入截图与查询输出 GUI 动作。README 明示 "[2024.12.5] Major Update: ShowUI is integrated into OOTB for local run!"、"See Computer Use OOTB ... for using ShowUI to control your PC"，并给出 `python3 api.py`（"you don't need a GPU to deploy the model locally"）、vLLM 推理与基于 Qwen2.5-VL 的微调/量化支持。
- **与主题关联**：可本地推理的开源 VLA GUI/Computer Use 模型，并给出控制本机 PC 的 OOTB 落地路径。

#### 255｜OS-Copilot/OS-Copilot

- **检索号**：Z-04　**类别**：Z 补漏：CUA 高星开源实现与官方示例仓库　**轮次**：第三轮
- **作者 / 机构**：OS-Copilot（GitHub 组织）
- **时间**：2024　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/OS-Copilot/OS-Copilot>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★1,797（GitHub REST API stargazers_count，2026-11-06 查询）+ 学术背书：README 明示 "*2024.3*: OS-Copilot is accepted at the LLM Agents Workshop@ICLR 2024!"，引用 "Os-copilot: Towards generalist computer agents with self-improvement"（arXiv:2402.07456），许可证 MIT（均可核验）
- **页面依据**："OS-Copilot is an open-source library to build generalist agents capable of automatically interfacing with comprehensive elements in an operating system (OS), including the web, code terminals, files, multimedia, and various third-party applications."
- **要点**：面向 OS 级通用 agent（FRIDAY），覆盖 web、代码终端、文件、多媒体与第三方应用。本地运行 README 给出 `conda create -n oscopilot_env python=3.10 -y`、`pip install -e .`、`python quick_start.py`，并需在 `.env` 配置 OpenAI API Key（`cp .env_template .env`）；另提供 Excel 自动化等教程与前端界面，注明 "FRIDAY currently only supports single-round conversation"。
- **与主题关联**：把"操作整个操作系统"做成开源库的本地通用计算机 agent，附 ICLR workshop 背书。

#### 256｜OpenHands/OpenHands（原 All-Hands-AI/OpenHands，已重定向）

- **检索号**：Z-05　**类别**：Z 补漏：CUA 高星开源实现与官方示例仓库　**轮次**：第三轮
- **作者 / 机构**：OpenHands（GitHub 组织；原 owner All-Hands-AI）
- **时间**：2024　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/OpenHands/OpenHands>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★92,797（GitHub REST API stargazers_count，2026-11-06 查询）+ 工程背书：官方 homepage openhands.dev、MIT 许可、README 明示 "It runs locally on your machine by default"，仓库 About 描述 "🙌 OpenHands: AI-Driven Development"，并列出 software-agent-sdk / automation 等多仓库体系（均可核验）
- **页面依据**："It runs locally on your machine by default, but can connect to multiple “agent backends”, e.g. running agents in Docker containers, on VMs, or within your company infrastructure."
- **要点**：本地默认运行的自托管"开发控制中心"（Agent Canvas），README 明示可在 "your laptop, on a dedicated computer like a Mac Mini" 上跑，也可接 Docker 容器沙箱。本地运行 `npm install -g @openhands/agent-canvas` + `agent-canvas`（要求 "Node.js 24 or later, uv"），或 `docker run ... ghcr.io/openhands/agent-canvas:1.36.0`，UI 在 http://localhost:8000。README 还给出 "Create automations and workflows ... Run on a schedule or in response to webhook events" 与 ACP/MCP 兼容说明。
- **与主题关联**：把"常驻、按 schedule/webhook 主动触发的本地 agent"落到家用 PC 的超高星实现，契合主动式 AI。

#### 257｜openinterpreter/openinterpreter（原 OpenInterpreter/open-interpreter，已重定向）

- **检索号**：Z-06　**类别**：Z 补漏：CUA 高星开源实现与官方示例仓库　**轮次**：第三轮
- **作者 / 机构**：Open Interpreter（组织 openinterpreter）
- **时间**：2023　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/openinterpreter/openinterpreter>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★68,817（GitHub REST API stargazers_count，2026-11-06 查询）+ 工程背书：homepage openinterpreter.com、Apache-2.0 许可、README 明示 "Runs commands inside native sandboxing on macOS, Linux, and Windows"，并单列 "Computer Use" 章节（均可核验）
- **页面依据**："Open Interpreter ships with a QA skill that lets any model operate and test interfaces. It can drive web apps in a real browser with agent-browser, or operate and test native apps with trycua."
- **要点**：本地终端里运行 `interpreter` 启动会话（macOS/Linux `curl -fsSL https://www.openinterpreter.com/install | sh`，Windows `irm https://www.openinterpreter.com/install.ps1 | iex`），在 macOS/Linux/Windows 原生沙箱执行命令。README "Computer Use" 章明示可经 agent-browser 操作真实浏览器网页、经 trycua 操作原生应用，并支持 ACP、MCP、Codex exec 协议与本地 `~/.openinterpreter` 状态。
- **与主题关联**：本地 PC 上以终端 agent + Computer Use QA skill 操作浏览器与原生应用的通用底座。

#### 258｜Skyvern-AI/skyvern

- **检索号**：Z-07　**类别**：Z 补漏：CUA 高星开源实现与官方示例仓库　**轮次**：第三轮
- **作者 / 机构**：Skyvern-AI（组织，skyvern.com）
- **时间**：2024　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/Skyvern-AI/skyvern>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★23,349（GitHub REST API stargazers_count，2026-11-06 查询；仓库页显示 "**23.3k** stars" 相互印证）+ 工程背书：AGPL-3.0 许可、homepage skyvern.com，README 明示 "Skyvern is a Playwright extension that adds AI-powered browser automation." 与 "It provides a Playwright-compatible SDK"（均可核验）
- **页面依据**："Skyvern automates browser-based workflows using LLMs and computer vision."
- **要点**：用 Vision LLM 代替 "code-defined XPath interactions" 学习并操作网页。本地运行 `pip install "skyvern[all]"` + `skyvern quickstart`，或 `git clone ... && cd skyvern` 后 `docker compose up -d`、`skyvern run all`；README 明示 "[Python 3.11, 3.12, or 3.13]"、"The Skyvern CLI supports Windows, WSL, macOS, and Linux environments."，Windows 另需 Rust 与 C++ 工具。还可通过 `BROWSER_TYPE=cdp-connect`、`BROWSER_REMOTE_DEBUGGING_URL=http://127.0.0.1:9222` "Let Skyvern control your existing Chrome browser — with all your cookies, logins, and extensions."
- **与主题关联**：本地自托管的视觉浏览器 CUA，可直接复用用户已有 Chrome 会话。

#### 259｜OthersideAI/self-operating-computer

- **检索号**：Z-08　**类别**：Z 补漏：CUA 高星开源实现与官方示例仓库　**轮次**：第三轮
- **作者 / 机构**：OthersideAI / HyperWriteAI（组织）
- **时间**：2023　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/OthersideAI/self-operating-computer>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★10,305（GitHub REST API stargazers_count，2026-11-06 查询）+ 工程背书：MIT 许可、homepage hyperwriteai.com，README 明示 "Released Nov 2023, the Self-Operating Computer Framework was one of the first examples of full computer-use"，并列出已集成 GPT-4o / GPT-4.1 / o1 / Gemini / Claude 3 / Qwen-VL / LLaVa 等多模态模型（均可核验）
- **页面依据**："Using the same inputs and outputs as a human operator, the model views the screen and decides on a series of mouse and keyboard actions to reach an objective."
- **要点**：`pip install self-operating-computer` 后运行 `operate`，让模型看屏幕并决定鼠标/键盘动作序列；macOS 需为 Terminal 授权 "Screen Recording" 与 "Accessibility" 权限，README 明示 "This project is compatible with Mac OS, Windows, and Linux (with X server installed)."。支持 `-m llava` 经本地 Ollama（`ollama pull llava`、`ollama serve`）跑本地多模态模型，以及 OCR 与 Set-of-Mark 提示模式。
- **与主题关联**：最早的完整 computer-use 框架之一，直接给出"截图→鼠标键盘"的本地 PC 落地链路与本地模型选项。

#### 260｜anthropics/claude-quickstarts（原 anthropics/anthropic-quickstarts，已重定向；含 computer-use-demo）

- **检索号**：Z-09　**类别**：Z 补漏：CUA 高星开源实现与官方示例仓库　**轮次**：第三轮
- **作者 / 机构**：Anthropic（组织 anthropics）
- **时间**：2024　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/anthropics/claude-quickstarts>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★19,118（GitHub REST API stargazers_count，2026-11-06 查询）+ 官方组织背书：Anthropic 官方 quickstarts 集合、MIT 许可，README "Available Quickstarts" 明确列出 "Computer Use Demo" 并链接 `.../blob/main/computer-use-demo`，README 明示 "This project demonstrates how to leverage the computer use capabilities of Claude"（均可核验）
- **页面依据**："An environment and tools that Claude can use to control a desktop computer."
- **要点**：官方 quickstart 仓库，其中 "Computer Use Demo" 提供让 Claude 控制桌面计算机的环境与工具，README 明确称其为 "containerized Computer Use Demo"。各 quickstart 通用步骤为 "Clone this repository"、"Navigate to the specific quickstart directory"、"Install the required dependencies"、"Set up your Claude API key as an environment variable"、"Run the quickstart application"；根 README 明示 "Each quickstart project comes with its own README and setup instructions."，故具体 docker 命令在子项目自带 README 内（根页未展开，未核实）。
- **与主题关联**：Anthropic 官方 computer use 示例，给出本地可跑的容器化桌面 CUA 参考实现。

#### 261｜ServiceNow/BrowserGym

- **检索号**：Z-10　**类别**：Z 补漏：CUA 高星开源实现与官方示例仓库　**轮次**：第三轮
- **作者 / 机构**：ServiceNow（组织，ServiceNow Research）
- **时间**：2024　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/ServiceNow/BrowserGym>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★1,430（GitHub REST API stargazers_count，2026-11-06 查询；仓库页显示 "**1.4k** stars" 相互印证）+ 学术背书：README 引用 "The BrowserGym Ecosystem for Web Agent Research"（arXiv:2412.05467，标注 Transactions on Machine Learning Research 2025 / OpenReview "Expert Certification"）与 WorkArena（ICML 2024，PMLR v235），许可证 NOASSERTION（均可核验）
- **页面依据**："BrowserGym is meant to provide an open, easy-to-use and extensible framework to accelerate the field of web agent research."
- **要点**：Gym 环境统一封装多个 web 基准，README "BrowserGym includes the following benchmarks by default" 明列 MiniWoB、WebArena、VisualWebArena、WorkArena、AssistantBench 等。本地 `pip install browsergym`、`playwright install chromium`，demo agent 需 `OPENAI_API_KEY` 并运行 `python demo_agent/run_demo.py --task_name openended --start_url https://www.google.com`，可用 `use_screenshot` 给 VLM。页面未明示 Python 版本或支持操作系统（未核实）。
- **与主题关联**：本地 PC 上评测/开发浏览器 CUA 的统一 Gym 环境与多基准入口。

#### 262｜openai/openai-cua-sample-app

- **检索号**：Z-11　**类别**：Z 补漏：CUA 高星开源实现与官方示例仓库　**轮次**：第三轮
- **作者 / 机构**：OpenAI（组织 openai）
- **时间**：2025　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/openai/openai-cua-sample-app>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★1,923（GitHub REST API stargazers_count，2026-11-06 查询）+ 官方组织背书：OpenAI 官方 CUA 示例仓库、MIT 许可，仓库描述 "Learn how to use CUA (our Computer Using Agent) via the API on multiple computer environments."，README 明示 "Both use the Responses API"（均可核验）
- **页面依据**："This repository contains two computer-use agents: one runs JavaScript with Playwright to control a browser; the other runs Python with PyAutoGUI to control a desktop through screenshots, mouse input, and keystrokes."
- **要点**：官方给出两条本地 CUA 参考实现——JS/Playwright 控浏览器、Python/PyAutoGUI 经截图+鼠标+键盘控桌面。运行前提 README 写明 "You need Node.js 22.20.0 and an OpenAI API key"、pnpm 10.26.0、`export OPENAI_API_KEY="your_api_key_here"`，Python 侧 "use Python 3.10+ (the repo pins 3.12)" 与 uv；启动 `pnpm dev:js` / `pnpm dev:python`，控制台在 http://127.0.0.1:3000。README 明示 Python 侧 "controlling a visible browser on your desktop"、"Python controls your real mouse and keyboard"。
- **与主题关联**：OpenAI 官方把 CUA 落到本地浏览器与真实桌面的最小可跑示例。

#### 263｜asweigart/pyautogui

- **检索号**：Z-12　**类别**：Z 补漏：CUA 高星开源实现与官方示例仓库　**轮次**：第三轮
- **作者 / 机构**：Al Sweigart（个人开发者，GitHub 用户 asweigart）
- **时间**：2014　**类型**：官方 GitHub 仓库
- **出处**：<https://github.com/asweigart/pyautogui>
- **核验**：直连 200 · GitHub 页使用「owner/repo: description」通用标题，已按仓库正文核验
- **影响力**：GitHub ★12,755（GitHub REST API stargazers_count，2026-11-06 查询）+ 工程背书：BSD-3-Clause 许可，README 明示 "PyAutoGUI supports Python 2 and 3." 并逐平台说明底层 API（Windows WinAPI/ctypes、macOS Cocoa、Linux Xlib），官方文档 pyautogui.readthedocs.org（均可核验）
- **页面依据**："PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard."
- **要点**：`pip install pyautogui` 后提供 `pyautogui.click()`、`moveTo()`、`write()`、`hotkey()` 等鼠标键盘注入，以及 `pyautogui.screenshot()`、`locateOnScreen('button.png')` 截图与图像定位。README 说明 "On Windows, PyAutoGUI accesses the Windows API ... through the built-in ctypes module"、"On macOS, PyAutoGUI uses the rubicon-objc module to access the Cocoa API"、"On Linux, PyAutoGUI uses the Xlib module to access the X11 or X Window System"，并注明 Windows 无额外依赖、macOS 需 pyobjc-core/pyobjc、Linux 需 python3-xlib 与 Pillow。
- **与主题关联**：本地 PC 上 CUA 最基础的跨平台鼠标/键盘注入与屏幕捕获库，被 openai-cua-sample-app 等上层示例直接复用。

### AA 类｜补漏：CUA 评测基准、数据集、公开榜单与关键方法论文（14 篇）

#### 264｜WebArena-x（WebArena 官方项目主页，条目标题「WebArena / A realistic web environment for building autonomous agents」）

- **检索号**：AA-01　**类别**：AA 补漏：CUA 评测基准、数据集、公开榜单与关键方法论文　**轮次**：第三轮
- **作者 / 机构**：WebArena-x 团队（项目页未列作者；配套论文 arXiv:2307.13854 作者为 Shuyan Zhou、Frank F. Xu、Hao Zhu、Graham Neubig 等）
- **时间**：2023-07　**类型**：官方项目页
- **出处**：<https://webarena.dev>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验；独立抓取二次确认「WebArena-x（WebArena 官方项目主页，站点 title 为项目短名）」
- **影响力**：官方项目页存在；页面对 WebArena 条目标注「NeurIPS 2024 · Oral」，并列出 VisualWebArena「ACL 2024」、TheAgentCompany「ICML 2025」等配套基准（DBLP 把配套论文记作 ICLR 2024，两处标注不一致，此处照录页面）；配套论文 arXiv:2307.13854 摘要给出 GPT-4 智能体端到端成功率 14.41%、人类 78.24%
- **页面依据**："A realistic web environment for building autonomous agents."
- **要点**：这是 WebArena 自托管可复现网页环境的官方入口，导航到 WebArena、WebArena-Infinity、VisualWebArena、TheAgentCompany 等同一团队基准；与已收录的 arXiv:2307.13854 为同一工作的不同形态——arXiv 页是论文正文与 14.41%/78.24% 数字，本页是官方复现资源与基准家族索引，便于按本地 PC 部署所需挑选环境镜像与任务集。WebArena 定义电商、论坛、协作开发、内容管理四类真实网站上的长时程、功能正确性任务，是浏览器型 CUA 评测的基座。
- **与主题关联**：为家用机上自托管 WebArena 类网页环境、复现 CUA 评测提供官方入口与任务/镜像索引。

#### 265｜WebArena-Infinity: Generating Browser Environments with Verifiable Tasks at Scale

- **检索号**：AA-02　**类别**：AA 补漏：CUA 评测基准、数据集、公开榜单与关键方法论文　**轮次**：第三轮
- **作者 / 机构**：页面未标注作者/机构（webarena-x / WebArena 官方项目子页）
- **时间**：n.d.　**类型**：官方项目页
- **出处**：<https://webarena.dev/webarena-infinity>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验；站点重定向至 https://webarena.dev/webarena-infinity/；独立抓取二次确认「Blog（webarena.dev 官方 WebArena-Infinity 发布页，站点通用 title）」
- **影响力**：官方项目页存在并给出量化规模：10 个环境、1,260 个可验证任务、2,070 条成功轨迹；页面「Performance of Browser-use Agents」列出 Gemini-3-Flash with Browser Use 69.3%（873/1260）、Qwen-3.5-Plus 49.1%、Kimi-K2.5 45.9% 等成功率；页面未标注会议信息
- **页面依据**："ten environments along with 1,260 verifiable tasks spanning multiple domains"
- **要点**：与 AA-01 的 WebArena 原始人工构建基准不同，本页是同团队的后续工作，主张自动生成高真实性、带 verifier 的浏览器环境与任务，覆盖 careers、DevOps、finance、healthcare、productivity 等领域；页面说明其成功率低于 WebArena、OSWorld-verified 等人工基准，反映自动生成任务仍有较高难度。它为本地 PC 提供可规模化生成、可自动判定的 CUA 训练/评测任务来源。
- **与主题关联**：给出在本地机器上批量生成可验证浏览器任务、降低人工标注成本的评测数据方案。

#### 266｜VisualAgentBench: Towards Large Multimodal Models as Visual Foundation Agents

- **检索号**：AA-03　**类别**：AA 补漏：CUA 评测基准、数据集、公开榜单与关键方法论文　**轮次**：第三轮
- **作者 / 机构**：Xiao Liu、Tianjie Zhang、Yu Gu、Iat Long Iong、Yifan Xu 等（arXiv 页未列机构；配套仓库 github.com/THUDM/VisualAgentBench）
- **时间**：2024-08　**类型**：论文
- **出处**：<https://arxiv.org/abs/2408.06327>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：页面量化成绩：对 9 个闭源 LMM API 与 8 个开源模型做系统评测（"Through rigorous testing across nine proprietary LMM APIs and eight open models"）；页面未标注会议信息（arXiv 预印本 2024-08）
- **页面依据**："we introduce VisualAgentBench (VAB), a comprehensive and pioneering benchmark specifically designed to train and evaluate LMMs as visual foundation agents across diverse scenarios, including Embodied, Graphical User Interface, and Visual Design"
- **要点**：定义跨具身、GUI、视觉设计三类场景、共 5 个环境的视觉基座智能体基准，并附带由程序式求解器、LMM 自举与人类示范混合构建的轨迹训练集用于行为克隆。其 GUI 分支（VAB-Mobile、VAB-WebArena-Lite）直接对应本地桌面/浏览器的截图—动作评测，提供「先看懂屏幕再操作」的统一打分口径。
- **与主题关联**：为本地 PC 上运行的多模态 CUA 提供 GUI 场景的公开评测集与可复用轨迹训练数据。

#### 267｜AgentBench: A Comprehensive Benchmark to Evaluate LLMs as Agents（官方仓库，含 Leaderboard）

- **检索号**：AA-04　**类别**：AA 补漏：CUA 评测基准、数据集、公开榜单与关键方法论文　**轮次**：第三轮
- **作者 / 机构**：Xiao Liu、Hao Yu、Hanchen Zhang、Yifan Xu 等（THUDM / 清华大学；据仓库 Citation 的 BibTeX）
- **时间**：2023-08　**类型**：官方项目页
- **出处**：<https://github.com/THUDM/AgentBench>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：GitHub 仓库标题明示「(ICLR'24)」；页面含官方 Leaderboard 与 8 个评测环境（Operating System、Database、Knowledge Graph、Digital Card Game、Lateral Thinking Puzzles 及 ALFWorld / WebShop / Mind2Web）；页面给出「Lite preset (laptops / limited RAM)」与 webshop 环境约 16GB 内存需求
- **页面依据**："AgentBench is the first benchmark designed to evaluate LLM-as-Agent across a diverse spectrum of different environments. It encompasses 8 distinct environments to provide a more comprehensive evaluation of the LLMs' ability to operate as autonomous agents in various scenarios."
- **要点**：与已收录的 arXiv:2308.03688 为同一工作的不同形态——arXiv 页给出论文与 8 维基准设计，本仓库页额外提供官方 Leaderboard、Docker Compose 一键部署、os_interaction 等本地 OS 任务环境，以及面向笔记本/有限内存的 lite 预设与各任务内存占用表。其中 os_interaction 任务让智能体在本地容器化 OS 中执行 shell 与文件操作，是本地 PC 实现 CUA 最早的可复现评测环境之一。
- **与主题关联**：直接给出在家用机（含内存受限）上容器化运行 OS 级智能体评测与榜单对齐的工程参照。

#### 268｜GAIA Leaderboard（GAIA 官方榜单）

- **检索号**：AA-05　**类别**：AA 补漏：CUA 评测基准、数据集、公开榜单与关键方法论文　**轮次**：第三轮
- **作者 / 机构**：页面未标注作者/机构（官方 GAIA Leaderboard；页面链接论文 arXiv:2311.12983）
- **时间**：2023-11　**类型**：官方榜单
- **出处**：<https://gaia-benchmark-leaderboard.hf.space>
- **核验**：直连 200 · 页面标题为站点通用标题 / 项目短标题 / 重定向页，已按正文核验；独立抓取二次确认「Gradio（GAIA benchmark leaderboard 托管于 Hugging Face Space，页面 title 为框架通用名）」
- **影响力**：官方 Leaderboard 存在并持续收录提交；页面量化：450+ 道需工具与自主性的题、按 3 个 level 划分并区分公开 dev 与私有 test；榜单给出实时分数（如 Keen AgenticOS V1.1 平均 94.35%、Level 1 97.85%、Level 3 89.8%，提交日期 2026-11-03）
- **页面依据**："GAIA is made of more than 450 non-trivial question with an unambiguous answer, requiring different levels of tooling and autonomy to solve. It is therefore divided in 3 levels"
- **要点**：与已收录的 arXiv:2311.12983 论文页为同一基准的不同形态——论文给题目设计与人类/模型基线，本页是持续更新的公开榜单，按平均分与 Level 1/2/3 分数、模型家族、机构、提交日期列出各系统成绩。GAIA 要求网页浏览、多模态文件处理、工具调用与多步推理，适合衡量本地主动式助理的「通用任务闭环」能力而非单步 GUI 动作。
- **与主题关联**：为家用机主动式 AI 提供「多工具 + 网页 + 文件」综合任务的公开对标榜单。

#### 269｜The BrowserGym Ecosystem for Web Agent Research

- **检索号**：AA-06　**类别**：AA 补漏：CUA 评测基准、数据集、公开榜单与关键方法论文　**轮次**：第三轮
- **作者 / 机构**：Thibault Le Sellier De Chezelles、Maxime Gasse、Alexandre Drouin、Massimo Caccia 等（arXiv 页未列机构；含 Graham Neubig、Ruslan Salakhutdinov、Nicolas Chapados、Alexandre Lacoste 等）
- **时间**：2024-12　**类型**：论文
- **出处**：<https://arxiv.org/abs/2412.05467>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：页面量化：首次大规模多基准实验，比较 6 个 SOTA LLM 在 6 个流行 web agent 基准上的表现，并指出 Claude-3.5-Sonnet 在多数基准领先、视觉任务上 GPT-4o 更优；页面未标注会议信息（arXiv 预印本 2024-12，v4 2025-02）；其前身 BrowserGym 由 WorkArena（arXiv:2403.07718）摘要自述引入
- **页面依据**："We propose an extended BrowserGym-based ecosystem for web agent research, which unifies existing benchmarks from the literature and includes AgentLab, a complementary framework that aids in agent creation, testing, and analysis."
- **要点**：把碎片化的网页智能体基准统一到 gym 式观测/动作空间，并用 AgentLab 管理智能体创建、大规模并行实验与轨迹分析；摘要明确指出评测方法不一致会导致结果难以复现。对本地 PC 而言，它给出在单机上用统一接口跑 WebArena、WorkArena、MiniWoB++ 等多基准并做可复现对比的框架层。
- **与主题关联**：提供本地浏览器 CUA 的统一环境接口与实验管理框架，解决多基准对接与可复现评测问题。

#### 270｜OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web

- **检索号**：AA-07　**类别**：AA 补漏：CUA 评测基准、数据集、公开榜单与关键方法论文　**轮次**：第三轮
- **作者 / 机构**：Raghav Kapoor、Yash Parag Butala、Melisa Russak、Jing Yu Koh、Kiran Kamble、Waseem Alshikh、Ruslan Salakhutdinov（arXiv 页未列机构）
- **时间**：2024-02　**类型**：论文
- **出处**：<https://arxiv.org/abs/2402.17553>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：页面量化：覆盖桌面应用与网页的截图+自然语言任务，最强基线 GPT-4 仅达人类生成可执行脚本水平的 15%；页面未标注会议信息（arXiv 预印本 2024-02，v3 2024-07）
- **页面依据**："we introduce OmniACT, the first-of-a-kind dataset and benchmark for assessing an agent's capability to generate executable programs to accomplish computer tasks"
- **要点**：任务输入为「一张屏幕截图 + 视觉接地的自然语言指令」，输出为能完整执行任务的可执行脚本，涵盖「播放下一首歌」等短任务与「给 John Doe 发邮件告知见面时间地点」等长时程任务，并明确超出传统网页自动化、覆盖桌面应用。相比只测点击坐标的基准，它更贴近本地 PC 上「感知屏幕→生成并运行脚本」的主动式自动化形态。
- **与主题关联**：为本地桌面 CUA 提供以可执行脚本为动作空间的评测范式与难度基线（GPT-4 约人类 15%）。

#### 271｜GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding

- **检索号**：AA-08　**类别**：AA 补漏：CUA 评测基准、数据集、公开榜单与关键方法论文　**轮次**：第三轮
- **作者 / 机构**：Dongping Chen、Yue Huang、Siyuan Wu、Jingyu Tang、Liuyi Chen 等（arXiv 页未列机构）
- **时间**：2024-06　**类型**：论文
- **出处**：<https://arxiv.org/abs/2406.10819>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：页面 Comments 明示「Accepted by ICLR 2025」；页面量化：覆盖 6 类 GUI 场景、8 类 GUI 问题、3 种格式，含 Human-MLLM 精细标注，并评测 Image LLM 与 Video LLM；配套项目页 gui-world.github.io
- **页面依据**："this paper introduces a new dataset, termed GUI-World, which features meticulously crafted Human-MLLM annotations, extensively covering six GUI scenarios and eight types of GUI-oriented questions in three formats"
- **要点**：与已收录的 ScreenSpot-Pro（静态高分辨率 grounding）与「LLM-Brained GUI Agents」综述不同，本工作专攻 GUI 的时序/动态理解：桌面软件、多窗口交互、动态网页内容与多步任务，结论是现有模型若无人工关键帧或操作历史便难以处理动态 GUI，Video LLM 在稀疏 GUI 视频上普遍不足。它补上了本地 CUA 在「连续屏幕变化、多窗口」下的评测与数据缺口。
- **与主题关联**：给本地桌面长期运行的主动式 CUA 提供动态 GUI / 多窗口理解的视频基准与失败边界。

#### 272｜osunlp/Online-Mind2Web · Datasets at Hugging Face（Online-Mind2Web 官方数据集页）

- **检索号**：AA-09　**类别**：AA 补漏：CUA 评测基准、数据集、公开榜单与关键方法论文　**轮次**：第三轮
- **作者 / 机构**：OSU NLP Group（页面标注组织 osunlp；配套论文 Tianci Xue、Weijian Qi、Tianneng Shi 等，arXiv:2504.01382）
- **时间**：2025-04　**类型**：官方数据集
- **出处**：<https://huggingface.co/datasets/osunlp/Online-Mind2Web>
- **核验**：本机直连受代理链路影响（502 / SSL 超时）；独立抓取二次确认「osunlp/Online-Mind2Web · Datasets at Hugging Face（数据集卡含 136 个网站、300 个任务与 arXiv:2504.01382 引用）」
- **影响力**：官方数据集页与官方 Leaderboard 均存在（页面链接 huggingface.co/spaces/osunlp/Online_Mind2Web_Leaderboard）；页面量化：300 个高质量任务、136 个热门网站；页面标注论文 arXiv:2504.01382 与配套代码仓 github.com/OSU-NLP-Group/Online-Mind2Web；数据集字段含 reference_length（人类完成所需步数）并定期更新失效任务
- **页面依据**："Online-Mind2Web is the online version of Mind2Web, a more diverse and user-centric dataset includes 300 high-quality tasks from 136 popular websites across various domains."
- **要点**：与已收录的 Mind2Web 静态数据集（arXiv:2306.06070 及官方仓库）不同，本页是其在真实在线网站上的在线版本，覆盖服装、食品、住房、交通等用户任务，并配套 Agent-as-a-Judge 式评测与公开榜单；页面明确会替换过期/含验证码的任务以维持基准有效性。它更适合检验本地 PC 上浏览器智能体面对真实、随时间变化的网站时的鲁棒性。
- **与主题关联**：为家用机浏览器 CUA 提供「真实在线网站 + 官方榜单」的持续有效性评测集。

#### 273｜OSWorld-Human: Benchmarking the Efficiency of Computer-Use Agents

- **检索号**：AA-10　**类别**：AA 补漏：CUA 评测基准、数据集、公开榜单与关键方法论文　**轮次**：第三轮
- **作者 / 机构**：Reyna Abhyankar、Qi Qi、Yiying Zhang（arXiv 页未列机构）
- **时间**：2025-06　**类型**：论文
- **出处**：<https://arxiv.org/abs/2506.16042>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：页面量化：在 OSWorld 上评测 16 个智能体，指出最佳智能体仍多走 2.7–4.3 倍于必要的步数，且规划/反思/判定的大模型调用占总延迟大头、后续每一步可达起始步骤 3 倍耗时；页面未标注会议信息（arXiv 预印本 2025-06，v2 2026-05）
- **页面依据**："We find that large model calls for planning, reflection, and judging account for most of the overall latency, and as an agent uses more steps to complete a task, each successive step can take 3x longer than steps at the beginning of a task."
- **要点**：这是少数专攻「效率/延迟」而非成功率的工作：构建带人类标注最优轨迹的 OSWorld-Human，指出 SOTA 系统虽刷高准确率，端到端延迟却达数十分钟、任务人类只需几分钟，因而在实际不可使用。对资源受限的家用机而言，它把步数冗余、规划反思调用次数、逐步变慢等成本项变成可测量指标，直接指导本地 CUA 的延迟与算力预算设计。
- **与主题关联**：为本地 PC 资源受限条件下运行 CUA 提供延迟、步数冗余与算力成本的量化评测依据。

#### 274｜AndroidLab: Training and Systematic Benchmarking of Android Autonomous Agents

- **检索号**：AA-11　**类别**：AA 补漏：CUA 评测基准、数据集、公开榜单与关键方法论文　**轮次**：第三轮
- **作者 / 机构**：Yifan Xu、Xiao Liu、Xueqiao Sun、Siyi Cheng、Hao Yu 等（配套仓库 github.com/THUDM/Android-Lab）
- **时间**：2024-10　**类型**：论文
- **出处**：<https://arxiv.org/abs/2410.24024>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：页面量化：预定义 Android 虚拟设备与 9 个 App 上的 138 个任务；构建 Android Instruction 数据集训练 6 个开源 LLM/LMM，平均成功率 LLM 从 4.59% 升至 21.50%、LMM 从 1.93% 升至 13.28%；页面未标注会议信息（arXiv 预印本 2024-10，v2 2024-11）
- **页面依据**："AndroidLab benchmark includes predefined Android virtual devices and 138 tasks across nine apps built on these devices."
- **要点**：与已收录的 AitW、GUIOdyssey、MobileAgentBench、AndroidWorld 等移动端基准不同，本工作在同一动作空间里同时支持 LLM 与 LMM、并给出可复现的操作环境 + 指令数据集 + 训练前后量化提升，强调对开源与闭源模型的系统性对照。其「虚拟设备 + 统一动作空间 + 可复现基准」结构可迁移到本地 PC 上以虚拟机运行桌面/移动 CUA 的评测搭建。
- **与主题关联**：补充移动端 GUI 数据集/基准维度，并示范「本地虚拟设备 + 指令微调」提升 CUA 成功率的完整链路。

#### 275｜GPT-4V(ision) is a Generalist Web Agent, if Grounded（SEEACT）

- **检索号**：AA-12　**类别**：AA 补漏：CUA 评测基准、数据集、公开榜单与关键方法论文　**轮次**：第三轮
- **作者 / 机构**：Boyuan Zheng、Boyu Gou、Jihyung Kil、Huan Sun、Yu Su（配套仓库 github.com/OSU-NLP-Group/SeeAct）
- **时间**：2024-01　**类型**：论文
- **出处**：<https://arxiv.org/abs/2401.01614>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：页面量化：在真实网站上把文本计划人工 grounding 成动作时，GPT-4V 可完成 51.1% 的任务，显著优于纯文本 GPT-4 及针对网页智能体微调的 FLAN-T5、BLIP-2；并指出 set-of-mark prompting 等现有 grounding 策略对网页智能体无效；页面未标注会议信息（arXiv 预印本 2024-01，v2 2024-03）
- **页面依据**："In addition to standard offline evaluation on cached websites, we enable a new online evaluation setting by developing a tool that allows running web agents on live websites."
- **要点**：提出 SEEACT 通用网页智能体，把「LMM 读截图做规划」与「把文本计划 grounding 成网页动作」明确拆开，并首次给出缓存网站的离线评测之外的在线真实网站评测工具；结论是 grounding 仍是主要瓶颈，最佳策略需同时利用 HTML 结构与视觉。对本地 PC CUA 而言，它定义了截图感知→计划→元素定位这一最核心方法链路及格化评测口径。
- **与主题关联**：为本地浏览器 CUA 提供「视觉理解 + HTML 结构接地」的关键方法基线与在线评测工具范式。

#### 276｜Scaling Agents for Computer Use

- **检索号**：AA-13　**类别**：AA 补漏：CUA 评测基准、数据集、公开榜单与关键方法论文　**轮次**：第三轮
- **作者 / 机构**：Gonzalo Gonzalez-Pumariega、Vincent Tu、Chih-Lun Lee、Jiachen Yang、Ang Li、Xin Eric Wang（Agent S3 配套论文）
- **时间**：2025-10（v1 2025-10-02，v2 2026-02-03）　**类型**：论文
- **出处**：<https://arxiv.org/abs/2510.02250>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：页面摘要给出 OSWorld 72.6% 的新 SOTA，并写明超过人类水平 72.36%；simular-ai/Agent-S 官方 README Updates 段标注 "The Agent S3 paper 'Scaling Agents for Computer Use' is accepted to TMLR 2026!"；arXiv 页面 Comments 为 "21 pages, 7 figures, 13 tables"，页面本身未标注会议信息
- **页面依据**："Using multiple rollouts, BJudge establishes a new state of the art (SoTA) in OSWorld at 72.6%, significantly outperforming prior methods and surpassing human-level performance at 72.36%"
- **要点**：提出 Behavior Judge（BJudge），把智能体的多次执行表示为「行为叙事」并在该层面对候选轨迹做比较与选择，以支持对长程 CUA 行为的推理时扩展；论文指出单次 rollout 误差会累积、方差高，而多次 rollout 的难点在于长程行为难以评估与挑选。摘要还给出对 WindowsAgentArena 与 AndroidWorld 的跨操作系统泛化结果。对本地 PC 而言，该文提供的是「用多次采样 + 轨迹选择提升成功率」的评测与方法证据，而非模型规模扩张。
- **与主题关联**：补齐 Agent S 系列在本地计算机 CUA 上的长程 scaling 与轨迹选择方法论文，与已收录的 Agent S（N-02）、Agent S2（N-08）构成同一条公开研究线。

#### 277｜Evolving Agent Interfaces

- **检索号**：AA-14　**类别**：AA 补漏：CUA 评测基准、数据集、公开榜单与关键方法论文　**轮次**：第三轮
- **作者 / 机构**：Saaket Agashe、Yuzhe Yang、Gonzalo Gonzalez-Pumariega、Bhuvan Chandra Koduru、Chih-Lun Li、Jiachen Yang、Ang Li、Xin Eric Wang（Agent S4 配套论文）
- **时间**：2026-10（v1 2026-10-20）　**类型**：论文
- **出处**：<https://arxiv.org/abs/2610.28601>
- **核验**：直连 200 · 页面标题与文献标题吻合
- **影响力**：页面摘要给出 OSWorld V2 上 21.3% binary score、为同一模型固定接口配置的 3.8 倍，并列明高于 GPT-5.5（13.0%）与 Claude Opus 4.8（20.6%）；simular-ai/Agent-S 官方 README Updates 段标注 2026/10/20 发布 Agent S4 及该论文；arXiv 页面未标注会议信息
- **页面依据**："We introduce Agent S4, an autonomous computer-use scientist that builds Evolving Agent Interfaces from task experience."
- **要点**：论文主张「接口设计本身应成为智能体能力」：元智能体在无成功标签的合成训练任务上检视任务智能体的轨迹，构建并修订一个接口与使用知识仓库，再由种群式演化按验证任务表现选择继续演化的仓库。摘要报告在 ScienceBoard 上同模型成功率从 41.4% 提升到 58.6%，并声明已开源代码。对本地 PC CUA 而言，它讨论的是桌面智能体可调用工具/接口形态随经验演化的问题，属于方法与评测证据。
- **与主题关联**：补齐 Agent S 系列 2026 年最新的 CUA 架构演进论文，使本地桌面 CUA 的公开研究线延伸到当前时点。

---

**边界说明**：本总集是资料集合，不构成对上述命题的结论性论证，也不含任何实现建议、选型比较、架构图、代码或项目计划。「与主题关联」一句仅说明该文献可支撑命题或 CUA 资料的哪一环，供后续取证时定位；「CUA 专题文献地图」只做资料分类定位，不是技术方案。**本步未构建任何项目。**
