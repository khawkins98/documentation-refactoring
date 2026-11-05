# Documentation refactoring

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

## Choose the useful specialists

| Need | Perspective we draw from |
| --- | --- |
| Distinguish learning, tasks, reference and explanation | Daniele Procida's Diátaxis; GitHub's documentation writer |
| Find mixed purposes, duplicate accounts and navigation drift | Samuel Berthe's docs structure audit |
| Fit a README to its audience and edit prose | Leonardo Flores / Softaworks' README and writing guidance |
| Maintain a smaller, accurate documentation set | Google's documentation practices |
| Check whether a fresh reader can use the result | Anthropic's coauthoring workflow; local evaluation fixtures |
| Prepare contribution titles and descriptions | Conventional Commits; dmythro's git-commit reference; project preferences |

Here, experts means specialist methods and source skills. One agent can apply the
needed perspectives; multiple agents are optional when authorized. The collection
is self-contained and does not automatically install or invoke external skills.

## Use

Install one or both with the [Skills CLI](https://skills.sh/docs/cli):

```sh
npx skills add khawkins98/documentation-refactoring --skill documentation-refactoring
npx skills add khawkins98/documentation-refactoring --skill contribution-conventions
```

You can also copy a selected skill folder to your agent's supported skills directory.
Invoke `$documentation-refactoring` for the documentation task, and
`$contribution-conventions` when preparing the requested contribution.

For example:

> Use $documentation-refactoring to improve this repository's documentation.
> Keep the setup working, separate current instructions from historical records,
> preserve required technical detail and verify the reader paths. Open a draft PR.

The workflow scales down to a single page. It does not install a documentation
framework, impose a folder tree or require an agent team.

## Develop the skills

Edit the instructions in `skills/`. Keep the entrypoints short and load supporting
references only when useful. Change rules in response to demonstrated behavior,
not by collecting a checklist for every past incident.

[CONTRIBUTING](CONTRIBUTING.md) describes how to review and evaluate changes.
[Evaluation scenarios](evals/README.md) exercise scope, authority, historical records,
distribution and contribution-rule conflicts. They complement syntax validation;
they do not prove the skill works in every project.

The [Scriptoscope case study](skills/documentation-refactoring/references/scriptoscope-lessons.md)
records where the method was tried and distinguishes reusable lessons from local
packaging and browser-lifecycle findings. The [Johnny Web application](evals/johnny-web-application.md)
records a second real-repository trial, semantic helper failures and validation
limits; neither case study is a held-out benchmark.

## License

Original contributions: [MIT](LICENSE). Directly reused material retains its
[upstream notices](THIRD_PARTY_NOTICES.md), including notices inside the installable
skill. See [SOURCES](SOURCES.md) for exact relationships and reviewed revisions.
