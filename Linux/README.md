Table of Contents
=================

* [Table of Contents](#table-of-contents)
* [Services](#services)
* [Block Devices](#block-devices)
   * [Software RAID setup](#software-raid-setup)
   * [Mount VHDX](#mount-vhdx)
* [File Systems](#file-systems)
   * [BTRFS](#btrfs)
   * [CIFS](#cifs)
      * [Create smb user](#create-smb-user)
* [Misc](#misc)
   * [Random Strings](#random-strings)
   * [dos2unix](#dos2unix)

# Services

list all
```
systemctl list-units --no-pager
```

stop service
```
systemctl stop servicename
```

disable service
```
systemctl disable servicename
```

# Block Devices

## Software RAID setup

ref: https://www.digitalocean.com/community/tutorials/how-to-create-raid-arrays-with-mdadm-on-ubuntu

## Mount VHDX

ref: https://gist.github.com/allenyllee/0a4c02952bf695470860b27369bbb60d

Install prerequisites

```
apt install qemu-utils nbd-client
```

configure nbd module

```
rmmod nbd
modprobe nbd max_part=16
```

mount block device
```
qemu-nbd -c /dev/nbd0 /path/to/image.vhdx
```

reload partition table
```
partprobe /dev/nbd0
```

check available partitions
```
fdisk -l /dev/nbd0
```

Mount target parition as usual
```
# RW (note I usually mount RO)
mount -o rw,nouser /dev/nbd0p2 /mnt/guest

# RO
mount -o ro,nouser /dev/nbd0p2 /mnt/guest
```

when done simply unmount

```
umount /mnt/guest
```

# File Systems

## BTRFS

relabel partition

```
btrfs filesystem label /dev/md0 super
```

example mount options for fstab

```
/dev/disk/by-label/super        /mnt/super      btrfs   noatime,compress-force=zstd:2   0 0
```

## CIFS

manual mount
```
mount -t cifs -o user=mem,rw //10.1.1.10/super$ /mnt/super
```

### Create smb user

this is needed when a smb.conf share is accessed by specific users.

It is not needed for mounting a share.

```
smbpasswd -a mem
```

# Misc

## Random Strings

For alpha numeric strings, I find pwgen to be the best option. you simply call it with the length you want and it provides a list of options.

selection of passwords
```
pwgen 8
```

single password
```
pwgen 8 1
```

## dos2unix

For when you want all text files in a dir to be converted.

bonus points, using parallel instead of xargs

```
find . -type f -exec file {} \; | grep -i "text" | cut -d: -f1 | parallel -j 4 dos2unix -f
```


