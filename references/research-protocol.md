# Research Protocol

## Goal

Find practical existing solutions before inventing a new one, decide what to reuse, modify, combine, or build — and keep the user's reading burden near zero.

## 1. Translate the task into search dimensions

Extract:

- problem domain and target users
- core workflow and must-have capabilities
- technical and deployment constraints
- privacy, compliance, scale, and commercial-use needs
- expected output and decision to support

Create several search tracks rather than one long query.

## 2. Source hierarchy

Prefer evidence in this order:

1. official repository and official documentation
2. releases, source code, issues, and pull requests
3. maintainers' technical posts or demos
4. reputable independent analysis
5. community discussion as supplementary evidence

Do not use a generated summary as the sole basis for a decision.

## 3. Candidate funnel

### Broad discovery

Collect enough candidates to understand the solution space. Do not present this raw list to the user.

### Hard-filter screen

Reject candidates with critical mismatches such as:

- wrong problem or architecture
- incompatible license
- unavailable source or documentation
- no plausible extension path
- unacceptable privacy or deployment model

### Quick reading of finalists (≤3)

For each finalist, actually read — do not skim titles:

- README and official docs
- code structure and extension points
- license file
- recent releases/commits and critical open issues
- date of the maintenance check

README claims alone are not evidence of capability; distinguish documented, inspected, and runtime-tested behavior.

**Never manufacture candidates to hit a quota.** If one direction clearly satisfies all hard constraints, record why additional alternatives would not change the decision.

## 4. Comparison dimensions

| Dimension | Questions |
|---|---|
| Functional fit | Which requirements exist now? Which are missing? |
| Technical fit | Does the stack fit the current system and team? |
| Architecture | Can required features be added without fighting the design? |
| Maintenance | Recent commits/releases and critical unresolved issues? |
| Documentation | Can a new developer install and extend it? |
| License | Modification, redistribution, SaaS, attribution, copyleft obligations? |
| Integration | APIs, data model, authentication, build system, plugin system? |
| Deployment | Local/cloud/container, dependencies, resource burden? |
| Security/privacy | Telemetry, external services, known vulnerabilities, data exposure? |
| Modification cost | Adaptation, rewrite, or hidden coupling? |
| Exit cost | Can data and custom code migrate later? |

## 5. Evidence ledger

For each load-bearing claim record:

- claim
- source and date
- evidence type: documentation, code inspection, issue/release, or runtime test
- confidence
- whether the claim is fact, inference, or assumption

Missing evidence is gray, not a negative fact and not a verified capability.

## 6. Reuse classification

Assign exactly one primary strategy per candidate:

- **Use directly**
- **Fork and modify**
- **Extract component**
- **Combine**
- **Reference only**
- **Reject**

## 7. Scoring

Use a 1–5 scale only as a decision aid. Never let a total score hide a critical failure.

Suggested weights:

- functional fit: 25%
- modification cost: 20%
- technical fit: 15%
- maintenance: 15%
- license: 10%
- documentation: 5%
- security/privacy: 5%
- exit cost: 5%

A critical license, security, privacy, or architecture failure overrides the score.

## 8. Output

Write the full report with [../assets/research-report-template.md](../assets/research-report-template.md) into the task workspace (default `99_workspace/rftc/<任务名>/`), then compress into the option card via the review gate.

The recommendation must state:

- preferred candidate or composition
- exact parts to reuse, modify, and build
- why alternatives were rejected
- assumptions that still need testing (these become the validation spike)
- risk grade and the single human decision required

What reaches the user is the option card, not this report.

## 9. Integrity rules

- Cite important claims.
- State the date of maintenance checks.
- Distinguish repository claims from inspected or runtime-verified behavior.
- Never say "supports X" when only a roadmap or issue mentions X.
- When internet access is unavailable, label output as a search plan or desk review.
- Candidates with unclear licenses (NOASSERTION) may inform concepts only; do not copy their text or code.
