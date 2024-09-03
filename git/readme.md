Cheat Sheet
===========

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
