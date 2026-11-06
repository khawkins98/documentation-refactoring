# Scriptoscope application — 2026-11-05

> Follow-up: the exact-head gate now passes. The initial failed attempt below
> is retained as history; the maintainer copy already existed and its path had
> not been configured. See the resolution at the end.

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

## Follow-up: header configuration resolved

A subsequent filename search found the existing Universal Interfaces 3.0.1 header
in the local shared maintainer tools. Its SHA-256 matched the generator's pinned
source, and the direct trap-table comparison passed. The full `lane:ready` gate
then passed on the same Scriptoscope head `797b57a`, including trap verification,
engine diff, source validation, typecheck and the full Node suite. Its passing
receipt replaced the failed receipt in PR #659.

The initial limitation was an unconfigured `SCRIPTOSCOPE_TRAPS_H` / `--traps-h`
path, not absence of the file from the machine. Calling the draft blocked before
checking the permitted local maintainer locations was premature. No header was
substituted, published or copied into the target checkout, and no source change
or gate waiver was needed.

## Landing and reusable lessons

[PR #659](https://github.com/khawkins98/scriptoscope/pull/659) merged on 2026-11-05
as [`50ef272`](https://github.com/khawkins98/scriptoscope/commit/50ef27259c11b17e12d8da598d840cf400f211dd),
after the exact pushed head passed its readiness gate and required CI. The squash
commit uses the project’s conventional title and contains no co-author trailer.

The portable corrections are narrow: distinguish missing configuration from a
missing asset before declaring a blocker, validate the complete base-to-head diff,
and distinguish CI from any required exact-head review receipt. The skill
entrypoints now state those decisions. The Apple header path, checksum and
Scriptoscope gate command remain project-local rather than becoming universal
skill requirements. Scenario D uses a small synthetic fixture to exercise the
configuration decision without distributing private material.

### Regression scenario

An independent evaluator ran the new synthetic configured-input scenario using
the revised documentation skill, without the maintainer checklist or this case
record. It found the documented reference, verified the pinned hash and ran the
gate with a command-local environment path. Validation passed. Parent comparison
confirmed every fixture file remained byte-for-byte identical, with no new files.
No network, Git mutation, installation or persistent configuration change occurred.

The evaluator configured the documented prerequisite before running the gate; it
did not reproduce an initial failed run. This checks the desired resolution path,
not every missing-file or wrong-version failure mode.
