# Elements of Style trials — 2026-11-07

## Inputs and scope

At the user's request, [Reader First #5](https://github.com/khawkins98/reader-first/pull/5)
first introduced a selective composition/prose revision, then supplied the frozen
skill at `f2ddf7f897dc6eddca4c2c24d9c2fdd7be995095` to two new agents. Each received
only that skill, a previously targeted repository and a restrained prose task.
No parent history, preferred rewrite or prior trial findings were supplied.

The task explicitly protected product pitches, taglines, literals, factual scope,
limits, credit, requirements and history; Blocklate's privacy promise was also
protected. These were realistic editorial constraints, not a test of whether the
skill would infer them without instruction. HTML prose could change, but tags,
attributes, JavaScript and CSS could not. Git operations and publication remained
with the parent. Work occurred in isolated clones; live working checkouts were
not edited.

The entrypoint SHA-256 was
`635281de31b40a3e4cd9b3e0bdeea6d0b47f661c7f8dd83c30acc5b63145d356`;
the revised style reference was
`1ae9de3ece45f4b26cb2de1e06129cb8f3bc2afd83ddbf2dbc2b73c3f3529a4b`.
All nine frozen package files stayed unchanged. The installed source record
identifies the reviewed Strunk edition and the independently written relationship.

## Application drafts

| Project | Base | Draft head | README words | All Markdown words |
| --- | --- | --- | ---: | ---: |
| [Pinment #23](https://github.com/khawkins98/pinment/pull/23) | `5ed1d2def7fee0fe44e3c2d1fc7ee5b9a7d64ca1` | `7f1273fb0726ab6822348cc45828418eb58fcd3a` | 736 → 743 | 3,139 → 3,153 |
| [Blocklate #5](https://github.com/khawkins98/blocklate/pull/5) | `efe6112757dce9f6323e4c60bf3e2fcee50231e9` | `6b974e0f9dd42a1dd664de2cf80252f380e2c38c` | 584 → 589 | 2,052 → 2,074 |

Both agents retained the existing structure and reported no factual repairs or
blocking skill friction. The parent accepted their source edits unchanged.
Pinment changes four prose files; Blocklate changes five, including the required
Unreleased bullet. No files were relocated. Small size increases accompany more
explicit actions and referents; neither reduction nor growth is a quality score.

### Pinment excerpt

Before:

> Replies and edits need a newly shared URL

After:

> To share replies or edits, create a new share URL.

Other edits identify the JSON-sharing behavior, local bookmarklet and extension
packager more explicitly. The existing privacy and compatibility guidance remains.

### Blocklate excerpt

Before:

> Return with the translated response copied or saved as text.

After:

> Copy the translated response or save it as text, then return to Blocklate.

Other edits put test prerequisites before the command and clarify draft recovery,
reconciliation filters and editing a prompt before copying it.

## Verification and limits

Pinment's agent completed a frozen-lockfile install, all 307 tests across seven
files and the production build on Node 24.18.0 / Yarn 1.22.22. A `url.parse()`
deprecation warning remained. The draft head's CI test job passed; deployment was
skipped. Real-browser installation, third-party CSP, mobile compatibility and PDF
appearance were not newly exercised.

Blocklate's agent ran all 35 browser-suite tests successfully in an isolated Chrome
profile with external networking blocked. No dependency installation was needed.
Drupal import, external AI services and manual editor/download workflows were not
newly exercised. There is no separate CI result for this draft.

Parent comparisons confirmed unchanged Markdown code/commands, README introductions,
HTML tags, attributes, comments, scripts and styles, and every source file outside
the allowed diffs. Licences, prior changelog entries, requirements and historical
records remain intact. All 15 Pinment and nine Blocklate local Markdown links and
anchors resolved; whitespace checks passed. The parent inspected the full diffs
without repeating the agents' product test suites.

These are two explicitly invoked, same-project follow-ups with new agents and no
prior-skill control. They establish feasible scoped applications, not a causal
benefit from the added composition guidance, automatic selection reliability or
a reader-study result. Several useful criteria already existed before the trial.
No extra general rule follows from the outcomes. This record covers draft
results; it does not record a landing.
