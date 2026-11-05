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
   in disposable workspaces. An independent reviewer should receive the user task,
   skill and raw fixture, without the intended answer or suspected failure.
   Keep side effects within the scenario's authorization. Record observable outcomes
   and limitations rather than just a reviewer score.

Follow existing authorization for draft PRs; opening one does not authorize merging
or publishing a release. Reviewers should look for scope expansion, lost contracts,
unverified claims, unnecessary permission loops and project-specific rules presented
as universal methodology.
