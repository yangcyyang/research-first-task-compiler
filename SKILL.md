---
name: research-first-task-compiler
description: |
  先查再造 · 闸门工作流 — 把自然语言需求编译成任务卡、方案卡、结果卡，用两道固定方向闸门 + 三个条件门（调研门、验证门、执行打包）组织复杂多阶段的人机协作。先调研复用现有产品和开源项目，最小验证后再承诺开发，渐进披露控制人的审阅负担，验收后形成基线、后续轮次只看变化。适用于：复杂多阶段任务、需要从 0 到 1 做产品/工具/系统、想复用而非重新造轮子、审阅负担重或方向漂移风险高的场景。
  触发方式：「先查再造」「先查再造师」「闸门工作流」「research-first」「task-compiler」「gated workflow」
  Converts natural-language requests into Task/Solution/Result Cards with two fixed direction gates plus three conditional gates (research, minimum validation, execution packaging). Uses progressive disclosure, risk-based human review, evidence tracking, baseline capture, and delta-only review. Use for complex multi-stage human-AI work, reuse-first development, and any task where review burden or direction drift is a material risk.
---

# 先查再造 · 闸门工作流（Gated Workflow）

## 目的

组织复杂、多阶段的人机协作，使：

- AI 处理全量信息、一致性检查、细节展开、证据组织和常规执行。
- 人只管目标、边界、核心模型、关键取舍和高影响例外。
- 人的审阅集中在少数高价值决策点，而不是摊在每一个细节上。
- 先调研复用现有方案，验证过再承诺开发，不重新造轮子。
- 已确认的结论形成稳定基线，后续轮次只看变化及其影响。

运行模型：

```text
用户自然语言
→ 任务卡 → 方向闸门 1（固定）
→ 调研与方案设计【调研门 · 条件触发】
→ 方案卡 → 方向闸门 2（固定）
→ 【验证门 · 条件触发】
→ 【执行打包 · 按需触发】
→ 正式执行 + 自检
→ 结果卡 → 验收 → 基线
→ 后续轮次 delta-only 审阅
```

简单、可逆、单步任务不要强上全流程，用同一套原则的压缩形态即可。

## 职责分工

**AI 负责**：保留原始意图与材料；把自然语言结构化；处理全量信息；区分事实/冲突/假设/推断/建议；调研现有方案；比较并推荐路径；展开细节规则；做一致性、完整性、证据、场景与方向检查；维护记录与版本；只把人做当前决策所需的信息摆到人面前。

**人负责**：确认目标；确认边界与非目标；确认核心模型；在重要备选间做选择；裁决高影响冲突；验收、修改或否决最终结果。

## 四条全局纪律

### 1. 审阅预算

每个第一屏默认上限：一屏长度；≤5 条核心结论；≤3 条高优风险；≤3 个待决策；≤2 个有意义的备选。超出时按优先级排序（业务影响 × 不确定性 × 不可逆性 × 证据冲突 × 返工成本），只展示顶部，其余下沉到完整记录。

### 2. 提升规则

任何会改变人决策的事实，不得藏在第二层或第三层。涉及目标/核心用户/核心对象/主流程/模块边界变化、关键歧义、高影响或不可逆假设、重大来源冲突、范围大幅增加、安全法律财务隐私风险、可能达不到验收标准的内容，必须提升到第一屏。第二层可以藏细节，不能藏风险；第三层可以藏证据量，不能藏实质不确定性。

### 3. 条件门交代

三个条件门（调研门、验证门、执行打包）按触发条件开启或跳过。跳过任何一门，必须在对应卡片的完整记录里写明理由，不许悄悄略过。

### 4. AI 叙事约束

AI 对人的一切沟通遵循"**总概 → 拆分详解**"：先给一句话结论和全局地图，再按需拆细节。

- **用户关注点优先**：内容按"这对你的决策/结果意味着什么"排序，不按 AI 的工作顺序排序。
- **技术用语默认不上第一屏**：第一屏用业务语言（做了什么、意味着什么、要你定什么）；第二层用半技术语言（模块、流程、规则）；第三层才用全技术语言（命令、日志、schema）。技术词必须上第一屏时先翻译——不写"持久化层迁移失败"，写"数据存不下来、重启会丢，原因是……"。

## 三卡模型与渐进披露

每张卡产出两个产物：

- **产物 A · 第一屏**：对话中的简洁回复，是默认展示层和正式确认层。必须足以让人选择：确认 / 局部修正 / 查看明细 / 退回。
- **产物 B · 完整 Markdown 记录**：持久化文件，含第一屏快照 + 第二层明细 + 第三层证据/来源/假设/冲突/版本。即使用户不读也必须生成和维护。

第一层确认后直接进入下一阶段，不强迫用户读第二、三层；用户问某处时只展开对应小节，不倾倒整份记录。详见 [references/progressive-disclosure.md](references/progressive-disclosure.md)。

## 主流程

### Stage 0 · 接收

