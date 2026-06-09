#!/usr/bin/env python3
"""
Atticus_Counsel Telegram Handler Template
Minimal polling handler that calls Hermes with a profile.
"""

import os
import time
import subprocess
import requests
from datetime import datetime

BOT_TOKEN = REDACTED
ALLOWED_IDS = [int(x) for x in os.getenv("ATTICUS_ALLOWED_IDS", "").split(",") if x.strip()]

if not BOT_TOKEN:
    print("ERROR: ATTICUS_BOT_TOKEN not set")
    exit(1)

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
HERMES_PROFILE = "atticus_counsel"

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"timeout": 30, "offset": offset}
    r = requests.get(url, params=params, timeout=35)
    return r.json()

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

def ask_hermes(message: str) -> str:
    cmd = ["hermes", "-p", HERMES_PROFILE, "chat", "--once", "--no-color"]
    result = subprocess.run(cmd, input=message, capture_output=True, text=True, timeout=120)
    return result.stdout.strip() if result.returncode == 0 else f"[Error] {result.stderr}"

def main():
    log(f"{HERMES_PROFILE} handler online")
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates.get("result", []):
            offset = update["update_id"] + 1
            msg = update.get("message", {})
            chat_id = msg.get("chat", {}).get("id")
            user_id = msg.get("from", {}).get("id")
            text = msg.get("text", "")
            if user_id not in ALLOWED_IDS or not text:
                continue
            reply = ask_hermes(text)
            send_message(chat_id, reply)
        time.sleep(1)

if __name__ == "__main__":
    main()