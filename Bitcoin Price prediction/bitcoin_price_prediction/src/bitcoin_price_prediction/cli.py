"""Console script for bitcion_price_prediction."""

import typer
from rich.console import Console

from bitcion_price_prediction import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for bitcion_price_prediction."""
    console.print("Replace this message by putting your code into "
               "bitcion_price_prediction.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
