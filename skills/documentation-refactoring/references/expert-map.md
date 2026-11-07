# Specialist sources and routing

This skill composes established specialist perspectives. Select those relevant
to the task; do not load every source, spawn a team or install other skills by
default. The local workflow is self-contained. The external links provide credit
and a way to study the source methods, not a requirement to fetch and execute them.

## Select the useful lens

| Situation | Perspective | Local application |
| --- | --- | --- |
| A page tries to teach, explain and list every option at once | Structure: Diátaxis, GitHub's documentation writer | Separate reader purposes where doing so helps |
| An existing docs set is hard to navigate | Information architecture: Samuel Berthe's structure audit | Inventory, find competing accounts, improve routes |
| Moved detail is difficult to find | Information scent: Raluca Budiu / Nielsen Norman Group | Check whether the link and its context predict the destination's answer |
| A README loses its intended audience | Audience: Softaworks' README guidance | Restore a clear entrance and working first success |
| Correct information is hard to read | Prose: Softaworks' writing guidance and William Strunk Jr.'s composition principles | Edit wording, clause placement and comparable steps after deciding what belongs |
| Prose feels formulaic or overworked | Voice and rhythm: Siqi Chen's Humanizer | Apply a compact, context-sensitive prose pass that preserves meaning |
| A diff needs a restrained editorial review | LangChain's docs-review and CI guidance | Find regressions, preserve meaning during cuts and allow no findings |
| A code change may affect documentation | Vercel / Next.js's update-docs | Trace reader-visible behavior to affected tasks and shared-content consumers |
| Authors assume knowledge readers lack | Reader checking: Anthropic's coauthoring workflow | Try representative reader tasks with fresh context when useful and authorized |

The synthesis adds the local project's authority, distribution and retention
requirements, plus the [recorded Scriptoscope experience](scriptoscope-lessons.md).
Repository rules and the user's scope govern application. Upstream workflows stay
in their own context; referencing a skill does not silently activate its interview,
approval, orchestration or external-action requirements.

## Provenance of the independently written synthesis

The entries below are **inspiration**, not copied text or vendored skills. These
credits identify the ideas used; source licenses do not become this project's
license merely because we link to them. Pinning records what was reviewed and
does not imply upstream endorsement. Initial repository sources reviewed
2026-11-05; LangChain, Next.js, Humanizer and the web article below reviewed 2026-11-06;
Strunk's text reviewed 2026-11-07.

### Structure and placement

