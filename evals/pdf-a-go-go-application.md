# PDF-A-go-go application — 2026-11-05

Applied the skills at `b28b6f23052c67eb27fabf3f66bf468dc3278f10` to
[PDF-A-go-go #35](https://github.com/khawkins98/PDF-A-go-go/pull/35).
This was maintainer dogfooding, followed by an authorized independent subagent
source review. Neither is a blind behavioral evaluation or user study.

## Reader paths and placement

The README retained a complete first embed, HTTP(S)/CORS requirements, read-only
and browser/CSP limits, and PDF.js/Lucide credit. Recipes moved to `EMBEDDING.md`;
configuration defaults stayed in the existing architecture/API reference.
Contributor instructions now identify those maintained homes. No runtime source,
license, agent constraint or historical CHANGELOG/IMPROVEMENTS record was rewritten.

The pass removed an undated competitor table and unverified fixed memory/browser
claims from active guidance rather than relocating them as if they were measured
evidence. It corrected a contradiction about bundled German UI translations.
The reference's existing longer technical detail remained for lookup.

README changed from 1,692 to 369 words. Final documentation review brought total
Markdown, including the new recipe guide, from 6,920 to 6,259 words. Advanced
integration tasks gain a guide click; the working initial snippet and material
adoption limits remain at the entrance. Counts are a navigation diagnostic, not
a claim of better product behavior.

## Initial validation and its boundary

A fresh install initially failed: the open Playwright test-runner range selected
1.65.0, whose exact `playwright-core@1.65.0` dependency was unavailable. The first
local build and 89 Chromium tests used a temporary link to the original checkout's
installed, satisfying dependency versions. Bundle-size budgets passed. The link
was removed and no original checkout files were changed.

A disposable built-artifact page derived from the README and all HTML recipes
checked the first rendered PDF, seven viewer instances, effective starting page 5,
dark theme, German labels and French overrides under the same-origin CSP recipe.
The examples' hosted asset/PDF URLs were replaced with local built files. That
validated the local artifact integration, not the original hosted/cross-origin
recipe. Markdown publication remains the GitHub/source repository; webpack ships
app assets from `dist/`. All 34 local links/images/anchors across seven Markdown
pages resolved. The browser and temporary resources were closed.

The initial PR's CI then failed at the same dependency-resolution step, before
build/tests. Cached local success was explicitly not a clean-install or green-CI
claim. The failure was preserved in the PR rather than waived.

## Review and clean-install resolution

The user subsequently authorized landing. Pinning the development test runner to
the already tested 1.62.1 restored a fresh `yarn install --frozen-lockfile` in the
isolated worktree without a dependency-directory symlink. A new production build,
89 Chromium tests and both bundle-size budgets passed on that installation.
This narrow development dependency change was part of authorized landing; it does
not imply that ordinary documentation scope always permits dependency changes.

The independent source reviewer found two documentation gaps before landing:

- A separately hosted `data-worker-url` needs its own module origin allowed in
  `script-src`, plus CORS; listing the bundle origin/`connect-src` alone is
  insufficient. PDF.js creates a blob wrapper that dynamically imports the
  worker module; [CSP inheritance for blob workers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy)
  supports the source finding. The custom-origin case was not newly browser-tested.
- Invalid translation overrides do not necessarily switch the UI to English:
  a valid selected locale still applies. The inherited reference now says
  selected-locale/English defaults. A UTF-8 scratch page with German plus malformed
  JSON confirmed the German next-page label. The first scratch page omitted its
  charset and displayed mojibake; correcting the fixture encoding resolved it
  without changing product code.

The reviewer had the target and skill source and was asked for research findings,
not an unprompted skill execution. It found existing Scenarios D–F already cover
related input/partial-validation/entrance decisions, so no new generic fixture
was added. The portable instruction change is only to report validation
substitutions and the original boundaries they leave untested. The Playwright
version, CSP tokens and locale strings remain project-local facts.

## Landing

[PR #35](https://github.com/khawkins98/PDF-A-go-go/pull/35) merged as
[`2596d3f`](https://github.com/khawkins98/PDF-A-go-go/commit/2596d3f2aaabdb76626c72b77e58f71130d1175c)
on 2026-11-05 after the exact candidate passed CI's install, build, 89-test and
size checks. The merged tree was compared with the reviewed candidate. The exact
Playwright pin resolves this observed installation failure; without a committed
lockfile it does not establish future whole-graph dependency reproducibility.
