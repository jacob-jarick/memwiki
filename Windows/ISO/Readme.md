# Create Windows 10 ISO

**Note:** Do this on a windows 10 pro install, the guide is only for windows 10 pro

Download Media Creation Tool: https://www.microsoft.com/en-au/software-download/windows10

Select Language `English (United States)` you can install additional language packs after. Chosing `English UK` will often cause software compatibility issues for niche applications. its easier to use US then add required language packs post install.

Select `ISO File`

Name ISO `Windows10MCT.iso`

# Backup Drivers

**Note:** The best way to get drivers for a fussy PC, is unfortunately to install windows, then use windows update.

**Note:** I highly advise using a generic USB to ethernet adaptor (or WiFi) if the PC has network peripherals that are not present on windows 10 iso by default. Then you can perform a windows update which will fetch all drivers (usually).

**Note:** best to use a USB drive, all further instructions for this section reference D:\ as the USB drive

open a terminal as administrator.

```powershell
mkdir D:\DriverBackup

dism /online /export-driver /destination:"D:\DriverBackup"
```

# Setup Environment

Create work dirs

```powershell
mkdir C:\W10_Work
mkdir C:\W10_Work\Temp
mkdir C:\W10_Work\ISO_Extract
mkdir C:\W10_Work\Mount
mkdir C:\W10_Work\Updates
```

use 7zip or explorer to extract `Windows10MCT.iso` contents to `C:\W10_Work\ISO_Extract`


Convert ESD to WIM

```
# Export Index 6 (Pro) from the compressed ESD to a manageable WIM
dism /Export-Image /SourceImageFile:"C:\W10_Work\ISO_Extract\sources\install.esd" /SourceIndex:6 /DestinationImageFile:"C:\W10_Work\ISO_Extract\sources\install.wim" /Compress:max /CheckIntegrity

# delete the ESD
Remove-Item -Path C:\W10_Work\ISO_Extract\sources\install.esd

# backup the install.wim
Copy-Item -Path "C:\W10_Work\ISO_Extract\sources\install.wim" "C:\W10_Work\Temp\install.wim"
```

# Inject Drivers into ISO

Mount Image: 

```powershell
dism /Mount-Wim /WimFile:"C:\W10_Work\ISO_Extract\sources\install.wim" /Index:1 /MountDir:"C:\W10_Work\Mount"

# Inject drivers
dism /Image:"C:\W10_Work\Mount" /Add-Driver /Driver:"D:\DriverBackup" /Recurse

#Unmount and Save
dism /Unmount-Wim /MountDir:"C:\W10_Work\Mount" /Commit
dism /Cleanup-Mountpoints
```

# Repack ISO

You will need to download and install `Windows ADK 10.1.26100.2454 (December 2024)`

https://go.microsoft.com/fwlink/?linkid=2337875

create updated ISO

```powershell
& "C:\Program Files (x86)\Windows Kits\10\Assessment and Deployment Kit\Deployment Tools\amd64\Oscdimg\oscdimg.exe" -m -o -u2 -udfver102 -bootdata:2#p0,e,bC:\W10_Work\ISO_Extract\boot\etfsboot.com#pEF,e,bC:\W10_Work\ISO_Extract\efi\microsoft\boot\efisys.bin "C:\W10_Work\ISO_Extract" "D:\Custom_Win10.iso"
```

# Unmount and cleanup 

```powershell
dism /Unmount-Wim /MountDir:"C:\W10_Work\Mount"
dism /Cleanup-Mountpoints
```

# Create bootable USB with Rufus

https://rufus.ie/en/#download