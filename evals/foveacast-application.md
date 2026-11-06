# Foveacast application — 2026-11-06

## Inputs and independent outcome

After Reader First #3 merged, a fresh agent received only the documentation skill
at `6bd1318416ee93e7262afd741aac1711b5a20d22`, a disposable
[Foveacast snapshot](https://github.com/khawkins98/Foveacast/tree/36743a3aee48cc5d5aacc3158b57dfed5a1fa572)
and a task to improve documentation for first-time users and contributors. No
parent history, preferred edits or prior findings were supplied. Runtime changes,
publication, Git mutation, external-service use and edits to historical evidence
were prohibited; temporary locked dependency installation was allowed.

The frozen entrypoint SHA-256 was
`839ce1cbabe496fb617f5860f884bcb9d8a8c0d2c8c488a5e0165689b9eef6d1`.
Parent comparisons confirmed that exactly six Markdown files changed, with no
additions/deletions, and all other 103 target files, the baseline and frozen skill
remained byte-identical. Temporary dependencies and test artifacts were removed.
The live checkout was not edited or published.

The candidate adds a first-screenshot path, supplies the missing model-download
step, distinguishes UI-only development from real inference, and routes contributor
commands to CONTRIBUTING. It corrects stale CI, model-size, metric and threading
claims, explains report outputs, and routes assistant instructions to maintained
setup. It identifies the absent PRD without treating the roadmap or implementation
as replacement authority. Credits, licences and dated evidence survive.

README decreases from 986 to 934 words. Total Markdown grows from 34,468 to 35,395,
chiefly for missing prerequisites and report interpretation. Contributor setup
requires an extra guide click. These are placement and completeness tradeoffs,
not a compression score.

## Checks and limits

The agent reported a successful frozen-lockfile install on Node 24.18.0, all
259 Vitest tests passing across 19 files, 35 edited-page links/anchors resolving,
and 11 local HTTP routes returning 200. Playwright listed eight demo tests and
ten full-suite tests. Execution stopped before browser testing because the matching
Chromium bundle was absent. Models were not downloaded; real loading, inference,
printing, offline reopening and production hosting remain unverified.

A contained copy of the smoke helper adapted only its repository root and log
paths to keep writes within the disposable workspace. Its existing assertion
failed on the retired `fc-controls-mount` after HTTP delivery succeeded. The
candidate documents the failure and a separate liveness route; it does not
rewrite the program to make the documentation pass. The parent independently
confirmed the marker mismatch against the shipped HTML.

The parent inspected the actual diff, checked model/report/CI claims against
source, and scanned all 53 local links across 15 Markdown pages. No new errors
were introduced. Two links in a historical spike still reference the absent PRD
and an old model; those records remain unchanged. Runtime text still advertises
a roughly 13 MB download, and Playwright configuration comments still describe
the former demo-only/no-E2E-CI state. Those residual conflicts are reported, not
presented as repaired by the Markdown changes. External research and commercial
service capabilities were not revalidated.

## Parent correction and feedback

The agent recommended no new skill rule: existing verification guidance had
successfully exposed the broken smoke assertion. Parent review then found one
overstated correction. Foveacast still wires canvas clicks to duration cycling
in `docs/src/main.js`; report tabs are another supported route. The candidate's
tab instructions were valid, but its change characterization treated the old
interaction as stale and the results guide lost that shortcut.

The original agent confirmed the finding in an informed follow-up. The parent
restored the shortcut in the guide and corrected the changelog characterization.
The parent also clarified that a failed silent demo model load produces a
developer-console warning, rather than implying a visible app warning.
These interventions are separate from the independent application. The reviewed
candidate still changes only six Markdown files; its total is 35,433 words.

The retained independent patch SHA-256 is
`cac4255ec3c47d007f8731ce2c5c70562315f3f3b8b0db3cbcdcb9763e923787`;
the parent-reviewed patch is
`9f4860b9e3892142f05fa80a41cde30a03ecd2f162c09d9f8aae1861ee600ac2`.
These are local trial artifacts, not merged Foveacast changes.

The skill now asks the agent to check whether a documented instruction remains a
supported alternative before calling it stale. This is a narrow clarification
of source verification, not a requirement to document every possible interaction.
No project-specific model, test or browser requirement becomes a general rule.

## Fresh supported-alternative check

A separate agent received only the revised frozen skill and raw
[Scenario I](README.md#scenario-i--supported-alternatives), without this application,
the parent finding or the maintainer checklist. It inspected the source/help,
executed the documented command and left README unchanged: `--check` remains a
supported alias for `--preview`. The parent independently ran both forms; each
printed `Preview: a-small-change` and created no files. All 12 frozen skill and
fixture files remained byte-identical, with no additions.

The frozen revised entrypoint SHA-256 was
`635281de31b40a3e4cd9b3e0bdeea6d0b47f661c7f8dd83c30acc5b63145d356`.
This is one synthetic CLI analogue of the alternative-interaction issue, without
a prior-skill comparison. It does not establish a causal improvement or browser
interaction coverage. Both skill validators and the skill repository's local
links/anchors and whitespace checks complete the PR validation.
