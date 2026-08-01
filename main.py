import typer
from rich import print
from core.client import ask_llm
from config import constants

app = typer.Typer()


@app.command()
def kage():
    greetings = ask_llm("greet me, tell me you name, and ask what i want")
    print(f"Kage: {greetings}")

    text = None
    while text is None or text.lower() not in constants.quiting:
        text = input("You: ")
        if text.lower() in constants.quiting:
            break
        response = ask_llm(text)
        print(f"Kage: {response}")


if __name__ == "__main__":
    app()
