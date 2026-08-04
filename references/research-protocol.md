# Research Protocol

## Goal

Find practical existing solutions before inventing a new one, then decide what to reuse, modify, combine, or build.

## 1. Translate the task into search dimensions

Extract:

- problem domain and target users
- core workflow and must-have capabilities
- technical and deployment constraints
- privacy, compliance, scale, and commercial-use needs
- expected output and decision to support

Create several search tracks rather than one long query.

Example for an image and prompt management system:

1. complete prompt management applications
2. digital asset management systems
3. infinite canvas and node editor components
4. local-first databases and file indexing
5. visual knowledge management tools

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

### Finalists

Deeply compare 3–5 serious candidates. Record why excluded candidates were filtered, but do not write a full essay for each.

## 4. Deep comparison dimensions

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

Use [../assets/research-report-template.md](../assets/research-report-template.md), then pass it through the review gate.

The recommendation must state:

- preferred candidate or composition
- exact parts to reuse, modify, and build
- why alternatives were rejected
- assumptions that still need testing
- minimum validation experiment
- risk grade and human decision required

## 9. Integrity rules

- Cite important claims.
- State the date of maintenance checks.
- Distinguish repository claims from inspected or runtime-verified behavior.
- Never say “supports X” when only a roadmap or issue mentions X.
- When internet access is unavailable, label output as a search plan or desk review.
