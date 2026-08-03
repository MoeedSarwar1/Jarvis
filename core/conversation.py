from core.client import ask_llm
from config import constants
from core.shutdown import shutdown

from rich import print


def conversation():
    text = None
    while text is None or text.lower() not in constants.quiting:
        text = input("> ")
        if text.lower() in constants.quiting:
            print(f"[#4C566A]影: {shutdown()}[/#4C566A]")
            break
        response = ask_llm(text)
        print(f"[#4C566A]影: {response}[/#4C566A]")
