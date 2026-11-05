---
name: documentation-refactoring
description: Apply a curated mix of documentation specialists to refactor existing repository docs around reader tasks, consolidate stale or duplicate explanations and verify the result. Use for README cleanup or repository-wide maintenance, scaled to the requested scope.
---

# Documentation refactoring

Improve readers' ability to choose a path, complete a task and find the maintained
contract. Shorter prose is useful only when those outcomes and necessary detail
survive. This skill does not require a particular documentation tree or companion
skill.

## Select the useful perspectives

Combine the lenses the task needs: Diátaxis and GitHub's documentation writer for
structure; Samuel Berthe's audit for information architecture; Leonardo Flores /
Softaworks for audience and prose; Google for maintenance; and Anthropic's
coauthoring workflow for fresh-reader checking. These are credited sources of the
independently written synthesis, not claims of a new documentation framework.
The [expert map and source records](references/expert-map.md) explain when each
lens helps, reviewed revisions and source-license boundaries. Consult them when
selecting a broad approach or checking provenance, not for every small correction.
No external skill installation, agent team or remote fetch is required.

## Establish scope and authority

Read applicable repository instructions and the user's requested boundaries.
For a small correction, inspect the affected page and relevant source/example.
For a repository-wide pass, first inventory paths, readers, purposes and sources
of truth. Classify from permitted metadata before opening restricted evidence.
Do not turn documentation maintenance into permission to inspect forbidden
material, change runtime behavior, alter release scope or publish anything.

Distinguish maintained instructions, lookup reference, explanation, proposals,
records, evidence, provenance and generated output. A dated failed experiment is
not stale usage advice. Preserve its original claims, conditions and limitations;
use a dated superseding note or navigation pointer when needed. Exact bytes must
survive when project evidence rules require it. When a generated document needs
updating, use its existing source or generator rather than editing it as ordinary
prose.

A canonical documentation home is the maintained reader-facing explanation.
Code, generated declarations or an adopted specification can remain its technical
authority. Resolve discrepancies using the project's authority rules; report
uncertainty rather than quietly choosing whichever source makes rewriting easiest.

## Refactor the reader's path

- Name the primary reader and result. Use Diátaxis to distinguish a tutorial
  (learning), how-to (a task), reference (lookup) and explanation (understanding).
  Do not force every project into four directories or split every heading.
- Keep the entrance focused on orientation, a complete first success, material
  adoption limits and useful routes. Preserve the project's voice where it helps.
- Update one authoritative explanation before adding another. Keep examples
  self-contained enough to run, but link exhaustive options and background.
  Merge duplicate accounts and retire obsolete active advice.
- Review material as keep, move, merge, delete or verify. Move it only when the
  destination serves an identifiable need. Do not bury prerequisites, cleanup,
  compatibility, accessibility or redistribution constraints to meet a word target.
- Prefer links to maintained inventories and release records over copied counts,
  rolling implementation status and recaps of every recent change.

For README work or a broad pass, assess the entrance explicitly: choose what
stays, moves or shortens, and explain an unchanged README. Apply the placement
and prose criteria in [entrance and style review](references/entrance-and-style.md)
when editing an entrance or polishing prose. Treat unresolved duplication,
unsupported claims and lost reader limits/credits as findings to resolve or report;
a shorter page or a passing link check alone does not establish editorial quality.

For a larger sweep, read [repository-wide work](references/repository-wide.md).
For a focused edit, the guidance here is sufficient.

## Verify the result

Check changed commands, names and claims against allowed source or executable
examples. Check moved relative links, heading anchors, inbound references and
agent-discovery files. A resolving link does not establish a working task: when a
linked helper depends on a changed UI or API, inspect its executable entrypoint
and current inputs. Repair it only within scope; otherwise identify its limitation
and route readers to a maintained alternative. Retain compatibility routes where
their navigation value justifies them.

Inspect the project's actual publication or packaging contract before moving
pages. A link that resolves in the checkout may fail in an installed package,
rendered site, source archive or release artifact. Exercise affected examples at
the boundary readers will use; apply the project's required checks without
inventing a full-suite requirement for every prose edit.

A missing-input error may mean an unset path rather than an absent asset. Check
the configuration and documented or explicitly permitted local locations, and
verify the required version/hash before declaring a blocker. Stay within the
authorized scope; do not substitute or publish restricted inputs to obtain a pass.

Test representative reader tasks: choosing a setup, reaching a working result,
finding an advanced option and identifying a relevant limitation. A fresh agent
can help when authorized and useful, but is not a user study. State exactly what
was checked and what remains uncertain. Distinguish command success from the
capabilities exercised: inspect skips and review-only warnings before claiming
validation. Synthetic fixtures and historical results keep their own conditions;
they do not establish current live behavior. Record validation substitutions,
such as reused dependencies instead of a fresh install or local assets/URLs
instead of the published example; report which original boundaries remain untested.

For broad cleanups, report both entrance-page size and total documentation change,
including added files and relocated material. Counts diagnose growth; they are
not a success criterion. Explain the navigation tradeoff and remaining long
references. Update the existing maintenance instructions that caused repeated
append-only growth; do not introduce an audit framework without a concrete need.

Deliver within the user's authorization. An authorized draft PR needs no new
permission ceremony, but the skill itself does not authorize push, publication,
merging or installing persistent configuration. Follow the project's contribution
rules if commits or PRs are part of the task.

Foundational method links (full credits in the expert map): [Diátaxis](https://diataxis.fr/compass/),
[applying it incrementally](https://diataxis.fr/how-to-use-diataxis/), and
[Google's minimum viable documentation guidance](https://google.github.io/styleguide/docguide/best_practices.html).
