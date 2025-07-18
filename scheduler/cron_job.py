# scheduler/cron_job.py

import os
from datetime import datetime
from scraper.tech_scraper import get_trending_articles
from prompts.prompt_builder import build_linkedin_prompt
from llm.openai_client import generate_post  # or use gemini_client
from utils.file_writer import save_post

USE_GEMINI = False  # toggle between OpenAI and Gemini

if USE_GEMINI:
    from llm.gemini_client import generate_post_gemini

def run_daily_post_generation():
    print("[⏰] Starting scheduled post generation...")

    articles = get_trending_articles()
    if not articles:
        print("[⚠️] No relevant articles found today.")
        return

    selected_article = articles[0]
    prompt = build_linkedin_prompt(selected_article["title"], selected_article["url"])

    if USE_GEMINI:
        post = generate_post_gemini(prompt)
    else:
        post = generate_post(prompt)

    save_post(post, selected_article["title"])
    print("[📁] Post saved successfully.")

if __name__ == "__main__":
    run_daily_post_generation()
