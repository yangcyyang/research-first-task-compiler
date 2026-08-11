# Review Gate Protocol

## Goal

Reduce human review load without hiding important uncertainty. Transform research output into a one-screen option card the user can decide from without follow-up reading.

## 1. Producer self-check (always)

The producer must verify:

- alignment with the latest task card
- every option states reused foundation, self-built scope, and evidence basis
- 1–2 genuine directions; no filler options
- separation of facts, inference, assumptions, and runtime verification
- contradictions, duplicated claims, and missing alternatives
- scope expansion
- known risks and untested items

## 2. Independent reviewer (risk-triggered, not default)

Trigger an independent reviewer (different agent, model, or isolated context) only when:

- any Red direction is presented
- the decision is high-cost or hard to reverse
- producer evidence conflicts or confidence is low

Give the reviewer:

- task card and acceptance criteria
- producer artifact
- evidence ledger or cited sources
- risk policy

Do not give the reviewer the producer's hidden reasoning or instruct it to defend the recommendation.

The reviewer answers only:

1. Did the producer solve the requested problem?
2. Which claims are strongly supported?
3. Which claims are unsupported, overstated, contradictory, or stale?
4. What important alternatives or edge cases were missed?
5. What are the top risks and their grades?
6. What requires human decision?
7. Accept, accept with conditions, revise, or reject?

The reviewer should not generate a second full report unless the first is unusable.

## 3. Deterministic checks first

Before using an LLM reviewer, run available objective checks:

- required fields and schema validation
- URL and repository existence
- date/version consistency
- license file presence
- duplicate and broken-reference detection

LLM review should focus on judgment that cannot be checked mechanically.

## 4. Option card

Use [../assets/review-package-template.md](../assets/review-package-template.md).

The card carries only: 概要结论, 方案目录（一行一个方案）, 需要你决定的, 风险灯, 详细材料位置. Detailed output remains in files and is the source for any follow-up expansion — never improvise expansions.

## 5. Reviewer integrity rules

- Treat unavailable evidence as gray, not green.
- Do not infer runtime success from documentation.
- Do not use a numeric score to override a critical failure.
- State disagreements between producer and reviewer.
- When reviewer confidence is low, request a targeted check rather than more prose.
