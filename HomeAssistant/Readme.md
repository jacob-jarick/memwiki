# About

I have an old raspberry pi B+ that I wanted to use to display a specific dashboard I have configured on Home Assistant.

The problem is the rpi is to weak to run any modern browser.

My solution was to use a server (I used fileserver.local / 10.1.1.10 ) to run a python script which uses playwright to open http://homeassistant.local/dashboard-power/0?kiosk 

render it to an image.

Save the file locally to /mnt/super/kiosk.png

then scp it to the raspberry pi mem@HaDash.local:/tmp/kiosk.png

# Lessons Learned

I tried HACS puppet plugin on HA but i found it nothing but trouble. I think it might be partly due to running the HA OVA image, but several hours later I decided to do the simple solution which was this.

# Servers

| Server | IP | Role | 
| --- | --- | --- |
| HomeAssistant.local | 10.1.1.228 | HA Server | 
| HaDash.local | 10.1.1.136 | Raspberry Pi dash display kiosk | 
| FileServer.local | 10.1.1.10| File server, runs dashboard image gen script | 

# Scripts

| file(s) | Permissions | Server | Location | Purpose |
| --- | --- | --- |  --- | --- |
| autostart | N/A | HaDash.local | /home/mem/.config/openbox/autostart | starts minimal xorg and displays image using feh |
| take_snapshot.py | a+x | FileServer.local | /home/mem/take_snapshot.py | generates snapshop of dashboard |
| .ha_credentials | 600 | FileServer.local | /home/mem/.ha_credentials | credentials for take_snapshot.py |

# Install

## Fileserver

generate ssh key, install on HaDash

```bash
ssh-keygen
ssh-copy-id mem@HaDash.local
```

setup ha credentials file

```bash
vi ~/.ha_credentials

# add your ha account details eg
# HA_USERNAME=mem
# HA_PASSWORD=password1
```

setup python script

```bash
# ensure /home/mem/take_snapshot.py exists

# install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment
/home/mem/.local/bin/uv venv

# Install Playwright Python package
/home/mem/.local/bin/uv pip install playwright

# Install required browser binaries (Chromium) and system dependencies
/home/mem/.local/bin/uv run playwright install chromium --with-deps
```

# Crontab 

## Fileserver (as user mem)

```bash
* * * * * cd /home/mem && /home/mem/.local/bin/uv run python /home/mem/take_snapshot.py > /dev/null 2>&1 && scp /mnt/super/kiosk.png HaDash.local:/tmp/
```

# Manual Run

login to fileserver

```bash
/home/mem/.local/bin/uv run python /home/mem/take_snapshot.py
```

login to HaDash

note: you shouldnt need to do anything. but you can force X to restart by running

```bash
sudo killall -9 Xorg
```