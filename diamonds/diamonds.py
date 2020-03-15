import click
import diamonds.brilliant_earth
import diamonds.graph


@click.group()
def cli():
    pass


@cli.command()
@click.option("--pages", nargs=2, type=int)
@click.option("--color", default="D,E,F,G,H,I,J")
@click.option("--shape", default="Round")
@click.option("--clarity", default="SI2,SI1,VS2,VS1,VVS2,VVS1,IF,FL")
@click.option("--cut", default="Fair,Good,Very Good,Ideal,Super Ideal")
@click.option("--sort")
def download(pages, color, sort, shape, clarity, cut):
    print("Downloading!")
    diamonds.brilliant_earth.download(pages[0], pages[1], color, sort, shape, clarity, cut)


@cli.command()
@click.option("--carat", nargs=2, type=float)
@click.option("--shape", default="Round")
@click.option("--color", default="D,E,F,G,H,I,J")
@click.option("--clarity", default="SI2,SI1,VS2,VS1,VVS2,VVS1,IF,FL")
@click.option("--cut", default="Fair,Good,Very Good,Ideal,Super Ideal")
@click.option("--price", nargs=2, type=float)
def graph(carat=None, shape=None, color=None, clarity=None, cut=None, price=None):
    diamonds.graph.graph(carat, shape, color, clarity, cut, price)
    # diamonds.graph.test()


if __name__ == "__main__":
    cli()
