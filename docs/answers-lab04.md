# Lab 04 — Release flow and configuration audit

Student: Trần Công Anh Khoa — 202416531.

## Why prepare a release on master?

The version, changelog and tests enter the integration branch through a
topic PR. A release branch is then created from that accepted checkpoint;
it does not need direct edits or a special unreviewed version commit.

## Why not merge release branches back into master?

A maintenance branch can carry its own version and release notes.
Merging it wholesale could bring an older version into development.
Carry focused fixes through separate cherry-pick PRs instead.

## How does this differ from GitFlow?

GitFlow normally uses develop for integration and main for published
releases. This course integrates on master and keeps release/labXX as
submission and maintenance lines, with no release-to-master merge.

## Why 1.0.0 instead of 0.4.0?

SemVer uses 0.y.z for initial development. The exercise chooses this
checkpoint as the first stable baseline, 1.0.0. The fourth lab number
does not impose a version number; this is a release decision.

## Tag versus release branch

A published tag identifies one exact commit and must never move.
Annotated tags also record a tagger and a message. A release branch can
advance through reviewed patches while old tags remain unchanged.

## How is a baseline audited?

Check out the tag in a detached worktree, run its own tests, inspect the
version and changelog, and list tracked files. git archive packages the
tracked tree of the chosen tag. A..B lists commits reachable from B but
not A. Testing a current checkout does not validate an older tag.

## Checks performed after publishing the baseline

Annotated v0.1.0, v0.2.0 and v0.3.0 identify the earlier checkpoints;
v1.0.0 identifies the Lab 04 baseline on release/lab04. Its GitHub Release
uses that existing tag. Master requires the successful CI check `test`.

Detached worktrees ran the v0.2.0 demo and the four-test v1.0.0 suite.
The 1.0.0 demo shows its version and 63.89 $. That baseline contains no
sorting. git archive produced aims-1.0.0.zip outside the repository.
The supplied older archive was preserved separately.

Sorting and its two tests are added after v1.0.0. The development suite
now contains six tests; the published 1.0.0 tag is unchanged.
