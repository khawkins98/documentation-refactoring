# Lessons from Scriptoscope

Source: [repository-wide draft #659](https://github.com/khawkins98/scriptoscope/pull/659),
building on [task-first #656](https://github.com/khawkins98/scriptoscope/pull/656)
and [Diátaxis #658](https://github.com/khawkins98/scriptoscope/pull/658).
These are observations from a particular draft and baseline, not universal targets
or a claim that all changes shipped.

The consolidated PR subsequently [merged as `50ef272`](https://github.com/khawkins98/scriptoscope/commit/50ef27259c11b17e12d8da598d840cf400f211dd).
The measurements below remain the recorded draft snapshot.

## Outcomes at the recorded baseline

The README was 10,874 words. Independent drafts tried preserving depth in separate
guides, curating task-specific detail, and compressing the existing structure.
The combined rollout classified 277 documentation pages. Active guidance and
navigation/reference families decreased from 89,418 to 68,785 words; the entire
corpus, including technical specifications, evidence and history, decreased from
622,128 to 602,121. New pages count in those totals.

The small README was not the whole outcome. Agent instructions, contribution
workflow, integration troubleshooting and theme-porting guidance also became
shorter, while detailed interaction and evidence references remained substantial.

## What transfers

- A maintenance recipe required every public API in README. Fixing that instruction
  mattered as much as editing existing prose: otherwise ordinary updates regrew it.
- Reader roles had different access to source evidence. Better indexes preserved
  those gates rather than turning "full repo" into unrestricted reading permission.
- An API could have one maintained reference while task guides retained runnable
  examples. A short entry page alone would not solve duplicated truth.
- Independent reader review found a lifecycle defect that link checks did not.
  Validation methods supply different evidence and have different limits.

## What remains project-specific

- npm included a new nested `docs/README.md`, violating this project's package
  file contract. The hub became `docs/index.md`. The portable lesson is to inspect
  the actual published artifact, not to prohibit nested README files everywhere.
- A theme-picker example disposed itself on every `pagehide`; Back/Forward cache
  restoration needed the persisted-event guard. This is a browser lifecycle
  example, not a required check for every documentation project.
- Original-engine evidence and clean-room implementer restrictions governed which
  records could be read or edited. Other projects have different authority and
  retention rules; discover them instead of copying these paths or restrictions.
- Conventional commits and no unsolicited co-author trailers were maintainer
  preferences. They belong in an independently selectable contribution skill,
  not in the documentation method.
