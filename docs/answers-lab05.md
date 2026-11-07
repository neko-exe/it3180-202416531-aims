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
