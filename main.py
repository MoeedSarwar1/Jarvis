import typer
from rich import print
from core.greetings import greet
from core.conversation import conversation

app = typer.Typer()


@app.command()
def kage():
    print(f"[#4C566A]影: {greet()}[/#4C566A]")
    conversation()


if __name__ == "__main__":
    app()
