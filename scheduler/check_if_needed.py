# scheduler/check_if_needed.py

import os
from datetime import datetime
from scheduler.cron_job import run_daily_post_generation

POSTS_DIR = "posts"

def post_exists_today() -> bool:
    today = datetime.today().strftime('%Y-%m-%d')
    if not os.path.exists(POSTS_DIR):
        return False
    for file in os.listdir(POSTS_DIR):
        if file.startswith(today):
            return True
    return False

if __name__ == "__main__":
    if post_exists_today():
        print(f"[⏸️] Post for today already exists. Skipping generation.")
    else:
        print(f"[🟢] No post for today. Generating one now...")
        run_daily_post_generation()
