# Review Gate Protocol

## Goal

Reduce human review load without hiding important uncertainty. Transform large agent outputs into a small, evidence-backed decision surface.

## 1. Producer self-check

The producer must verify:

- alignment with the latest task card
- required sections and deliverables
- source and evidence completeness
- separation of facts, inference, assumptions, and runtime verification
- contradictions, duplicated claims, and missing alternatives
- scope expansion
- known risks and untested items

Self-check is necessary but is not independent validation.

## 2. Independent reviewer

Use a different agent, model, or isolated context when available. Give the reviewer:

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
- calculations and table totals
- license file presence
- build, lint, type, unit, integration, and smoke tests
- duplicate and broken-reference detection

LLM review should focus on judgment that cannot be checked mechanically.

## 4. Evidence sampling

For large repetitive outputs:

- verify all red-risk items
- verify all yellow decision items
- sample green items according to task risk
- increase sample size when errors are found

Suggested starting sample:

- low-risk repetitive work: 5–10%
- medium-risk work: key items plus 20%
- high-risk or irreversible work: 100%

Sampling is not appropriate for architecture decisions, security boundaries, destructive actions, contracts, or production migrations.

## 5. Review package

Use [../assets/review-package-template.md](../assets/review-package-template.md).

Keep the decision surface short. Detailed output remains accessible but is not the default reading path.

## 6. Reviewer integrity rules

- Treat unavailable evidence as gray, not green.
- Do not infer runtime success from documentation.
- Do not use a numeric score to override a critical failure.
- State disagreements between producer and reviewer.
- When reviewer confidence is low, request a targeted test rather than more prose.
