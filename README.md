# Reader First

Two highly opinionated agent skills for contributions and documentation.

I made these because I kept giving AI agents the same brief on every project,
then cleaning up the results. They capture how I like to work so I can reuse
those preferences instead of explaining them again.

| Skill | Use it for |
| --- | --- |
| [contribution-conventions](skills/contribution-conventions/SKILL.md) | My contribution defaults: Conventional Commits, focused PRs, and no unsolicited AI co-author trailers or tool signatures. |
| [documentation-refactoring](skills/documentation-refactoring/SKILL.md) | The more broadly useful one: separate reader tasks, keep explanations in maintained homes, fix stale guidance and give prose a light style pass. |

Use either skill on its own or adapt it to your project. Project and user
instructions take precedence over my defaults. Neither skill grants permission
to push, publish or merge.

The foundations belong to their authors: **Daniele Procida (Diátaxis), GitHub and
awesome-copilot contributors, Samuel Berthe, Leonardo Flores / Softaworks,
William Strunk Jr., Google, Anthropic, Siqi Chen (Humanizer), dmythro and the
Conventional Commits contributors**.
The [source and reuse records](SOURCES.md) credit each contribution and distinguish
inspiration, adaptation and direct reuse.

## Before and after

From this README:

**[Before](https://github.com/khawkins98/reader-first/blob/6d937cfcc60c923ba5a35920f67e45884f9b3e3d/README.md)**

> A curated, mixture-of-experts-style collection of agent skills for maintaining
> repository documentation. It brings together established specialists in document
> structure, audience, prose, reader review and contribution conventions, with a
> small layer for selecting and applying their methods to a project.

**[After](https://github.com/khawkins98/reader-first/blob/a25afe268fbcafa940b302902927af851c23cacf/README.md)**

> Two highly opinionated agent skills for contributions and documentation.

## Use

With Node.js 22.20 or later, run the [Skills CLI](https://github.com/vercel-labs/skills#install-a-skill)
from your target repository. It prompts for your agent and installs into that
project by default. Add `-g` to make a skill available across projects.

Install one or both:

```sh
npx skills add khawkins98/reader-first --skill documentation-refactoring
npx skills add khawkins98/reader-first --skill contribution-conventions
```

To use a local Reader First checkout, replace `khawkins98/reader-first` with its path.
You can also copy a selected skill folder to your agent's supported skills directory.

To try once without installing the skill into your project:

```sh
npx skills use khawkins98/reader-first@documentation-refactoring
```

This prepares temporary skill files and prints a prompt for a local agent. See
the [command reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-use)
for options to launch an agent directly.

For a single-page documentation task, ask your agent:

> Use $documentation-refactoring to improve README.md for a first-time reader.
> Keep the setup working, preserve required technical detail and verify the
> reader paths.

When preparing a contribution:

> Use $contribution-conventions to prepare a PR title and description for this
> diff, following this repository's contribution rules. Report the checks run.

Both skills are self-contained. Each skill's linked expert map explains its
specialist perspectives.

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
