# Changed-entrypoint fixture checks — 2026-11-05

These are maintainer smoke checks of Scenario E, not an independent behavioral
evaluation of the revised skill. The maintainer knew the fixture's design and
wrote the example README correction. A future blind evaluator should receive
only the task, skill and raw fixture specified in the scenario.

## Executed checks

A disposable copy of all five fixture files was made. Both Python commands ran
with `-B` to avoid bytecode files:

| Command | Exit | Observed output |
| --- | --- | --- |
| `python3 -B preview.py` | 1 | `ERROR: launch control #launch-classic not found` |
| `python3 -B verify.py` | 0 | Public control PASS, manual layout-review WARN, reference-rendering SKIP because `reference.bin` is not supplied |

Before/after hashes confirmed execution left all five copied files unchanged.
A maintainer-authored README correction then replaced the helper launch advice
with the current local page/Play route, identified the old helper's limitation,
and separated the passing public check from the warning and unavailable check.
The existing headings were retained; only README changed and no file was added.
No source repair, reference creation, network, Git mutation or installation was
performed in the fixture workspace.

This demonstrates that the raw scenario exposes the intended decision and that
a scoped documentation correction is possible. It does not demonstrate how an
independent agent would respond, validate rendered pixels, exercise the optional
reference-present branch, or establish superiority over the prior skill.
