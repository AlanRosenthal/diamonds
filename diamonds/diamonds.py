import click
import diamonds.store
import diamonds.brilliant_earth


@click.command()
@click.option("--download", is_flag=True)
@click.option("--start", type=int)
@click.option("--end", type=int)
@click.option("--color", default="J,F,G,I,E,D,H")
@click.option("--sort")
def main(download=False, start=1, end=100, color=None, sort="asc"):
    if download:
        print("Downloading!")
        diamonds.brilliant_earth.download(start, end, color, sort)


if __name__ == "__main__":
    main()
