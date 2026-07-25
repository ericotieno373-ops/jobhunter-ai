from ollama import Client

from app.ai.providers.base import AIProvider


class OllamaProvider(AIProvider):
    def __init__(self, model: str = "qwen2.5:7b"):
        self.client = Client(host="http://127.0.0.1:11434")
        self.model = model

    def chat(self, prompt: str) -> str:
        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]