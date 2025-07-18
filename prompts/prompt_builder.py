# prompts/prompt_builder.py

from datetime import datetime

def build_linkedin_prompt(title: str, url: str = "", category: str = "") -> str:
    today = datetime.today().strftime("%B %d, %Y")

    prompt = f"""
        You are a LinkedIn tech content creator.
        Write a concise, engaging LinkedIn post (max 200 words) about the following tech topic:
        🔹 **Title**: {title}
        🔹 **Category**: {category if category else 'Test Automation / QA / DevOps / Python / Java / Data Science'}
        🔹 **Source**: {url if url else 'N/A'}
        
        Structure:
        - Start with a short, bold hook.
        - Explain the core idea in 2–3 sentences.
        - End with a takeaway or call to action.
        - Use a professional tone, but feel free to include light casual flair.
        - Add 2–4 relevant hashtags.
        
        Audience: QA Engineers, Automation Developers, SDETs, and Tech Leads interested in Test Automation and CI/CD tooling.
        
        Output format:
        Just the text of the post. No markdown formatting.
        
        Date: {today}
        """
    return prompt.strip()
