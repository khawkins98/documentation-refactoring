# Change-driven applications — 6 November 2026

## Risk & Resilience Maps: a real feature diff

The user authorized documentation work on the paused feature branch in
[PreventionWeb/undrr-risk-resilience-maps PR #65](https://github.com/PreventionWeb/undrr-risk-resilience-maps/pull/65).
The owning agent committed its pending work first. A new agent received the task,
skill `d1421c217128b4298f973769b4291ec6ab734d1a` and current checkout at
`d893c1675831534f5a2fc8d95739cf22135bf683`, with feature merge base
`20ef02bf6cdfc31e5b0a75fa0ac1301c86291a6b`. It did not receive the parent's
conversation, suspected defects or previous trial findings. Normal platform/tool
instructions remained available; project evidence was confined to the checkout.

The agent found actual feature drift: Sources now links users into the viewer,
but architectural and lifecycle guidance still described downloads on Sources.
It also corrected the importer recipe: adding an inventory row does not create
the required layer/source configuration. A first-use walkthrough, CSV metadata
and filtering details, and the distinction between schema checks and actual data
vetting became clearer.

**Parent intervention was necessary.** The first edit replaced a proposed product
requirement and programme question with criteria inferred from the prototype.
Source inspection established implemented behavior, not stakeholder approval.
After review, the original requirement and question remained unchanged, with
dated November clarification and follow-up. This is a supervised application with
an initially independent pass, not an unassisted success.

[Documentation commit `a7494f2`](https://github.com/PreventionWeb/undrr-risk-resilience-maps/commit/a7494f2f9b7721bf986d1d9572cff1d615902d88)
changes README, ARCHITECTURE, the download guide and product specification only.
The parent compared file hashes: every other tracked file, including runtime,
tests, configuration and historical records, was byte-identical. README changes
from 1,078 to 1,079 whitespace words; all 19 Markdown files from 57,486 to 57,877.
No files were added or moved in the target. This is a task-completion improvement,
not a compression result.

The agent ran lint, 1,175 unit tests, a temporary-directory production build,
an importer dry run (138/138 matches, no changes), 10 focused Chromium tests and
a live contract check (21 hosted files, 70 CSV views; warning: 42 use reference
names). The parent read the logs and source and checked all 98 local links/anchors.
Local dependencies were reused. Browser tests stubbed MapX and bypassed the PIN;
the live contract checked view definitions and HEAD metadata, not attribute-table
contents. A synthetic 24-row CSV was parsed with Python's standard library;
pandas/R calls, live MapX browser behavior, Safari and large transfers were not
exercised. Remote validation and the full stubbed Chromium E2E job subsequently
passed for the documentation commit; they do not establish live MapX behavior.

The parent also rewrote the PR description around the final feature. Earlier
Sources-based live-browser measurements remain historical in its edit history,
not evidence for controls that were removed. The PR stays open and unmerged.

## Narrow follow-up and Scenario G

The operating skill now makes one existing authority boundary concrete: preserve
proposal/requirement intent and approval status when documenting a divergent
prototype; use a dated note or open question. Existing rules already cover
related-page inspection, accurate PR descriptions and honest validation, so no
additional workflow stages were added.

A fresh agent then executed [Scenario G](README.md#scenario-g--prototype-behavior-and-programme-requirements)
with only its task, revised installable skill and raw synthetic fixture. It
documented the opt-in URL preview and print-only limitation, preserved both
programme criteria and the original question, and added a dated implementation
note. No parent correction was supplied. Only the two permitted Markdown files
changed; program, patch and instructions stayed byte-identical in the test copy.
The parent inspected the result and reran default, prototype and help commands.
The fixture patch's context was subsequently compacted without changing the
represented source change. This small case supports the decision rule, not broad
independent reliability or a causal comparison with the previous skill.

Tested entrypoint SHA-256:
`6d07aab8ce99759a70532d7cf919cd7b733c4c07029223ec00b61c2f7ed80eff`.

## Johnny Web repeat: restraint on an already-refactored repo

Another fresh agent used `d1421c2` on Johnny Web baseline `1d725c8`, finding a
missing extractor prerequisite and exact-ZIP requirement. It changed CONTRIBUTING
only; README stayed at 716 words. Tests (662 passed, 138 skipped), build and CI
passed. Full proprietary-data extraction remained untested.
[PR #89](https://github.com/khawkins98/johnny_web/pull/89) merged as
`5f8a04d4eaa58abb1ddea735ecb86636fc7b8cd8`; the parent verified its tree matched
reviewed head `bbc6ea3bb35e3a1082c1f1399e3336b833ccbef9`. Total Markdown increased
from 65,334 to 65,476. This supports leaving an effective entrance intact while
repairing a demonstrated task gap; it is not a formal no-change control.
