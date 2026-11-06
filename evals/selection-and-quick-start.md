# Selection and quick-start checks — 2026-11-06

## Inputs and scope

The fresh advisory review recommended clearer installation scope, an easier trial
route and less repetition between the documentation entrypoint and references.
It also identified that A–H explicitly name a skill, leaving selection untested.

These maintainer-run checks used the skills at
`0b20fce6206013c3b499bb3edbe8e0629ba75eae`. The PR leaves both descriptions and
agent metadata unchanged. It consolidates repeated authority, distribution and
size-reporting instructions while preserving their governing rules in the
entrypoint; the actual-artifact check now explicitly covers affected routes and
packaging. Prior evaluation records, fixtures, credits and licence files remain
unchanged. The consolidation was source-reviewed, not independently replayed
against all earlier behavioral scenarios.

## One-off CLI route

With Node.js `24.18.0`, executed the published Skills CLI `1.7.6`:

```sh
npx --yes skills@1.7.6 use khawkins98/reader-first@documentation-refactoring
```

The maintainer used a disposable directory and npm cache, disabled CLI telemetry
and captured stdout/stderr rather than launching an agent. Exit status was zero.
The output contains the skill instructions and a temporary directory for resolving
relative references. The maintainer compared all nine downloaded package files
with the pinned source, including supporting references and full licence texts.
No project skill directory or lock file was installed. This verifies prompt
generation and package retrieval, not the optional agent-launch mode or a full
documentation task through that generated prompt.

The [CLI requirements](https://github.com/vercel-labs/skills#install-a-skill)
specify Node.js 22.20 or later, project scope by default and agent selection;
`-g` changes installation to user scope. The
[command reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-use)
describes temporary preparation and optional direct agent launch. No upstream
prose is imported into the skill.

## Selection without naming the skill

Each request ran in a separate disposable directory through Codex CLI `0.167.0`,
with both skill folders copied to `.agents/skills`. Each directory contained the
raw Scenario H README and operational rules limiting the agent to read-only
inspection, with no network tools, installation or Git mutation. These are the
exact requests; no skill name or preferred selection was supplied:

1. “Please copyedit this README into clear, natural prose while preserving its
   facts and the writer's voice. Show the proposed wording without editing files.”
2. “Prepare a commit message for changing an existing export feature from an
   undocumented overwrite to a documented preview-first workflow. There is no
   breaking runtime change. Follow the project's contribution rules; do not make
   a commit.”
3. “Explain at a high level how git rebase differs from git merge for someone
   learning Git. Do not inspect or change this repository, and do not prepare a
   contribution.”

Invocation for each independent session, with its own request file:

```sh
codex exec --ignore-user-config --ephemeral --sandbox read-only \
  --skip-git-repo-check --json -C /path/to/disposable-project - < request.txt
```

| Request | Observed skill reads in the JSON event trace |
| --- | --- |
| README copyedit | Documentation entrypoint and entrance/style reference |
| Commit message | Contribution entrypoint |
| Git explanation | Neither skill; no repository/tool inspection |

All three sessions completed with exit status zero. Two emitted transient
transport-retry messages before succeeding. File comparisons confirmed all 19
input files in each project remained byte-identical, with no additions. Agent
tool traces contained only read commands. The prose response retained the pitch,
personal origin, credit, capabilities, limits and literal UI/command strings.
The contribution response supplied a proposed message; no real contribution diff
was supplied, so its accuracy is not independently established.

This is one request per category in one host. The default model was not pinned;
existing user/system skills were also available. These observations support
selection for the tested prompts, not a general routing success rate, other-host
compatibility, causal improvement over a plain prompt or coverage of every
documentation review/change-triggered task. No description expansion follows
from these results.
