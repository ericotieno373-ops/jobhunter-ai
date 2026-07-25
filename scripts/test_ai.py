from app.ai.ai_service import AIService


def main():
    ai = AIService()

    reply = ai.chat(
        "Reply with exactly: Ollama connection successful."
    )

    print(reply)


if __name__ == "__main__":
    main()