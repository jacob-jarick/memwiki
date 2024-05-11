# services

<pre>
# list all
systemctl list-units --no-pager

# stop service
systemctl stop servicename

# disable service
systemctl disable servicename
</pre>

# File Systems

## BTRFS

<pre>
# relabel partition
btrfs filesystem label /dev/md0 super
</pre>

example mount options for fstab
<pre>/dev/disk/by-label/super        /mnt/super      btrfs   noatime,compress-force=zstd:2   0 0</pre>

## CIFS

<pre>
# manual mount
mount -t cifs -o user=mem,rw //10.1.1.10/super$ /mnt/super
</pre>
