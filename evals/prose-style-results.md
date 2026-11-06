# Compact prose pass — 2026-11-06

## Change and source

The documentation skill adds a small prose pass within its existing entrance/style
reference. It favors natural rhythm, concrete claims and the writer's existing
voice. Ken Hawkins's punctuation preference generally avoids em dashes, with
exceptions when they help; quotations, UI labels and code retain their wording.
The independently installable contribution skill includes that punctuation
preference for PR descriptions, without depending on the documentation skill.

Siqi Chen's Humanizer provided conceptual inspiration. The installed
[source record](../skills/documentation-refactoring/references/expert-map.md#compact-prose-pass)
pins revision `0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0`, version 3.1.0, and its
MIT licence. The maintainer inspected the skill, licence and repository notices.
No upstream prose or examples were imported. Its full pattern catalogue, strict
dash rule and multi-stage output workflow were not adopted.

## Fresh Scenario H execution

A new agent received only the [Scenario H](README.md#scenario-h--natural-prose-and-punctuation)
task, frozen installable skill and raw fixture in a disposable workspace. It had
no parent history, checklist, intended rewrite or source-research conclusions.
No intervention was needed. The agent reported no network, installation, Git
mutation or delegation. File-inventory and SHA-256 comparisons confirmed that
only the copied README changed; instructions and all nine skill files remained
byte-identical, with no additions.

The maintainer read the actual diff. The result removes unsupported promotion and
staged opening/closing lines, retains the short pitch and personal origin, and
replaces repeated dash interruptions with direct export instructions:

> Choose an output folder that already exists, then select "Export — local files".
> Fieldpad writes Markdown files and leaves your original notes unchanged. It works
> offline and makes no uploads. An export can contain 2–5 notes and does not include
> images.

The existing-folder prerequisite, Markdown format, unchanged originals, offline
behavior, no-upload claim, note range and image exclusion survive. The maintainer
also compared the quoted UI label and fenced command byte-for-byte and checked
the unchanged tagline and Dana Example credit. No program was run: this is a
synthetic prose fixture, not an installed app. Its 120-to-78-word change describes
the artifact; it is not the quality criterion.

Frozen inputs and resulting README, SHA-256:

| Artifact | Hash |
| --- | --- |
| Skill entrypoint | `444ee0e68920405f9c93944c9b7688f261db0073092f694787e5122bcff4a949` |
| Entrance/style reference | `a1921eb827e7dc6e5f49998f59836603d6202a2002f42188f778d439df60449d` |
| Raw README | `a1a8e5b7c4ad73d38de5b4c44e3ce1871ec035b9be2f7be9ddddfface285464f` |
| Project instructions | `efffa4d3ef9709235dd98fcb5eccd3920e7123f1f4f9f9aef57ec6706b6525dc` |
| Result README | `88124f008fc7d094370c8919207a23a7615aac741e1af37cf82d61a9c11a2d0a` |

This is one conspicuous synthetic example, not evidence of general effectiveness
or causal improvement over the old skill. It checks literal punctuation retention,
but does not establish judgment about a useful em dash in ordinary prose. There
is no zero-dash requirement, banned-word score or exact expected rewrite.

## Maintainer application to this PR

The maintainer also applied the documentation skill to the full PR: entrance
placement, prose, sources, licensing and reader paths. This informed self-review
trimmed a repeated opening claim and kept the practical before/after ahead of
installation, with author credits and maintained specialist detail still routed
to their existing homes. The README grows from 361 to 493 words to add the
requested example and personal framing; no separate prose skill is introduced.

The Tidy example's unsupported flags, dry run, unchanged files and actual overwrite
were checked in a disposable fixture copy. Both skills pass the system
`/Users/khawkins/.codex/skills/.system/skill-creator/scripts/quick_validate.py`.
Local Markdown paths/anchors and full-diff whitespace checks pass. These checks
do not constitute a user study or rerun earlier real-project applications.
