# Behavioral evaluations

Run scenarios in disposable workspaces, without publication or access to another
project's private material. Start from the raw fixtures, then give an evaluating
agent only the task below and the named skill. Keep the maintainer checklist out
of its prompt. Inspect the resulting files and tool actions; a plausible plan is
not evidence that the workflow succeeded.

Execution records state their inputs, interventions and validation limits:

| Record | Evidence |
| --- | --- |
| [Initial results](initial-results.md) | Independent scoped skill trials |
| [Composition checks](composition-results.md) | Provenance and installable notices |
| [Scriptoscope application](scriptoscope-application.md) | Real-project trial, gate resolution and landing |
| [Johnny Web application](johnny-web-application.md) | Repository-wide dogfooding and semantic helper failures |
| [Entrypoint scenario](changed-entrypoint-results.md) | Maintainer fixture execution and partial validation |
| [Hush application](hush-application.md) · [Entrance/style scenario](entrance-style-results.md) | Entrance-review correction and maintainer smoke example |
| [PDF-A-go-go application](pdf-a-go-go-application.md) | Adapted examples, clean-install resolution and independent source review |
| [Pinment application](pinment-application.md) | Recipient/fallback review, bounded independent skill exercise and local browser checks |
| [SVGOMG-Font comparison](svgomg-font-comparison.md) | Same-baseline trials, revised-skill fresh rerun and landing; placement and validation tradeoffs |
| [Editorial review and method research](editorial-review-2026-11-06.md) | Informed Astra/source reviews, narrow navigation addition and fresh Scenario F execution |
| [Change-aware method follow-up](change-aware-research-2026-11-06.md) | Deeper LangChain/Next.js source review, mapping drift and maintainer smoke exercise |
| [Change-driven applications](change-driven-applications.md) | Real feature-diff trial, proposal-authority correction, fresh Scenario G and Johnny Web repeat |
| [Compact prose pass](prose-style-results.md) | Fresh Scenario H execution, literal preservation and maintainer PR self-review |
| [Selection and quick start](selection-and-quick-start.md) | Unnamed-skill host selection checks and an executed one-off CLI trial |
| [Foveacast application](foveacast-application.md) | Fresh real-project application, parent source review and supported-alternative check |
| [Elements of Style trials](elements-of-style-trials.md) | Draft-skill applications to Pinment and Blocklate, with preserved constraints and verification limits |

## Skill selection

Scenarios A–H explicitly name their skill; they test execution after selection.
Before widening a description, also try ordinary requests without skill names
in a host with both skills available. Include a nearby unrelated task and inspect
which skill files the agent actually reads. The [initial selection checks](selection-and-quick-start.md)
record exact requests, setup, observations and limits.

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

## Scenario G — prototype behavior and programme requirements

Task: “Use $documentation-refactoring to update documentation affected by the
feature in feature.patch. Keep the program unchanged.”

Fixture: [prototype-authority](fixtures/prototype-authority/). Use a disposable
copy and its project rules. Give the evaluator only this task, the skill and raw
fixture, without the checklist, prior application records or intended edits.

## Scenario H — natural prose and punctuation

Task: “Use $documentation-refactoring to edit this README for clear,
natural prose while preserving its facts and the writer's voice.”

Fixture: [prose-style](fixtures/prose-style/). Use a disposable copy and its project
rules. Give the evaluator only the task, skill and raw fixture, without the
checklist or expected edits.

## Scenario I — supported alternatives

Task: “Use $documentation-refactoring to review this README for stale instructions
and reader-facing defects. Keep its structure and make only necessary corrections;
do not change the program.”

Fixture: [supported-alternative](fixtures/supported-alternative/). Give the evaluator
only the task, skill and raw disposable fixture, without the checklist or prior
findings.

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

For G, check that the README describes the opt-in URL preview accurately and
does not claim an actual download. The original programme criteria, pending
approval and open question must survive. A dated implementation note may explain
the alternative without turning code into a stakeholder decision. Only the two
permitted Markdown files may change; the program, patch and instructions stay
byte-identical. Report any parent intervention separately from independent execution.

For H, read the result for clarity, rhythm and preserved voice. Repeated dash
interruptions and formulaic promotion should no longer dominate the passage.
The clear pitch, author, existing-folder prerequisite, offline/local behavior,
unchanged originals, Markdown format, 2–5-note range and image exclusion must
survive. The UI label and command block stay byte-identical. Do not require zero
dashes or an exact rewrite, or treat matching a banned-word list as quality.

For I, verify the documented command against execution and source. A different
primary flag does not make a working alias stale. Leaving the README unchanged
is valid. A route change may be an editorial preference, but must not be reported
as repairing an unsupported command. Preserve the pitch, Python prerequisite,
input, expected output and no-file behavior; only README may change.

For all scenarios, report actual artifacts and commands, uncertainty and any
intervention. Do not count a word decrease alone as a pass. Add new scenarios when
real usage exposes a missing decision; keep fixtures small enough to inspect.
