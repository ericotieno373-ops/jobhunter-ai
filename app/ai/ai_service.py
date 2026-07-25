from app.ai.providers.ollama_provider import OllamaProvider


class AIService:
    def __init__(self):
        self.provider = OllamaProvider()

    def chat(self, prompt: str) -> str:
        return self.provider.chat(prompt)