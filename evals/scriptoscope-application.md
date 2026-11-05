# Scriptoscope application — 2026-11-05

Applied the curated skills at revision
`89f138f293e863d64537d91fdcf71ed25da1c` to the existing
[Scriptoscope documentation draft #659](https://github.com/khawkins98/scriptoscope/pull/659).
The target began at `d98dc98`; the follow-up is `797b57a`.

This is an application to the same project that informed the skill, not a held-out
benchmark or evidence of superiority over the credited source approaches.

## Observed outcomes

An independent read-only reviewer used the skill entrypoints, target instructions,
permitted guides and public source. It tried hosted/npm setup, diagnostics and
current-versus-historical maintenance paths. The parent verified and corrected:

- The theme-switching guide promised every promoted window changes scheme, but
  authored per-window theme overrides use separate managers and remain fixed.
- The cascade guide said relative positioning applies only when needed, but the
  helper always sets the container's inline position to relative. The guide now
  explains that behavior and suggests an outer positioned wrapper when needed.
- A contribution command index omitted the required render slug; it now routes
  to a complete example. Both linked diagnostic commands executed successfully.
- The full branch whitespace check found two trailing blank lines. Removed them.

The local policy now credits the specialist methods and distinguishes maintained
documentation homes from technical authority. Source attribution remains separate
from optional commit trailers. No upstream skill text or table was copied into
Scriptoscope, and no skills were installed into its checkout or global settings.

## Verification and limits

The current audit classifies 277 pages with zero errors and five retained size
advisories. Four audit regression tests pass. The differential link/anchor check
examined 660 local/same-repository targets with no new failures. The diagnostic
render/placement commands and full-branch whitespace checks pass.

The required exact-head `lane:ready` check caught a missing receipt in the PR.
After commit/push, all available checks passed, including clean-room lint,
coverage, ledger/history, engine diff, source validation, typecheck and the full
Node suite. The gate still **fails** because its private `Traps.h` is not configured,
so trap-table verification cannot run. The actual failed receipt is preserved in
the draft PR; no substitute header or waived check is presented as a pass.

This pass used static reader/source review rather than a new browser user study.
Earlier package/browser results remain associated with their earlier candidate.
The private-header requirement is project-local; the skill did not gain a new
universal rule or dependency to accommodate it.
