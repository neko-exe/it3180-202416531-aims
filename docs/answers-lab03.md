# Lab 03 — Bugfixes, conflicts and undo

Student: Trần Công Anh Khoa — 202416531.

## What is a merge base?

It is a best common ancestor of two commits. Git compares each side with
that ancestor. Conflicting edits to the same area need a resolution.

## Why keep the failing test before the fix?

Issue #6 records the 21st-DVD bug. Test commit
`f881bc4` fails because adding DVD 21 returns
True. Fix commit `d2309a0` changes > to >=;
the same test then passes. PR #7 closes
the issue and retains the regression test.

## Why target the feature branch?

The unfinished formula lived on feature/discount. Bugfix PR
#9 targets that feature, not master.
The corrected feature enters master in PR #8.
Four tests pass: capacity, discounted total, invalid percent, title search.
100 with 20 percent off is 80; -1 and 150 raise ValueError.

## How was the conflict resolved?

Two branches changed the exact same add_dvd print line. After the
Vietnamese PR #11 merged, merging
origin/master into the title branch produced UU aims/cart.py and conflict
markers. The resolution combined Vietnamese text and the DVD title.
Four tests and the 63.89 $ demo passed before title PR
#10 merged.

The private rebase exercise also produced a real conflict in a separate
practice file. I resolved it, continued the rebase, and returned to the
application branch. Practice branches were not pushed or integrated.

## Why revert shared history?

Reset moves a branch and can discard shared commits. Revert adds an
inverse commit while preserving history. `git revert -m 1` reversed the
title merge relative to its first parent. PR
#12 retained the earlier Vietnamese text.

## What did reset and reflog show?

- Soft reset kept the deliberate demo file staged.
- Mixed reset left that new file untracked in the working tree.
- Hard reset removed the committed demo file from the private branch.
- Reflog retained `07473b5`. The local branch
  `rescue/local-undo-practice` makes that commit reachable again.

These operations affected only unpublished practice commits. Reflog
helps recover commits, not arbitrary uncommitted edits. A direct push of
a harmless private commit to master was rejected by GitHub protection;
that file never entered master. Solo: no peer review is claimed.
