import typer
from rich import print
from core.client import ask_llm
from core.greetings import greet
from core.shutdown import shutdown
from config import constants

app = typer.Typer()


@app.command()
def kage():
    print(f"[#4C566A]影: {greet()}[/#4C566A]")

    text = None
    while text is None or text.lower() not in constants.quiting:
        text = input("> ")
        if text.lower() in constants.quiting:
            print(f"[#4C566A]影: {shutdown()}[/#4C566A]")
            break
        response = ask_llm(text)
        print(f"[#4C566A]影: {response}[/#4C566A]")


if __name__ == "__main__":
    app()
