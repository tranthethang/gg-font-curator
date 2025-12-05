import click

from app.fetch_data import fetch_fonts
from app.filter_curate import main as filter_main


@click.group()
def cli():
    """Google Fonts Curator - Fetch and filter Google Fonts data."""
    pass


@cli.command()
def fetch():
    """Fetch fonts from Google Fonts API and save to output/yyyy-mm-dd/raw_fonts.json."""
    fetch_fonts()


@cli.command()
@click.option("--input-file", default=None, help="Path to raw fonts JSON file")
@click.option(
    "--top-n", default=20, type=int, help="Number of top fonts to extract (default 20)"
)
@click.option(
    "--date",
    default=None,
    help="Date folder in yyyy-mm-dd format (default: today's date)",
)
def filter(input_file, top_n, date):
    """Filter and curate fonts data."""
    try:
        filter_main(input_file=input_file, top_n=top_n, date_str=date)
    except FileNotFoundError as e:
        click.echo(f"Error: {e}", err=True)
        raise SystemExit(1)


if __name__ == "__main__":
    cli()
