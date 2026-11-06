# Editorial review and related-method research — 2026-11-06

## Inputs and decisions

Starting point: `c768a16646cc597993a7d502da425bc898d59fb2`. At the maintainer's
request, an Astra agent reviewed the actual skills, references and application
records with the project history and editorial preferences. A separate agent
researched primary web sources. Both were informed reviews, not blind trials.
Neither edited the repository or installed external skills.

The revision makes the threshold for changing product copy explicit: correct a
likely reading that would lead the intended reader to choose or act incorrectly;
do not replace working copy merely with a narrower paraphrase. Useful comparisons
can stay. Qualifiers belong where they first affect a decision or action.

Verification now follows the paths affected by a change. The entrypoint retains
helper semantics, recipient prerequisites, distribution checks, configured inputs
and honest reporting of partial checks and substitutions. It no longer implies a
full product tour for a small correction. Repeated style-exception reporting was
removed, contribution validation uses general candidate terminology, and task
selection descriptions lead with capabilities. Independent execution and informed
design review are now distinguished in CONTRIBUTING.

The documentation entrypoint goes from 1,039 to 964 whitespace-delimited words;
entrance/style guidance goes from 777 to 790. These counts describe the edit,
not its quality. Required notices, reused artifacts and prior evidence stay intact.
Astra's final informed diff review found no substantive safeguard regression.

## Related methods

- **Use now:** Raluca Budiu / NN/G's [information scent](https://www.nngroup.com/articles/information-scent/)
  sharpens the relocation check: can the intended reader predict the destination's
  answer from the remaining link and context? The installed expert map records
  the article date, review date and [rights policy](https://www.nngroup.com/copyright-and-reprint-info/).
  This is conceptual inspiration with independently written instructions; no
  article prose or artwork is included.
- **Optional:** LangChain's [docs-review](https://github.com/langchain-ai/docs/blob/0e9200466a1424c828266939ada9c0d32a90f78c/.agents/skills/docs-review/SKILL.md)
  limits review to changed prose, allows no findings and checks compression for
  lost conditions or referents. Reviewed revision `0e9200466a1424c828266939ada9c0d32a90f78c`;
  the skill declares MIT and the [root license](https://github.com/langchain-ai/docs/blob/0e9200466a1424c828266939ada9c0d32a90f78c/LICENSE)
  agrees. Its Vale and phrase rules remain project policy. No text is imported.
- **Optional:** Vercel / Next.js's [update-docs](https://github.com/vercel/next.js/blob/4f350fb33cfbdb13b63ecd2d594e8588f6d667e0/.agents/skills/update-docs/SKILL.md)
  maps a source diff to affected documentation. Reviewed revision
  `4f350fb33cfbdb13b63ecd2d594e8588f6d667e0`, [MIT](https://github.com/vercel/next.js/blob/4f350fb33cfbdb13b63ecd2d594e8588f6d667e0/license.md).
  This could help change-driven maintenance later; its paths, templates and
  per-edit confirmations do not become local instructions.
- **Already covered:** GDS's [user-needs guidance](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs/)
  largely overlaps the reader/result and maintenance decisions. An action-only
  interpretation would underserve explanation. No source material is imported.

The researcher used skills.sh for discovery, then inspected actual primary
sources and license evidence. Popularity was not treated as evidence of fit.
The maintainer re-opened the adopted NN/G source and policy, LangChain skill and
license, and Next.js skill and license. No new mandatory workflow was added.

## Fresh Scenario F execution

A new agent received only the [Scenario F](README.md#scenario-f--entrance-placement-and-prose)
task, raw fixture and frozen installable skill, without parent history, proposed
edits or the maintainer checklist. Work stayed in a disposable copy. The agent
reported no network, installation or Git changes; the maintainer confirmed that
only README and the existing command reference changed and no files were added.

README went from 215 to 121 words; all four Markdown pages went from 411 to 356.
The result retains the workshop origin, Alex Example's credit, Python prerequisite
and local-processing limit. First use stays at the entrance; argument/help detail
has one maintained reference, and the synthetic survey is clearly identified.
The agent reported examples, help flags, required-argument behavior and local
links checked. The maintainer inspected the diff, reran text, quoted-phrase,
help and missing-argument commands, and compared every original file hash.
Program, instructions and dated survey bytes were unchanged; no files were added.

The frozen entrypoint SHA-256 was
`b00d955299256362d66dd5c95dd3fd9d84de6c78ee845bff4f10dfd431582289`.
The frozen entrance/style reference was
`76b2ef2d6bbddb8737f6c7e5bea5edaad0af4b6c8c390bb2b60a620c4b3b4ed9`.
After freezing, the final reference only dropped two repeated reporting demands;
the tested decision rules and entrypoint did not change. This is one small
synthetic trial. Its conspicuous filler does not establish preservation of strong
real-world product pitches or causal improvement over the previous skill.

The maintainer also read the condensed verification rules against existing D/E
decisions: permitted configured inputs, current helper entrypoints and skipped
rendering checks remain covered. Those scenarios were not rerun. Both skills
pass the system skill-creator `scripts/quick_validate.py`; local paths/anchors and
full-diff whitespace checks pass. No packaging structure changed, so the earlier
copy-install result remains historical evidence rather than a new install claim.
