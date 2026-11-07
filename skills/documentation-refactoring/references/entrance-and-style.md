# Entrance placement and editorial review

Use for README work, broad refactoring or a prose/style pass. These criteria apply
to maintained guidance, not a license to rewrite dated evidence or required notices.
They independently apply the audience/prose/structure perspectives credited in
[the expert map](expert-map.md); no upstream prose is reproduced.

## Decide what the entrance serves

Name the primary reader and the first useful result. Review the README itself,
even when duplication is more obvious in contributor/agent files. For each large
section, decide keep, shorten, move or merge. Leaving the entrance unchanged is
valid when it already serves the reader or is outside scope.

| Material | Placement decision |
| --- | --- |
| What this is, who it helps, first success | Keep the concise explanation and complete setup/download path at the entrance. |
| Adoption limits, prerequisites, access/privacy/platform caveats | Summarize what changes the choice to use the tool or the first task. Put actionable caveats beside the affected step; link detailed compatibility and troubleshooting guidance. |
| Competitor tables, pricing or a dated survey | Summarize why the project exists; use a clearly dated comparison page if the survey remains useful. Moving it does not refresh its claims. |
| Detailed implementation, endpoint inventories, audit commands | Route to an existing technical/privacy guide; create one only for a concrete reader task. |
| Personal origin and acknowledgements | Preserve the project's voice and visible credit. Longer provenance can move with an obvious link; required notices and source-use restrictions must survive. |
| Exhaustive command catalogs and navigation | Link the canonical task/reference guide; do not replace one large README with an equally large index. |

Update the destination before removing the old account. Check inbound anchors and
relative links after relocation. Check that the remaining link and its context
let the intended reader predict what the destination answers. Do not pursue a
percentage reduction by hiding critical limits,
fragmenting a short explanation or deleting evidence.

For each discovered detail, identify the decision or action it changes. First use
needs a complete path, not an explanation of every option and failure mode.
Route later lookup to its maintained home. Review findings and validation logs
are evidence for the change; they need not all become user-facing guidance.

When the product also ships onboarding or help for the same task, compare those
active instructions with the README. Correct conflicting labels, prerequisites
and promises within scope, or report the remaining conflict. A complete producer
path can still leave a new recipient unable to install, open or restore a result.

## Apply the prose criteria

For a diff review, identify reader regressions and applicable project-rule
violations, keeping optional preferences separate. Read enough surrounding text
to understand the change; leave unrelated prose outside the review. Finding no
issue is a valid outcome. When editing, honor project/user style and required
wording:

- Make the smallest edit that resolves the reader's problem. If one format,
  label or clause is wrong, correct that part before rewriting a working paragraph.
  Preserve its surrounding voice and meaning.
- Lead with the result or action. Use concrete nouns, active verbs and direct
  instructions rather than noun-heavy phrases. Passive voice is useful when the
  actor is unknown or the result deserves the focus. Cut staged openings, narration
  about what the text will explain, and closing lines that merely repeat the point.
- Show rather than tell when a short example makes the point clearer. Use an
  excerpt, a command and its result, or an input/output pair instead of describing
  the benefit. Prefer verified real material; label illustrative examples.
- Give each paragraph one purpose and make its point clear early. Cut padding,
  repeated product promises, duplicate setup advice and unsupported claims.
  Preserve useful emphasis, comparisons and the project's voice.
- Keep conditions and qualifiers beside the actions or claims they govern, and
  make pronoun references clear. Reordering must preserve who does what and when.
- Give comparable steps and options a consistent grammatical form so readers can
  compare them. Preserve literal UI labels and code.
- Preserve a clear product pitch unless its likely reading would lead the intended
  reader to choose or act incorrectly. Do not rewrite working copy solely because
  narrower, more literal wording is available. Put a qualification where it first
  changes a decision or action; it belongs in the opening only when needed to
  understand what the product is or whether to use it.
- Prefer a positive, precise statement to rhetorical contrasts and reassurance
  about unrequested alternatives. Name actual limits rather than adding vague
  promises such as “seamless”, “robust” or “fully secure”. Keep direct prohibitions
  when they prevent a mistake.
- Generally avoid em dashes. Prefer commas, colons, semicolons or full stops as
  the grammar allows. Keep a dash when it makes an interruption or aside clearer.
  Apply this to prose, preserving literal quotations, UI labels, identifiers and code.
- Let the meaning shape the rhythm. Avoid forcing points into matching groups
  of three or repeated sentence patterns; keep genuine lists and useful contrasts.
- Keep the writer's existing voice. Do not invent anecdotes, opinions, citations
  or facts to make a passage sound personal. Judge phrases in context rather than
  maintaining a banned-word list.
- Use descriptive links and the UI/CLI's actual names. Put actions in order,
  prerequisites before commands and warnings beside the affected action.
- Use headings for reader tasks, lists for parallel choices/steps, and tables for
  genuine comparisons or lookup. Remove decorative separators, excessive bold
  and one-sentence sections when they interrupt reading. Do not impose fixed
  paragraph lengths or prohibit useful tables.

## Check the outcome

Within scope, unresolved duplicate active instructions, unsupported claims, lost material
caveats/credit, and a README section with no useful role are review findings to
fix before delivery, or explicitly report when scope/authority prevents a fix.
Compare the original and revised opening and first task. Check shortened passages
for lost conditions, defaults or requirements and references whose subject was
cut. Keep changes that improve understanding or action; check that qualifications
arrive when useful and that deeper explanations have a maintained home. Report
material unresolved findings and navigation tradeoffs. Assess the prose by reading
it, not by keyword bans or heading and word counts.
