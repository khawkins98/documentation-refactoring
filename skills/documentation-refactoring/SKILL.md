---
name: documentation-refactoring
description: Refactor existing repository documentation around reader tasks, correct stale instructions, consolidate duplicate explanations and verify affected reader paths. Use for README cleanup, documentation navigation or repository-wide maintenance, scaled to the requested scope.
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

For an update prompted by code changes, trace the relevant diff to affected reader
tasks, examples and shared-content consumers. Treat code-to-docs maps as search
leads; verify current paths and behavior. Check related pages for contradictions
caused by the change without widening into unrelated cleanup. An internal
refactor may need no documentation change.

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
Keep implementation and approval distinct. When a prototype differs from a
proposal or requirement, preserve its intent and approval status; add a dated
implementation note or open question. Changing acceptance or release criteria
follows the project's decision process, rather than being inferred from code.

## Refactor the reader's path

- Name the primary reader and result. Use Diátaxis to distinguish a tutorial
  (learning), how-to (a task), reference (lookup) and explanation (understanding).
  Do not force every project into four directories or split every heading.
- Keep the entrance focused on orientation, a complete first success, material
  adoption limits and useful routes. Preserve the project's voice and clear product
  pitch; place practical caveats where readers need them to act.
- Update one authoritative explanation before adding another. Keep examples
  self-contained enough to run, but link exhaustive options and background.
  Route contributor and agent entrances to maintained setup/rules instead of
  copying them, retaining any instructions required at those entrypoints.
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

Read [repository-wide work](references/repository-wide.md) for a larger sweep;
it is unnecessary for a focused edit.

## Verify the result

Verify changed commands, names and claims against permitted source or executable
examples. Check affected relative links, anchors, inbound references and
agent-discovery files. Follow linked helpers far enough to establish that their
current inputs and entrypoints support the documented task; a resolving link is
insufficient. Repair defects within scope, or describe the limitation and route
readers to a maintained alternative.

Exercise representative reader paths affected by the change. For a handoff,
include the recipient's prerequisites and how they open or restore the result.
Apply the project's required checks and choose additional checks for the
capability being claimed; a small prose correction does not require a full
product tour or test suite. A fresh agent can help when authorized and useful,
but is not a user study.

Before moving pages, inspect the publication or packaging contract. Verify
affected routes and examples where readers use them, since checkout,
installed-package and published-site behavior can differ. Preserve compatibility
routes when they serve actual readers.

Before declaring a missing-input blocker, check configuration and documented or
explicitly permitted locations, including any required version or hash. Do not
substitute restricted inputs or change persistent configuration without
authorization.

Report what the checks establish and what remains uncertain. Distinguish
successful commands from skipped checks, review warnings and capabilities not
exercised. Disclose substitutions such as reused dependencies or local URLs,
and the original boundary left untested. Historical results and synthetic
fixtures retain their own conditions.

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
