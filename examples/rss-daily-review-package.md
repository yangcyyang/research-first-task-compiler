# 示例：RSS 日报生成器审阅包 — Gate B

> 这是调研与自检完成后、任何验证或开发之前展示给用户的决策包。

- Review-package version: RP-1
- Displayed in: [conversation message reference]

## 1. One-sentence conclusion

推荐先采用本地 RSS 拉取 + Markdown 模板的轻量方案（方案 B），以最低集成成本验证日报核心闭环。

## 2. Decision summary

| Item | Conclusion |
|---|---|
| Recommended direction | 方案 B：本地脚本 + RSS 解析 + Markdown 输出 |
| Reuse strategy | 提取成熟 RSS 解析库，沿用现有日报 Markdown 结构 |
| Strongest reason | 不引入托管平台，输出可审阅、可回滚 |
| Main risk | RSS 源质量与稳定性尚未运行验证 |
| Next allowed action | Wait for post-display Gate B selection for RP-1 |

## 3. Key evidence

| Claim | Evidence | Evidence type | Confidence |
|---|---|---|---|
| 本地脚本可避免自动外发 | 输出仅写入 Markdown 文件 | Inspected | High |
| RSS 解析库可支持去重 | 已找到维护中的解析库与文档 | Sourced | Medium |
| 目标源可稳定读取 | 尚未在本机运行 | Not tested | Low |

## 4. Risk lights

### Red — explicit approval required

- 自动发布到外部渠道不在本阶段范围内。

### Yellow — decision required

- 是否接受方案 B 的本地脚本形态，而非托管工作流？

### Gray — not verified

- 目标 RSS 源稳定性与实际抓取时长。

### Green — may proceed after Gate B

- 在本地创建 Markdown 草稿。

## 5. Decision required from the human

请选择：`方案 A（RP-1，托管自动化）` / `方案 B（RP-1，本地脚本，推荐）` / `方案 C（RP-1，仅人工流程）` / `退回调研`。

## 6. Reviewer verdict

- Verdict: Accept with conditions
- Reviewer concerns: 先验证 3 个目标 RSS 源可抓取，再进入开发包。
- Required corrections: 无。

## 7. Detailed artifacts

- Full research/report: `research-report.md`
- Evidence ledger: `evidence-ledger.md`
- Validation logs: 尚未生成（Gate B 未通过）
- Decision record: `decision-log.md`

## 8. Gate B status

- Status: Decision pending
- Next allowed action: Wait for a post-display explicit selection or delegated choice for RP-1
- Red-action note: 任何自动外发仍需单独明确批准
