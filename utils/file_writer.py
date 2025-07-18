# utils/file_writer.py

import os
import re
from datetime import datetime

def slugify(text: str) -> str:
    return re.sub(r'\W+', '-', text.lower())[:50]

def save_post(post_text: str, title: str):
    date_str = datetime.today().strftime('%Y-%m-%d')
    slug = slugify(title)
    os.makedirs("posts", exist_ok=True)
    filepath = f"posts/{date_str}_{slug}.md"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(post_text)
    print(f"[✅] Saved post to: {filepath}")
