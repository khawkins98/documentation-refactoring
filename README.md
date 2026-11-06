# Reader First

A curated, mixture-of-experts-style collection of agent skills for maintaining
repository documentation. It brings together established specialists in document
structure, audience, prose, reader review and contribution conventions, with a
small layer for selecting and applying their methods to a project.

The foundations belong to their authors: **Daniele Procida (Diátaxis), GitHub and
awesome-copilot contributors, Samuel Berthe, Leonardo Flores / Softaworks, Google,
Anthropic, dmythro and the Conventional Commits contributors**. The
[source and reuse records](SOURCES.md) credit each contribution and distinguish
inspiration, adaptation and direct reuse.

| Skill | Use it for |
| --- | --- |
| [documentation-refactoring](skills/documentation-refactoring/SKILL.md) | README cleanup, stale or duplicated guidance, repository-wide documentation maintenance |
| [contribution-conventions](skills/contribution-conventions/SKILL.md) | Conventional commit/PR titles, clear review descriptions and maintainer attribution preferences |

The skills are independent. Documentation refactoring does not require the
contribution skill, and neither grants permission to push, publish or merge.
Project and user instructions take precedence over these defaults.

## Use

Use Node.js with npm/npx. Install one or both with the
[Skills CLI](https://skills.sh/docs/cli):

```sh
npx skills add khawkins98/reader-first --skill documentation-refactoring
npx skills add khawkins98/reader-first --skill contribution-conventions
```

From a local checkout, use `.` as the source:

```sh
npx skills add . --skill documentation-refactoring
```

You can also copy a selected skill folder to your agent's supported skills directory.
Invoke `$documentation-refactoring` for the documentation task, and
`$contribution-conventions` when preparing the requested contribution.

For example:

> Use $documentation-refactoring to improve this repository's documentation.
> Keep the setup working, separate current instructions from historical records,
> preserve required technical detail and verify the reader paths. Open a draft PR.

The workflow scales down to a single page and is self-contained. Selecting the
specialist perspectives is covered in each skill's linked expert map.

## Develop the skills

[CONTRIBUTING](CONTRIBUTING.md) covers edits, validation and source reuse.
The [evaluation index](evals/README.md) links runnable scenarios and application
records with their checks, interventions and limitations. Syntax checks and these
same-project trials do not establish general effectiveness.

## License

Original prose uses [CC BY 4.0](LICENSE); code, executable fixtures and code/command
examples use [MIT](LICENSE-MIT). The [licence map](LICENSING.md) defines the split.
Third-party material retains its [upstream terms](THIRD_PARTY_NOTICES.md), and each
installable skill carries its own licence map and both full texts.
