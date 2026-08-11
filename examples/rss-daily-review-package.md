# 示例：RSS 日报生成器方案卡 — Gate B

> 这是调研完成、快速阅读入围项目之后展示给用户的决策卡。完整报告与证据已写入文件。

- Review-package version: RP-1
- Displayed in: [conversation message reference]

## 1. 概要结论

**推荐：方案 A** —— 本地脚本 + 成熟 RSS 解析库 + Markdown 模板输出，先跑通日报核心闭环。

理由：不引入托管平台，数据本地可回滚；解析库已快速阅读确认维护中且 API 覆盖去重需求。

## 2. 方案目录

| 方案 | 一句话定位 | 复用 / 自研 | 选它如果… | 风险灯 |
|---|---|---|---|---|
| A（推荐） | 本地脚本 + RSS 解析库 | 复用：feedparser 式解析库（MIT，近半年有 release）；自研：模板渲染与源配置（约百行） | 你在意数据不出本机、输出可审阅 | 🟡 本地形态需确认 |
| B | 托管自动化平台 | 复用：平台 RSS 触发器 + 动作编排；自研：仅配置 | 你不想维护任何脚本 | 🔴 自动外发需单独批准 |

依据：两个候选均已快速阅读官方文档与仓库（维护状态、license、issue），详见文件。

## 3. 需要你决定的

是否接受本地方案意味着日报生成要由你手动或本机定时触发？

请选择：`方案 A（RP-1）` / `方案 B（RP-1）` / `退回调研`

## 4. 风险灯

- Red：方案 B 的自动外发动作；方案 A 无红灯。
- Gray：3 个目标 RSS 源的实际可抓取性与抓取时长未本机验证——已列入计划首个验证 spike（30 分钟熔断）。

## 5. 详细材料

追问任一方案时从以下文件展开，不现编：

- 完整调研报告：`99_workspace/rftc/rss-daily/research-report.md`
- 证据账本：`99_workspace/rftc/rss-daily/evidence-ledger.md`
- 决策记录：`99_workspace/rftc/rss-daily/decision-log.md`

## 6. Gate B status

- Status: Decision pending for RP-1
- Next allowed action: Wait for a post-display explicit selection or delegated choice for RP-1
- Red-action note: 自动外发即使随方案 B 被选中，执行前仍需单独显式批准

Any material research or package revision creates RP-(N+1), invalidates the selection for RP-N, and keeps Gate B pending until a new post-display selection or delegation is recorded.
