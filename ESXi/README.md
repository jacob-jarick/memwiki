# Pass through disks

ref: https://medium.com/@aj.abdelwahed/vmware-esxi-8-how-to-mount-physical-disk-into-a-virtual-machine-without-wiping-data-687053a5cdcb

<pre>
# list disks
ls -l /vmfs/devices/disks

# confirm full path to disk
# note do not use a partition which has a :N after it
ls -l /vmfs/devices/disks/t10.ATA_____Samsung_SSD_840_EVO_500GB_______________S1DHNSAF633948P_____

# make a directory to store pass through VMDKs
mkdir /vmfs/volumes/DATASTORE2-SAMSUNG/PASSTHRU

# attach disk as RDM
vmkfstools -z /vmfs/devices/disks/t10.ATA_____Samsung_SSD_840_EVO_500GB_______________S1DHNSAF633948P_____ /vmfs/volumes/DATASTORE2-SAMSUNG/PASSTHRU/500GB_Samsung_SSD_840_EVO_500GB.vmdk
</pre>

Then you can add to a VM by adding an existing disk.
