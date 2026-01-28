Cheat Sheet
===========

- [Cheat Sheet](#cheat-sheet)
- [Setup GitHub Access](#setup-github-access)
- [Specific File](#specific-file)
  - [History](#history)
  - [Checkout Specific Commit](#checkout-specific-commit)
  - [Checkout File from Specific Commit](#checkout-file-from-specific-commit)
- [Handy Diff Arguments](#handy-diff-arguments)
- [Branches](#branches)
  - [Reset](#reset)
  - [Delete Local Branch](#delete-local-branch)
  - [Compare](#compare)
- [Rollback Changes](#rollback-changes)
- [Misc](#misc)
  - [Clear VS Code History](#clear-vs-code-history)
  - [Cd to Repository Root Directory](#cd-to-repository-root-directory)

# Setup GitHub Access

Password authentication has been disabled. You now need to use the gh tool, which is fortunately very straightforward.

You will need SSH keys. If you don't have any, run the command below. It is safe to use defaults for all.

Notes:

- I use SSH; HTTPS is fine though.
- If you have multiple keys, pick your preferred, ideally the strongest encryption.
- If the web URL doesn't open, just open it manually—it's very straightforward.
- You will need MFA set up if you do not have it already.

```bash
ssh-keygen
```

Install gh tool

```bash
sudo apt install gh
```

login
```bash
gh auth login
```

# Specific File

operations focusing on a specific file

## History

simple history

```bash
git log -- path/file.txt
```

Show changes (patch -p)

```bash
git log -p -- path/file.txt
```

## Checkout Specific Commit

For finding when something broke.

This will put you in a detached HEAD state.

```bash
git checkout ff04bcb0c1a6447ff282187d1dafa9ca724dc9ba
```

To get back to HEAD:

```bash
git checkout main
```

## Checkout File from Specific Commit

Very handy for reverting a specific file.

Revert file.txt to how it was in commit 916f2e9:

```bash
git checkout 916f2e9 file.txt
```

# Handy Diff Arguments

ignore all whitespace changes
```bash
git diff -b
```

show filename only
```bash
git diff -b --name-only
```

Show diff between current and previous commit.  
Also filtering by file type.
```bash
git diff HEAD~1 HEAD -- '*.cs'
```

# Branches

## Reset

Restores the branch to exactly match the remote.

```bash
git reset --hard origin/master
```

## Delete Local Branch

I use this when I accidentally create a branch I didn't want.

```bash
git branch -d branchname
```

## Compare

```bash
git fetch
git pull

git diff -w DEV master
```

# Rollback Changes

ref: https://stackoverflow.com/a/21718540/5023361

The safest approach is to create a new commit that rolls back changes made in previous commits.

Roll back every change made after commit 0d1d7fc3
```bash
git revert --no-commit 0d1d7fc3..HEAD
git commit
```

Rollback the last commit
```bash
git revert --no-commit HEAD~1..HEAD
```

Rollback the last 5 commits
```bash
git revert --no-commit HEAD~5..HEAD
```
# Misc


## Clear VS Code History

Ref 1: https://stackoverflow.com/a/43560079/5023361

Ref 2: https://git-scm.com/docs/git-clean/2.23.0

VS Code has this annoying habit of caching file edits, so when editing the file in VS Code it doesn't match what is shown on the disk or in GitHub until you save (or whatever triggers syncing to disk).

To forcefully revert:

Change to your repository's root.

```bash
cd $(git rev-parse --show-toplevel)
```

Forcefully delete all untracked files (gets rid of VS Code litter).

**-d**: Remove untracked directories in addition to untracked files.

**-f**: --force

```bash
git clean -fd
```

Check out the repository again.

**--** arguments after this are file paths, not branch names.

```bash
git checkout -- .
```

## Cd to Repository Root Directory

Ref:

```bash
cd $(git rev-parse --show-toplevel)
```

Optionally, make an alias for this by adding the following to your bashrc:

```bash
alias gitroot='cd $(git rev-parse --show-toplevel)'
```
