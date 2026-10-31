# Initial Setup

## VIM

```bash
apt install -y vim
update-alternatives --set editor /usr/bin/vim.basic
```

## misc packages

```bash
# console basic
apt install -y \
 zip zstd 7zip bzip2 \
 screen plocate yq ripgrep screen curl iotop tuned \
 vim
    

# python 
curl -LsSf https://astral.sh | sh # uv install
apt -y install python3-pip pipx

# build
apt -y install build-essential gfortran git

# xorg / wayland

apt install -y xeyes x11-apps firefox mpv
