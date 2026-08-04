# Minimum Validation Protocol

## Goal

Use the smallest practical experiment to determine whether a selected project or component is viable before committing to full implementation.

## 1. Define falsifiable questions

Turn the decision into 2–5 questions that can fail clearly.

Examples:

- Can the project start in the target environment?
- Can an image node store custom prompt metadata?
- Can canvas state persist locally and restore correctly?
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

## 5. Make one representative modification

A project that runs may still be difficult to extend. Make one small change similar to intended work, such as adding a field, component, node type, persistence connection, or API.

Record touched modules, complexity, coupling, and test burden.

## 6. Inspect engineering risks

- architecture and extension points
- dependency and build health
- data storage and migration
- authentication and permissions
- telemetry/external calls
- license obligations
- unresolved critical issues

## 7. Decision and review

Conclude one of:

- Continue
- Continue with conditions
- Combine with another component
- Run an additional focused experiment
- Reject and return to research

Then generate a review package. Raw logs remain supporting evidence, not the primary output.

## 8. No-runtime fallback

When execution tools are unavailable:

- label report “desk review only”
- list exact commands and expected evidence for a future run
- mark runtime behaviors Not tested and gray
- do not present documentation claims as test results
