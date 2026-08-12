# 任务卡｜第一屏

<!-- 叙事约束：先总概后拆分；按用户关注点排序，不按 AI 工作顺序；技术用语不上第一屏，必须出现时先翻译成业务语言 -->

> 任务ID：{{TASK_ID}}  
> 状态：awaiting-confirmation  
> 版本：{{VERSION}}

## 建议执行模型（可选，非 gate，可跳过）

<!-- 按任务能力缺口给一句匹配建议：调研/聚合型 → 联网检索强的模型；视觉/出图型 → 图像能力模型；代码验证/执行型 → 代码能力模型；默认 → 当前模型不切换。用户可在确认时一并决定（如「确认任务卡，用 XX 模型」）或直接忽略本节。切换执行者后应先读 workflow-state 再继续，避免上下文断裂。 -->

{{SUGGESTED_RUNNER_MODEL_OR_SKIP}}

## 一句话任务

{{ONE_SENTENCE_TASK}}

## 目标

{{GOAL}}

## 本轮产物

{{DELIVERABLES}}

## 本轮范围

{{IN_SCOPE}}

## 明确不做

{{NON_GOALS}}

## 核心模型初步判断

{{CORE_MODEL}}

## 主要风险或限制

{{MAIN_RISKS_MAX_3}}

## 需要你确认

{{CONFIRMATIONS_MAX_3}}

## AI建议动作

{{RECOMMENDED_ACTION}}
