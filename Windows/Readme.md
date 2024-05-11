# System Health

<pre>
SFC /scannow

DISM /online /cleanup-image /restorehealth
</pre>

# Installs

For stuff that should be simple but isnt (typical windows BS)

## WSL

Error:

<pre>
Installing, this may take a few minutes...
WslRegisterDistribution failed with error: 0x8007019e
Error: 0x8007019e The Windows Subsystem for Linux has not been enabled.

Press any key to continue...
</pre>

ref 1: https://learn.microsoft.com/en-us/answers/questions/1152199/wslregisterdistribution-failed-with-error-0x800701
ref 2: https://blog.csdn.net/m0_54917022/article/details/128620422


Install using windows store:

Ubuntu 24.04 (or whatever is the latest)
Terminal

run following cmds in cmd.exe as administrator:

<pre>
wsl --install

dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

wsl --set-default-version 2
</pre>

# Issues

# Window not blanking

assuming you have screen blanking enabled, check whats holding it open

<pre>
powercfg -requests
</pre>
