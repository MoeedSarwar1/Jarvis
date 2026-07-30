from openai import OpenAI
from config.settings import settings
from core.personality import SYSTEM_PROMPTS

client = OpenAI(api_key=settings.openrouter_api_key,
                base_url=settings.openrouter_base_url)


def ask_llm(message: str) -> str:
    response = client.chat.completions.create(
        model=settings.ai_model,
        messages=[
            {'role': 'system', 'content': SYSTEM_PROMPTS},
            {'role': 'user', 'content': message}
        ]
    )
    return response.choices[0].message.content
