# 文献覆盖度审查（对《家用机「主动式 AI」文献总集》277 篇）
> 本文件只做覆盖度核对，**不补收文献、不写方案、不画架构、不写代码、不构建任何项目**。
## 一、结论
**没有补全。** 按「家用机实现主动式 AI + 本地 CUA」所需的一手技术资料逐项核对 69 项：**有 39 项、偏薄 4 项、缺 26 项**。
覆盖得扎实的是：主动式方法论文、云端 API 工具调用/结构化输出、协议栈、记忆与评测基准、桌面截屏与输入注入的跨平台官方接口、GUI grounding 与 CUA 系统论文、高星开源实现。缺口集中在**「常驻运行的 OS 机制」「主动触发的事件源」「本地推理服务化的具体接口」「语音 always-on 通道」「若干具体命令/专页级别的一手文档」「少数基准的独立入口」**这六处。
其中 2 项其实已经在检索候选池里，只是首轮「收敛到 100 篇」时被主题收敛剔除，不需要重新检索即可恢复；其余是真未采集。
需要说清这个结论的边界：这里判断的是**这份 69 项一手资料清单（明细见第四节）**是否齐备，不是「世界上再无相关文献」的证明。清单按「触发 → 感知 → 推理 → 规划/记忆 → 执行 → 评测 → 常驻工程化」这条能力链列出，覆盖判断可复跑；但任何清单都不能穷尽所有需要的技术资料。
## 二、口径与可复现测量
- 核对对象：`家用机主动式AI_文献总集.md` 的 277 篇（= 三轮 302 条候选 − 首轮剔除 20 − 二轮去重剔除 5）。
- **严格口径**：判定只看每条的 `标题 + URL`。上一版脚本把 `要点/依据/影响力` 也纳入扫描，导致「某篇论文要点里提到 GGUF」被误判为「已收 GGUF 规范」，本次已修正。
- 另设 `偏薄`：严格口径命中了，但命中条目只是间接包含/内含该资料，不算真正收齐。
- 候选池检查：同时检查首轮主题收敛剔除的 20 条与二轮去重剔除的 5 条，标注可直接恢复的条目。
- 复跑：`.workbuddy-ai/research/check-coverage2.py`（只读，不改动总集）。
- 总集自检：编号 001–277 连续、唯一 URL 277、空要点/空依据/空出处 0、核验分布 `OK 200 / TITLE_MISMATCH 47 / FAIL 17 / BLOCKED 13`。
## 三、按模块统计
| 模块 | 有 | 偏薄 | 缺 |
|---|---:|---:|---:|
| 1 触发与常驻 | 2 | 0 | 5 |
| 2 API 编排与协议 | 7 | 1 | 5 |
| 3 记忆与状态 | 4 | 0 | 1 |
| 4 屏幕与输入 | 8 | 0 | 4 |
| 5 浏览器接口 | 2 | 0 | 2 |
| 6 本地推理 | 3 | 1 | 4 |
| 7 评测与榜单 | 5 | 2 | 2 |
| 8 语音与桌面 | 4 | 0 | 3 |
| 9 主动式方法 | 4 | 0 | 0 |
| **合计** | **39** | **4** | **26** |

