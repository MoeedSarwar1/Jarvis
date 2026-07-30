import typer
from rich import print

app = typer.Typer()


@app.command()
def hello():
    print("[bold cyan]Kage is now online.[/bold cyan]")


if __name__ == "__main__":
    app()
