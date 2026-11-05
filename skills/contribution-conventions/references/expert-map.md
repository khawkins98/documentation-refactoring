# Contribution sources and reuse

Use the relevant specialist for the contribution task. This local skill combines
a standard commit vocabulary with the maintainer's explicitly overridable title,
description and attribution preferences. It does not require installing an
upstream skill or activating an external workflow.

## Direct reuse: commit-type reference

- Credit: **dmythro and contributors**, `dmythro/agent-skills`.
- Source: [git-commit / Types](https://github.com/dmythro/agent-skills/blob/91e6bb1a8405a00c350cea9207c18d11feb88f2f/skills/git-commit/SKILL.md).
- Reviewed revision: `91e6bb1a8405a00c350cea9207c18d11feb88f2f`.
- Local file: [commit-types.md](upstream/dmythro/commit-types.md).
- Reuse: **unmodified excerpt** of the upstream Types table; the rest of the skill
  is not vendored. No changes to the excerpt.
- Source file SHA-256: `580d1ec0bf04b653f5d24b623c72b82b4326c4ca0a992fb70f8771fec5ed35cc`.
- Local excerpt SHA-256: `34afb68159920312932590ed419cf3907283420c3ea5333b1d1aae1f0e801a2c`.
- License: upstream [MIT notice](upstream/dmythro/LICENSE), preserved byte-for-byte
  from [the same revision](https://github.com/dmythro/agent-skills/blob/91e6bb1a8405a00c350cea9207c18d11feb88f2f/LICENSE). The upstream
  notice has no named copyright line; no new one has been invented for it.

For commit type lookup, read that table. The surrounding guidance in our skill
is independently written. Project requirements and user instructions still
control titles and attribution; the excerpt is a vocabulary, not new authority.
The two skills' fixtures remain original project material.

## Standard and inspiration

- **Conventional Changelog / Conventional Commits contributors**: the
  [Conventional Commits specification](https://www.conventionalcommits.org/) supplies
  the syntax used by the local preferences. Reviewed repository revision
  `7d293dc59e88abc8ce6c6698344d4da518ff3f27`;
  [upstream MIT license](https://github.com/conventional-commits/conventionalcommits.org/blob/7d293dc59e88abc8ce6c6698344d4da518ff3f27/LICENSE).
  Source link and conceptual application only; no specification prose is copied.
- **dmythro and contributors**: the same upstream git-commit skill also informed
  attention to project overrides, meaningful titles and optional concise bodies.
  Our workflow instructions are rewritten synthesis, not a copy of that skill.
- **Ken Hawkins's project conventions** supply the local defaults and are labeled
  as preferences. They are not presented as requirements of Conventional Commits.

Reviewed 2026-11-05. Upstream authors are credited for their work; inclusion does
not imply endorsement. When updating the direct excerpt, record the new revision,
verify the license at that revision, preserve its notice and describe changes.