## 四、差什么（逐项点名）
按「缺口对实现的影响」排序，先列会卡住能力链的，再列专页/命令级的一手文档。
| # | 缺的一手资料 | 为什么需要 | 现有最接近的替代 | 候选池可否恢复 |
|---:|---|---|---|---|
| 1 | **Microsoft Graph 变更通知 / Google Calendar Events API 官方**（1 触发与常驻） | 邮件/日历到来的主动触发需要一手订阅接口 | I-08 RFC 2177 IMAP IDLE（仅邮件，非日历/云账户） | 不可，需新检索 |
| 2 | **Modern Standby / powercfg / 唤醒定时器官方**（1 触发与常驻） | 家用机睡眠后能否被定时唤醒，决定「主动」是否可持续 | 无 | 不可，需新检索 |
| 3 | **Windows 服务 / 登录自启动 / 后台任务官方**（1 触发与常驻） | 无人登录时的常驻运行方式 | F-05 Node-RED 本地运行、F-09 Windmill 自托管（应用层，非 OS 机制） | 不可，需新检索 |
| 4 | **inotify(7) / ReadDirectoryChangesW / FSEvents 官方**（1 触发与常驻） | 文件变动是家用机最典型的主动触发源 | I-07 GitHub webhooks、I-08 IMAP IDLE（网络事件，非本地文件事件） | 不可，需新检索 |
| 5 | **launchd / LaunchAgents 官方手册**（1 触发与常驻） | macOS 上唯一官方的常驻守护机制 | 无（Apple 侧只有 ScreenCaptureKit/AXUIElement） | 不可，需新检索 |
| 6 | **GGUF 格式官方规范**（6 本地推理） | 权重格式与量化类型定义 | W-05 Ollama docs、W-06 quantize README（仅提到 GGUF） | 不可，需新检索 |
| 7 | **LM Studio 官方文档**（6 本地推理） | 家用机 GUI 本地推理的一手文档 | R-03 agenticSeek README 中提到（非官方） | 不可，需新检索 |
| 8 | **llama-server / OpenAI 兼容服务官方页**（6 本地推理） | 本地起 HTTP 服务的一手说明 | 无 | 不可，需新检索 |
| 9 | **vLLM 官方部署文档**（6 本地推理） | 本地服务化另一主线的官方页 | W-01 PagedAttention 论文 | 不可，需新检索 |
| 10 | **JSON-RPC 2.0 规范**（2 API 编排与协议） | MCP 传输层的底层规范 | G-01 MCP 主规范（引用但未收规范原文） | 不可，需新检索 |
| 11 | **MCP 分页规范（Transports / Tools / Resources / Prompts）**（2 API 编排与协议） | 主规范落地页之外的四类原语细节 | G-01 /specification/latest、G-02 architecture（总览级） | 不可，需新检索 |
| 12 | **Prompt caching 官方技术页**（2 API 编排与协议） | 家用机长期常驻调用的成本控制一手资料 | K-03 Pricing、D-02 DeepSeek 硬盘缓存新闻（价格/新闻，非技术页） | 可：C-04（首轮主题收敛剔除） |
| 13 | **Streaming 响应官方页**（2 API 编排与协议） | 长任务流式反馈与可中断控制 | G-06 SSE 规范、K-07 Realtime API（协议/实时，非 HTTP 流式响应页） | 可：C-02（首轮主题收敛剔除） |
| 14 | **约束解码官方（Guidance / Outlines / XGrammar / llguidance）**（2 API 编排与协议） | 本地推理强制输出合法 JSON 的一手资料 | C-01 云端 Structured Outputs（云端能力，非本地约束解码） | 不可，需新检索 |
| 15 | **Windows Graphics Capture 专页**（4 屏幕与输入） | 新一代窗口级截屏 API | S-06 Screen capture 聚合页、Y-07 Desktop Duplication（旧 API） | 不可，需新检索 |
| 16 | **Windows.Media.Ocr / OcrEngine 官方**（4 屏幕与输入） | Windows 原生 OCR | S-11 Tesseract、Y-10 Apple Vision OCR、S-12 OpenCV | 不可，需新检索 |
| 17 | **adb shell input / uiautomator dump 官方命令页**（4 屏幕与输入） | 移动端动作注入与 UI 树导出的直接命令 | Y-05 adb 总览、S-07 UI Automator 测试页 | 不可，需新检索 |
| 18 | **多显示器 / DPI 缩放 / 窗口焦点官方**（4 屏幕与输入） | 坐标 grounding 落到真实屏幕的关键校正 | 无 | 不可，需新检索 |
| 19 | **Playwright connectOverCDP 官方专页**（5 浏览器接口） | 接管用户已登录的浏览器会话 | Y-01 Playwright Installation 总览、Y-02 CDP Viewer | 不可，需新检索 |
| 20 | **Selenium 官方文档**（5 浏览器接口） | 另一条主流浏览器自动化路线的官方文档 | Y-04 W3C WebDriver 规范（协议层，非实现文档） | 不可，需新检索 |
| 21 | **全局快捷键 / 系统托盘官方**（8 语音与桌面） | 常驻桌面入口 | X-08 Tauri、Y-11 Electron（框架总览） | 不可，需新检索 |
| 22 | **本地 TTS 官方（Piper / Kokoro / sherpa-onnx）**（8 语音与桌面） | 主动播报输出通道 | K-07 Realtime API（云端语音） | 不可，需新检索 |
| 23 | **本地 VAD / 唤醒词官方（Silero VAD / openWakeWord / Porcupine）**（8 语音与桌面） | always-on 语音触发的一手资料 | 无（只有 X-01 Whisper 离线识别） | 不可，需新检索 |
| 24 | **OSWorld-Verified 官方**（7 评测与榜单） | 修正版基准与榜单口径 | T-02 OSWorld 2.0 主页（不同版本） | 不可，需新检索 |
| 25 | **OpenAI Operator System Card / CUA 技术报告**（7 评测与榜单） | CUA 官方能力边界与评测口径 | M-02 Computer-Using Agent 官方研究页（产品/研究页，非 system card） | 不可，需新检索 |
| 26 | **sqlite-vec / FAISS / Qdrant 官方**（3 记忆与状态） | 家用机轻量嵌入式向量检索一手资料 | H-04 Chroma、H-06 HNSW 论文、X-02 FTS5 | 不可，需新检索 |

