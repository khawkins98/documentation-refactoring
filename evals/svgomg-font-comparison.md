# SVGOMG-Font paired application — 2026-11-06

Compared [context-informed PR #13](https://github.com/khawkins98/svgomg-font/pull/13)
at `315afef2de38b69a315721e78d40f8b458a9919d` with
[fresh-agent PR #14](https://github.com/khawkins98/svgomg-font/pull/14)
at `49ac23c52b1b92603b18a6b1a194a75406f3dfb5`.
Both started from `main` at `f0d5daee6a49ca18800f7d463325b88af9d92378` and used
the skill at `388416511857961018d44da393f74ee4074c66c0`.

The user explicitly requested the fresh application. That agent had no parent
conversation history. It received only the raw checkout, its normal project
instructions and a pinned copy of the installable documentation-refactoring
folder, including its references and license. It did not receive the other PR,
findings or preferred edits, and was instructed not to inspect other PRs,
branches, worktrees or trial artifacts. It chose its changes and checks and
opened its own draft. No parent edits were integrated into either candidate for
this comparison. This is one same-project comparison, not proof that context
caused the differences or a held-out benchmark.

## Outcomes and tradeoffs

Whitespace-separated counts include all tracked Markdown and relocated material:

| Page | Baseline | With context #13 | Fresh #14 |
| --- | ---: | ---: | ---: |
| README | 452 | 443 | 782 |
| ABOUT | 462 | 517 | 363 |
| CLAUDE | 531 | 547 | 390 |
| CONTRIBUTING | 390 | 526 | 700 |
| All nine Markdown pages | 5,782 | 6,000 | 6,182 |

Both independently corrected automatic processing, custom-font handling,
subsetting availability, export steps and the stale no-linter claim. Neither
changed runtime code, dependencies or workflows. Parent comparisons confirmed
the fresh candidate changed only four active Markdown pages; its license, rules,
research, changelog, samples and ledger records remained identical to the base.
The context candidate also added an Unreleased changelog entry.

The fresh candidate made better use of canonical homes: CLAUDE links to maintained
setup/checks and RULES rather than repeating commands and constraints. It also
documents useful details about CDN weight selection, network failure before
fallback and external resources left outside font embedding. Its fuller README
keeps those details at the entrance while ABOUT and CLAUDE shrink. That is a
placement tradeoff, not evidence that every added word is waste.

The context candidate gives a shorter initial path and preserves the original
introduction. The fresh candidate rewrites the opening and places network and
viewer qualifications earlier. Recent maintainer feedback favored less
qualification in lead copy. However, preserving the original is not sufficient
either: its WOFF2-specific description does not cover the implementation's possible
TrueType output. A small factual repair can retain the pitch without accepting
the inaccurate detail or replacing the whole paragraph.

## Evidence boundaries

Both candidates passed clean installation, lint, 33 tests and production build on
Node 24.18.0; both final candidates passed CI. The locked toolchain's documented
Node version requirements differ from the workflows' Node 20 selection, but this
comparison did not observe a CI failure from that mismatch.

The context run exercised Chromium downloads, SVGO payload retention, a missing
font with denied local permission, and manual font-file recovery. The fresh run
checked dev/preview HTTP routes and live fonts through an ad hoc Node/happy-dom
pipeline, not browser interaction. Its exploratory optimized-SVG XML parse did
not complete. These methods establish different boundaries; unit/build/HTTP
success is not interchangeable with browser rendering or a completed download.
Both live subset checks fell back to full fonts; neither established successful
glyph reduction or downstream viewer compatibility. Parent link checks found no
broken local paths/anchors in either candidate.

## Reconciliation in the skill

The comparison supports refining existing criteria rather than imposing README
word caps, requiring browsers for every edit, or treating the shorter candidate
as the correct answer. The revision strengthens routing from agent/contributor
entrances, asks which decision each new detail changes, favors a small factual
repair, and compares the old/new opening and first task during final prose review.

The paired run tested the prior skill revision. These refinements are an
evidence-based hypothesis, checked by manual editorial review, validators,
navigation checks and a [Scenario F smoke check](entrance-style-results.md#reconciliation-smoke-check--2026-11-06).
At that point, they had not been tried in a new independent application. Both SVG
PRs remained unchanged by that skill revision.

## Revised-skill application and landing

The maintainer closed #13 and #14 without merging and requested another fresh
application. A new agent received the revised skill at
`c09395a88c51a6dfc1f30b381034ce4f1d72c77b` and the same `f0d5dae` main baseline,
with the same task and scope. It had no parent history, earlier drafts, findings
or preferred edits. Only SKILL.md and the entrance/style reference differed
between its pinned bundle and the prior run; notices and other references were
identical. The parent did not edit or steer its result.

It opened [PR #15](https://github.com/khawkins98/svgomg-font/pull/15) at
`744587e162be33196af3f4c5112d2e84f7d40770`.

| Page | First fresh run #14 | Revised-skill run #15 |
| --- | ---: | ---: |
| README | 782 | 587 |
| ABOUT | 363 | 614 |
| CLAUDE | 390 | 408 |
| CONTRIBUTING | 700 | 700 |
| All nine Markdown pages | 6,182 | 6,292 |

The rerun moved more pipeline explanation into ABOUT and kept canonical setup
and rule routes. It corrected the opening's WOFF2-only description, while still
adding network/privacy qualifications. The shorter README and larger total
describe a placement change, not overall compression or proof of better prose.
This is partial support for the revised criteria from one fresh application;
agent variation and the same-project task prevent attributing the difference
solely to the instruction changes. No additional universal rule was inferred.

Five existing Markdown files changed. A dated LEARNINGS pointer preserved all
original text; runtime, samples, dependencies, workflows, rules, release history,
licenses and ledger records were unchanged. Fresh installation, lint, 33 tests,
build, dev/preview HTTP routes and live Roboto/Lato pipeline checks passed on
Node 24.18.0. Happy-dom XML parsing rejected the original Roboto sample too;
ElementTree then parsed both processed outputs. This validates the XML/payload
boundary, not browser rendering, installed-font permission, font upload,
clipboard, successful glyph reduction or downstream viewer behavior. Existing
fontkit/SVGO/build warnings and dependency advisories remained disclosed.

Both final-head CI jobs passed. The maintainer approved landing; the parent
repeated lint, 33 tests, build, 29 local links/anchors and whitespace checks, then
merged the exact reviewed head as
[`e4ddfbf`](https://github.com/khawkins98/svgomg-font/commit/e4ddfbf9c729388188a4b4357adcdd348bb3c4da)
on 2026-11-06. The merged tree matches the candidate.
