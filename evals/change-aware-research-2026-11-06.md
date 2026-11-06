# Change-aware methods: deeper review — 2026-11-06

Follow-up to the [initial research and Astra review](editorial-review-2026-11-06.md),
starting at `fd7714abdc1dcdf94859413305cb5239cafca509`. This is maintainer source
research and a synthetic smoke exercise, not a new independent execution trial.

## Findings and decisions

**LangChain:** read docs-review, its CI mode, docs-edit, docs-restructure,
verify-against-source, the skills index and relevant AGENTS sections at
`0e9200466a1424c828266939ada9c0d32a90f78c`. The [review skill](https://github.com/langchain-ai/docs/blob/0e9200466a1424c828266939ada9c0d32a90f78c/.agents/skills/docs-review/SKILL.md)
distinguishes mechanical rules from judgments and permits no findings. Its
[CI guidance](https://github.com/langchain-ai/docs/blob/0e9200466a1424c828266939ada9c0d32a90f78c/.agents/skills/docs-review/ci-mode.md)
qualifies diff-only review: follow contradictions, stale links and shared-content
effects the change creates elsewhere. Shortening can erase a condition or the
subject of a later reference while leaving lint clean. These decisions are now
explicit in the local skill. Mandatory phrase searches, majority-style counts,
report schemas and page-reduction requirements are not adopted. The inspected
review workflow separates agent findings from posting; its existence does not
establish review effectiveness, and no automation is being installed here.

**Next.js:** read update-docs and both references, the skills index, adjacent
guide/reference authoring skills and relevant AGENTS sections at
`4f350fb33cfbdb13b63ecd2d594e8588f6d667e0`. The [mapping reference](https://github.com/vercel/next.js/blob/4f350fb33cfbdb13b63ecd2d594e8588f6d667e0/.agents/skills/update-docs/references/CODE-TO-DOCS-MAPPING.md)
offers a useful route from altered behavior to documentation, including consumers
of shared content. However, its first four component source paths do not exist
in the same revision's complete Git tree. For example, it lists
`packages/next/src/client/components/image.tsx`; the tree instead contains
[`packages/next/src/client/image-component.tsx`](https://github.com/vercel/next.js/blob/4f350fb33cfbdb13b63ecd2d594e8588f6d667e0/packages/next/src/client/image-component.tsx).
This establishes a path mismatch, not semantic equivalence of implementations.
The local addition therefore treats maps as search leads and allows no docs
change for an internal refactor. Paths, templates, per-edit confirmations and
lint-as-validation assumptions are not imported.

**NN/G:** Jakob Nielsen's [Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/),
published 2006-12-03 and reviewed 2026-11-06, reinforces keeping frequently needed
material at the entrance and making deeper routes clear. Our placement and
destination-prediction checks already cover that decision. No further rule is
added; NN/G reserves rights and permits linking under its
[policy](https://www.nngroup.com/copyright-and-reprint-info/).

The installed expert map now records LangChain/Next.js inspiration, pinned sources
and MIT evidence. Both root licenses and the complete `.agents` path inventories
were inspected; no more-specific license/notice files were found there. All local
instructions use independent expression; no foreign skill or artifact is vendored.

## Maintainer smoke exercise

A disposable CLI example changed its default output from lowercase to uppercase.
The proposed README showed the new output but dropped the Python prerequisite and
left an orphaned “This is optional.” Its unchanged reference still described the
old default; a source map pointed at a nonexistent `src/emit.py`.

Applying the revised decisions restored the prerequisite, removed the orphaned
reference and corrected the affected mode reference. The valid product pitch,
program and unrelated background page stayed unchanged. Actual local executions
produced `HELLO` by default and `hello` with explicit lowercase mode; help also
succeeded. A comment-only follow-up warranted no documentation edit on inspection.
No shared-content build, browser task or external action was tested. The
maintainer constructed the case and knew its intended answers: this demonstrates
the decisions in a small example, not independent skill reliability.

Both skill validators, local Markdown paths/anchors and full-diff whitespace
checks pass. Prior fixtures, evaluation records, licenses and reused artifacts
are unchanged. No packaging structure or persistent installation changed.
