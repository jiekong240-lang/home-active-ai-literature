# Computer Use Agent 研究调研报告

**检索日期**：2026-11-06（UTC+8，系统本地时间 `2026-11-06 21:23 +0800`）
**重点覆盖窗口**：2025-11-06 — 2026-11-06（最近 12 个月）；纳入必需的更早经典研究并单独标注
**交付形态**：单份报告。本次只做实际检索、原文核验与整理；**未构建项目、未写方案、未执行代码、未运行任何基准测试**

---

## 1 结论与证据边界

### 1.1 能力边界（先说清楚本次实际能做什么）

| 能力 | 本次是否具备 | 实际执行情况 |
|---|---|---|
| 联网搜索发现线索 | 具备 | 已执行多轮中英文 WebSearch |
| 打开并抓取网页正文 | 具备 | 已打开 arXiv abs/HTML、官方项目页、厂商官方文档、GitHub README |
| 读取 PDF / 论文全文 | **部分** | 已取得 arXiv 提供的 PDF 与 HTML 链接，并实读 3 篇 2026 论文 HTML 正文的指定章节；**部分长文正文在抓取时被截断**，未取得完整正文、全部图表与附录 |
| 读取底层实现源码 | 具备但未做 | 只读了参考实现 README 与目录结构，**未检查源码实现** |
| 调用 GitHub 官方 API | 具备 | 已执行，取得 14 个仓库的许可证/star/维护状态快照 |
| 运行代码、跑 benchmark、独立复现 | **本次未执行** | 0 次 |

因此本报告**不会**出现「验证通过」「独立复现」「已读全文」「资料全部搜齐」「100% 正确」。网页抓取返回的是经处理的文本提取，不保证逐字全文；部分站点存在 JS 渲染、反爬或地区限制。

### 1.2 阅读与验证状态分级（本报告统一使用）

| 码 | 含义 | 本轮数量 |
|---|---|---|
| S0 | 仅检索发现，未打开原始条目 | 候选索引中 6 项 |
| S1 | 已核原始条目：打开原始页面，核对标题、作者/机构、日期、版本、DOI/arXiv ID、链接 | 29 项全部 |
| S2 | 已读摘要 | 29 项中的 24 项 |
| S3 | 已读指定章节（含正文局部、榜单、文档小节） | 8 项 |
| S4 | 已读全文（含该版本全部图表与附录） | **0 项** |
| S5 | 已检查实现（源码） | **0 项** |
| S6 | 已独立复现 | **0 项** |

> 说明：一篇材料可同时具备多个码，例如「S1+S2+S3」。**S4/S5/S6 本轮均为 0**，这是能力与时长的实际边界，不是遗漏声明。

### 1.3 证据类型标签（全文通用）

`[作者报告]` 论文/仓库作者自述 · `[维护方榜单]` 基准维护方运行并公布的官方结果 · `[官方文档]` 厂商一手文档 · `[本次实测元数据]` GitHub REST API 本次查询 · `[独立证据]` 第三方独立复现（**本轮 0 项**） · `[助手推断]` 我基于已核材料做的综合判断 · `[建议]` 待验证的行动主张。

### 1.4 由标题拆出的关键子问题与范围假设

| 编号 | 子问题 |
|---|---|
| Q1 | CUA 的边界是什么？哪些工作算 CUA，哪些只是相邻领域？ |
| Q2 | 主流技术路线有哪几条，各自解决什么、代价是什么？ |
| Q3 | 评测口径如何演变？三代 OSWorld 与跨平台基准能否互相比分？ |
| Q4 | 最近 12 个月真正的新进展是什么（而非分数刷新）？ |
| Q5 | 工程落地的一手依据：官方 tool loop、依赖、成本、隔离、许可证？ |
| Q6 | 有哪些局限、负面结果、失败案例与冲突证据？ |
| Q7 | 若要把某条结论变成可执行判断，最小验证实验是什么？ |

**范围**：CUA 指「在真实或仿真桌面/浏览器/移动 GUI 中，通过截图或结构化界面观测、以鼠标键盘动作执行任务」的智能体。排除纯 API/CLI 编排（仅在混合接口作为对照时提及）、具身机器人、以及以攻防/安全测评为唯一目标的专项基准。**排除安全类专项是沿用本会话前序约束，不是本次标题自带的要求。**

**合理假设（明写，未擅自加限制）**：
1. 标题与本次要求**没有给出**设备、预算、操作系统、部署场景或并发规模，因此本报告**不预设**这些限制，也不把前序「家用机」语境带进来当约束。
2. 以「真实 GUI 环境 + 截图/动作循环」为主线；浏览器智能体、移动端 GUI 智能体作为相邻路线单列。
3. 厂商官方文档是**接口与工程约束**的一手证据，不是**性能**证据；性能结论只来自论文与维护方榜单。
4. 「开源」不等于可商用：代码、模型权重、数据、依赖的许可证必须分别查（见 §6.3）。

### 1.5 主要结论

