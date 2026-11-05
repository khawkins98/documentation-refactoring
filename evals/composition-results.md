# Composition and provenance checks — 2026-11-05

This pass verifies the curated specialist composition and its packaging. The
[initial behavioral trials](initial-results.md) remain the earlier baseline;
these checks are not a new claim of behavioral coverage or legal certification.

- Reviewed immutable upstream source revisions and applicable license files;
  recorded named credits and whether the local relationship is inspiration or
  direct reuse. Framework ideas are linked rather than importing their prose.
- Verified the directly reused dmythro commit-type table is an unchanged excerpt
  of the pinned source, and the bundled upstream MIT notice matches source bytes.
- Ran both skill-creator validators and checked local documentation link targets.
- Installed both selected skills into a disposable project with Skills CLI copy
  mode, targeting Codex. Confirmed the original-project license, expert map and
  instructions survive byte-for-byte in each installed skill; the contribution
  skill also retains the exact upstream license and commit-type table.
- An independent review found the original-project MIT notice was initially
  absent from selected skill folders. Added those notices separately from the
  upstream one, then repeated the installation check successfully.

The sources remain credited inside each installable skill, rather than only in
root repository files. No skills were installed into the maintainer's other
projects or global skill directory. External source links, revisions and license
evidence are recorded in the source maps; updating them requires another check.
