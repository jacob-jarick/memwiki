Safecopy
========

# About

A brilliant disk imaging tool. Many commerical solutions are simply a shameless rip off this tool.

Latest version can be found on sourceforge: https://sourceforge.net/projects/safecopy/

ref: https://niziak.spox.org/wiki/datarecovery:safecopy

Special shout out to the awesome personal wiki above which has the best information ive found on safecopy.

# Safe Copy disk imaging

## ENV setup

set your source and destionation files

```
# source drive
SRC=/dev/sda

# destination image
DEST=/mnt/backup/a/a.img

# working dir for image (automatically set from DEST)
WDIR="$(dirname "${DEST}")"

# create and change to working dir
mkdir -p "$WDIR"
cd "$WDIR"
```

## Stage 1

```
safecopy --stage1 -I /dev/null "$SRC" "$DEST"
```

### Stage 1 resume

Yes you can resume stage1, you need to use /dev/null as your badblocks file it will use the size of the image to work out its resume point. Ive done this many times, works great.

All other stages can be resumed by running the stage command again, stage1 is special as it doesnt have a badblocks file to use for its resume reference.

```
safecopy --stage1 -I /dev/null "$SRC" "$DEST"
```

## Stage 2

Additional stages should only be run IF there were skipped sectors in the previous stage. your stage1.badblocks file will have entries (not empty)

remove dupes from bad blocks file, this is only needed when you have resumed the previous stage.

```sort -n stage1.badblocks | uniq > stage1.badblocks.uniq```

start stage 2, note if you didnt do the above step fix yout badblocks filename (delete .uniq)

```safecopy --stage2 -I stage1.badblocks.uniq "$SRC" "$DEST"```

## Stage 3

remove dupes from badblocks
```sort -n stage2.badblocks | uniq > stage2.badblocks.uniq```

start stage 3
```safecopy --stage3 -I stage2.badblocks.uniq "$SRC" "$DEST"```

## Stage 4 - thrash drive to death mode

Note: this will as the header says likely thrash a spindle drive to death in the last ditch attempt to read blocks stage 3 couldnt. 

Note: Only use this for last ditch attempts when stage 3 still had unreadable blocks.

Note: this isnt an offical mode, it is stage3 with much more aggresive settings.

Remove dupes from badblocks

```sort -n stage3.badblocks | uniq > stage3.badblocks.uniq```

start stage 4

```safecopy --stage3 -R 12 -I stage3.badblocks.uniq -o stage4.badblocks "$SRC" "$DEST"```