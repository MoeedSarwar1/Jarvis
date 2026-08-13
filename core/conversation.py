
from core.client import ask_llm
from config import constants
from core.shutdown import shutdown
from rich.console import Console
from rich.markdown import Markdown

# Initialize the Console object
console = Console()


def conversation():
    text = None
    while text is None or text.lower() not in constants.quiting:
        text = input("> ")
        if text.lower() in constants.quiting:
            console.print(f"[#4C566A]影: {shutdown()}[/#4C566A]")
            break

        # 1. Fetch the raw text response from the LLM
        response = ask_llm(text)

        # 2. Convert the response into a Rich Markdown object
        md_response = Markdown(response, style="#4C566A")

        # 3. Print the prefix and the styled Markdown together
        console.print("[#4C566A]影:[/#4C566A]", md_response)
