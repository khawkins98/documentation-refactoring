# Johnny Web application — 2026-11-05

Applied documentation-refactoring and contribution-conventions at
`d878c41ba5578b20bc9a7ea5d60266e50fde2130` to
[Johnny Web #88](https://github.com/khawkins98/johnny_web/pull/88).
The PR merged as
[`1d725c8`](https://github.com/khawkins98/johnny_web/commit/1d725c84ad225be914a23aa570be336b40e80ea6)
after red-team fixes and passing CI on the final candidate. The merged tree was
verified identical to the reviewed candidate. The user's timeline/time feature
had already landed, so the documentation PR targeted current main.

This was maintainer dogfooding by the same agent, not a held-out benchmark,
independent reader evaluation or user study. The skills were read from their PR
without installing them into Johnny Web or global configuration.

## Application and outcomes

The initial five-page trial expanded to an inventory of 49 Markdown pages and
changes to 14 pages, including one task index. Detailed player controls stayed in
their existing guides; specialized development and research routes moved behind
the index. Trace details moved from architecture into the debugging guide while
the old architecture heading remained a working route.

The final README went from 1,043 to 716 words. Total repository Markdown,
including the new index and red-team corrections, went from 64,936 to 65,334 words
(+398). Specialized developer tasks gained an index click; common player guides
and first-run setup stayed directly linked. Long references remained useful;
entrance-page shrinkage was not treated as total documentation shrinkage.

Twenty-five generated, historical, methodology and vendor records were checked
byte-for-byte against the base and preserved, including generated coverage and
scene flows, release records, executable findings and license/provenance notes.

## Findings that transfer

- All 207 baseline Markdown link/image targets resolved, but two linked browser
  helpers still selected removed Classic/Enhanced launch controls. One also wrote
  a retired clock-storage key. Their active README instructions became explicit
  legacy guidance with routes to current playback controls. The helper scripts
  were not repaired by a documentation-only change.
- The local suite passed 662 tests and skipped 138 without extracted proprietary
  game data. That established neither live playback nor fidelity. A documented
  planner smoke command ran on the Math.random path; the faithful-RNG path still
  needed the absent executable.
- The CRT integration fixture started with the effect off to check allocation,
  while fresh game preferences used Balanced CRT. The guide now separates those
  contexts instead of suggesting that a fixture's initial state is the app default.
- Final red-team review corrected a trace claim: a rolling recorder can evict its
  opening metadata. A small bounded-recorder reproduction confirmed that outcome;
  bug reporters are now told to include the panel build ID separately.
- The sequencing check can pass with actor-coverage and duration warnings. The
  entry guide now distinguishes its hard assertions from signals requiring review.

The reusable change is source-backed task verification and accurate reporting of
what each check establishes. Johnny's selectors, storage keys, 50,000-event limit,
actor threshold and asset paths remain local facts, not new universal skill rules.

## Validation and limits

The final candidate passed the required test suite and production build, all 243
Markdown local links/images and anchors, two HTML image paths and the planner
smoke run. CI and commit-message checks passed before the authorized squash merge.
No runtime source changed, private asset was retrieved or proprietary capture was
published. No new live gameplay or browser study was performed, and external URLs
were not exhaustively rechecked. Historical validation counts keep their original
scope rather than being presented as current checks.

[Scenario E](README.md#scenario-e--changed-helper-and-partial-validation) distills
the helper/partial-validation decision into a public synthetic fixture. Its
[execution record](changed-entrypoint-results.md) separates deterministic fixture
checks from any future independent evaluation of the revised skill.
