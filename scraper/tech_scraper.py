# scraper/tech_scraper.py
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from scraper.filters import is_relevant_topic

DEVTO_URL = "https://dev.to"
HACKER_NEWS_URL = "https://news.ycombinator.com"

KEYWORDS = [
    "test automation", "QA", "SDET", "data science",
    "python", "java", "jenkins", "kubernetes", "selenium",
    "pytest", "CI/CD", "robot framework"
]

def scrape_devto_articles():
    print("[🔍] Scraping Dev.to...")
    response = requests.get(f"{DEVTO_URL}/tag/qa")
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = []

    for a in soup.find_all('a', class_='crayons-story__hidden-navigation-link'):
        title = a.get_text(strip=True)
        link = DEVTO_URL + a['href']
        if is_relevant_topic(title, KEYWORDS):
            articles.append({"title": title, "url": link})
    return articles

def scrape_hacker_news():
    print("[🔍] Scraping Hacker News...")
    response = requests.get(HACKER_NEWS_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = []

    for item in soup.find_all("tr", class_="athing"):
        title_tag = item.find("a", class_="storylink") or item.find("span", class_="titleline")
        if not title_tag:
            continue
        title = title_tag.get_text(strip=True)
        url = title_tag['href']
        if is_relevant_topic(title, KEYWORDS):
            articles.append({"title": title, "url": url})
    return articles

def get_trending_articles():
    devto = scrape_devto_articles()
    hn = scrape_hacker_news()
    combined = devto + hn
    print(f"[✅] Total relevant articles found: {len(combined)}")
    return combined
