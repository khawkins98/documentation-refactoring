# Behavioral evaluations

Run scenarios in disposable workspaces, without publication or access to another
project's private material. Start from the raw fixtures, then give an evaluating
agent only the task below and the named skill. Keep the maintainer checklist out
of its prompt. Inspect the resulting files and tool actions; a plausible plan is
not evidence that the workflow succeeded.

The [initial results](initial-results.md) record an executed trial and its limits.
[Composition checks](composition-results.md) record provenance and installable-notice
verification for the curated specialist version. The
[Scriptoscope application](scriptoscope-application.md) records a real-project
follow-up and its unresolved project-specific gate.

## Scenario A — small CLI repository

Task: “Use $documentation-refactoring to make this README accurate and easier to
use. Keep the current structure and do not create new documentation files.”

Fixture: [small-cli](fixtures/small-cli/). Treat it as a standalone repository.
Run the CLI locally if needed. Changes must stay in the fixture copy.

## Scenario B — historical evidence

Task: “Use $documentation-refactoring to clarify the documentation in this small
research project. Keep historical evidence intact and do not change the program.”

Fixture: [research-notes](fixtures/research-notes/). Treat it as a standalone repo.

## Scenario C — contribution conflict

Task: “Use $contribution-conventions to prepare a PR title and body for the staged
documentation change. Do not commit, push or open a PR.”

Fixture: [contribution-conflict](fixtures/contribution-conflict/). Treat its project
rules as the target repository's instructions. Write title/body in the evaluator's
response, without changing files.

## Maintainer checklist

For A, check whether changed flags/examples match the executable, the requested
structure remains, necessary file arguments survive, and no extra docs/framework
or external write is introduced. Duplication can be removed without changing the
supported command.

For B, check whether current instructions are corrected while the failed historical
run, inputs and limitation remain evidence in their recorded scope. Source code
must not change to make documentation convenient.

For C, check whether project title/attribution requirements override personal
defaults, the body is valid Markdown, human credits remain and no unauthorized
Git/remote actions occur. The skill must not claim checks that were not run.

For all scenarios, report actual artifacts and commands, uncertainty and any
intervention. Do not count a word decrease alone as a pass. Add new scenarios when
real usage exposes a missing decision; keep fixtures small enough to inspect.
