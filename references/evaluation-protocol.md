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

- 3–5 serious candidates, not link dumping
- official sources for critical claims
- current maintenance date
- license verified
- facts vs inference vs runtime evidence separated
- recommendation names reuse/modify/build boundaries
- minimum validation questions are falsifiable

## Evaluation of review packages

Check:

- one-sentence conclusion is consistent with evidence
- all yellow/red/gray items are surfaced
- no critical detail appears only in an appendix
- human questions are bounded and answerable
- detailed artifact location is provided

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