## 五、判为「偏薄」的项（不算缺口，但也不算收齐）
| 项 | 判定理由 |
|---|---|
| MCP 主规范 / 架构 / 官方 SDK | 主规范/架构/TS SDK 齐；Python SDK 未单独收 |
| llama.cpp 量化工具页 / 主仓库 | 部分：W-06 是 tools/quantize 子页；主仓库 K-10 在候选池被剔 |
| ScreenSpot 独立数据集页 / ScreenSpot-v2 | 间接：T-09 是 SeeClick 仓库、N-04 是 OS-ATLAS 论文，未见 ScreenSpot / v2 独立数据集页或论文 |
| Anthropic computer-use-demo 独立仓库 | 间接：Z-09 为 claude-quickstarts 总仓库，demo 只是其中子目录 |

## 六、上一版脚本的误判修正
| 被误判为「有」的项 | 实际命中条目 | 为什么不算 | 修正结论 |
|---|---|---|---|
| OSWorld-Verified 官方 | AA-02 WebArena-Infinity | 要点里出现 verified / OSWorld 字样，条目本身是 WebArena-Infinity | 缺 |
| GGUF 格式官方规范 | W-05 Ollama docs、W-06 quantize README | 两篇只是提到 GGUF，不是格式规范原文 | 缺 |
| LM Studio 官方文档 | R-03 Fosowl/agenticSeek | 第三方仓库 README 提到 LM Studio，非官方一手文档 | 缺 |
| prompt caching 官方文档 | K-03 Claude Pricing | 价格页不是 caching 技术页 | 缺（候选池 C-04 可恢复） |
| ScreenSpot 独立论文 | O-03 SeeClick、O-04 OmniParser、M-07 UI-TARS 等 8 条 | 均为论文正文引用该数据集，未见独立数据集页 | 偏薄（有间接替代） |
| Anthropic computer use demo 仓库 | Z-09 claude-quickstarts | 总仓库含 demo 子目录，非独立 demo 仓库 URL | 偏薄（有间接替代） |

说明：上一版宽松脚本只核了 36 项、判缺 14 项；本次把清单扩展到 69 项并收紧为「只看标题 + URL」，得到缺 26 项、偏薄 4 项。两次数字的差异来自**清单扩展 + 口径收紧**，不是同一份清单上凭空多出缺口；上面 6 处是「原本判有、复核后改判」的部分。

## 七、没有问题的部分
- **CUA 主线论文**：系统架构（N）、GUI grounding（O）、浏览器（P）、移动端（Q）、VLM 基座（U）、规划恢复（V）六类共 70+ 篇，含 UI-TARS / Agent S 系列 / OS-ATLAS / OmniParser / SeeClick / ShowUI / OSWorld / WAA / Spider2-V / Agent Company 等主要工作。
- **高星开源实现**：GitHub REST API 快照成功 51 个仓库（失败 5 个不编造数字），R/Z 两类共 24 个仓库页，star 数交叉校验无数量级偏差。
- **跨平台桌面控制底座**：Windows（UI Automation / SendInput / mouse_event / Screen capture / Desktop Duplication）、macOS（AXUIElement / Quartz Events / ScreenCaptureKit / Vision OCR）、Linux（AT-SPI / XTEST）、Android（adb / UI Automator / AccessibilityService）四大平台官方页齐备。
- **出处可信度**：277 篇全部带 URL、页面依据、要点；40 条二次确认明细、21 处独立抽检记录；明确区分 `403 反爬 / 地区重定向 / 代理 502 / PDF 无 HTML 标题 / GitHub 通用标题` 与「链接失效」。
- **边界**：全部资料排除安全类；文件不含方案设计、架构图、代码、部署步骤，未构建任何项目。

## 八、复跑方式
```bash
cd ".workbuddy-ai/research" && python check-coverage2.py
```
脚本读取 `items.json` / `items-new.json` / `items-supp.json`，按严格口径重算本表并覆盖生成工作区根目录的 `文献覆盖度审查.md`；不改动 277 篇总集。
