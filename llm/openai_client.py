# llm/openai_client.py

import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_post(prompt: str, model="gpt-4") -> str:
    try:
        print("[🤖] Sending prompt to OpenAI...")
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a professional LinkedIn content writer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        post_text = response.choices[0].message.content.strip()
        print("[✅] Post generated successfully.")
        return post_text
    except Exception as e:
        print(f"[❌] OpenAI API error: {e}")
        return "Error generating post."
