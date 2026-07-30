import typer
from rich import print
from core.client import client, ask_llm

app = typer.Typer()


@app.command()
def hello():
    print(f"[bold cyan]Kage is now online.{client}[/bold cyan]")


@app.command()
def bye():
    print("[bold cyan]Kage is now shutting down..[/bold cyan]")


@app.command()
def ask(message: list[str]):
    response = ask_llm(" ".join(message))
    print(f"[bold cyan]{response}[/bold cyan]")


if __name__ == "__main__":
    app()