1. 原始输入逐字存入运行记录。
2. 识别问题、背景、目标、约束、期望产物、已有材料。
3. 区分用户明示要求与 AI 推断。
4. 任务卡批准前不开始正式执行（低风险且用户明确要求立即执行除外）。
5. 缺失信息有安全可逆默认值时，记默认值，不打扰用户；只升级影响方向、边界、核心模型或验收的缺失。

### Stage 1 · 任务卡 —— "做什么"

第一屏按模板 [templates/task-card-screen.md](templates/task-card-screen.md) 输出：一句话任务、目标、产物、范围、明确不做、核心模型初判、主要风险、≤3 个待确认、AI 建议动作。完整记录用 [templates/task-card-record.md](templates/task-card-record.md)。


**方向闸门 1**：用户可确认 / 局部修正 / 查看明细 / 退回 / 部分确认部分搁置。确认后标记 `confirmed`、记录批准版本、更新基线候选，进入 Stage 2。

### Stage 2 · 调研与方案设计【调研门 · 条件触发】

- **触发**：方案涉及"要不要用现成的东西"（开源项目、可比产品、行业标准、可复用组件）时，调研门**必开**，按 [references/research-gate.md](references/research-gate.md) 执行：搜索轨道拆解 → 信源分级 → 候选漏斗 → 深度对比 → 证据账本 → 复用六分类。
- **跳过**：纯自有材料梳理、文档写作、用户已指定实现、调研成本明显高于任务价值时可跳过，记录理由。
- 无论开门与否，产出都要区分：有来源的事实、跨源综合、AI 推断、建议、未解决冲突。
- 至少给出一个推荐方案；存在真实取舍时给备选。**不制造假选择**——只有一条可信路径时只给一条。
- 调研全文不进对话，沉淀到方案卡第三层。

### Stage 3 · 方案卡 —— "怎么做"

第一屏按 [templates/solution-card-screen.md](templates/solution-card-screen.md) 输出：一句话结论、推荐方案（含复用什么/自建什么）、执行抽象模型、预期成效、关键取舍、主要风险、≤3 个待决策、AI 建议选择。完整记录用 [templates/solution-card-record.md](templates/solution-card-record.md)。

每个高影响决策单独出决策卡（[templates/decision-card.md](templates/decision-card.md)）：改变目标/边界/核心模型/主流程/权限/数据定义、逆转成本高、来源冲突、不同选项结果差异大、有安全合规财务运营后果的决策才算高影响。低影响可逆决策用默认值并记录，不打扰用户。

**方向闸门 2**：确认后冻结执行边界，记录所选方案与取舍。

### Stage 3.5 · 验证门【条件触发】

方案批准 ≠ 可以承诺开发。按 [references/validation-gate.md](references/validation-gate.md) 执行：

- **触发**：调研证据账本中存在**承重灰项**（结论依赖未实跑验证的宣称）时必开。
- **轻档（默认）**：桌面评审——只读文档、issue、release，承重结论标灰存疑。
- **重档**：灰项承重且方案将被大量依赖时升级——clone → 安装启动 → 测关键工作流 → 做一次代表性修改测改造难度 → 工程与许可证风险检查。
- **结论五选一**：继续 / 有条件继续 / 组合其他组件 / 补针对性实验 / 否决回到 Stage 2。否决触发方向警报。
- 无运行环境时标"仅桌面评审"，运行时行为一律标灰，不把文档宣称当测试结果。
- 验证报告用 [templates/validation-report.md](templates/validation-report.md)，第一屏只给结论 + 红绿灯 + 待拍板项。

### Stage 4 · 执行打包与正式执行

**执行打包【按需触发】**，按 [references/delivery-package.md](references/delivery-package.md)：

- 当前会话 AI 续作（上下文在手）：**轻档**——在方案卡完整记录里内嵌一节"执行边界清单"（不做什么、验收标准、停点），不单独成文。
- 派工给其他 Agent / 工具 / 人，或跨会话执行：**重档**——完整开发任务包（PKG-###，[templates/dev-task-package.md](templates/dev-task-package.md)），这是唯一的上下文传递载体。
- 第一阶段只做一条能跑通的端到端闭环，砍掉吸引人但非必要的功能。

**正式执行**：处理全量相关信息；维护 来源 → 事实 → 决策 → 产出 的追溯链；细节留在完整记录；偏离已批准方案立即记录；低风险实现细节用默认值并记录；高影响例外出决策卡或方向警报。不声称存储思维链，存结构化产物：证据、假设、对比、检查、决策、简要理由。

### Stage 5 · 自检

交付结果卡前按 [references/self-check-and-drift.md](references/self-check-and-drift.md) 做五维自检：方向一致性、完整性、证据可追溯、场景可跑通、跨产物一致性。

触碰方向漂移触发器（核心用户/核心业务对象/主流程变化、一级模块增删、范围大幅扩张、关键权限边界变化、重要验收标准失效、核心来源冲突无法调和、>3 个高影响假设悬而未决、代表性核心案例跑不通）→ 停止该分支，发方向警报：已批准方向 / 检测到的变化 / 出现原因 / 下游影响 / AI 建议 / 需要人决定什么。