1. **[维护方榜单 + 作者报告] 领域重心已从「短任务成功率」转向「长时程可靠性与可验证性」**。同一团队的三代基准给出完全不同量级：OSWorld-Verified 官方榜最高 **86.0%**（100 steps，2026-08-01，[OSWorld v1 官方页](https://osworld-v1.xlang.ai/)），而 OSWorld 2.0 官方榜（最后更新 2026-10-15）最高只有 **44.33% binary / 77.67% partial**（[OSWorld v2 官方页](https://osworld-v2.xlang.ai)）。论文摘要里的 20.6% 是更早期的快照（[arXiv:2606.29537](https://arxiv.org/abs/2606.29537)）。
2. **[作者报告] 长时程失败的形态已被系统归类**：OSWorld 2.0 §4.4 指出五类——信息与约束跟踪、感知-动作时序、领域工件理解、验证与反思、长程状态漂移；§4.1.2 进一步量化「recovery + repair 合计不到 7% 的动作预算」，`>163 分钟` 的任务所有受测模型 binary completion 归零（[HTML v2 §4.1.2 / §4.4](https://arxiv.org/html/2606.29537v2)）。
3. **[作者报告] 恢复是被独立量化且当前很弱的能力**：CUA-Recovery 在 6 个 agent × 6 个接管深度上，Error Awareness Rate 最高 **44.0%**、Pass@3 最高 **25.5%**；「意识到错误」与「修复成功」几乎脱钩（aware vs unaware 的 verifier pass rate 仅 **15.6% vs 12.2%**，[arXiv:2610.27645 §5.2](https://arxiv.org/html/2610.27645v1)）。
4. **[助手推断] 近 12 个月的路线分化**为六类：原生端到端 GUI 模型、结构化感知增强、分层规划+经验/测试时扩展、多智能体并行、接口自演化、合成环境训练；同时「评测本身」成为研究对象（verified 榜单、agentic judge、negative tasks）。
5. **[官方文档] 工程落地的硬约束已相当明确且两家趋同**：隔离 VM/容器、站点与动作 allowlist、把屏幕内容视为不可信、有现实后果的动作需人工确认、以及「检查保存下来的结果而不是相信模型最终回答」（[Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)、[OpenAI](https://platform.openai.com/docs/guides/tools-computer-use)）。
6. **[本次实测元数据] 许可证必须分开看**：`microsoft/OmniParser` 为 `CC-BY-4.0`、`BangProx/ReTRACE` 的 `license` 字段为 `None`；其余样本多为 MIT / Apache-2.0（查询时间 `2026-11-06T21:33:09+08:00`，见 §6.2）。**不能凭仓库有代码就推断权重、数据集、依赖可商用。**
7. **[助手推断] 最大的阅读风险是数字错配**：binary vs partial、100 vs 300 vs 500 steps、单次 vs 多 rollout、`v2026.06.24` vs `v2.1`、作者自报 vs 维护方验证。本报告在 §4.2 给出「禁止横比矩阵」，在 §7 列出 12 条冲突。

### 1.6 本报告不主张什么

不主张已搜齐全部资料；不主张全部读懂；不主张任何模型分数在本次被复现；不主张对会议正式出版状态做过完整核验；不主张给出可直接上线的工程方案。凡未核实字段，一律标注为「未查到 / 原文未报告 / 当前无法访问 / 尚未核实」四者之一（见 §7.4）。

---

## 2 最新进展与研究地图

### 2.1 最近 12 个月时间线（按一手条目日期）

| 日期 | 事件 | 一手来源 | 类型 |
|---|---|---|---|
| 2025-10-04 | OpenCUA v3 修订，OpenCUA-72B 在 OSWorld-Verified 报 45.0% | [arXiv:2508.09123](https://arxiv.org/abs/2508.09123) | 预印本修订 |
| 2026-02-03 | Agent S3 / BJudge 论文 v2 修订（v1 为 2025-10-02） | [arXiv:2510.02250](https://arxiv.org/abs/2510.02250) | 预印本修订 |
| 2026-05-18 | OSWorld-Human v2：16 个 agent 效率研究 | [arXiv:2506.16042](https://arxiv.org/abs/2506.16042) | 预印本修订 |
| 2026-06-01 | Multi-Agent Computer Use：manager DAG + 并行子智能体 | [arXiv:2606.01533](https://arxiv.org/abs/2606.01533) | 首次发表 |
| 2026-06-09 | Mind the Gap：NCRE 办公实操考试，agentic 68.8% | [arXiv:2606.10956](https://arxiv.org/abs/2606.10956) | 首次发表 |
| 2026-06-28 / 07-13 | OSWorld 2.0 v1 / v2：108 个长时程工作流 | [arXiv:2606.29537](https://arxiv.org/abs/2606.29537) | 首次发表/修订 |
| 2026-09-14 / 09-21 | CADWorld v1/v2：FreeCAD 工件可验证评测，17.5% vs 专家 87.0% | [arXiv:2609.16251](https://arxiv.org/abs/2609.16251) | 首次发表/修订 |
| 2026-10-08 | AgentHorizon：1,373 条「指令-轨迹」对，检验自动裁判 | [arXiv:2610.11050](https://arxiv.org/abs/2610.11050) | 首次发表 |
| 2026-10-15 | OSWorld 2.0 官方榜更新至 v2.1，榜首 44.33% / 77.67% | [osworld-v2.xlang.ai](https://osworld-v2.xlang.ai) | 榜单发布 |
| 2026-10-19 | WildAWM：341 个 GUI+MCP+CLI 合成长程环境 | [arXiv:2610.26828](https://arxiv.org/abs/2610.26828) | 首次发表 |
| 2026-10-20 | CUA-Recovery / ReRail；Lost in Recovery / ReTrace；Agent S4 / Evolving Agent Interfaces（同日三篇） | [2610.27645](https://arxiv.org/abs/2610.27645)、[2610.27954](https://arxiv.org/abs/2610.27954)、[2610.28601](https://arxiv.org/abs/2610.28601) | 首次发表 |
| 2026-10-21 | Agent-S 仓库更新至 S4，README 列出 S/S2/S2.5/S3/S4 五代 | [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S) | 软件发布 |

### 2.2 研究地图（按「要解决什么」分层）

```
CUA（截图/结构化观测 → 鼠标键盘动作 → 环境反馈）
├─ 感知层：GUI grounding / 屏幕解析
│    OmniParser(2408.00203) · SeeClick · ScreenSpot-Pro(2504.07981) · UI-TARS(2501.12326)
├─ 决策层：规划、经验、动作接口
│    Agent S / ACI(2410.08164) → Agent S2(2504.00906) → Agent S3/BJudge(2510.02250)
│    → Agent S4/Evolving Interfaces(2610.28601)
│    UI-TARS-2 多轮 RL(2509.02544) · OpenCUA(2508.09123) · MACU(2606.01533)
├─ 执行层：官方 tool loop 与本地驱动
│    Anthropic computer_toolset_20260801 · OpenAI tools:[{"type":"computer"}]
│    PyAutoGUI / Playwright / CDP · 无障碍树 · 隔离容器
├─ 可靠性层（近 12 个月最活跃）
│    恢复：CUA-Recovery/ReRail(2610.27645) · ReTrace(2610.27954)
│    效率：OSWorld-Human(2506.16042)
│    裁判可靠性：AgentHorizon(2610.11050)
│    环境合成：WildAWM(2610.26828)
└─ 评测层
     短任务：OSWorld(2404.07972) → OSWorld-Verified(2025-07-28)
     长时程：OSWorld 2.0(2606.29537) · CADWorld(2609.16251)
     跨域：WindowsAgentArena(2409.08264) · AndroidWorld(2405.14573)
           WebArena(2307.13854) · macOSWorld(2506.04135) · Mind the Gap(2606.10956)
     评测治理：verified leaderboard / Public Evaluation Guideline / 自报与验证分栏
```

### 2.3 三代 OSWorld 的口径演进（**这是全篇最重要的可比性前提**）

| 代 | 任务规模 | 人类耗时 | 指标 | 步数上限 | 当前最好成绩 | 来源 |
|---|---|---|---|---|---|---|
| OSWorld 1.0（2024） | 369 任务（8 个 Google Drive 任务可排除→361；另 43 个 Windows 分析任务） | 未标注；论文给人类完成率 >72.36% | 执行式评估脚本，134 个 evaluator | 论文按 15/50/100 等设置 | 论文 2024 快照：最佳模型 12.24% | [论文](https://arxiv.org/abs/2404.07972) / [官方页](https://osworld-v1.xlang.ai/) |
| OSWorld-Verified（2025-07-28） | 同 369（可 361） | 未标注 | 榜单列名 `Success Rate (Avg±Std)`，出现小数分子与多次运行均值，**页面未定义是否纯 binary** | 榜中 15/30/50/100 | `claude-fable-5[1m]` 86.0% @100（2026-08-01） | [官方页](https://osworld-v1.xlang.ai/) / [升级博客](https://xlang.ai/blog/osworld-verified) |
| OSWorld 2.0（2026-06-28） | 108 工作流 / 7 领域 / 21 子类 / 31 自建站点 | 中位约 1.6 h；69.6% 任务 >1 h | **binary completion** 与 **partial score** 双指标；平均 27.25 个 checkpoint | 主结果 500；榜单可筛 150/300/450/500 | 论文摘要 20.6%/54.8%；官方榜 2026-10-15 为 44.33%/77.67%（v2.1） | [论文](https://arxiv.org/abs/2606.29537) / [官方榜](https://osworld-v2.xlang.ai) |

**判定**：这三代的分数**不能放在同一张趋势图里**当作同一指标的时间序列。Verified 修复了 300+ 社区反馈并把评估迁到 AWS（10+ 小时→分钟级、最多 50 个环境并行、VM 镜像 50GB→25GB），本身改变了测量条件（[升级博客](https://xlang.ai/blog/osworld-verified)）。

### 2.4 近 12 个月真正的「新东西」

`[助手推断]` 不是分数又涨了，而是四件事：
1. **把「失败与恢复」变成可测量的对象**（ReRail 用真实策略失败而非人工注入错误；ReTrace 提出 Transition-Consistent Recovery）。
2. **把「接口」变成可优化对象**（Agent S4 让 meta-agent 从无成功标签的轨迹里演化工具接口，而非只调 prompt 或换模型）。
3. **把「评测裁判」本身拿去评测**（AgentHorizon 用交换指令构造 negative tasks，发现工具调用对开放权重模型反而变差）。
4. **把「环境」变成可规模合成的训练资源**（WildAWM 用纯开源模型合成 GUI+MCP+CLI 环境，声称跨 8 个 OOD 基准有增益）。

---

## 3 核心资料总表

### 3.1 总表（29 项，均为 S1；状态列含更深阅读级别）

> 「价值」列取值：**可采用**（一手、结论可直接使用）/ **需改造**（结论依赖特定条件）/ **仅作背景** / **暂不适用** / **证据不足**。理由见 §3.2 与 §7。

| # | 资料（标题 / 机构 / 年份与版本） | 类型与原始链接 | 状态 | 关键结论与原文定位 | 价值 |
|---|---|---|---|---|---|
| 01 | OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments；Tianbao Xie 等；v1 2024-04-11 / v2 2024-05-30 | [arXiv:2404.07972](https://arxiv.org/abs/2404.07972) | S1+S2 | 369 任务；人类 >72.36%，最佳模型 12.24%（摘要，2024 快照） | 可采用（历史基线） |
| 02 | OSWorld / OSWorld-Verified 官方项目页与 Verified 榜单；XLANG Lab；持续更新，升级公告 2025-07-28 | [osworld-v1.xlang.ai](https://osworld-v1.xlang.ai/) | S1+S3（榜单与 Benchmark 段） | 68 条官方结果；最高 86.0% @100；`Success Rate (Avg±Std)`；361/369 任务说明 | 可采用（须带日期/步数） |
| 03 | OSWorld-Verified 升级说明博客；XLANG Lab；2025-07-27 | [xlang.ai/blog/osworld-verified](https://xlang.ai/blog/osworld-verified) | S1+S3 | 300+ 反馈修复；VMware/Docker→AWS；50 环境并行；VM 镜像 50GB→25GB；上榜需维护方运行并披露实现 | 可采用 |
| 04 | OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks；Mengqi Yuan 等 36 人；v1 2026-06-28 / v2 2026-07-13 | [arXiv:2606.29537](https://arxiv.org/abs/2606.29537) | S1+S2+S3（§2.1.3、§3.1、§3.2、§4.1–4.4） | 108 工作流；binary@500 20.6% / partial 54.8%；§4.4 五类失败；§4.1.2 恢复动作 <7% | 可采用 |
| 05 | OSWorld 2.0 官方项目主页与 Leaderboard；XLANG Lab；Last update 2026-10-15 | [osworld-v2.xlang.ai](https://osworld-v2.xlang.ai) | S1+S3（榜单、指标、脚注） | 榜首 Claude Opus 5 v2.1 44.33%/77.67%；`Task Horizon Remains a Hard Limit`；v2026.08.08 结果对 Opus 5 平均 7 runs | 可采用（最新上限） |
| 06 | Windows Agent Arena；Rogerio Bonatti 等（Microsoft）；v1 2024-09-12 / v2 2024-09-13 | [arXiv:2409.08264](https://arxiv.org/abs/2409.08264) | S1+S2 | 150+ Windows 任务；Azure 并行约 20 分钟；Navi 19.5% vs 人类 74.5% | 可采用（跨平台） |
| 07 | AndroidWorld；Christopher Rawles 等（Google）；v1 2024-05-23 / v5 2025-04-06 | [arXiv:2405.14573](https://arxiv.org/abs/2405.14573) | S1+S2 | 116 任务 / 20 App；最佳 30.6%；任务变体显著影响成绩；桌面 agent 迁移到移动端变差 | 可采用（负面证据） |
| 08 | WebArena；Shuyan Zhou 等（CMU）；v1 2023-07-25 / v4 2024-04-16 | [arXiv:2307.13854](https://arxiv.org/abs/2307.13854) | S1+S2 | 最佳 GPT-4 agent 14.41% vs 人类 78.24%（摘要）；**arXiv 摘要未给任务总数** | 仅作背景 |
| 09 | ScreenSpot-Pro；Kaixin Li 等；v1 2025-04-04 | [arXiv:2504.07981](https://arxiv.org/abs/2504.07981) | S1+S2 | 23 应用 / 5 行业 / 3 OS；已有最佳 grounding 仅 18.9%；ScreenSeekeR 免训练 48.1% | 可采用（grounding 瓶颈） |
| 10 | CADWorld；Zihan Dong 等；v1 2026-09-14 / v2 2026-09-21 | [arXiv:2609.16251](https://arxiv.org/abs/2609.16251) | S1+S2 | 200 个 FreeCAD 任务 / 11 类；工件可执行校验；7 个 agent 最佳 17.5% vs 专家 87.0% | 可采用（工件可验证） |
| 11 | macOSWorld；Pei Yang 等；v1 2025-06-04 / **v2 2025-06-05 已撤稿(withdrawn)** / v4 2025-10-18 | [arXiv:2506.04135](https://arxiv.org/abs/2506.04135) | S1+S2 | 202 多语任务 / 30 应用 / 5 语言；闭源 >30%，开源轻量 <5%；阿拉伯语相对英语平均降 28.8% | 需改造（须指定 v4） |
| 12 | Mind the Gap: Can Frontier LLMs Pass a Standardized Office Proficiency Exam?；Tengchao Lv 等（Microsoft）；2026-06-09 | [arXiv:2606.10956](https://arxiv.org/abs/2606.10956) | S1+S2 | NCRE 200 任务 / 7,118 条可机评标准；单轮最高 36.6%，带执行反馈的 agentic 68.8%，社区参考 95.5% | 可采用（负面证据） |
| 13 | AgentHorizon: Evaluating Agentic Judges…；Xing Han Lù 等；2026-10-08 | [arXiv:2610.11050](https://arxiv.org/abs/2610.11050) | S1+S2 | 1,373 指令-轨迹对 / 166 小时人类轨迹 / 3 OS；最佳裁判 GPT-5.5 平衡准确率 80.9%；工具调用对开放权重模型反而变差 | 可采用（评测可靠性） |
| 14 | Agent S: An Open Agentic Framework…；Saaket Agashe 等；2024-10-10 | [arXiv:2410.08164](https://arxiv.org/abs/2410.08164) | S1+S2 | ACI + 经验增强分层规划；OSWorld 上 +9.37 个百分点（83.6% 相对提升）；泛化到 WAA | 可采用（经典） |
| 15 | Agent S2；Saaket Agashe 等；2025-04-01 | [arXiv:2504.00906](https://arxiv.org/abs/2504.00906) | S1+S2 | Mixture-of-Grounding + 主动分层规划；OSWorld 15/50 步相对提升 18.9%/32.7%；WAA 52.8%、AndroidWorld 16.52%（均为相对） | 需改造（相对百分比） |
| 16 | Scaling Agents for Computer Use（Agent S3 / BJudge）；Gonzalo Gonzalez-Pumariega 等；v1 2025-10-02 / v2 2026-02-03 | [arXiv:2510.02250](https://arxiv.org/abs/2510.02250) | S1+S2 | 多 rollout + 行为叙述选择；OSWorld 72.6%，超过人类 72.36%；泛化到 WAA / AndroidWorld | 需改造（多 rollout 口径） |
| 17 | Evolving Agent Interfaces（Agent S4）；Saaket Agashe 等；2026-10-20 | [arXiv:2610.28601](https://arxiv.org/abs/2610.28601) | S1+S2+S3（§2–§5、§7.3、Table 2） | 无成功标签轨迹→接口仓库演化；OSWorld V2 21.3% binary、$1.10/task；ScienceBoard 41.4%→58.6% | 需改造（跨 harness/步数） |
| 18 | UI-TARS: Pioneering Automated GUI Interaction with Native Agents；Yujia Qin 等（ByteDance）；2025-01-21 | [arXiv:2501.12326](https://arxiv.org/abs/2501.12326) | S1+S2 | 纯截图端到端；OSWorld 24.6@50 步 / 22.7@15 步；AndroidWorld 46.6 | 可采用（路线代表） |
| 19 | UI-TARS-2 Technical Report；Haoming Wang 等（ByteDance）；v1 2025-09-02 / v2 2025-09-05 | [arXiv:2509.02544](https://arxiv.org/abs/2509.02544) | S1+S2 | 数据飞轮+稳定多轮 RL+GUI/文件系统/终端混合环境；Online-Mind2Web 88.2、OSWorld 47.5、WAA 50.6、AndroidWorld 73.3 | 需改造（技术报告、自报） |
| 20 | OmniParser for Pure Vision Based GUI Agent；Yadong Lu 等（Microsoft）；2024-08-01 | [arXiv:2408.00203](https://arxiv.org/abs/2408.00203) | S1+S2 | 屏幕解析为结构化元素；提升 GPT-4V 在 ScreenSpot / Mind2Web / AITW 的表现 | 可采用（感知增强） |
| 21 | OpenCUA: Open Foundations for Computer-Use Agents；Xinyuan Wang 等（HKU/Moonshot 等）；v1 2025-08-12 / v3 2025-10-04 | [arXiv:2508.09123](https://arxiv.org/abs/2508.09123) | S1+S2 | AgentNet 跨 3 OS、200+ 应用；OpenCUA-72B 在 OSWorld-Verified 平均 45.0%，开源 SOTA | 可采用（开放基座） |
| 22 | CUA-Recovery / ReRail；Xu Hu 等；2026-10-20 | [arXiv:2610.27645](https://arxiv.org/abs/2610.27645) | S1+S2+S3（§3–§5、Appendix A/B） | 2,250 人工核验错误状态 / 100 任务；8,577 训练轨迹；EAR ≤44.0%、Pass@3 ≤25.5%；微调后 EAR 19.9→35.2 | 可采用（负面证据） |
| 23 | Lost in Recovery / ReTrace；Byeonghun Bang 等；2026-10-20 | [arXiv:2610.27954](https://arxiv.org/abs/2610.27954) | S1+S2 | Transition-Consistent Recovery；受控错误注入+目标导向动作回放；模型未利用潜在恢复能力 | 仅作背景（未读正文） |
| 24 | Multi-Agent Computer Use；Jing Yu Koh 等（CMU）；2026-06-01 | [arXiv:2606.01533](https://arxiv.org/abs/2606.01533) | S1+S2 | manager 将任务拆为 DAG、并行子 agent、持续重规划；跨 4 基准提升 3.4–25.5%（**口径未明**）；Odysseys 墙钟约快 1.5× | 需改造 |
| 25 | Agent World Model in the Wild（WildAWM）；Zhaoyang Wang 等（MSR 等）；2026-10-19 | [arXiv:2610.26828](https://arxiv.org/abs/2610.26828) | S1+S2 | 341 个 GUI+MCP+CLI 长程环境-任务对，部分需 >100 步；GPT-6-Astra 仅解 60%；纯开源模型驱动合成 | 需改造（作者自报泛化） |
| 26 | OSWorld-Human: Benchmarking the Efficiency…；Reyna Abhyankar 等；v1 2025-06-19 / v2 2026-05-18 | [arXiv:2506.16042](https://arxiv.org/abs/2506.16042) | S1+S2 | 首次研究时间性能；规划/反思/裁判的大模型调用是主要延迟；16 个 agent 中最好的也多走 2.7–4.3× 步数 | 可采用（成本负面证据） |
| 27 | Large Language Model-Brained GUI Agents: A Survey；Chaoyun Zhang 等（Microsoft）；v1 2024-11-27 → v12 2025-05-06 | [arXiv:2411.18279](https://arxiv.org/abs/2411.18279) | S1+S2 | 框架/数据/大型动作模型/评测四线综述；附持续更新的论文库 | 仅作背景（截止 2025-05） |
| 28 | Computer use tool（Claude Platform Docs）；Anthropic；当前版本 `computer_toolset_20260801` | [docs.anthropic.com](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) | S1+S3（工具定义/17 动作/循环/Limitations/Pricing） | 17 个成员工具；约 4,500 input tokens 定义开销；2,576 px / 4,784 visual tokens；≤20 图/请求；ZDR/HIPAA eligible；8 条 Limitations | 可采用（工程一手） |
| 29 | Computer use（OpenAI API Docs）；OpenAI；Responses API `tools:[{"type":"computer"}]` | [platform.openai.com](https://platform.openai.com/docs/guides/tools-computer-use) | S1+S3（工具定义/循环/Run safely/Cost） | 9 种动作；`computer_call`→执行→`computer_call_output`+`computer_screenshot`；`previous_response_id`；代码执行替代路径；Python 3.11+/Node 22.6+ | 可采用（工程一手） |

> **关联声明（避免重复计证据）**：01/02/03 属同一 OSWorld 研究体系（论文 + 项目页 + 升级博客 + [GitHub 仓库](https://github.com/xlang-ai/OSWorld)）；04/05 属同一 OSWorld 2.0 体系；14/15/16/17 与 [Agent-S 仓库](https://github.com/simular-ai/Agent-S) 属同一演进系列但为四篇不同研究；18/19 与 [UI-TARS 仓库](https://github.com/bytedance/UI-TARS) 同理。**它们不是多份独立实验证据。**

### 3.2 关键资料逐项深度摘录（12 项）

> 用户要求对核心资料逐项提取「解决什么问题 / 方法与前提 / 数据与工具与评价 / 条件与基线与结果及原文位置 / 局限与替代解释 / 价值判断」。受本轮抓取与输出预算限制，以下对**12 项最影响判断的资料**做完整摘录；其余 17 项在 §3.1 总表中给出已核字段与结论摘要，**未做同等深度摘录**，属本轮未完成项（§8.7）。

---

**[#04] OSWorld 2.0（arXiv:2606.29537, v2 2026-07-13；68 页 / 42 图；DOI 10.48550/arXiv.2606.29537）**
- **解决什么**：已有 CUA 基准不够真实、不够长，无法暴露前沿 agent 的局限。
- **方法/前提**：108 个端到端工作流，7 个专业领域、21 子类、31 个自建站点；任务基于真实输入工件与有状态用户档案；含独立 safety reports。
- **数据/工具/评价**：每个任务平均 27.25 个 checkpoint，按最终环境状态对所有 checkpoint 打分（非固定顺序）；functional evaluation 优先，model-based evaluation 占总分的 11.53%，且没有任务依赖它超过 50%（[§2.1.3](https://arxiv.org/html/2606.29537v2)）。7 个模型族全部用截图观测；Claude 用原生 `claude_computer_use` tool，其余输出 `pyautogui` 代码动作；输出上限 16K tokens（MiniMax M3 为 8K）；每动作后 3 秒暂停；AWS `us-east-1` `t3.2xlarge`，release `v2026.06.24`（§3.1）。
- **条件/基线/结果**：主指标 `binary-completion @500 steps`；Claude Opus 4.8（max thinking + batched tool calls）20.6% binary / 54.8% partial；GPT-5.5 token 效率高但平台期约 13–14%；强模型 partial 集中 41–54%，六倍 token 只换约 5 个 partial 点，却区分 13% vs 20% binary（§3.2 Table 3）。短任务（<45 min）可达 20–24% binary，137–163 min 组无模型 >10%，>163 min 全为 0。
- **局限/替代解释**：§4.4 五类失败；§4.1.2 中 visual grounding 15.5%、tool-semantics 13.8%、information extraction 12.8% 高于 execution 10.1% 与 verification 9.8%，recovery+repair <7%——**另一种解释是模型把预算花在「理解」而非「执行」，而非单纯「不会点」**。§4.3：human-easy 任务仅 11.1% 对 agent 也 easy，说明人类难度不能线性预测 agent 难度。§4.2 的 216 条轨迹里约 33% 绕过用户可见界面、约 14% 提取隐藏应用状态，意味着高分也可能来自「绕过 GUI 直接改状态」，与「GUI 操作能力」不是同一构念。
- **未取得**：§6 Limitations 正文、binary 精确判定阈值、partial 权重公式、主评估重复次数/随机种子、Appendix E.2 / H.4 正文（抓取在 §4.4 后截断）。
- **价值**：**可采用**，但引用必须写明 release version 与日期；把 20.6% 说成「当前 SOTA」是错的。

**[#05] OSWorld 2.0 官方榜单（osworld-v2.xlang.ai，Last update 2026-10-15）**
- **解决什么**：给持续更新的、含 step budget / release version / cost / 轨迹链接的可比结果。
- **评价口径**：`Binary accuracy` 与 `Partial` 双列；step budget 可筛 150/300/450/500；release 可筛 `v2.1` / `v2026.06.24` / `v2026.08.08`；Offline set = 82 个无需联网的任务；`v2026.08.08` 结果对 Claude Opus 5 平均 7 runs、对 GPT-5.6 Sol 平均 2 runs。
- **结果**：#1 Claude Opus 5 Max+Batch v2.1 = 44.33% / 77.67%；#2 MuseSpark 1.3 = 39.25% / 69.56%；#12 Opus 4.8 Max+Batched v2026.06.24 = 20.6% / 54.8%；#18 GPT-5.5 Xhigh = 13.0% / 49.5%。页面还给出 `Output tokens` 对照（Opus 4.8 max 244K vs Opus 5 max 103K）。
- **局限**：页面未解释「摘要 20.6% 与榜单 44.33%」的差异原因；各条目实际采用的 step budget 未逐行标注；不同 release 的任务集是否完全一致未核实。
- **价值**：**可采用**作为「截至 2026-10-15 的官方上限」，不可与论文摘要混引。

**[#02] OSWorld-Verified 官方页（osworld-v1.xlang.ai，升级 2025-07-28）**
- **评价口径**：榜单列名 `Success Rate (Avg±Std)`，出现 `307.73/358` 这类小数分子与 `45.0±0.9%`，**页面未给出评分公式**，不能断定是纯 binary success；官方声明「These are official results evaluated by our team under unified settings and environment」。
- **结果（本次抓取可见 68 条）**：`claude-fable-5[1m]` 86.0% @100（2026-08-01）、`claude-opus-5[1m]` 83.4%、`Muse Spark 1.1` 80.7%、`Holo3-35B-A3B` 80.4±2.2%、`UI-TARS-2-2509` 53.1%、`opencua-72b-preview` 45.0±0.9%、`opencua-32b` 34.8±0.8%、`computer-use-preview` 30.5±0.9%、`o3` 23.0%。
- **局限**：`self-reported results` 只有文案链接且 `href="#"`，**本次无法取得该表内容**；页面摘要仍写着 2024 年的「best model 12.24%」，与榜单并存但无版本说明。
- **价值**：**可采用**，但必须带步数与「verified / self-reported」标签。

**[#03] OSWorld-Verified 升级博客（xlang.ai，2025-07-27）**
- **解决什么**：社区各自改环境、改任务导致分数不可比。
- **方法**：收集并人工修复 300+ 条反馈（约 10 人、约 2 个月）；基础设施 VMware/Docker→AWS，最多 50 环境并行，10+ 小时→分钟级；VM 镜像 50GB→25GB、调整 IOPS 与 `t3.medium`/`t3.large` 的动作间延时。
- **治理**：上榜需与维护方约时间、由维护方运行 agent 代码并公布结果，且需上传并允许披露 agent 实现；可信机构可改为共享监控数据与轨迹；提供 [PUBLIC_EVALUATION_GUIDELINE.md](https://github.com/xlang-ai/OSWorld/blob/main/PUBLIC_EVALUATION_GUIDELINE.md)。
- **局限**：原文用 `300+` / `nearly 300` 而非精确整数；trajectories 是否为**所有**提交的强制项未写明。
- **价值**：**可采用**，是解释「为什么 verified 与自报分数不能混」的一手依据。

**[#16] Scaling Agents for Computer Use / Agent S3（arXiv:2510.02250, v2 2026-02-03）**
- **解决什么**：单次 rollout 脆弱，误差累积、方差大；长轨迹难以评估与挑选。
- **方法**：BJudge 把执行表示为 behavior narrative，在该层比较候选行为；在多 rollout 中选择。
- **结果**：OSWorld 72.6%，超过论文所述人类 72.36%；泛化到 WindowsAgentArena 与 AndroidWorld；含消融。
- **条件差异**：这是**多 rollout + 选择**的系统成绩，不是单次运行；与 §3.1 的 100-step 单配置榜、与 OSWorld 2.0 的 500-step 长时程任务均不可横比。
- **局限/冲突**：[Agent-S README](https://github.com/simular-ai/Agent-S) 的 BibTeX 把它写作 `The Unreasonable Effectiveness of Scaling Agents for Computer Use`，与 arXiv 页标题 `Scaling Agents for Computer Use` 不一致；README 自报 2025-12-15「首个超过人类」与 2026-07-30「TMLR 2026 accepted」，**会议状态本次未从 TMLR 官方核实**。
- **价值**：**需改造**（须标注多 rollout 与选择机制）。

**[#17] Evolving Agent Interfaces / Agent S4（arXiv:2610.28601, 2026-10-20）**
- **解决什么**：人给 agent 的接口是手工写死的，agent 只能逐格填表格、把 2000 行文件打印出来找一个函数。
- **方法/前提**：把接口形式化为 `I=⟨c_I, 𝒜_I, 𝒪_I⟩`、仓库 `R=(ℐ(R), K(R))`；meta-agent 只读**无成功标签**的 synthetic training trajectories，通过 mutation / crossover 生成 descendant；用 meta-agent 看不到的 validation tasks 做二元锦标赛选择（§3.1–§3.3）。OSWorld V2 用 30 个合成训练任务 + 15 个官方 validation 任务，30 个 descendants；task agent 与 meta-agent 均为 `Qwen3.8-27B`，131,072 上下文、32,000 输出上限、persistent IPython kernel、Prime Agent harness `0.8.0-beta.546.1.a9b5d88`。
- **结果（Table 2）**：Qwen CUA 固定接口 5.56% / $1.39 → 演化接口（无 scratch VM）21.30% / $1.10、partial 46.90%；对照 GPT-5.5 batched 13.00% / $25.50、Claude Opus 4.8 batched 20.60% / $72.40；ScienceBoard 41.4%→58.6%。
- **关键条件差异**：自身 rollout 为 **300-step**，而外部参考结果走 OSWorld V2 reference harness 的 **500-step**；对照模型成绩与每任务成本取自 [Yuan et al. 2026] 的 Table 3（即更早期的论文快照）；成本按 Parasail token 费率估算、假设 80% input-cache 命中、**不含接口仓库构建与运行时基础设施**。
- **局限**：无独立 Limitations 章节；§7.3 自述长时程任务 run-to-run 方差大（ScienceBoard 的 `if-003` 首次 73.33%，二次均值降到 60.00%），且 OSWorld V2 **不做** denoise；最终 full-benchmark 的独立重复次数与随机种子 not shown；本次读到的正文**没有出现** `shadow interface` 这一术语（前序上下文曾提及，标注为未核实）。
- **价值**：**需改造**。结论「21.3% 超过 20.6%」只在作者选定的旧快照基线下成立；官方榜 2026-10-15 已有 44.33%。

**[#22] CUA-Recovery / ReRail（arXiv:2610.27645, 2026-10-20）**
- **解决什么**：已有基准只看端到端成绩，少数恢复基准依赖人工注入错误，不反映真实策略诱发的失败。
- **方法/前提**：`gold lineage` 记录每步正确值；从真实 agent 失败中定位 root cause，用可执行 verifier 冻结与 mutation test 筛选任务（Appendix B.4：一次生成运行 17,857 次 mutation executions / 417 candidates，去掉 freezing 与 divergence check 后 median R 降到 0、417 个候选仅 3 个存活）；GUI+CLI 持久化桌面环境。
- **数据/评价**：测试集 2,250 个人工核验错误状态 / 100 任务（6 个 takeover depth `d∈{0,5,10,15,20,25}`），训练集 8,577 条 verified recovery trajectories / 377 任务；`EAR` = 是否明确识别继承的错误（§5.1），`Pass@3` = 3 次 rollout 中任一次满足全部 criteria（§3）；6 个 agent：GPT 5.5、Claude Opus 4.8、Kimi-K3、Qwen3.5-35B-A3B、EvoCUA-32B、OpenCUA-72B；上下文最近 K=20 张截图。
- **结果与定位**：EAR 最高 44.0%（Opus 4.8 @d=5），Pass@3 最高 25.5%（GPT 5.5 @d=20），见 Table 2；§5.2 Finding 2：`Kimi-K3` clean-start MyPCBench Pass@3 66.9% 却只识别自身失败中 7.8–18.5% 的 inherited errors → **clean-start 成绩不能预测错误意识**；Finding 3：aware vs unaware 的 verifier pass 15.6% vs 12.2% → **意识到 ≠ 修得好**。微调后 EAR 19.9→35.2、Rubric 5.0→16.1、MyPCBench +15.3 个百分点、Odysseys +10.8 个百分点（Table 3）。
- **资源成本（Appendix A）**：API 总计 **$16,493**；GPU 共 **9,322 GPU-hours**（微调 64 GPU × 18 h = 1,152）；sandbox **2,050 小时**；本地模型服务用 8 张 AMD MI308X，32 并发 sandbox 时最多 256 GPU。
- **局限**：无独立 Limitations 章节；EAR judge prompt（Appendix D.3）与人机一致性（Appendix E）正文未取得；论文页为 `CC BY 4.0`，代码仓库 [GitHub API 实测](https://github.com/xu-hu-2002/CUA-Recovery) 为 MIT，但**数据集单独许可证 not shown**。
- **价值**：**可采用**，是本轮最扎实的负面证据与复现成本参照。

**[#13] AgentHorizon（arXiv:2610.11050, 2026-10-08）**
- **解决什么**：自动裁判（用于训练或无人评测）在长轨迹上是否可靠？轨迹「看起来完成」可能违反约束或引入副作用。
- **方法**：1,373 个「指令-轨迹」对，来自 166 小时人类录制轨迹、3 个 OS；为相近指令录制成对轨迹，**交换指令构造 negative tasks**。三个 split：AH / AH-S / AH-D；评估 11 个 judge，最长 300 张截图+动作，分「直接给全轨迹」与「作为 coding agent 跨 5 种 harness」两种用法。
- **结果**：最佳 agentic judge GPT-5.5 在 AH 上平衡准确率 80.9%；工具使用改善部分模型，却让**开放权重模型更差**；judge 之间「接受有效轨迹」与「拒绝失败轨迹」的能力差异极大。
- **对本研究的含义**：`[助手推断]` 任何依赖 model-based judge 的 CUA 评测（包括 OSWorld 2.0 占 11.53% 的那部分）都带有可量化的裁判误差；这不是因果证明，只是误差来源提示。
- **价值**：**可采用**。

**[#10] CADWorld（arXiv:2609.16251, v2 2026-09-21）**
- **解决什么**：既有基准少覆盖「输出是持久化、结构化专业工件」的工程工作流。
- **方法**：200 个 FreeCAD 任务 / 11 类（草图、零件建模、装配、CAM、FEM、测量、网格、工程图等）；agent 只能通过截图与 GUI 动作操作；成功由对保存的 FreeCAD 工件与辅助输出执行的 task-specific checks 判定（几何属性、参数结构、约束、制造状态、仿真结果）。
- **结果**：7 个 agent 中最佳 17.5%，专家参考通过率 87.0%；弱 agent 常在做不出有效工件前就失败，强 agent 越来越多地失败在结构、几何与构造过程要求上。
- **价值**：**可采用**，代表「artifact-grounded evaluation」这条与 screenshot-only 判分不同的路线。

**[#26] OSWorld-Human（arXiv:2506.16042, v2 2026-05-18）**
- **解决什么**：SOTA 只优化准确率，端到端延迟高到不实用（人类几分钟，agent 几十分钟）。
- **方法**：首个 CUA 时间性能研究；人工标注 OSWorld 每任务的人类决定轨迹；评估 16 个 agent 的效率。
- **结果**：规划/反思/裁判的大模型调用占主要延迟；任务越往后每步可能比开头慢 3×；最好的 agent 也多走 2.7–4.3× 步数。
- **价值**：**可采用**，是「成功率之外的成本维度」的一手负面证据。

**[#28] Anthropic Computer use tool 官方文档（当前 `computer_toolset_20260801`）**
- **接口**：一个 `{"type":"computer_toolset_20260801"}` 条目声明 17 个成员工具（`screenshot`、`zoom`、`left_click`、`right_click`、`middle_click`、`double_click`、`triple_click`、`left_click_drag`、`mouse_move`、`left_mouse_down/up`、`cursor_position`、`scroll`、`type`、`key`、`hold_key`、`wait`）；每个 `tool_use` 带 `toolset_name:"computer"`，**不需要 beta header**；旧版为 `computer_20251124`（beta `computer-use-2025-11-24`）与 `computer_20250124`。
- **循环**：Claude 返回 member tool calls → 应用按顺序执行（batch 内**顺序执行、遇第一个失败即停**）→ 每个 `tool_result` 回显 `toolset_name` → 直到不再请求工具；`max_iterations` 是防止无限循环与意外 API 成本的保护。
- **工程约束/成本**：toolset 定义约带来 **4,500 input tokens**（禁用 `zoom` 省约 410）；截图按图像输入计费，每张约 **1,000–1,800 input tokens**；单请求 >20 张图会触发更严格的单边限制；建议保留最近 3 张截图、每 25 turns 批量裁剪，否则破坏 prompt caching 前缀；Opus 4.7+ 上限为长边 2,576 px / 4,784 visual tokens（约 3.75 MP），更早模型 1,568 px / 1.15 MP；坐标在**返回给模型的图片像素空间**，缩放后必须按比例映射（macOS Retina 2×）。
- **官方明确的限制**：latency；坐标幻觉；工具选择错误；滚动不可靠；表格单元格操作；社交/通信平台能力受限；越狱与提示注入（原文：`instructions on webpages or contained in images might override your instructions`）；并声明 `Do not use Claude for tasks requiring perfect precision or sensitive user information without human oversight`。`Managed Agents` 标注 Not available；ZDR / HIPAA eligible；截图存于**你的环境**而非 Anthropic。
- **价值**：**可采用**（工程一手，不是性能证据）。

**[#29] OpenAI Computer use 官方文档（Responses API）**
- **接口**：`tools: [{"type": "computer"}]`；输出 `computer_call`（含有序 `actions` 数组），应用执行后返回 `computer_call_output`，其中 `output.type = "computer_screenshot"`（base64 PNG，建议 `detail:"original"`），用 `previous_response_id` 续接。动作共 9 种：`click / double_click / drag / move / scroll / keypress / type / wait / screenshot`。首个调用可能只请求截图。
- **两条实现路径**：SDK 的 `ComputerToolset` / `AsyncComputerToolset` / `BrowserToolset`（driver 由应用提供）；或 code execution 路径（`exec_py` + `execute_in_sandbox`，用 PyAutoGUI / Playwright 写脚本，一次调用可含循环与条件逻辑）。文档对 `GPT-6 Astra` **推荐 code execution**，`computer` tool 作为替代。
- **状态约束**：原文 `The API conversation and the execution environment have separate state`、`Continuing a response does not restore a browser session, login state, or runtime variables`；缩放截图必须把坐标映射回环境坐标。
- **依赖/成本/安全**：Python 3.11+、Node.js 22.6+；示例锁 `openai==3.31.0` / `playwright==1.61.0` / `openai@7.33.0` / `playwright@1.61.1`；示例最多 6 次 Responses 请求；partner 环境列出 Browserbase、Browser Use、Daytona、E2B Desktop；截图算图像输入、每次 Responses 请求可能产生输入/输出 token 费用、托管环境另计；`Run safely` 四条：隔离浏览器/VM + allowlist、屏幕内容视为不可信、有后果的动作需人工确认、设置步数/时间/成本上限并检查实际结果。
- **未显示**：HTTP endpoint/path、具体价格数值、地区可用性、GA 状态。
- **价值**：**可采用**（工程一手）。

### 3.3 候选索引（未纳入核心总表，仅作查漏与覆盖说明）

| 资料 | 状态 | 为何未进核心表 |
|---|---|---|
| [A Survey on (M)LLM-Based GUI Agents, arXiv:2504.13865 v2](https://arxiv.org/abs/2504.13865)（已核 S1+S2） | 已核 | 与 #27 综述功能重叠；四组件框架（感知/探索/规划/交互）可补充 taxonomy |
| [SeeClick, arXiv:2401.10935](https://arxiv.org/abs/2401.10935) | S0（本轮未重开） | 前序 277 篇总集已收录；grounding 由 #09/#20 代表 |
| [Set-of-Mark Prompting, arXiv:2310.11441](https://arxiv.org/abs/2310.11441) | S0（本轮未重开） | 同上 |
| [ShowUI, arXiv:2411.17465](https://arxiv.org/abs/2411.17465) / [Aguvis, arXiv:2412.04454](https://arxiv.org/abs/2412.04454) | S0 | 视觉型统一动作模型，与 #18/#19 路线重叠 |
| [WebVoyager, arXiv:2401.13919](https://arxiv.org/abs/2401.13919) / [Mind2Web, arXiv:2306.06070](https://arxiv.org/abs/2306.06070) | S0 | 浏览器路线；本轮以 WebArena / Online-Mind2Web（见 #24）代表 |
| [Agent S2.5 / S3 / S4 各版本 README](https://github.com/simular-ai/Agent-S) | S1+S3（仓库 README） | 属 #14–#17 的软件发布关联，不单列独立证据 |
| [RiOSWorld 等 CUA 安全专项基准](https://arxiv.org/abs/2610.03818) | S0 | 按本次范围排除安全攻防专项；OSWorld 2.0 的 safety report 已在 #04 内作为局限提及 |
| [openai_agents_guide.pdf（本地既有文件）](./openai_agents_guide.pdf) | 未读 | 本地文件，非本次联网一手来源，未纳入证据链 |

---

## 4 主要路线比较表

### 4.1 六条路线（只列优点会失真，故局限与成本同列）

| 路线 | 代表资料 | 适用范围 | 证据强度 | 资源/成本 | 实施难度 | 主要局限 |
|---|---|---|---|---|---|---|
| A 原生端到端 GUI 模型（纯截图→动作） | #18 UI-TARS、#19 UI-TARS-2、#21 OpenCUA | 需要跨应用、无需 DOM/API 的通用桌面与移动端 | 中：多为作者技术报告/自报，部分分数可在 [#02 官方榜](https://osworld-v1.xlang.ai/) 找到对应条目（如 `UI-TARS-2-2509` 53.1%、`opencua-72b-preview` 45.0±0.9%） | 高：需大规模轨迹数据与多轮 RL；#19 用「数百台虚拟机」做在线轨迹；#21 需 3 OS / 200+ 应用数据 | 高 | 闭源权重/数据许可未核；训练成本与复现门槛高；分数常是特定 step budget 下的自报 |
| B 结构化感知增强（屏幕解析→通用 VLM） | #20 OmniParser、#09 ScreenSpot-Pro | 已有强通用 VLM、希望快速提升定位精度 | 中高：#09 给出「已有最佳 18.9%」这一硬负面结果 | 中：需额外检测/描述模型与标注数据 | 中 | 高分辨率专业场景仍差（#09）；`microsoft/OmniParser` 仓库许可证为 `CC-BY-4.0`，需署名，模型/数据许可另查 |
| C 分层规划 + 经验 + 测试时扩展 | #14 Agent S、#15 S2、#16 S3/BJudge | 长任务、需要跨 OS 泛化与误差缓冲 | 中：多为作者报告；#16 的 72.6% 未在本次可见的官方 Verified 68 条中出现 | 中高：多 rollout + judge 显著增加 token 与延迟（#26） | 中 | 多 rollout 与单 rollout 不可比；BJudge 需要「评估长行为」的能力，规模化成本未给出 |
| D 多智能体并行协调 | #24 MACU | 可分解、可并行的长任务 | 中：单篇 2026 预印本，作者自报 | 高：多个子 agent 并发，API 成本与并发沙箱线性增长 | 高 | 原文 `3.4−25.5%` 未写是百分点还是相对比例；部分可观测环境下的状态传递依赖 manager；无独立复现 |
| E 接口自演化 | #17 Agent S4 | 有稳定 harness、可承受合成任务与演化搜索 | 中：单篇 2026 预印本 + 详细消融（§7.3 自述方差） | 中高：30 descendants × 长时程 rollout；但每任务成本报 $1.10 | 高 | 自身 300-step vs 参照 500-step；成本不含接口构建；对照基线取自旧快照；未报告最终重复次数 |
| F 合成环境训练 / 恢复专项 | #25 WildAWM、#22 CUA-Recovery、#23 ReTrace | 缺真实轨迹、需专门提升鲁棒性 | 中：三篇 2026 预印本；#22 有可执行 verifier 与人工核验状态，方法学最扎实 | 极高：#22 报 $16,493 API + 9,322 GPU-hours + 2,050 sandbox-hours | 极高 | 合成到真实的迁移是作者自报；#22 训练集/测试集同工作流严格隔离但仍是同一任务分布；`BangProx/ReTRACE` 无许可证字段 |

**横切路线：官方 tool loop（#28/#29）不是第六条「智能方法」，而是所有路线的执行底座**——它决定动作空间、坐标空间、截图成本与隔离边界。

### 4.2 禁止直接横比矩阵（重要）

| 组 | 数字 A | 数字 B | 为何不能比 |
|---|---|---|---|
| 1 | OSWorld 1.0 论文 12.24%（2024） | Verified 榜 86.0%（2026） | 相隔两年、任务修复 300+ 处、评估基础设施从 VMware/Docker 换到 AWS、模型与步数都不同 |
| 2 | Verified 榜 86.0% @100 steps | OSWorld 2.0 榜 44.33% @500 steps | 任务集不同（369 短任务 vs 108 长工作流）、指标不同（Avg±Std 且公式未公开 vs binary/partial）、步数不同 |
| 3 | Agent S3 72.6%（OSWorld，多 rollout + BJudge） | 任一单次运行榜单条目 | 多次尝试 + 选择机制，不是单次成功率；且人类 72.36% 来自 2024 原论文 |
| 4 | 论文摘要 20.6% / 54.8% | 官方榜 44.33% / 77.67% | 同为 OSWorld 2.0，但 release `v2026.06.24` vs `v2.1`、模型 Opus 4.8 vs Opus 5、榜单更新时间 2026-10-15 |
| 5 | Agent S4 21.3% | Claude Opus 4.8 20.6% / GPT-5.5 13.0% | 自身 300-step harness vs 参照 500-step harness；成本口径不含接口构建；引的是旧快照 Table 3 |
| 6 | CADWorld 17.5% / 专家 87.0% | OSWorld 2.0 20.6% | 判分对象不同（FreeCAD 持久化工件 vs 通用桌面状态），专家参考不是人类完成率基线 |
| 7 | WebArena 14.41% / 人类 78.24% | AndroidWorld 30.6% | 平台、任务数、评分器、年代均不同 |
| 8 | UI-TARS-2 论文 OSWorld 47.5 | 官方榜 `UI-TARS-2-2509` 53.1% @100 | 评测条件与步数配置不同，论文未解释差异；标「尚未核实」 |
| 9 | Mind the Gap 68.8% Score Rate | OSWorld 2.0 54.8% partial | 都是「部分得分」但 rubric、任务域、量表完全不同（100 分制 7,118 条标准 vs 27.25 checkpoint） |

### 4.3 措辞核查：比例、百分点、相对提升与因果

| 原文表述 | 正确解读 | 常见误读 |
|---|---|---|
| Agent S：`+9.37% on success rate (an 83.6% relative improvement)` | 绝对提升 9.37 **个百分点**，相对提升 83.6% | 写成「提升 83.6 个百分点」 |
| Agent S2：`18.9% / 32.7% relative improvements`；WAA `52.8%`、AndroidWorld `16.52% relatively` | 全部是**相对**提升，原文未给绝对分数 | 当作绝对成功率 |
| MACU：`improves ... by 3.4−25.5%` | 摘要**未写**是百分点还是相对比例 | 直接写成「提升 25.5 个百分点」 |
| ReRail：`+15.3 points` / `EAR 19.9%→35.2%` | 前者是百分点，后者是比例水平变化（+15.3 pp） | 写成「提升 15.3%」 |
| OSWorld 2.0：`20.6% binary` 与 `54.8% partial` | 同一运行下两个不同指标 | 相加或当作区间 |
| `15.6% vs 12.2%` verifier pass（#22 §5.2） | 观察性关联，说明「意识到错误」与「通过」弱相关 | 写成「错误意识导致 3.4 个百分点提升」（因果未证明） |
| OSWorld 2.0 §4.3 `76.3% human-hard 也是 agent-hard` | 相关性描述 | 写成「人类难度决定 agent 难度」（原文同时指出 human-easy 中 44.4% 对 agent 仍 hard） |

**评价泄漏/额外条件检查**：#16 多 rollout + BJudge 选择、#17 用 15 个 official validation tasks 选仓库（虽对 meta-agent 隐藏分数，但仍是同一 benchmark 分布）、#22 fine-tune 1 epoch on 8,577 verified trajectories、#19 反射式在线轨迹迭代训练——这些都属于「额外尝试 / 额外训练 / 额外选择」，与「同一模型零微调单次运行」不是同一证据等级。#04 明确 model-based evaluation 占 11.53% 且无任务超过 50%，是本轮少数主动披露该类风险的来源。

---

## 5 推荐阅读顺序

**第一阶段：建立坐标（约 5 项）**
1. [#27 综述 v12](https://arxiv.org/abs/2411.18279) — 先拿到框架/数据/动作模型/评测四条线（注意截止 2025-05，不含近 12 个月进展）。
2. [#01 OSWorld 原始论文](https://arxiv.org/abs/2404.07972) — 369 任务、执行式评估脚本、72.36% 人类基线的出处。
3. [#03 OSWorld-Verified 升级博客](https://xlang.ai/blog/osworld-verified) — 理解「为什么分数不能随便比」。
4. [#02 官方 Verified 榜](https://osworld-v1.xlang.ai/) — 看真实榜单的列、步数、日期，建立「读榜要看元数据」的习惯。
5. [#09 ScreenSpot-Pro](https://arxiv.org/abs/2504.07981) — 先看到 grounding 这一底层瓶颈的硬负面数字（18.9%）。

**第二阶段：近 12 个月主线（约 6 项）**
6. [#04 OSWorld 2.0 论文](https://arxiv.org/abs/2606.29537) 与 [#05 官方榜](https://osworld-v2.xlang.ai) — **必须连着读**，否则会把 20.6% 当成当前水平。
7. [#22 CUA-Recovery](https://arxiv.org/html/2610.27645v1) — 恢复能力的可操作定义（EAR / Pass@3）与失败证据；顺带看 Appendix A 的真实复现成本。
8. [#13 AgentHorizon](https://arxiv.org/abs/2610.11050) — 在相信任何「自动判分」结论之前读。
9. [#26 OSWorld-Human](https://arxiv.org/abs/2506.16042) 与 [#12 Mind the Gap](https://arxiv.org/abs/2606.10956) — 把「成功率」之外的效率、专业软件能力补齐。
10. [#17 Agent S4](https://arxiv.org/html/2610.28601v1) 与 [#24 MACU](https://arxiv.org/abs/2606.01533) — 两条「不换模型也能提升」的系统路线；读时对照 §4.2 第 5 组。
11. [#25 WildAWM](https://arxiv.org/abs/2610.26828) 与 [#10 CADWorld](https://arxiv.org/abs/2609.16251) — 环境与评测两端的扩展方向。

**第三阶段：工程落地（约 4 项）**
12. [#28 Anthropic docs](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) 与 [#29 OpenAI docs](https://platform.openai.com/docs/guides/tools-computer-use) — 对照读，理解两套 tool loop 在动作空间、`tool_result` 形态、状态归属上的差异。
13. [Anthropic computer-use-demo README](https://github.com/anthropics/claude-quickstarts/tree/main/computer-use-demo) 与 [OpenAI sample app README](https://github.com/openai/openai-cua-sample-app) — 看依赖、屏幕分辨率建议、单会话限制、以及「Run finished 不等于成功」的明确警告。
14. 最后回看 [#16 BJudge](https://arxiv.org/abs/2510.02250) 与 [#21 OpenCUA](https://arxiv.org/abs/2508.09123) — 在已知可比性陷阱后，再评估「超人类」与「开源 SOTA」这类表述的适用条件。

---

## 6 可行性与验证路线

### 6.1 两套官方 tool loop 对照（工程落地核查）

| 维度 | Anthropic（#28） | OpenAI（#29） |
|---|---|---|
| 工具声明 | `{"type":"computer_toolset_20260801"}`（1 个 toolset → 17 成员工具，无 beta header） | `tools:[{"type":"computer"}]`（内置工具）+ 可选 `ComputerToolset` SDK |
| 动作空间 | 17 个成员：`screenshot/zoom/left_click/.../hold_key/wait` | 9 种：`click/double_click/drag/move/scroll/keypress/type/wait/screenshot` |
| 结果返回 | 每个 `tool_result` 需回显 `toolset_name:"computer"`；batch 顺序执行、首个失败即停，未执行块必须返回精确文本 `Not executed: an earlier computer action in this turn failed.` | `computer_call_output` 带匹配 `call_id`，`output.type=computer_screenshot`，用 `previous_response_id` 续接 |
| 状态归属 | 客户端工具；截图与文件存于你的环境；文档称 ZDR / HIPAA eligible | API 会话与执行环境状态分离；续接不恢复浏览器会话、登录态或运行时变量 |
| 坐标 | 在返回给模型的图片像素空间；2,576 px / 4,784 visual tokens（Opus 4.7+）；缩放后按比例映射 | `detail:"original"` 保分辨率；若降采样，必须把坐标映射回环境坐标空间 |
| 上下文成本 | toolset ~4,500 input tokens；每图 1,000–1,800 tokens；>20 图触发更严格限制；prompt caching 需按批裁剪 | 截图算图像输入；每次 Responses 请求计费；托管环境另计；**具体价格数值 not shown** |
| 依赖 | 参考实现：Docker + X11 + VNC + Streamlit，建议 XGA 1024×768 | Python 3.11+ / Node 22.6+；`openai==3.31.0`、`playwright==1.61.0`；示例最多 6 次请求 |
| 替代执行路径 | 同请求可加 `bash_20250124` / `text_editor_20250728` | code execution：`exec_py` + `execute_in_sandbox`，PyAutoGUI / Playwright 脚本，一次调用可含循环 |
| 安全要求 | 最小权限 VM/容器、allowlist、敏感数据隔离、人工确认、审查日志；提示注入分类器 | 隔离浏览器/VM + allowlist、屏幕内容不可信、后果性动作人工确认、步数/时间/成本上限并核验实际结果 |
| 平台状态 | `Managed Agents: Not available`；旧版需 beta header | HTTP endpoint/path、地区可用性、GA 状态 **not shown** |

### 6.2 GitHub 官方 API 元数据快照（本次实测，非文献）

查询时间 `2026-11-06T21:33:09+08:00`，接口 `https://api.github.com/repos/{owner}/{repo}`，14/14 成功。原始结果留存于 `.workbuddy-ai/research/cua-licenses.json`（过程文件，不单独交付）。

| 仓库 | star | 许可证(SPDX) | archived | 最近 push |
|---|---:|---|---|---|
| `browser-use/browser-use` | 120,191 | MIT | 否 | 2026-11-06 |
| `bytedance/UI-TARS-desktop` | 39,558 | Apache-2.0 | 否 | 2026-10-09 |
| `trycua/cua` | 31,860 | MIT | 否 | 2026-11-06 |
| `microsoft/OmniParser` | 25,609 | **CC-BY-4.0** | 否 | 2026-07-20 |
| `anthropics/claude-quickstarts` | 19,120 | MIT | 否 | 2026-11-04 |
| `simular-ai/Agent-S` | 12,893 | Apache-2.0 | 否 | 2026-10-30 |
| `bytedance/UI-TARS` | 11,681 | Apache-2.0 | 否 | 2026-01-27 |
| `xlang-ai/OSWorld` | 3,253 | Apache-2.0 | 否 | 2026-11-02 |
| `openai/openai-cua-sample-app` | 1,923 | MIT | 否 | 2026-10-19 |
| `showlab/ShowUI` | 1,929 | Apache-2.0 | 否 | 2026-04-24 |
| `OS-Copilot/OS-Copilot` | 1,797 | MIT | 否 | 2024-09-09 |
| `xlang-ai/OSWorld-V2` | 411 | Apache-2.0 | 否 | 2026-10-23 |
| `BangProx/ReTRACE` | 4 | **None** | 否 | 2026-10-23 |
| `xu-hu-2002/CUA-Recovery` | 2 | MIT | 否 | 2026-10-09 |

> star 数是**热度**不是**质量或证据强度**；两篇 2026-10 最新论文对应的仓库只有个位数 star，恰好说明「新 ≠ 被广泛验证」。

### 6.3 许可证分离核查（不能凭「开源」推断可商用）

| 层级 | 本次查到 | 未核实 |
|---|---|---|
| 代码仓库 | 上表 14 个 SPDX 字段；`openai-cua-sample-app` README 亦明示 MIT；`anthropics/claude-quickstarts` MIT | `MSR-Orchard/WildAWM`、`jykoh.com/multi-agent-computer-use` 对应仓库未查询 |
| 论文文本 | arXiv HTML 页眉普遍显示 `CC BY 4.0`（如 #22、#17） | 各预印本是否允许衍生、是否已有会议版权转移 |
| 模型权重 | 未查 | UI-TARS / OpenCUA / Qwen / EvoCUA 等权重的 Hugging Face 许可证**全部未核实** |
| 数据集 | 未查 | AgentNet、ScreenSpot-Pro、CUA-Recovery 数据、`xlangai/*` 轨迹数据的单独许可证**全部未核实**；#22 明确 dataset license not shown |
| 依赖项 | 未查 | Playwright / PyAutoGUI / 沙箱运行时 / 商业 API 服务条款与数据处理条款 |
| 特别提示 | `CC-BY-4.0`（OmniParser）需署名；`license: None`（ReTRACE）**不能**推断为可商用或可再分发 | 以上不构成法律意见 |

### 6.4 证据等级区分（严格按用户要求）

| 等级 | 本轮状态 |
|---|---|
| 论文有效（作者报告的结果在其设定下成立） | 多篇，如 #04、#16、#17、#22、#25；**均为作者报告** |
| 作者开源 | #14–#17（Agent-S）、#18/#19（UI-TARS）、#21（OpenCUA 声明释放工具/数据/代码/模型）、#22、#23、#25、#28/#29 参考实现 |
| 他人复现 | **未查到**任何第三方对 OSWorld-Verified / OSWorld 2.0 头部成绩的独立复现报告 |
| 本次复现 | **0 项**（未运行代码、未跑基准） |
| 本项目集成通过 | **不适用**：本任务不含集成目标，且未构建项目 |

维护方 verified 榜单属于「维护方运行并公布」，比作者自报更严格，但**仍不等于独立第三方复现**。

### 6.5 关键建议（每条给前提、依据、反证与最小验证实验）

| 建议 | 前提 | 依据 | 可能推翻它的证据 | 最小验证实验 | 证据不足时的结论 |
|---|---|---|---|---|---|
| R1 引用任何 CUA 分数时，强制记录「基准版本 + release + step budget + 指标 + 尝试次数 + 验证方」六元组 | 读者需要跨报告比较 | #04 摘要 20.6% 与 #05 榜单 44.33% 的差异；#03 关于分数不可比的说明 | 若某基准公开声明各 release 任务集与评分完全一致且给出转换表，则部分字段可省略 | 取同一模型在两个 release 下各跑 3 次固定任务子集，比较 binary 与 partial 的差值是否超出 run-to-run 方差 | 尚不能判断不同 release 分数可否换算 |
| R2 把「恢复/验证」作为独立验收指标，而不是只看最终成功率 | 任务有持久化状态、错误可能级联 | #22 EAR ≤44% / Pass@3 ≤25.5%；#04 §4.1.2 恢复动作 <7%；#13 裁判 80.9% 平衡准确率 | 若目标任务全部可逆、可一键重置，则恢复能力的边际价值下降 | 在一个可复现的桌面任务集上，人为注入 1 处状态错误，测量「是否察觉 / 是否修复 / 最终 verifier 是否通过」三个独立率，重复 3 次 | 尚不能判断某具体系统的恢复能力 |
| R3 先固化执行层（截图尺寸、坐标映射、动作 allowlist、结果核验），再比较上层方法 | 工程条件会直接改变成绩 | #28 坐标空间与 2,576 px 限制、点击偏移诊断表；#29 状态分离与 `check the saved result` | 若某方法完全不依赖像素坐标（纯 accessibility tree / 纯 API），部分约束不适用 | 在同一任务上分别以 1024×768 与 1280×800 截图跑同一 agent，记录点击偏移率与成功率差异 | 尚不能判断分辨率对该任务的影响幅度 |
| R4 对「成本优势」结论要求披露是否含训练/搜索/基础设施 | 存在接口演化、多 rollout、合成环境等前期投入 | #17 成本明确排除 repository construction 与 runtime infra；#22 $16,493 API + 9,322 GPU-hours | 若一次性构建成本可摊销到极大调用量，则单任务成本对比仍可能成立 | 记录一次完整演化/训练流程的总 token、GPU 小时与人工小时，除以推理调用量，给出摊销后单任务成本 | 尚不能判断总拥有成本 |
| R5 商用前逐项核对代码/权重/数据/依赖四层许可证 | 存在 CC-BY-4.0 与 license:None 两类非典型情形 | §6.2/§6.3 实测 | 若上游补发明确授权或替换为自有资产，则限制解除 | 对计划使用的每个资产，保存许可证文件快照与获取日期，形成四层清单 | 尚不能判断可商用性 |

> 以上均为 `[建议]`，**没有一条经过本次验证**。

### 6.6 未执行声明

本次**没有**：安装任何依赖、启动任何容器/VM、调用任何付费 API 跑 CUA 循环、运行任何 benchmark、检查任何源码文件、执行任何复现实验。§6.1 的全部内容来自官方文档与 README 的已读指定章节；§6.2 来自一次 GitHub REST API 只读查询。

---

## 7 冲突与资料缺口

### 7.1 冲突清单

| # | 冲突 | 双方一手/二手来源 | 判定 |
|---|---|---|---|
| C1 | OSWorld 2.0「最好成绩」是 20.6% 还是 44.33%？ | [论文 v2 摘要](https://arxiv.org/abs/2606.29537) vs [官方榜 2026-10-15](https://osworld-v2.xlang.ai) | 时间/版本差异：论文 `v2026.06.24` + Opus 4.8；榜单 `v2.1` + Claude Opus 5。**引用必须同时写日期与 release** |
| C2 | 72.6%（Agent S3）vs 86.0%（Verified 榜）vs 90.2%（新闻） | [arXiv:2510.02250](https://arxiv.org/abs/2510.02250) / [官方页](https://osworld-v1.xlang.ai/) / [网易转载](https://c.m.163.com/news/a/L3GAEE100512D71I.html) | 多 rollout+选择 / 官方 verified 100 steps / 新闻自报，三者不同口径。90.2% **本次无法在官方页核实** |
| C3 | 多个聚合站给出的模型分数（GPT-5.4 75.0%、Claude Sonnet 5 81.2%、Gemini 3.6 Flash 83.0%、Intelligence-Indeed Agent 90.19%、149 条 verified、16 条超人类） | [百度百科](https://baike.baidu.com/item/OSWorld-Verified/67674180) / [decodethefuture](https://decodethefuture.org/?p=3662) vs 本次抓取的官方 68 条（最高 86.0%） | **不一致，均未采信**。可能为 self-reported 表或不同时间快照；官方 self-reported 表本次 `href="#"` 无法取得 |
| C4 | 二手文章把 OSWorld 2.0 来源标为 `arXiv 2607.26041` | [runwise 文章](https://runwise.co/computer-use-agent-guide/273364) vs [实际 arXiv:2606.29537](https://arxiv.org/abs/2606.29537) | 二手来源标识符错误，**不能作为引用依据**；该文自述也承认不同来源数字不一致 |
| C5 | Agent S4「21.3% 超过 Opus 4.8 20.6%」是否仍成立 | [arXiv:2610.28601 Table 2](https://arxiv.org/html/2610.28601v1) vs [官方榜](https://osworld-v2.xlang.ai) | 只在作者选择的旧快照基线内成立；官方榜已有 44.33%，且步数/harness 不同 |
| C6 | OpenCUA 是 34.8% 还是 45.0%？ | [论文 v3](https://arxiv.org/abs/2508.09123) 与 [官方榜](https://osworld-v1.xlang.ai/) | **已解决**：`opencua-32b` 34.8±0.8%、`opencua-72b-preview` 45.0±0.9%，均为 100 steps；新闻稿常把 32B 的 34.8% 当作框架整体成绩 |
| C7 | UI-TARS-2 在 OSWorld 是 47.5 还是 53.1%？ | [arXiv:2509.02544](https://arxiv.org/abs/2509.02544) vs 官方榜 `UI-TARS-2-2509` 53.1% @100 | 评测条件/步数差异，论文未解释；**尚未核实** |
| C8 | OSWorld-Verified 发布日是 2025-07-27 还是 07-28？ | [博客](https://xlang.ai/blog/osworld-verified) `Jul 27, 2025` vs [项目页](https://osworld-v1.xlang.ai/) `2025-07-28` | 时区或「博客发布 / 榜单切换」口径差异，不影响技术结论 |
| C9 | Agent S3 论文标题 | [arXiv 页](https://arxiv.org/abs/2510.02250) `Scaling Agents for Computer Use` vs [Agent-S README BibTeX](https://github.com/simular-ai/Agent-S) `The Unreasonable Effectiveness of Scaling Agents for Computer Use` | 同一 arXiv ID 标题不一致；引用以 arXiv 页为准，README 版本可能是旧题名 |
| C10 | Anthropic 示例模型不一致 | [docs 示例](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) `claude-opus-5-5` vs [demo README](https://github.com/anthropics/claude-quickstarts/tree/main/computer-use-demo) 默认 `claude-opus-4-8` | 页面更新时间差异；**尚未核实**哪个为最新默认 |
| C11 | OSWorld 1.0 摘要的 12.24% 被当作「当前水平」 | [arXiv:2404.07972](https://arxiv.org/abs/2404.07972) 摘要 vs 2026 榜单 | 时间错置。摘要原文同时仍在官方页展示但无版本说明，容易误读 |
| C12 | `shadow interface` 是否为 Agent S4 的机制名 | 前序会话上下文提及；本次读到的 [HTML v1 正文](https://arxiv.org/html/2610.28601v1) §2/§3/§7.2 未出现该术语 | **未核实**，本报告不采用该术语 |

### 7.2 版本 / 撤稿 / 更正 / 失效记录

- **撤稿**：[macOSWorld arXiv:2506.04135](https://arxiv.org/abs/2506.04135) 的 **v2（2025-06-05, 1 KB）标记 `(withdrawn)`**；v3（2025-07-16）与 v4（2025-10-18）为后续版本。引用应指定 v4，不得引 v2。
- **替代版本**：OSWorld 2.0 论文 v2（2026-07-13）的 headline 数字已被官方榜 `v2.1`（2026-10-15）刷新；[OpenCUA](https://arxiv.org/abs/2508.09123) v1/v2/v3 中 v3 修改了作者列表与首页格式（`Comments: Updata author list, modify first page format, correct typos`）；[综述 2411.18279](https://arxiv.org/abs/2411.18279) 有 v1→v12 共 12 个版本。
- **会议正式出版状态**：[Agent-S README](https://github.com/simular-ai/Agent-S) 自报 Agent S 获 ICLR 2025 接收及 workshop 最佳论文、S2 获 COLM 2025 接收、S3 获 TMLR 2026 接收；**本次未从会议官方论文集核实**，标 `[作者报告]`。OSWorld 的 NeurIPS 2024 亦仅见于二手报道，arXiv `Comments` 字段未标注。
- **失效/不可访问**：OSWorld v1 官方页的 `self-reported results` 链接为 `#`；部分 arXiv HTML 长文在抓取时正文截断。没有发现核心条目整体 404。
- **未检索到撤稿声明**：本次未做系统性撤稿库检索，因此这是「未查到」，不是「不存在」。

### 7.3 负面结果与失败证据汇总

| 证据 | 数字 | 来源 |
|---|---:|---|
| 长时程 binary completion 随任务时长崩塌 | >163 分钟任务所有受测模型为 0 | [#04 §3.2 / #05](https://arxiv.org/html/2606.29537v2) |
| 恢复动作预算极低 | recovery + repair < 7% | #04 §4.1.2 |
| 错误意识与修复脱钩 | EAR ≤44.0%、Pass@3 ≤25.5%；aware vs unaware 15.6% vs 12.2% | [#22 §5.2](https://arxiv.org/html/2610.27645v1) |
| 效率远逊人类 | 最好的 agent 仍多走 2.7–4.3× 步数；后续每步可达开头 3× 时长 | [#26](https://arxiv.org/abs/2506.16042) |
| 高分辨率专业 grounding | 已有最佳 18.9%（免训练搜索法也仅 48.1%） | [#09](https://arxiv.org/abs/2504.07981) |
| 专业工件任务 | CAD 最佳 17.5% vs 专家 87.0% | [#10](https://arxiv.org/abs/2609.16251) |
| 办公实操 | 单轮 ≤36.6%，带反馈 agentic 68.8%，社区参考 95.5% | [#12](https://arxiv.org/abs/2606.10956) |
| 自动裁判 | 最佳 80.9% 平衡准确率；工具调用让开放权重模型更差 | [#13](https://arxiv.org/abs/2610.11050) |
| 跨平台/多语言 | 桌面 agent 迁到 Android 变差；阿拉伯语相对英语平均降 28.8%；开源轻量 macOS <5% | [#07](https://arxiv.org/abs/2405.14573) / [#11](https://arxiv.org/abs/2506.04135) |
| 任务变体鲁棒性 | 任务参数变化显著改变成绩，静态测试集会高估实用性 | [#07 摘要](https://arxiv.org/abs/2405.14573) |
| 安全副作用 | 216 条轨迹中约 33% 绕过用户可见界面、约 14% 提取隐藏应用状态 | [#04 §4.2](https://arxiv.org/html/2606.29537v2) |

### 7.4 资料缺口（按四种状态分列）

**未查到**
- 任何第三方对 OSWorld-Verified / OSWorld 2.0 头部成绩的独立复现报告。
- 针对 #16 BJudge 72.6%、#17 Agent S4 21.3%、#25 WildAWM 跨 8 基准增益的外部复现。
- 系统性的撤稿/更正声明（除 macOSWorld v2 外）；本次未检索 Crossref/Retraction Watch 等专门库。

**原文未报告**
- OSWorld 2.0：binary completion 精确阈值与公式、partial score 权重公式、主评估重复次数/随机种子、§4.4 各类失败的单独发生率、§6 Limitations 正文。
- Agent S4：最终 full-benchmark 独立重复次数与随机种子、Parasail 具体费率、独立 Limitations 章节。
- CUA-Recovery / ReTrace：独立 Limitations 章节、EAR judge prompt 正文、数据集单独许可证。
- WebArena：arXiv 摘要未给任务总数（二手来源称 812 个，未采信）。
- Anthropic / OpenAI 文档：HTTP endpoint、具体价格数值、地区可用性、GA 状态。

**当前无法访问**
- OSWorld v1 官方页 `self-reported results` 表（`href="#"`）。
- OSWorld 2.0 HTML 的 §6、Appendix E.2（Safety Result Details）、Appendix H.4（Safety Case Studies）正文——抓取在 §4.4 后截断。
- OSWorld 2.0 榜在 150 / 300 / 450 step budget 下的分别得分；每条榜单行的实际 step budget。
- 部分 PDF 的图表与附录逐项内容（本轮主要读 HTML/abs 页）。

**尚未核实**
- 模型权重、数据集、依赖项的单独许可证（§6.3）。
- 各论文会议正式出版状态（多为作者自报或二手）。
- 聚合站给出的模型名称与分数（C3）。
- `shadow interface` 术语（C12）、`UI-TARS-2` 47.5 vs 53.1 的差异（C7）、Anthropic 默认模型版本（C10）。
- #24 MACU `3.4−25.5%` 是百分点还是相对比例。

---

## 8 参考来源与检索说明

### 8.1 实际检索渠道（按使用顺序）

1. **WebSearch**（联网关键词检索，返回摘要与链接；仅用于发现线索）。
2. **WebFetch**（打开原始条目正文，抽取并核对标题、作者、日期、版本、标识符、摘要与指定章节）。
3. **arXiv `/abs/` 与 `/html/` 页面**：核对 submission history、v1..vN、comments、DOI、作者列表、摘要；3 篇实读 HTML 指定章节。
4. **官方项目页与榜单**：`osworld-v1.xlang.ai`、`osworld-v2.xlang.ai`、`xlang.ai/blog/osworld-verified`。
5. **厂商官方文档**：`docs.anthropic.com`、`platform.openai.com`。
6. **GitHub REST API**（`api.github.com/repos/...`）：14 个仓库的许可证、star、fork、archived、created/pushed_at；另有 GitHub 网页 README。
7. **本地线索索引**：前序会话生成的 `.workbuddy-ai/research/audit-all.txt`（277 篇已核验清单），**仅用于取回精确的 arXiv 编号与官方 URL，不作任何结论依据**；所有纳入条目本轮均重新打开原始页面核对。
8. **未使用**：新闻/百科/知乎/CSDN/聚合站**仅作线索**，未作为任何关键结论的依据；发现的错误编号见 C4。

### 8.2 主要关键词（中英文与同义词）

- 英文：`computer use agent`, `CUA`, `computer-using agent`, `GUI agent`, `GUI grounding`, `screen parsing`, `visual grounding`, `screenshot-only agent`, `native GUI agent`, `OSWorld`, `OSWorld-Verified`, `OSWorld 2.0`, `long-horizon computer use`, `error recovery CUA`, `failure recovery benchmark`, `multi-agent computer use`, `agent world model`, `environment synthesis`, `agentic judge`, `computer use tool`, `computer_call`, `toolset`, `PyAutoGUI`, `Playwright`, `accessibility tree`, `binary completion`, `partial score`, `leaderboard`, `license`, `withdrawn`.
- 中文：`电脑操作智能体`、`图形界面智能体`、`屏幕定位 / 视觉定位`、`长时程任务`、`错误恢复`、`失败案例`、`评测榜单`、`人类基线`、`多智能体并行`、`合成环境`、`自动裁判`、`许可证`、`撤稿`。
- 同义词与前后向追踪：`OSWorld → OSWorld-Verified → OSWorld 2.0`；`Agent S → S2 → S2.5 → S3(BJudge) → S4(Evolving Agent Interfaces)`；`UI-TARS → UI-TARS-1.5 → UI-TARS-2`；`ScreenSpot → ScreenSpot-Pro`；`WebArena → VisualWebArena → Online-Mind2Web`；由 #04 的 §2.1.3 追到 model-based evaluation，再由 #13 追到 judge 可靠性；由 #22 的 Table 1 追到 AgentNet / GUI-Reflection / ProCUA-SFT 等训练集；由 #28/#29 的文档链接追到两个参考实现仓库。

### 8.3 纳入 / 排除规则

- **纳入**：原论文 / 正式出版页 / 可信预印本（arXiv，含版本历史）/ 研究机构与作者项目页 / 官方仓库 / 官方文档 / 基准官方榜单与数据平台。
- **排除作结论依据**：新闻稿、百科、转载、聚合站、AI 摘要、无出处的教程；本次共识别 4 个此类来源并列入 C3/C4。
- **排除主题**：安全攻防专项基准（沿用会话前序约束）；纯 API/CLI 编排（仅作混合接口对照）。
- **核心表规模**：29 项（落在要求的 15–30 项内），未为凑数加入低质量内容；另有 8 项候选索引与覆盖说明在 §3.3。
- **同一研究关联**：论文 + 项目页 + 博客 + 仓库按一组处理，不计为多份独立实验证据（§3.1 末尾声明）。

### 8.4 本次核验动作与字段

对 29 项逐条核对：完整标题、作者或机构、年份与全部版本日期、arXiv ID / DOI、Comments、出处链接、代码/数据链接、发表状态（首次发表 / 修订 / 软件发布 / 榜单发布）、阅读深度。**未凭记忆补齐任何字段**；缺失即标 `not shown` 或归入 §7.4 四类。

### 8.5 交付前自检

| 检查项 | 结果 |
|---|---|
| 8 节顺序是否符合要求 | 是（1 结论与证据边界 → 2 最新进展与研究地图 → 3 核心资料总表 → 4 主要路线比较表 → 5 推荐阅读顺序 → 6 可行性与验证路线 → 7 冲突与资料缺口 → 8 参考来源与检索说明） |
| 每条核心资料是否标明阅读与验证状态 | 是（§3.1「状态」列，S0–S6） |
| 是否虚报「全文已读 / 验证通过 / 独立复现」 | 否，S4/S5/S6 = 0，并已在 §1.1、§6.6 明写 |
| 关键结论是否附可点击原始链接与章节定位 | 是（§1.5、§3.2、§4.2、§7 均含链接，并尽量给到 §3.2 / Table 2 / §4.4 / Appendix A 等位置） |
| 数字是否标明条件 | 是（§4.2 禁止横比矩阵、§4.3 措辞核查） |
| 是否区分作者报告 / 维护方榜单 / 官方文档 / 助手推断 / 建议 | 是（§1.3 标签贯穿全文） |
| 是否区分代码/权重/数据/依赖许可证 | 是（§6.3，且明确列出未核实项） |
| 是否列出负面结果与冲突证据 | 是（§7.1 12 条、§7.3 10 类） |
| 是否列出未完成条目 | 是（§3.2 深度摘录仅覆盖 12/29；§7.4；§8.7） |
| 是否存在「对话结束后继续后台工作」的承诺 | 否 |
| 交付前对最吃重的两个数字做二次抽检 | 是，见下方 §8.5.1 |

**§8.5.1 交付前二次抽检（2026-11-06 21:55 +0800，重新打开原始页面）**

| 抽检对象 | 报告采用值 | 本次重新打开官方页所得 | 是否一致 |
|---|---|---|---|
| OSWorld-Verified 榜首 | `claude-fable-5[1m]` 86.0% @ Max Steps 100，日期 2026-08-01，列标签 `Success Rate (Avg±Std)` | 页面 `Rank 1 *`，`**86.0%**`，`Max Steps: 100`，`📅 Aug 1, 2026`，列 `Success Rate (Avg±Std)`；任务规模声明 369（可排除 8 个 → 361），该榜首行 `Success/Total` 分母为 358 | 一致；分母差异已在 §3.2 #02 记录 |
| OSWorld 2.0 榜首 | 44.33% binary / 77.67% partial，最后更新 2026-10-15，108 长时程任务 | 页面 `Rank 1` `Claude Opus 5`（Anthropic / Max / Batch tool / v2.1）= 44.33% / 77.67%，`Last update time: 2026-10-15`，`108 Long-horizon tasks`；主指标口径为 `primary binary-completion metric at 500 steps`，榜单筛选行显示 `Step budget: All` | 一致；`All` 与 500 steps 的口径差别列为 §7 未关闭问题 |

> 抽检只重新核对这两处数字及其条件，**不代表**其余 27 项做了全文复读；其余条目的阅读深度仍以 §3.1 状态列为准。

### 8.6 完整链接索引（按 §3.1 编号）

01 https://arxiv.org/abs/2404.07972 · 02 https://osworld-v1.xlang.ai/ · 03 https://xlang.ai/blog/osworld-verified · 04 https://arxiv.org/abs/2606.29537 · 05 https://osworld-v2.xlang.ai · 06 https://arxiv.org/abs/2409.08264 · 07 https://arxiv.org/abs/2405.14573 · 08 https://arxiv.org/abs/2307.13854 · 09 https://arxiv.org/abs/2504.07981 · 10 https://arxiv.org/abs/2609.16251 · 11 https://arxiv.org/abs/2506.04135 · 12 https://arxiv.org/abs/2606.10956 · 13 https://arxiv.org/abs/2610.11050 · 14 https://arxiv.org/abs/2410.08164 · 15 https://arxiv.org/abs/2504.00906 · 16 https://arxiv.org/abs/2510.02250 · 17 https://arxiv.org/abs/2610.28601 · 18 https://arxiv.org/abs/2501.12326 · 19 https://arxiv.org/abs/2509.02544 · 20 https://arxiv.org/abs/2408.00203 · 21 https://arxiv.org/abs/2508.09123 · 22 https://arxiv.org/abs/2610.27645 · 23 https://arxiv.org/abs/2610.27954 · 24 https://arxiv.org/abs/2606.01533 · 25 https://arxiv.org/abs/2610.26828 · 26 https://arxiv.org/abs/2506.16042 · 27 https://arxiv.org/abs/2411.18279 · 28 https://docs.anthropic.com/en/docs/build-with-claude/computer-use · 29 https://platform.openai.com/docs/guides/tools-computer-use

补充一手链接：https://github.com/xlang-ai/OSWorld · https://github.com/xlang-ai/OSWorld-V2 · https://github.com/simular-ai/Agent-S · https://github.com/bytedance/UI-TARS · https://github.com/anthropics/claude-quickstarts/tree/main/computer-use-demo · https://github.com/openai/openai-cua-sample-app · https://github.com/xu-hu-2002/CUA-Recovery · https://github.com/BangProx/ReTRACE · https://github.com/MSR-Orchard/WildAWM · https://github.com/xlang-ai/OSWorld/blob/main/PUBLIC_EVALUATION_GUIDELINE.md · https://jykoh.com/multi-agent-computer-use · https://cad-world.github.io

### 8.7 已完成 / 未完成 / 未关闭问题 / 下一步

**已完成**：29 项核心资料的一手条目核验；3 篇 2026 论文指定章节实读；2 个官方榜单与 1 个升级博客的关键段落；两家厂商 CUA 官方文档指定章节；14 个仓库的官方 API 元数据；12 条冲突与 10 类负面证据整理；8 节中文报告。

**未完成**：其余 17 项核心资料的逐项深度摘录（只做了总表级）；所有条目的全文阅读（S4=0）；源码检查（S5=0）；任何复现与实验（S6=0）；模型权重/数据/依赖许可证核查；会议出版状态官方核验；PDF 图表与附录逐项核对。

**未关闭问题**：C1（不同 release 分数能否换算）、C3（self-reported 表真实内容）、C7（UI-TARS-2 分数差异）、C10（Anthropic 默认模型）、C12（shadow interface 术语）、§4.3 中 MACU 提升口径、OSWorld 2.0 §6 Limitations 内容。

**下一步（需新指令才会执行，本报告不会在对话结束后自行继续）**：① 取得官方 self-reported 表与 OSWorld 2.0 完整 PDF 附录，关闭 C1/C3/C7；② 对 17 项补齐逐项深度摘录；③ 若需工程结论，再单独授权进行依赖安装、许可证逐层核对与最小验证实验（R1–R5）。

---

*报告结束。本报告为资料核验与综合判断，不含方案设计、架构图、代码、部署步骤，也未构建任何项目。*
