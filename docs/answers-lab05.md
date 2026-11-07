# Lab 05 — Hotfixes across release lines

Student: Trần Công Anh Khoa — 202416531.

## Release first versus upstream first

Release first begins from the version affected users actually run. The
patch stays focused on that code, but must reach every affected branch.
Upstream first fixes development before backporting; the older release
may need an adapted patch. Both approaches require regression tests on
all affected versions. This exercise uses release first.

## Why separate the fix from the version bump?

Only the behavior change and its regression test should be cherry-picked.
The 1.0.x maintenance line advances to 1.0.1, while master and lab05 keep
1.1.0. Picking the version commit would introduce the wrong version.

## What does cherry-pick -x add?

The new commit message names the source commit. Destination commits have
different identities, but remain traceable. git cherry compares equivalent
patches; git tag --contains checks ancestry of the exact source commit.
Neither replaces a test of the application behavior.

## How would a missed lab05 backport be found?

Run the lowercase title query on that release: lion must find The Lion
King. Inspect its own cherry-pick history as well. A successful master
check does not prove the release contains the fix.

## Why wait to tag 1.1.0?

Create release/lab05 before the hotfix, without a tag, to practice updating
an existing maintenance line. Publish v1.1.0 only after its backport and
tests pass. If an affected tag had already been published, publish a new
patch version rather than moving that tag.

## Actual verification and traceability

The detached v1.0.0 reproduction returned [] for lowercase lion. Issue
#18 records that bug. Source fix
`3a156cd24641e48127f56c89f8fadf33e09d6fba` changes only search.py and its regression test;
the 1.0.1 version and changelog change are a separate commit.

PR #19 targets release/lab04 and changes
exactly four files: aims/search.py, tests/test_search.py, aims/__init__.py
and CHANGELOG.md. Five tests pass at v1.0.1. Its tag and GitHub Release
were created after that maintenance PR merged.

Cherry-pick commits `0b59ab1` on master and
`57283f1` on lab05 both contain the source SHA
trailer from -x. PRs #20 and
#21 target master and release/lab05
respectively. The master PR closes the issue with Fixes. Both destinations
retain 1.1.0 and have eight passing tests. git cherry marks the original
fix as an equivalent patch on both destinations; the maintenance version
commit is not picked. No release branch was merged into master.

The lab05 branch existed before the hotfix and had no v1.1.0 tag. That tag
was created only after the backport merged and its eight tests passed.
The v1.0.0 baseline remains unchanged and contains no sorting or category
search. No published tag was moved.

## CI and the intentionally rejected PR

The Python 3.12 workflow is present on master, release/lab04 and
release/lab05. It runs for PRs to master or release/** and pushes to master.
Master requires a successful test check with administrator enforcement.
Release protection requires PRs, with zero approvals in this solo setup;
release rules do not require a status check, but their hotfix PR CI passed.
Earlier lab01-lab03 checkpoints precede the workflow and do not contain it.

PR #22 deliberately adds 1 to total_cost. Its eight-test suite fails
locally and the GitHub test job fails. GitHub reports the PR blocked, and
the merge command is rejected. The PR was closed without merging; master
keeps the correct code and its eight tests pass.

- [Rejected CI run](https://github.com/neko-exe/it3180-202416531-aims/actions/runs/42382769227/job/128433699513)
- [Closed, unmerged demonstration PR](https://github.com/neko-exe/it3180-202416531-aims/pull/22)

This is a solo exercise: no peer review or second-person approval is
claimed. All referenced commits, issues, PRs and CI results are from this
repository, rather than the supplied reference student's history.
