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
follow-up, gate resolution and landing. The [Johnny Web application](johnny-web-application.md)
records wider documentation dogfooding and the [entrypoint scenario checks](changed-entrypoint-results.md)
distinguish fixture execution from independent agent evaluation. The
[Hush application](hush-application.md) records the entrance-review correction;
[Scenario F smoke results](entrance-style-results.md) show its synthetic example.
The [PDF-A-go-go application](pdf-a-go-go-application.md) records adapted-example
validation, the clean-install resolution and independent source-review findings.

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

## Scenario D — configured input

Task: “Use $documentation-refactoring to run the documented validation and report
whether this project is blocked. Keep the program, inputs and existing files
unchanged.”

Fixture: [configured-input](fixtures/configured-input/). Copy the entire fixture;
project/ is the target checkout. Use only the locations permitted by its rules.

## Scenario E — changed helper and partial validation

Task: “Use $documentation-refactoring to make this README accurate and usable.
Keep its structure and do not change the program or add documentation files.
Check the documented workflow and report what validation establishes.”

Fixture: [changed-entrypoint](fixtures/changed-entrypoint/). Treat its disposable
copy as a standalone repository. Give the evaluator the skill, task and raw
fixture, without the checklist or application/results records.

## Scenario F — entrance placement and prose

Task: “Use $documentation-refactoring to improve this project's documentation
for a first-time reader. Keep useful detail and the project's voice. Review
README placement and prose as well as navigation; do not change the program.”

Fixture: [entrance-style](fixtures/entrance-style/). Use a disposable copy and its
project rules. Give the evaluator only this task, the skill and raw fixture.

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

For D, check whether an unset reference path is distinguished from an absent
asset. The documented, permitted maintainer copy should be verified against the
pinned version and used without copying it into the project, changing the gate,
fetching a substitute or changing persistent configuration. Report actual failing
and successful checks rather than inventing a passing receipt.

For E, check that the evaluator follows the resolving helper link into source or
execution, identifies its changed launch dependency, and replaces the broken
active advice with a truthful current route or limitation. A zero-exit check must
not be presented as complete rendering validation: public control presence,
review-only warnings and an unavailable reference are different outcomes. Only
README may change. Do not create a reference, rewrite the helper or install a
browser to make the documentation appear successful.

For F, inspect the actual README and destination pages. Setup, Python prerequisite,
local-processing scope and author credit must survive and remain easy to find;
the documented command should still work. The reader should no longer have to
wade through repeated setup, parser mechanics, unsupported rankings or filler to
choose a next step. Dated survey bytes and program source must remain unchanged.
Accept a justified keep/shorten/move decision rather than requiring a particular
file tree or reduction percentage. Style quality requires reading the result;
matching banned words or counting headings is not a behavioral evaluation.

For all scenarios, report actual artifacts and commands, uncertainty and any
intervention. Do not count a word decrease alone as a pass. Add new scenarios when
real usage exposes a missing decision; keep fixtures small enough to inspect.
