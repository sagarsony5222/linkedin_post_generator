# scraper/filters.py
def is_relevant_topic(title, keywords):
    title_lower = title.lower()
    for keyword in keywords:
        if keyword.lower() in title_lower:
            return True
    return False
