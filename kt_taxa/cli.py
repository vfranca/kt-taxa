"""
Scripts de console
"""
from kt_taxa import kt_taxa
import click


@click.command()
@click.argument("premio", type=float)
@click.argument("preco", type=float)
def cli(premio, preco):
    """Calcula a taxa da venda coberta."""
    risco = kt_taxa.risco(premio, preco)
    taxa = kt_taxa.taxa(premio, risco)
    click.echo("%.2f%%" % taxa)
