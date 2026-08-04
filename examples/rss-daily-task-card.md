# 示例：RSS 日报生成器任务卡 — Gate A

> 这是用户在对话中首先看到的完整卡片。此时不开始调研。

- Task-card version: TC-1
- Displayed in: [conversation message reference]

## 1. Problem

团队每天需要从多个 RSS 源提炼行业动态，当前靠人工打开网页，耗时且容易遗漏。

## 2. Desired outcome

工作日 9:00 前生成一份可追溯来源的中文 AI 行业日报草稿，供编辑审核后发布。

## 3. Users and scenarios

- Primary user: 内容编辑
- Core scenario: 早晨查看前一天至当前的高信号 AI 新闻并快速定稿
- Frequency: 每个工作日一次

## 4. Existing foundation

- Current product/project: 现有 Obsidian 知识库
- Available files/data/code: RSS 源清单与日报 Markdown 样例
- Existing constraints: 不自动外发；保留每条来源链接

## 5. Must-have capabilities

1. 拉取并去重 RSS 条目
2. 依据来源生成带链接的中文摘要
3. 输出可人工编辑的 Markdown 草稿

## 6. Out of scope

- 自动发布到公众号或邮件
- 付费新闻源接入

## 7. Constraints

- Technical: 可在现有 macOS 自动化环境运行
- Time/cost: 单次处理在 10 分钟内完成
- Privacy/security: 不发送私有笔记内容给外部服务
- License/commercial use: 仅使用允许聚合与摘要的公开源

## 8. Deliverables

- 可复用的第一阶段方案与一份示例日报

## 9. Acceptance signals

- 一次运行产生包含至少 5 条来源链接的 Markdown 草稿

## 10. Assumptions

- 已有 RSS 源可公开访问

## 11. Unresolved decisions

- 摘要模型与运行成本上限

## 12. Initial risk profile

- Green: 本地生成 Markdown 草稿
- Yellow: 选择托管服务或模型供应商
- Red: 自动对外发布
- Gray: RSS 源稳定性尚未验证

## 13. Current phase and next gate

- Current phase: Gate A — task-card confirmation pending
- Next action: Wait for `确认任务卡 TC-1` / `修改：…` / `补充：…`
- Approval owner: User

## 14. Gate A response

请回复：`确认任务卡 TC-1` / `修改：…` / `补充：…`。修改或补充会使 TC-1 失效，并展示 TC-2。
