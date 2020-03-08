import click
import diamonds.brilliant_earth


@click.group()
def cli():
    pass


@cli.command()
@click.option("--pages", nargs=2, type=int)
@click.option("--color", default="D,E,F,G,H,I,J")
@click.option("--sort")
def download(pages, color, sort):
    print("Downloading!")
    diamonds.brilliant_earth.download(pages[0], pages[1], color, sort)


@cli.command()
def graph():
    print("TODO")


if __name__ == "__main__":
    cli()
