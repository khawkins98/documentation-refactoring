# Documentation refactoring

Reusable agent skills for making repository documentation easier to use and
maintain. The method combines task-oriented organization, Diátaxis, progressive
disclosure and one maintained explanation per contract. It aims to improve reader
outcomes, rather than minimize word counts.

| Skill | Use it for |
| --- | --- |
| [documentation-refactoring](skills/documentation-refactoring/SKILL.md) | README cleanup, stale or duplicated guidance, repository-wide documentation maintenance |
| [contribution-conventions](skills/contribution-conventions/SKILL.md) | Conventional commit/PR titles, clear review descriptions and maintainer attribution preferences |

The skills are independent. Documentation refactoring does not require the
contribution skill, and neither grants permission to push, publish or merge.
Project and user instructions take precedence over these defaults.

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
packaging and browser-lifecycle findings.

## License

[MIT](LICENSE).
