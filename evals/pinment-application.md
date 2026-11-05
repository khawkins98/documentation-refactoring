# Pinment application and recipient review — 2026-11-05

Applied the skill at `baa9a3eaf44fcd1296576d9cd4850dfc423f971f` to
[Pinment #22](https://github.com/khawkins98/pinment/pull/22), starting from
`b1156c0ebcd0dd999eae225658a4c82c7dea35aa`. The initial trial produced
`ef479f9202623e9be55117f444c6bcaaeefa40ba`; the reviewed revision is
[`4666c59`](https://github.com/khawkins98/pinment/commit/4666c59).
The PR remains a draft. This is same-project dogfooding, source review and a
bounded independent follow-up, not a held-out benchmark or reader study.

## Placement and the review correction

The first pass moved the source map, v2 state example and technical rationale
from README into `DEVELOPING.md`, aligned Node/Yarn commands with CI, and kept
reviewer tasks, adoption limits and original visible inspiration at the entrance.
README fell from 1,060 to 582 words. A controlled browser handoff passed, but
those results did not establish that the instructions served a new recipient.

The user requested independent subagent review. The reviewer inspected the skill,
draft and source, with the prior task context. It found missing recipient
installation and JSON restore steps, conflicting shipped onboarding, and overly
broad page/placement/PDF promises left in `index.html`. Source review also exposed
the page-script access boundary for localStorage/light-DOM annotations and the
scope of PDF screenshots. The moved schema example validated and round-tripped
through the actual share encoder/parser; the split itself had no schema defect.

The revised draft completes recipient setup, direct JSON restoration and manual
hash-route loading. It aligns landing-page steps and the viewer hint with actual
labels, replaces guaranteed clipboard/placement claims, and explains page-script
access and checking PDFs for content beyond comments. Contributor setup now
includes a separate target page, the running development server and the local
versus production hub distinction. Duplicate maintenance prose became a pointer.

Final README is 738 words; all Markdown, including the new 886-word developer
guide, grows from 2,587 to 3,132 words. This growth supplies missing handoff,
recovery and setup instructions. Advanced implementation lookup gains a guide
click. PRD, LEARNINGS, CHANGELOG, license, manifests/lockfile and the original
Background & inspiration text remain byte-identical; runtime source is unchanged.

## Bounded independent skill exercise

A separate agent received only the updated skill, a raw disposable archive of
Pinment at `ef479f9`, and the task to improve documentation for first-time reviewers
and contributors. It did not receive the review findings, proposed corrections,
PR description or this record. Its scope allowed README, CONTRIBUTING, DEVELOPING
and HTML prose; no network, installation, Git mutation or browser access.

Its actual edits completed recipient installation and JSON restoration, corrected
onboarding labels and clipboard assumptions, and supplied a local first-review
path. It independently found that hub JSON import renders a review without
updating the address: **Copy share URL** therefore does not create a link for that
import, and **Open target page** puts the data back into a URL. The integrated
draft routes large reviews directly to target-page import and explains the hub
preview/sharing limitation. This finding added useful evidence beyond repeating
the first review.

Parent comparisons confirmed only the four allowed files changed, no extra files
remained, HTML tags/attributes/footer were unchanged, and original README credit
survived. The evaluator checked 19 local links/anchors and parsed the schema.
Its `yarn test` and `yarn build` attempts failed to start because the disposable
archive had no Vitest/Vite installation; no dependencies were installed. Its
source findings are not browser-test claims. It left the earlier hash-route advice
less explicit than the integrated draft and retained some meta prose; this was a
useful bounded result, not a perfect editorial pass. Its README grew from 582 to
769 words. The existing private security-report instruction still lacks a named
contact address; no contact was invented or verified.

## Integrated validation and substitutions

In the isolated development worktree, a fresh `yarn install --frozen-lockfile`
passed. The suite passed 307 tests across seven files, and site/extension builds
passed after the prose changes. All 15 local Markdown paths/anchors across six
pages resolved; whitespace checks passed. The actual final CI result belongs to
the linked PR, rather than being inferred from these local checks.

Chromium checks on the built local artifact established:

- The initial sender → hub → target round-trip retained a comment, author and
  single pin, including the target query string.
- Manual share-URL loading worked with clipboard reads/writes deliberately
  rejected and preserved a synthetic original `#docs-original` fragment.
- A downloaded JSON file restored its comment/author/pin, allowed an edit, and
  exported the edit. The new export omitted the original target fragment, as
  documented.
- Hub JSON preview displayed the target URL and comment without changing its
  address, confirming that it did not create a share URL for the import.
- A valid synthetic review whose share URL measured 29,894 bytes restored a
  24,000-character comment directly on the target page. Copy was disabled and
  JSON export remained enabled. This exercised the recommended large-review path.
- Rebuilt landing instructions and layout were inspected; no horizontal overflow
  appeared in the desktop check.

The bookmarklet bundle was loaded by a script rather than installed through the
bookmarks bar. The initial share hub origin/path was changed to the local preview,
retaining its encoded fragment. Clipboard denial was a browser-side stub.
Automated JSON selection exposed the app's detached file input in the temporary
DOM and bypassed the native file picker, while exercising its real FileReader and
import handlers. No source file was changed for these substitutions. Synthetic
pages/fragments do not establish real third-party layout or hash-router support.
The extension was built, not loaded; strict-CSP pages, PDF export, Firefox, mobile,
native bookmark installation and the published hub were not newly tested. Browser
and temporary servers were closed.

## Portable changes

The skill now explicitly checks recipient prerequisites and restoration when a
task hands off a result. Its entrance reference includes competing shipped
onboarding/help within the affected task and authorized scope. Neither addition
requires every documentation change to run a browser or introduce a checklist.
The case retains Pinment's URL budget, labels, storage and bundling facts locally.

No new generic fixture was added: the disposable real-repository exercise supplied
observable behavior for these narrow instruction changes. The root README and
PR description now route trial detail to evaluation records rather than growing
another copy of every application's history.
