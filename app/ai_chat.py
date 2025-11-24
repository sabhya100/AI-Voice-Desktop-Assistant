"""
ai_chat.py
AI chat logic using OpenRouter/DeepSeek via HTTP.
Make sure to set OPENROUTER_API_KEY in your environment variables.
"""

import os
import requests
from typing import Optional

OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')  # set this in your environment
MODEL = "deepseek/deepseek-chat"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def chat_with_ai(query: str) -> Optional[str]:
    if not OPENROUTER_API_KEY:
        print("OpenRouter API key not set. Please set OPENROUTER_API_KEY env variable.")
        return "AI service not configured."

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful and intelligent AI assistant named Alex."},
            {"role": "user", "content": query}
        ],
        "temperature": 0.7,
        "max_tokens": 500,
    }

    try:
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=20)
        response.raise_for_status()
        data = response.json()
        if "choices" in data and len(data["choices"]) > 0:
            reply = data["choices"][0]["message"]["content"]
            print("AI reply:", reply)
            return reply
        else:
            print("Unexpected API response:", data)
            return None
    except requests.RequestException as e:
        print("Error calling OpenRouter:", e)
        return None
