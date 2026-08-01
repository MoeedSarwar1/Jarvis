from openai import OpenAI
from config.settings import settings
from core.personality import SYSTEM_PROMPTS

client = OpenAI(api_key=settings.openrouter_api_key,
                base_url=settings.openrouter_base_url)

conversation = [
    {'role': 'system', 'content': SYSTEM_PROMPTS}
]


def ask_llm(message: str) -> str:
    conversation.append({'role': 'user', 'content': message})
    response = client.chat.completions.create(
        model=settings.ai_model,
        messages=conversation
    )
    reply = response.choices[0].message.content
    conversation.append({'role': 'assistant', 'content': reply})
    return reply
