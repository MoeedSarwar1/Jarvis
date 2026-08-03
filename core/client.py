from openai import OpenAI, APIError, AuthenticationError, APIConnectionError
from config.settings import settings
from core.personality import SYSTEM_PROMPTS
from core.tools import TOOLS, tool_dictionary
from core.error import error
import json

client = OpenAI(api_key=settings.openrouter_api_key,
                base_url=settings.openrouter_base_url)

conversation = [
    {'role': 'system', 'content': SYSTEM_PROMPTS}
]


def ask_llm(message: str) -> str:
    try:
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
            args = json.loads(call.function.arguments)
            func = tool_dictionary[tool_name]
            result = func(**args)
            conversation.append(msg)
            conversation.append(
                {'role': 'tool', 'tool_call_id': call.id, 'content': result})
            response = client.chat.completions.create(
                model=settings.ai_model,
                messages=conversation,
                tools=TOOLS
            )
            msg = response.choices[0].message
            reply = msg.content

        else:
            reply = msg.content

        conversation.append({'role': 'assistant', 'content': reply})
        return reply
    except (APIError, AuthenticationError, APIConnectionError):
        return error()
