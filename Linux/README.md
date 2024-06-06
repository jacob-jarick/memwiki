Table of Contents
=================

* [services](#services)
* [Block Devices](#block-devices)
   * [Mount VHDX](#mount-vhdx)
* [File Systems](#file-systems)
   * [BTRFS](#btrfs)
   * [CIFS](#cifs)
* [Software RAID setup](#software-raid-setup)


# services

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

create smb user

this is needed to access password protected shares

```
smbpasswd -a mem
```

# Software RAID setup

ref: https://www.digitalocean.com/community/tutorials/how-to-create-raid-arrays-with-mdadm-on-ubuntu


