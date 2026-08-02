from openai import OpenAI
from config.settings import settings
from core.personality import SYSTEM_PROMPTS
from core.tools import TOOLS, get_time_date

client = OpenAI(api_key=settings.openrouter_api_key,
                base_url=settings.openrouter_base_url)

conversation = [
    {'role': 'system', 'content': SYSTEM_PROMPTS}
]


def ask_llm(message: str) -> str:
    conversation.append({'role': 'user', 'content': message})
    response = client.chat.completions.create(
        model=settings.ai_model,
        messages=conversation,
        tools=TOOLS
    )
    msg = response.choices[0].message

    if msg.tool_calls:
        call = msg.tool_calls[0]
        tool_name = call.function.name

        if tool_name == "get_time_date":
            result = get_time_date()
            conversation.append(msg)
            conversation.append(
                {'role': 'tool', 'tool_call_id': call.id, 'content': result})
            response = client.chat.completions.create(
                model=settings.ai_model,
                messages=conversation,
                tools=TOOLS
            )

            reply = msg.content
    else:
        reply = msg.content

    conversation.append({'role': 'assistant', 'content': reply})
    return reply
