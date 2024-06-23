
Table of Contents
=================

* [Table of Contents](#table-of-contents)
* [System Health](#system-health)
* [Installs](#installs)
   * [WSL](#wsl)
      * [Error](#error)
      * [Install](#install)
      * [Cleanup](#cleanup)
* [Issues](#issues)
   * [Window not blanking](#window-not-blanking)
* [Sound](#sound)
   * [Dolby ATMOS](#dolby-atmos)
      * [Setup](#setup)
      * [VLC](#vlc)
* [Config](#config)
   * [Disable web search in startmenu](#disable-web-search-in-startmenu)

# System Health

```
echo repair system
SFC /scannow

echo Repair Windows Image
DISM /online /cleanup-image /restorehealth

echo done
```

# Installs

For stuff that should be simple but isnt (typical windows BS)

## WSL

ref 1: https://learn.microsoft.com/en-us/answers/questions/1152199/wslregisterdistribution-failed-with-error-0x800701

ref 2: https://blog.csdn.net/m0_54917022/article/details/128620422

### Error

<pre>
Installing, this may take a few minutes...
WslRegisterDistribution failed with error: 0x8007019e
Error: 0x8007019e The Windows Subsystem for Linux has not been enabled.

Press any key to continue...
</pre>

### Install

Install using windows store:

Ubuntu 24.04 (or whatever is the latest)
Terminal

run following cmds in cmd.exe as administrator:

```
wsl --install

dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

wsl --set-default-version 2

echo done
```

### Cleanup

I end up with two ubuntu, I only want the latest.

List Installed distros:


```
wsl --list --verbose
```

<pre>
  NAME            STATE           VERSION
* Ubuntu          Stopped         2
  Ubuntu-24.04    Running         2
</pre>

to remove the default ubuntu install

```
wsl --unregister Ubuntu
```

Then we need to remove it as an option in Terminal, else it auto installs when you click it (annoying as).

In terminal, go to settings, scroll down to profiles, select "Ubuntu" and either delete profile (right at the bottom) or "Hide profile from dropdown".

# Issues

## Window not blanking

assuming you have screen blanking enabled, check whats holding it open

```
powercfg -requests
```

# Sound

## Dolby ATMOS

ref 1: https://www.reddit.com/r/VLC/comments/dwzy9p/how_to_fix_dolby_atmos_in_vlc/?share_id=1yYKBsJNbBlHwkde5PVud&utm_content=1&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=5


Its a two part solution, first you need to set output to dolby atmos and install dolby atmos via the windows store.

### Setup

Sound Properties, Spatial Sound, Select Dolby Atmos (windows store will pop up asking to install, do so)


### VLC

Go to Preferences > All > Audio > Output modules

Change "Audio output module" to "Windows Multimedia Device output"

Go to the "MMDevice" settings

Change the "Output back-end" to "Windows Audio Session API output"

Set "HDMI/SPDIF audio passthrough" to "Enabled"

# Config

## Disable web search in startmenu

ref: https://www.tomshardware.com/how-to/disable-windows-web-search

yet another feature from microsoft NO ON FUCKING ASKED FOR

Run the [reg file](regfixes/DisableSearchBoxSuggestions.reg) and reboot (or manually enter it)
