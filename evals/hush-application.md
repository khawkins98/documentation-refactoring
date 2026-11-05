# Hush application and entrance review — 2026-11-05

[Hush #1027](https://github.com/khawkins98/Hush/pull/1027) is a draft application of
this collection to a desktop app's documentation. Its initial candidate was
`d8dc8e2851eeafce777562ca72350d7d430fee54`. This is maintainer dogfooding, not a
held-out benchmark or independent user study. The PR remains a draft.

## Initial outcome and missed scope

The initial pass consolidated contributor commands in `docs/developing.md`,
extracted the IPC recipe, and corrected Node, feature-flag, reset and screenshot
instructions. Contributor/agent pages became shorter while preserving project
constraints. The 1,999-word README remained unchanged.

The user challenged that outcome. The pass had concentrated on contributor
entrances and had not justified leaving the product README untouched. Its dated
competitor table, detailed network audit and long engineering/attribution prose
still required a placement decision. A cleaner contributor path did not establish
that the primary entrance had been reviewed.

## Revised outcome

The follow-up keeps the personal introduction unchanged and retains product
purpose, the install path, unsigned-app warnings, platform/testing limits,
network/offline caveats, visible credits and source-use restrictions in README.
It moves the dated survey, detailed privacy verification and full acknowledgements
to focused pages with direct links. The old main README section anchors remain.
The survey is explicitly a 2026-07-28 snapshot, not a newly verified comparison.

README falls from 1,999 to 613 whitespace-delimited words. Across all eight
affected/new pages, including moved material, words fall from 12,532 to 10,254
(about 18%). Readers gain a link for detailed comparison, privacy audit and
attribution; the adoption limits and first-use route remain at the entrance.
Full survey and acknowledgement text is retained, with relative links adjusted.

Source review also corrected an inherited privacy claim: manual update requests
identify Hush and its version in the User-Agent and send GitHub API headers.
The guide no longer claims only a default user agent. The README privacy summary
links the detailed account without repeating its endpoint/implementation inventory.

## Reusable correction

The skill now requires an explicit entrance assessment within README/broad work,
and explains a keep/shorten/move decision even when the README stays unchanged.
Its editorial reference provides concrete placement and prose criteria: direct
actions, active verbs, one purpose per paragraph, descriptive links, less repeated
setup/promotion, and formatting that supports tasks rather than decoration.
Lost material limits or credits, unsupported claims and duplicate active guidance
are findings to resolve or explicitly report. Word targets are not a substitute
for those checks; project voice, historical evidence and required notices survive.

## Validation and limits

The revised Hush frontend check passes with zero errors/warnings. The full
base-to-head Markdown/link scan introduces no new path/anchor errors; it also
records existing unrelated link issues rather than presenting the entire corpus
as clean. Relocated survey/credits, the personal origin and agent conventions/
module constraints were compared with the base. The normal pre-push hook repeats
Rust formatting, no-default-feature clippy and the frontend check.

Earlier screenshot discovery found 16 tests, but execution was blocked by a
missing Chromium binary. No new screenshot, native startup, dictation or reset
execution is claimed for this Markdown-only follow-up. Historical/architecture
records, runtime source and required attribution policies remain untouched.

[Scenario F](README.md#scenario-f--entrance-placement-and-prose) provides a small
synthetic entrance/style task. Its [smoke record](entrance-style-results.md)
distinguishes a maintainer-authored correction from a future independent skill
trial.
