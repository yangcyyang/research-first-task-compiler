# Validation Spike Protocol

## Goal

A validation spike is the **first task of the execution plan**, not a separate phase before the user chooses a direction. Its purpose is to falsify the chosen direction quickly and cheaply — not to prove completeness.

## Hard rules

1. **30-minute timebox with circuit breaker.** If the spike is not conclusive within the timebox, stop: mark the result gray, record exactly what was tried and where it blocked, and report. Never keep grinding.
2. **Cheapest falsifiable check first.** Order: license → install → core workflow → one representative modification. Most candidates fail early and cheaply; stop as soon as the decision is informed. The representative-modification step may be skipped when install + core flow already answer the question.
3. **Time cost is agent-side.** The spike runs in the background of execution; the user only sees its conclusion.
4. **Outcome routing:**
   - Pass → continue the plan.
   - Fail a critical assumption → this is a material change: return to research, issue a new RP version, Gate B re-opens.
   - Gray/inconclusive → record in the validation report; gray never counts as passed.

## 1. Define falsifiable questions

Turn the decision into 2–5 questions that can fail clearly.

Examples:

- Can the project start in the target environment?
- Can the component be embedded without replacing the current architecture?
- Does the license permit the intended distribution or commercial use?

## 2. Prepare the environment

Record OS, runtime, package manager, repository commit/release, installation commands, environment variables, external services, and resource constraints. Do not expose secrets.

## 3. Run the baseline

- obtain official source
- follow documented installation first
- record deviations
- start the application or demo
- capture useful logs or screenshots

## 4. Test the critical workflow

For each test record setup, action, expected result, actual result, evidence, and status.

Statuses:

- Passed
- Partially passed
- Failed
- Not tested

## 5. Inspect engineering risks

- architecture and extension points
- dependency and build health
- data storage and migration
- telemetry/external calls
- license obligations
- unresolved critical issues

## 6. Report

Use [../assets/validation-report-template.md](../assets/validation-report-template.md). Conclude one of: Continue / Continue with conditions / Run an additional focused experiment / Reject and return to research. Raw logs remain supporting evidence, never the primary output.

## 7. No-runtime fallback

When execution tools are unavailable:

- label the report "desk review only"
- list exact commands and expected evidence for a future run
- mark runtime behaviors Not tested and gray
- do not present documentation claims as test results
