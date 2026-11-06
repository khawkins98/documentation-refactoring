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
awesome-copilot contributors, Samuel Berthe, Leonardo Flores / Softaworks, Google,
Anthropic, Siqi Chen (Humanizer), dmythro and the Conventional Commits contributors**.
The [source and reuse records](SOURCES.md) credit each contribution and distinguish
inspiration, adaptation and direct reuse.

## Before and after

A small illustrative repair, based on the [synthetic Tidy fixture](evals/fixtures/small-cli/):

**Before**

> Use `--force` to overwrite a file. You can preview with `--check`.

**After**

> With Python 3 and an existing `input.txt`, run:
>
> ```sh
> python3 tidy.py input.txt --output clean.txt --dry-run
> ```
>
> It prints `Would write clean.txt` without changing files. Remove `--dry-run` to
> write the cleaned text; an existing `clean.txt` is replaced.

The revised instructions use supported flags, show the expected result and explain
what gets overwritten. Broader passes also consolidate duplicate explanations and
give detailed reference material a maintained home.

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
