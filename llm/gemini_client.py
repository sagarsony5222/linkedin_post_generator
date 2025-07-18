# llm/gemini_client.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

def generate_post_gemini(prompt: str, model_name="gemini-1.5-pro") -> str:
    try:
        print("[🤖] Sending prompt to Gemini...")
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)

        if response.text:
            print("[✅] Post generated using Gemini.")
            return response.text.strip()
        else:
            print("[⚠️] Gemini returned no content.")
            return "Gemini generated an empty response."
    except Exception as e:
        print(f"[❌] Gemini API error: {e}")
        return "Error generating post with Gemini."
