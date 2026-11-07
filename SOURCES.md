# Sources and composition

This repository is a curated mix of established specialist approaches, with a
small local layer for choosing, applying and checking them in a project.

| Skill | Sources and relationship |
| --- | --- |
| [Documentation refactoring](skills/documentation-refactoring/SKILL.md) | [Expert map and credits](skills/documentation-refactoring/references/expert-map.md): Diátaxis by Daniele Procida; GitHub's documentation writer; Samuel Berthe's docs structure audit; Raluca Budiu / NN/G's information scent; Leonardo Flores / Softaworks' README and prose guidance; William Strunk Jr.'s composition principles; Siqi Chen's Humanizer; LangChain's change-aware review; Vercel / Next.js's code-change routing; Google's documentation practices; Anthropic's fresh-reader workflow |
| [Contribution conventions](skills/contribution-conventions/SKILL.md) | [Reuse record](skills/contribution-conventions/references/expert-map.md): Conventional Commits, dmythro's git-commit skill and the maintainer's project preferences |

Each record identifies its source, author/project credit, reviewed repository
revision (or publication and review dates for web-only sources), rights evidence
and local application. The categories mean:

- **Inspired by:** concepts inform independently written instructions; source text
  is not included. Credit the work without implying that we invented the method.
- **Adapted from:** wording or an artifact is modified from a source. Identify the
  changed files, original revision, modifications and applicable notices/terms.
- **Direct reuse:** an unmodified file or excerpt is included, with its source,
  scope and license notice. Preserve upstream credit when installing that skill.

The initial version uses independently written synthesis plus one directly
reused commit-type table. It does not vendor whole external skills. If a license
is unclear, reference the source but do not copy its wording or artifacts until
permission is established. The attribution files and required notice travel
inside the installable skill folders; this root index is not their only record.

Original prose uses [CC BY 4.0](LICENSE); code and examples use [MIT](LICENSE-MIT),
as defined in the [licence map](LICENSING.md). Reused material keeps the terms
identified in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Public visibility,
a directory's badge or another repository's top-level license alone is not a
substitute for checking the actual material and any more-specific notices.
