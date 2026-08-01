import typer
from rich import print
from core.client import client, ask_llm
from config import constants

app = typer.Typer()


@app.command()
def hello():
    print(f"[bold cyan]Kage is now online.{client}[/bold cyan]")


@app.command()
def bye():
    print("[bold cyan]Kage is now shutting down..[/bold cyan]")


@app.command()
def ask():
    text = None
    while text is None or text not in constants.quiting:
        text = input("You: ")
        if text.lower() in constants.quiting:
            break
        response = ask_llm(text)
        print(f"Kage: {response}")


if __name__ == "__main__":
    app()
