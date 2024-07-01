
Table of Contents
=================

* [About](#about)
* [cinema offsets](#cinema-offsets)
   * [Install Deps](#install-deps)
      * [yt-dlp](#yt-dlp)
      * [audio-offset-finder](#audio-offset-finder)
   * [prepare](#prepare)
   * [helper scripts](#helper-scripts)
      * [yt](#yt)
      * [calc_offset](#calc_offset)
      * [Workflow](#workflow)


# About

This focuses on modding.

# cinema offsets

When its a pain to calculate the offset, I use the yt-dlp and audio-offset-finder

## Install Deps

### yt-dlp

```apt -y install yt-dlp```

### audio-offset-finder

Needs a venv (what python app doesnt at this point)

```
# go to home
cd ~

# create venv
python3 -m venv audio-offset-finder

# change to venv
source ~/audio-offset-finder/bin/activate

# install
pip install audio-offset-finder

# downgrade numpy
pip install 'numpy<2'
```

## prepare

copy the song file from beat saber to a temp dir, you can confirm its a the correct file using the tool file

```file song.egg```

download the target youtube video audio

```
# change to temp dir you are using
cd /tmp/

# list available audio formats
yt-dlp --list-formats https://www.youtube.com/watch?v=somemusicvideo

# download an audio format, its not to fussy but I chose mp4
yt-dlp -f 233 https://www.youtube.com/watch?v=somemusicvideo

# swap to venv
source ~/audio-offset-finder/bin/activate

# find offset
audio-offset-finder --find-offset-of song.egg --within somemusicvideo.mp4
```

note the score, above 10 is considered very accurate, eg from my test

```
Offset: 29.616 (seconds)
Standard score: 14.573068627778227
```

## helper scripts

there are two scripts in this directory. copy them to the venv's virtual directory.
I use both to save time.

```
cp yt calc_offset ~/audio-offset-finder/bin/
```

### yt

just an alias for
```
yt-dlp -f 233 $1
```


### calc_offset

uses find in current directory to find first .egg and file .mp4 files.

then runs the below command.

```
audio-offset-finder --find-offset-of "$bsfile" --within "$ytfile"
```

### Workflow

pick empty temp dir
```cd /tmp/calc_offset
```

empty it
```rm -f *```


Copy beat saber song file to temp dir.


download video from youtube
```yt URL```

run calc_offset
```
calc_offset
```
