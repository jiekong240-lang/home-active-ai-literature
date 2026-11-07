# 家用机主动式 AI 文献资料集（home-active-ai-literature）

本仓库汇集「家用机实现主动式 AI / 本地 Computer-Use Agent（CUA）」相关研究资料，按**差集补全 + 来源可核验**的原则整理。所有文献均为可独立复核的一手来源（arXiv 预印本 / 官方文档），不含博客聚合、营销材料或方案设计文档。

## 仓库结构

```
home-active-ai-literature/
├── README.md
├── docs/
│   ├── 01-literature-100.md                # 初版 100 篇文献清单（按 12 子类）
│   ├── 02-literature-collection-277.md     # 全量总集 277 篇（含 CUA 全量补收，编号 001–277）
│   ├── 03-coverage-review.md               # 覆盖度审查：69 项一手资料，有 39 / 偏薄 4 / 缺 26
│   ├── 04-execution-learning-supplement.md # ★ 核心补编：执行力与学习能力两条线，差集 28 篇（来源可查）
│   └── 05-cua-research-report.md           # CUA 高质量调研报告（8 节，29 项核心资料）
└── scripts/
    ├── dedup-supp.py                       # 与 277 总集的 arXiv ID 差集核验
    └── verify-supp-sources.py              # 调用 arXiv API + HTTP 可达性，核验来源可查
```

## 各文档说明

| 文档 | 内容 | 性质 |
|---|---|---|
| `01-literature-100.md` | 12 类、100 篇，初始盘点 | 文献清单 |
| `02-literature-collection-277.md` | 三轮检索合并为 277 篇总集（唯一 URL 277） | 文献总集 |
| `03-coverage-review.md` | 对 277 总集的覆盖度审计，点名 26 项缺口 | 覆盖度审查 |
| `04-execution-learning-supplement.md` | **相对 277 总集的差集补全，28 篇技术论文** | ★ 核心补编 |
| `05-cua-research-report.md` | CUA 方向中文调研报告 | 调研报告 |

## 核心交付：补编（04）

`04-execution-learning-supplement.md` 是本次整理的重点——它补齐「执行力」与「学习能力」两条能力线**总集尚未覆盖**的二阶/专精文献，共 28 篇（S-01…S-28），全部为 arXiv 技术论文，且逐条实跑核验：

- **自我验证 / 批评（8 篇）**：Training Verifiers、Let's Verify Step by Step、Math-Shepherd、Shepherd、Agent-as-a-Judge、CRITIC、CoVe、GPT-4 Doesn't Know It's Wrong
- **反思 / 恢复精炼（2）**：Self-Refine、ADAS
- **规划（1）**：RAP
- **工具调用规模化（3）**：Gorilla、ToolLLM、XGrammar
- **执行基准（4）**：SWE-bench、SWE-agent、CRMArena、DigiRL
- **学习 / 自我改进 / 强化自训练（6）**：STaR、Self-Rewarding、SPIN、SCoRe、ReST、Darwin Gödel Machine
- **轨迹 / 技能数据合成（4）**：Voyager、AgentTrek、OS-Genesis、GUI-R1

> 说明：277 总集**已含** 12 篇基础经典（ReAct / Toolformer / Reflexion / Generative Agents / ToT / Android-in-the-Wild / WebArena / AgentBench / GAIA / τ-bench / UI-R1 / BFCL），不在补编重复列入。

## 来源可查性

补编 28 条每篇均附**稳定 arXiv ID + `https://arxiv.org/abs/<id>` 出处链接**。可一键复现核验：

```bash
cd scripts
python verify-supp-sources.py     # arXiv API 取回标题比对 + abs 链接 HTTP 可达性
python dedup-supp.py             # 与 277 总集做 arXiv ID 差集（零重复）
```

实跑结果：28/28 均为「技术论文 + HTTP 200 可打开 + 标题一致」。

## 许可证与边界

- 论文多为 arXiv 预印本，具体许可证 / 商用限制需逐篇在对应源码仓库确认；本仓库仅作资料整理，不构成任何授权。
- 全部资料排除安全类；不含方案设计、架构图、代码实现或部署步骤。
- 阅读深度为 S1（已核原始条目：标题/作者/日期/版本/摘要），未读全文、未跑实验。

---
由 WorkBuddy AI 整理（2026-11-06 至 2026-11-07）。
