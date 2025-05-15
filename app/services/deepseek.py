from openai import OpenAI
from app.config import GROQ_API_KEY, BASE_URL, MODEL_NAME, APP_URL, APP_NAME
from typing import List
from app.models.chat import Message


class DeepseekService:
    def __init__(self):
        self.client = OpenAI(
            base_url=BASE_URL,
            api_key=GROQ_API_KEY
        )

    async def generate_response(self, messages: List[Message], temperature: float = 0.7, max_tokens: int = 1000):
        try:
            # Convert Message objects to dictionaries
            formatted_messages = [{"role": msg.role, "content": msg.content} for msg in messages]
            
            # Ensure we have a system instruction
            if not any(msg.get("role") == "system" for msg in formatted_messages):
                formatted_messages.insert(0, {
                    "role": "system", 
                    "content": "You are a helpful, intelligent assistant powered by the deepseek-r1-distill-llama-70b model on Groq Cloud. Provide accurate, concise, and helpful responses."
                })
            
            completion = self.client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": APP_URL,
                    "X-Title": APP_NAME,
                },
                extra_body={},
                model=MODEL_NAME,
                messages=formatted_messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return {
                "response": completion.choices[0].message.content,
                "model": MODEL_NAME
            }
        except Exception as e:
            return {"error": str(e)}