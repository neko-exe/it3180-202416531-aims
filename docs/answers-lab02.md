# Lab 02 — Features, topics and pull requests

Student: Trần Công Anh Khoa — 202416531.

## Why synchronize master before a PR?

Parallel changes can depend on an outdated baseline. The second GitHub
clone started title search before cart printing merged, then fetched and
merged origin/master. The integrated demo still printed `63.89 $`.

## When should rebase be avoided?

Do not rewrite commits shared with others or published master/release
history. Rebase changes commit identities. Private practice branches can
be rebased safely; shared corrections use new commits or revert.

## Feature versus topic

Feature branches add application behavior, such as printing or searching.
Topic branches cover a focused subject such as templates or documentation.
Both are integrated through PRs.

## Three merge methods

- PR #3 uses a merge commit and retains
  the three printing commits.
- PR #4 uses squash for title search.
- This use-case documentation PR uses rebase and merge for linear history.

Together with the Lab 01 refactor and PR template, this completes five
merged PRs at the Lab 02 checkpoint after this documentation is merged.

## Protection and solo review

Master requires a PR, enforces the rule for administrators, dismisses
stale approvals and forbids force pushes and deletion. The repository
allows all three merge methods and deletes merged topic branches.

The solo option uses zero required approvals. The empty-cart improvement
was found by self-checking; there was no second reviewer and no real
Changes requested/Approved cycle. No peer review is claimed.
