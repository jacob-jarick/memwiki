# Cheat Sheet

## checkout file from specific commit

very handy for reverting a specific file.

```
git checkout <COMMIT> <FILE>
```

Example
```
git checkout 916f2e9 package.json
```


## compare branches

```
git fetch
git pull

git diff -w DEV master
```

## handy diff arguments

```
# ignore all whitespace changes
git diff -b

# show filename only
git diff -b --name-only
```

## Reset branch

restores branch to exactly what it is remotely

```
git reset --hard origin/master
```

## Delete local branch

I use this when I accidentally create a branch I didnt want

```
 git branch -d branchname
```

