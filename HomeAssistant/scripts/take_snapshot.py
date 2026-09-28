import fcntl
import os
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

# --- File Locking ---
LOCK_FILE = "/tmp/ha_take_snapshot.lock"
lock_fd = open(LOCK_FILE, "w")

try:
    # Acquire non-blocking exclusive lock
    fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
except BlockingIOError:
    # Another instance is actively running; exit cleanly without error
    sys.exit(0)

# --- Load Simple Credentials ---
ENV_FILE = Path("/home/mem/.ha_credentials")


def load_env(filepath):
    config = {}
    if filepath.is_file():
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    config[k.strip()] = v.strip().strip("'\"")
    return config


env = load_env(ENV_FILE)

URL = "http://HomeAssistant.local/dashboard-power/0?kiosk"
USERNAME = env.get("HA_USERNAME", "mem")
PASSWORD = env.get("HA_PASSWORD", "")
OUTPUT_PATH = "/mnt/super/kiosk.png"

if not PASSWORD:
    raise ValueError(f"Password not found in {ENV_FILE}")

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir="/tmp/ha_chrome_profile",
        headless=True,
        viewport={"width": 1280, "height": 720},
    )
    page = browser.new_page()
    page.goto(URL, wait_until="networkidle")

    # Handle login if redirected
    if "auth/authorize" in page.url:
        print("Logging in...")

        page.locator("input[name='username']").fill(USERNAME)
        password_field = page.locator("input[name='password']")
        password_field.fill(PASSWORD)

        # Submit by pressing Enter on the password field
        password_field.press("Enter")

        # Wait for authentication redirect back to dashboard
        page.wait_for_url(
            lambda url: "auth/authorize" not in url, timeout=15000
        )

    # Wait for Lovelace dashboard components to render
    print("Waiting for dashboard to render...")
    page.wait_for_selector(
        "ha-app-layout, home-assistant-main, hui-view", timeout=15000
    )

    # Allow extra time for WebSockets and custom cards to settle
    time.sleep(5)

    page.screenshot(path=OUTPUT_PATH, full_page=False)
    print(f"Snapshot saved to {OUTPUT_PATH}")
    browser.close()