"""
Scripts de console
"""
from kt_taxa import kt_taxa
from kt_taxa import __version__
import click


@click.command()
@click.argument("premio", type=float, required=False)
@click.argument("preco", type=float, required=False)
@click.option("--version", is_flag=True, help="Exibe a versao")
def cli(premio, preco, version):
    """Calcula a taxa da venda coberta."""
    if version:
        click.echo("kt-taxa %s" % __version__)
        return 0
    if not premio:
        click.echo("Usage: tx [OPTIONS] [PREMIO] [PRECO]")
        return 0
    risco = kt_taxa.risco(premio, preco)
    taxa = kt_taxa.taxa(premio, risco)
    click.echo("%.2f%%" % taxa)
