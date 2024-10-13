Cheat Sheet
===========

# setup github access

password auth has been disabled now, you need to use the gh tool which is fortunately very straight forward.

You will need ssh keys, if you dont have any run the command below, it is safe to use defaults for all.

notes:

- I use SSH, HTTPS is fine though
- if you have multiple keys, pick your prefered, ideally the strongest encryption.
- if Web url doesnt open just open it manually its very straight forward
- you will need MFA setup if you do not have it already.

```
ssh-keygen
```

Install gh tool

```
sudo apt install gh
```

login
```
gh auth login
```

# checkout file from specific commit

very handy for reverting a specific file.

revert file.txt to how it was in commit 916f2e9
```
git checkout 916f2e9 file.txt
```

# compare branches

```
git fetch
git pull

git diff -w DEV master
```

# handy diff arguments

ignore all whitespace changes
```
git diff -b
```

show filename only
```
git diff -b --name-only
```

# Reset branch

restores branch to exactly what it is remotely

```
git reset --hard origin/master
```

# Delete local branch

I use this when I accidentally create a branch I didnt want

```
git branch -d branchname
```

# Rollback changes

ref: https://stackoverflow.com/a/21718540/5023361

The safest approach is to create a new commit that rolls back changes made in previous commits.

Roll back every change made after commit 0d1d7fc3
```
git revert --no-commit 0d1d7fc3..HEAD
git commit
```

Rollback the last commit
```
git revert --no-commit HEAD~1..HEAD
```

Rollback the last 5 commits
```
git revert --no-commit HEAD~5..HEAD
```

# Clear VS Code History

ref 1: https://stackoverflow.com/a/43560079/5023361

ref 2: https://git-scm.com/docs/git-clean/2.23.0

VS Code has this annoying habbit of caching file edits, so when editing the file in VS Code it doesnt match what is shown on the disk or in github until you save (or whatever triggers syncing to disk).

To forcefully revert you can use these two commands:

```
git clean -fd
git checkout -- .
```

-d: Remove untracked directories in addition to untracked files.
-f: --force
