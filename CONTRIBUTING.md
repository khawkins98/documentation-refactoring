# Contributing

Keep each change focused on a demonstrated problem or useful capability. Avoid
adding a universal instruction for a single project's constraint.

Use Conventional Commit titles for commits and PRs. Choose the type by capability:
`feat: ...` for a new skill, `docs: ...` for instruction corrections, or `test: ...`
for evaluation fixtures. Do not add unsolicited
co-author trailers, AI signatures or tool branding. Preserve existing human
credits and third-party terms. PR bodies should explain the problem, resulting
behavior, validation and material limitations in ordinary readable Markdown.

Before requesting review:

1. Check that the skill description selects the intended task and does not pull
   unrelated work into scope. Keep the two skills independently useful.
2. Verify every supporting reference is linked from an appropriate entrypoint.
   Check examples and commands that changed.
3. Run your agent platform's skill validator when available. Report the validator
   and version/path used; YAML validity does not establish behavioral quality.
4. For a material behavior change, exercise relevant [evaluation scenarios](evals/README.md)
   in disposable workspaces. When evaluating independent skill execution, supply
   the task, skill and raw fixture without the intended answer or suspected failure.
   Design and source reviews may use full context. Keep side effects within the
   scenario's authorization. Record which kind of review occurred, observable
   outcomes, interventions and limitations rather than just a reviewer score.

Follow existing authorization for draft PRs; opening one does not authorize merging
or publishing a release. Reviewers should look for scope expansion, lost contracts,
unverified claims, unnecessary permission loops and project-specific rules presented
as universal methodology.

## Maintaining this repository

README owns skill selection, installation and first invocation. Keep specialist
selection and operating detail in each installable skill and its references;
use SOURCES and the expert maps for provenance, and the evaluation index for
scenarios and results. Preserve required notices and dated evidence.

## Credit and reuse

Treat this as a curated composition. Explain which specialist contributes to a
change and what the local layer adds, without claiming we invented established
methods or framing the project as a replacement born from others' inadequacy.

- Record source URL, author/project credit, immutable reviewed repository revision
  (or publication and review dates for web-only sources), and the material's
  applicable license or rights policy. Check file/directory notices as well as the
  repository license; third-party notices for other components are not a grant.
- Label the relationship as inspired, adapted or directly reused in the
  [source records](SOURCES.md). Inspired guidance uses our own expression.
  Adaptations identify modifications; direct reuse identifies the copied scope.
- Before copying or adapting material, establish permission and fulfill its terms.
  Preserve required notices and change disclosures. Unknown licensing means link
  and credit only until permission is established, not silently assume MIT.
- Place the original-project license, provenance and required upstream notices
  inside the installable skill that uses the material, with a root index for repository readers. Check that installation
  carries them. A root-only credit file does not travel with a selected skill.
- Do not relabel upstream work as our original MIT text. The no-unsolicited-AI-
  trailer preference never removes author credit, copyright or license notices.

When updating reused content, record the new revision, compare the local artifact
with that source and recheck notices. Keep a small useful excerpt when sufficient;
vendoring a whole manual merely for attribution creates unnecessary maintenance.
