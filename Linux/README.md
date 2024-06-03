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


