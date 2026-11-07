# Lab 01 — Environment and refactoring

Student: Trần Công Anh Khoa — 202416531 (neko-exe).

## Global and local configuration

Global configuration belongs to the current OS user, usually in
`~/.gitconfig`. Local `.git/config` overrides it for one repository.
This repository uses my name and GitHub noreply email locally, without
changing the identity of other projects.

## Why use git mv?

It moves the file and stages the change. Git detects renames by content
similarity, rather than storing a separate rename instruction. The
staged summary showed 100% renames for Cart and DVD; `git log --follow
-- aims/cart.py` follows the earlier path.

## Is release/lab01 a baseline?

It is the accepted checkpoint when created after the refactor PR merges.
A branch can advance through later reviewed corrections; a published tag
identifies one fixed commit and must not move.

## Why use a PR when working alone?

The PR records the purpose, diff and actual checks before integration.
The solo option uses zero required approvals. There is no peer review,
and I do not claim to have requested or received another person's review.

## Local exercises performed

- Ran the starter and refactored program: both printed `63.89 $`.
- Used `git restore cart.py` on a temporary unstaged comment.
- Staged a temporary main.py comment, then used `restore --staged`:
  the index became clean while the working-tree edit remained.
- Restored that comment and verified a clean working tree.
- Amended a misspelled initial message before publishing any commits.
- Used `git mv` to move both classes, then updated main.py imports.
- `.gitignore` excludes Python cache files and virtual environments.

The original repositories supplied in the workspace belong to a different
student. They are preserved outside this repository as reference copies;
their GitHub PR numbers and claimed results are not my lab evidence.