- Credit: GitHub, Inc. and awesome-copilot contributors.
- Source: [github/awesome-copilot/skills/documentation-writer/SKILL.md](https://github.com/github/awesome-copilot/blob/96543145e9cb97711020b57b9d88f968062c4fc7/skills/documentation-writer/SKILL.md).
- Reviewed revision: `96543145e9cb97711020b57b9d88f968062c4fc7`.
- Upstream license: [MIT](https://github.com/github/awesome-copilot/blob/96543145e9cb97711020b57b9d88f968062c4fc7/LICENSE).
- Use: independently written guidance informed by this perspective. Choose the document type, reader, task and scope.

### Repository information architecture

- Credit: Samuel Berthe (samber) and contributors.
- Source: [samber/developer-relations-skills/skills/developer-docs-structure-audit/SKILL.md](https://github.com/samber/developer-relations-skills/blob/a2ae344aa93847e45a1ecb8b2e87c69a8a0b5d6e/skills/developer-docs-structure-audit/SKILL.md).
- Reviewed revision: `a2ae344aa93847e45a1ecb8b2e87c69a8a0b5d6e`.
- Upstream license: [MIT](https://github.com/samber/developer-relations-skills/blob/a2ae344aa93847e45a1ecb8b2e87c69a8a0b5d6e/LICENSE).
- Use: independently written guidance informed by this perspective. Inventory before judging structure; look for mixed purposes, duplicate accounts and navigation drift.

### Predictable navigation

- Credit: **Raluca Budiu / Nielsen Norman Group**.
- Source: [Information Scent: How Users Decide Where to Go Next](https://www.nngroup.com/articles/information-scent/), published 2020-02-02; reviewed 2026-11-06. This web article has no pinned repository revision.
- Rights: NN/G's [copyright and reprint policy](https://www.nngroup.com/copyright-and-reprint-info/) reserves rights and permits linking.
- Use: conceptual inspiration for checking that a link and its context help readers
  anticipate the destination's answer. No article wording, artwork or checklist
  is reproduced; the local instruction is independently written.

### Audience and first success

- Credit: Leonardo Flores / Softaworks and contributors.
- Source: [softaworks/agent-toolkit/skills/crafting-effective-readmes/SKILL.md](https://github.com/softaworks/agent-toolkit/blob/3027f20f3181758385a1bb8c022d4041dfb4de84/skills/crafting-effective-readmes/SKILL.md).
- Reviewed revision: `3027f20f3181758385a1bb8c022d4041dfb4de84`.
- Upstream license: [MIT](https://github.com/softaworks/agent-toolkit/blob/3027f20f3181758385a1bb8c022d4041dfb4de84/LICENSE).
- Use: independently written guidance informed by this perspective. Match the entry page to its audience and the quickest working path.

### Sentence-level editing

- Credit: Leonardo Flores / Softaworks and contributors.
- Source: [softaworks/agent-toolkit/skills/writing-clearly-and-concisely/SKILL.md](https://github.com/softaworks/agent-toolkit/blob/3027f20f3181758385a1bb8c022d4041dfb4de84/skills/writing-clearly-and-concisely/SKILL.md).
- Reviewed revision: `3027f20f3181758385a1bb8c022d4041dfb4de84`.
- Upstream license: [MIT](https://github.com/softaworks/agent-toolkit/blob/3027f20f3181758385a1bb8c022d4041dfb4de84/LICENSE).
- Use: independently written guidance informed by this perspective. Apply selective copyediting after content decisions; preserve precise technical meaning.

### Change-aware editorial review

- Credit: **LangChain and contributors**.
- Sources: [docs-review](https://github.com/langchain-ai/docs/blob/0e9200466a1424c828266939ada9c0d32a90f78c/.agents/skills/docs-review/SKILL.md) and its [CI guidance](https://github.com/langchain-ai/docs/blob/0e9200466a1424c828266939ada9c0d32a90f78c/.agents/skills/docs-review/ci-mode.md).
- Reviewed revision: `0e9200466a1424c828266939ada9c0d32a90f78c`.
- Upstream license: the skill declares MIT, consistent with the [root license](https://github.com/langchain-ai/docs/blob/0e9200466a1424c828266939ada9c0d32a90f78c/LICENSE); no more-specific license or notice files were found under `.agents`.
- Use: independently written guidance for scoped review, preserving meaning when
  shortening text and following contradictions caused outside the diff. House
  phrase rules, CI schemas and automation are not adopted.

### Code-change impact

- Credit: **Vercel, Inc. and Next.js contributors**.
- Sources: [update-docs](https://github.com/vercel/next.js/blob/4f350fb33cfbdb13b63ecd2d594e8588f6d667e0/.agents/skills/update-docs/SKILL.md) and its [code-to-docs mapping](https://github.com/vercel/next.js/blob/4f350fb33cfbdb13b63ecd2d594e8588f6d667e0/.agents/skills/update-docs/references/CODE-TO-DOCS-MAPPING.md).
- Reviewed revision: `4f350fb33cfbdb13b63ecd2d594e8588f6d667e0`.
- Upstream license: [MIT](https://github.com/vercel/next.js/blob/4f350fb33cfbdb13b63ecd2d594e8588f6d667e0/license.md); no more-specific license or notice files were found under `.agents`.
- Use: independently written guidance tracing source changes to documentation
  impact. Verify mapping entries before relying on them. Next.js paths, templates
  and confirmation steps are not adopted. No source text is included.

### Composition and sentence clarity

- Credit: **William Strunk Jr.**, *The Elements of Style*, 1920 edition; electronic
  transcription by Jana Srna and the Online Distributed Proofreading Team.
- Source: [Project Gutenberg eBook 37134, Chapter III](https://www.gutenberg.org/files/37134/37134-h/37134-h.htm).
  The ebook was last updated 2011-08-19; reviewed 2026-11-07. Selected principles
  from sections 8, 10–13 and 15–16 inform the prose criteria.
- Rights: the [catalogue](https://www.gutenberg.org/ebooks/37134) identifies the
  underlying text as public domain in the USA. The ebook carries Project Gutenberg
  distribution terms; no ebook text or examples are reproduced here.
- Use: conceptual inspiration, independently written. The local criteria preserve
  project voice, necessary detail, useful passive voice and direct prohibitions.
  Later Strunk–White editions and the book's full usage catalogue are not adopted.

### Compact prose pass

- Credit: **Siqi Chen (blader) and Humanizer contributors**.
- Source: [blader/humanizer/SKILL.md](https://github.com/blader/humanizer/blob/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0/SKILL.md), version 3.1.0.
- Reviewed revision: `0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0`.
- Upstream license: [MIT, copyright 2025 Siqi Chen](https://github.com/blader/humanizer/blob/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0/LICENSE). No more-specific license/notice files were found in the inspected tree.
- Use: conceptual inspiration for a small prose pass, written independently.
  Staged openings, repetitive rhythm and inflated claims merit contextual review.
  Ken Hawkins's em-dash preference allows useful exceptions; Humanizer's full
  pattern catalogue, strict dash rule and output workflow are not adopted.
- Lineage: Humanizer credits [Wikipedia's Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. Neither source prose nor its examples are reproduced here.

### Documentation framework

- Credit: **Daniele Procida**, creator of [Diátaxis](https://diataxis.fr/), including
  the [compass](https://diataxis.fr/compass/) and incremental application guidance.
- Reviewed source revision: `957c09ca40b4a1edc23874f713e01937d50d54d5`.
- Upstream license: [CC BY-SA 4.0](https://github.com/evildmp/diataxis-documentation-framework/blob/957c09ca40b4a1edc23874f713e01937d50d54d5/LICENSE.rst).
- Use: conceptual inspiration and source links. No website prose, diagrams or
  translations are reproduced here. A future textual adaptation must be reviewed
  under its actual license rather than treated as original project prose.

### Minimum viable documentation

- Credit: **Google and the Google style-guide contributors**.
- Source: [Documentation Best Practices](https://github.com/google/styleguide/blob/e22e4c6fb737bc68cdc973a81dff0e7f88f26b94/docguide/best_practices.md).
- Reviewed revision: `e22e4c6fb737bc68cdc973a81dff0e7f88f26b94`.
- Upstream license for repository prose: [CC BY 3.0](https://github.com/google/styleguide/blob/e22e4c6fb737bc68cdc973a81dff0e7f88f26b94/LICENSE).
- Use: inspiration for maintaining a smaller, accurate set of explanations and
  linking instead of duplicating. No source prose is reproduced.

### Fresh-reader review

- Credit: **Anthropic and contributors**, [doc-coauthoring](https://github.com/anthropics/skills/blob/ca45fc496a3436251f191354091d557da31c15b5/skills/doc-coauthoring/SKILL.md).
- Reviewed revision: `ca45fc496a3436251f191354091d557da31c15b5`.
- Use: inspiration for evaluating documentation with a reader who lacks the
  author's context. The local instructions and fixtures are independently written.
- License status: no license for this skill was located in its frontmatter,
  directory or repository root at the inspected revision. The repository's
  third-party notices do not establish a license for this skill. Do not copy,
  adapt its wording or vendor it without establishing permission.

The Softaworks writing skill also explicitly credits **William Strunk Jr.'s
1918 _The Elements of Style_** for its composition principles. That credit is
retained here as lineage; no book text or its companion reference files are
included in this skill.
