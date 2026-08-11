# Evaluation and Regression Protocol

## Goal

Turn quality review from ad-hoc reading into repeatable checks that can run after every meaningful change.

## Evaluation order

1. **Deterministic assertions** — required fields, JSON/schema validity, exact strings, counts, URLs, file existence.
2. **Program tests** — unit, integration, build, smoke, persistence, permission, and regression tests.
3. **Golden cases** — representative inputs with expected properties or outcomes.
4. **Evidence checks** — source freshness, citation support, claim-to-evidence mapping.
5. **Model-based evaluation** — rubric-based judgment only for qualities that cannot be checked deterministically.
6. **Human approval** — yellow/red decisions and subjective product trade-offs.

## Golden cases

Maintain a small, diverse set of real examples:

- normal case
- edge case
- ambiguous input
- missing-information case
- high-risk or approval-required case
- known prior failure

Each case records:

- input
- expected phase
- required artifact
- deterministic assertions
- rubric criteria
- expected risk grade
- unacceptable behavior

Use [../assets/golden-eval-cases.md](../assets/golden-eval-cases.md).

## Evaluation of research outputs

Check:

- finalists were actually quick-read (README, docs, code structure, license, issues), not link dumping
- 1–2 presented directions, no filler options
- official sources for critical claims
- current maintenance date
- license verified
- facts vs inference vs runtime evidence separated
- recommendation names reuse/modify/build boundaries
- spike questions are falsifiable and time-boxed

## Evaluation of option cards

Check:

- one-sentence conclusion is consistent with evidence
- each option states reused foundation, self-built scope, and evidence basis
- each option line has a choose-it-if condition and risk light
- all yellow/red/gray items are surfaced
- no critical detail appears only in the files
- the human question is bounded and answerable
- detailed artifact locations are provided for follow-up expansion

## Model judge rules

- use a clear rubric and source material
- require reasons and cited evidence
- avoid asking the same model/context to be the sole judge of its own work
- compare against deterministic results
- treat model scores as signals, not truth

## Regression gate

A change may pass only when:

- critical deterministic checks pass
- no red-risk case regresses
- golden cases meet their thresholds
- new known failure becomes a regression case
- untested items are explicit
