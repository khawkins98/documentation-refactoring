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

## Self-application — 2026-11-06

At the maintainer's request, applied the skill to its own proposed PR after the
SVGOMG-Font rerun landed. The repository inventory distinguishes the root user
entrance, project contribution rules, two independently installable skills and
their references/notices, source records, evaluation records and raw fixtures.
The source/legal records, raw fixtures and earlier evidence stay in their roles.

README keeps the project introduction, visible author credit, two-skill selection,
installation, first invocation and license routes. The repeated specialist table
is replaced by the existing expert-map routes; duplicate evaluation navigation is
consolidated. CONTRIBUTING now records those maintained homes. README falls from
528 to 346 whitespace-separated words. Total Markdown grows from 13,114 to
13,668 words because the SVG rerun/landing and these checks add evidence.
Specialist selection costs a reference click; first invocation remains at the
entrance. Both installed entrypoints were reviewed and retained: their routing,
authority and validation instructions remain useful, and each must carry its own
credits/notices when installed alone. No instruction change was added merely
because another application completed.

Skills CLI 1.7.6 discovered exactly two skills with `skills add . --list`.
Copy-mode installation from the local checkout into a disposable Git project,
targeting Codex, installed both; `skills list --agent codex --json` confirmed
project scope. Every installed source file matched its checkout bytes, including
licenses, expert maps, instructions, metadata and the reused contribution table
and upstream notice. No global or other-project installation was used.

A direct draft-branch URL failed: the CLI interpreted `tree/feat/initial-skills`
as branch `feat` and path `initial-skills`. That route is not recommended. The
README's local-checkout source form works for the draft; the owner/repository
form reads the default branch, where the skills become available when this PR
merges. The check therefore establishes local packaging and discovery, not a
successful default-branch install of the unmerged PR.

Both skills pass the system skill-creator validator at
`/Users/khawkins/.codex/skills/.system/skill-creator/scripts/quick_validate.py`;
61 local documentation paths/anchors and full base-to-head whitespace
checks pass. This was maintainer self-review and installation verification, not
another independent skill-behavior test. Original licenses, source maps, third-
party notices, reused artifacts, raw fixtures and prior evidence remain intact.

## CC BY prose and MIT code — 2026-11-06

At the maintainer's explicit request, changed licensing from the all-MIT original
project notice at `d14633b` to the material-level split in [LICENSING](../LICENSING.md).
Original Markdown prose uses CC BY 4.0; original code, configuration, fixture data
and code/command examples use MIT. Third-party material retains its own terms.
The exact upstream table and notice are unchanged. Earlier records above describe
the MIT packages inspected then; their claims and measurements were not rewritten.

The CC legal text came from [Creative Commons' official plain-text source](https://creativecommons.org/licenses/by/4.0/legalcode.txt),
reviewed 2026-11-06. Only trailing blank lines were normalized to one final newline;
all legal text is retained. Bundled SHA-256:
`9e5f1b3c610b9c2da5c313bf81d577a7d1acec686bdb0384edefa6df0f90cd94`.
The MIT text retains Ken Hawkins's existing copyright and full permission notice.
Root and selected skills each carry both full texts and a scope map. Skill metadata
routes to that map; operating instruction bodies are unchanged.

Skills CLI 1.7.6 independently installed each selected skill into a separate
disposable Git project, targeting Codex in project scope and copy mode. Every
source file matched the installed bytes: nine files for documentation-refactoring,
eight for contribution-conventions. Both full texts and scope maps survived;
their local links resolved, with no symlinks or dependency on another installed
skill. The reused table and upstream notice stayed byte-identical. No global or
other-project skill installation was performed.

Both system skill-creator validators, local Markdown paths/anchors and full-diff
whitespace checks pass. This verifies packaging and declared scope, not a new
behavioral evaluation or legal opinion about third-party rights.