### Stage 6 · 结果卡 —— "做成了什么，能验收吗"

第一屏按 [templates/result-card-screen.md](templates/result-card-screen.md) 输出：一句话结果、整体完成情况、核心成果、与已确认方案的差异、未完成事项、主要风险或缺口、≤3 个验收决策、AI 建议动作。完整记录用 [templates/result-card-record.md](templates/result-card-record.md)。

验证证据确定性优先：schema 与确定性断言 → 单测/集成/构建 → 黄金用例与回归 → 来源核验 → LLM 评审（无法确定性检查的部分）→ 人对黄/红项的审阅。跑不了的检查标灰并说明原因。

### Stage 7 · 验收与基线

用户验收后：把已接受的事实、边界、模型、决策、产出、已知风险、搁置项记入基线（[templates/baseline.md](templates/baseline.md)）；关联三张卡与决策卡；赋基线版本号（BASE-###）。已验收基线不得悄悄改写。

### Stage 8 · 后续轮次 delta-only

后续所有迭代：与最新基线对比，只展示新增/修改/删除/影响/风险/待确认（[templates/change-summary.md](templates/change-summary.md)）；不要求重审未变内容；只更新受影响产物；对已验收场景和决策跑回归。用户口语反馈自动编译成结构化变更单（现状/问题/期望/约束/影响面/验收标准/回归检查/风险等级），接入本循环，不让用户把反馈重写成正式 prompt。详见 [references/baseline-and-delta.md](references/baseline-and-delta.md)。

## 升级矩阵

| 影响 | 不确定性 | 默认处理 |
|---|---|---|
| 高 | 高 | 必须人决策 |
| 高 | 低 | 人简要确认 |
| 低 | 高 | AI 选可逆默认值并记录 |
| 低 | 低 | AI 直接执行 |

法律、财务、运营、安全敏感的决策无论矩阵结果一律升级。

## 用户响应协议

每个闸门支持四种回复：

- `确认` — 批准当前第一屏
- `局部修正：...` — 只改指定项
- `查看明细：...` — 只展开被点名的第二/三层小节
- `退回：...` — 作废当前卡并重建

用户确认后：不重发整卡，简述确认项，保存确认版本，进入下一阶段。

## 运行产物目录

```text
runs/<run-id>/
├── 00-intake/original-request.md
├── 01-task-card/{task-card-screen.md, task-card-record.md}
├── 02-research/research-report.md            # 调研门开启时
├── 02-solution-card/{solution-card-screen.md, solution-card-record.md, decision-cards.md}
├── 03-validation/validation-report.md        # 验证门开启时
├── 04-execution/{dev-task-package.md, artifact-index.md, work-products/}
├── 05-result-card/{result-card-screen.md, result-card-record.md}
├── 06-governance/{source-index.md, assumption-log.md, baseline.md, changes.md}
└── 07-validation/final-validation-report.md
```

用 `scripts/new_run.py --name "<任务名>" --out ./runs` 初始化；用 `scripts/validate_run.py ./runs/<run-id>` 校验一次运行的产物。

## 标识符与状态

稳定 ID：`TASK-###`、`SOL-###`、`RESULT-###`、`DEC-###`、`SRC-###`、`ASM-###`、`CONFLICT-###`、`BASE-###`、`CHANGE-###`、`CASE-###`、`VAL-###`（验证项）、`PKG-###`（任务包）。

状态：`draft` → `awaiting-confirmation` → `confirmed` →（`validating` → `validated`）→ `executing` → `accepted` → `baselined`；异常态：`at-risk`、`needs-revision`、`superseded`。

## 质量规则

- 结论先行；人决策先于细节；细节先于证据堆砌。
- 区分事实、推断、建议、冲突、未知。
- 不用编造的置信度百分比当信任信号；用证据、冲突状态、场景结果、可逆性说话。
- 不把所有 AI 产出当成人的必读内容；不把实质风险藏进附录。
- 不悄悄改变已确认方向；后续轮次不重发未变内容。
- 已承诺产物缺失时，不许说任务完成。

## 参考文件索引

按需读取，不要一次全载：

- [references/workflow-and-artifacts.md](references/workflow-and-artifacts.md) — 三卡与产物的完整规范
- [references/progressive-disclosure.md](references/progressive-disclosure.md) — 三层披露与提升规则细则
- [references/human-review-and-decisions.md](references/human-review-and-decisions.md) — 审阅预算、决策卡、升级矩阵细则
- [references/self-check-and-drift.md](references/self-check-and-drift.md) — 五维自检与方向漂移处理
- [references/baseline-and-delta.md](references/baseline-and-delta.md) — 基线与 delta-only 审阅细则
- [references/research-gate.md](references/research-gate.md) — 调研门：触发条件、搜索轨道、候选漏斗、证据账本、复用六分类
- [references/validation-gate.md](references/validation-gate.md) — 验证门：轻重两档、可证伪问题、代表性修改、五选一结论
- [references/delivery-package.md](references/delivery-package.md) — 执行打包：两档形态、任务包七问、验证清单、反馈编译
