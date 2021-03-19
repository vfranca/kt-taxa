from kt_taxa import kt_taxa
import click


@click.command()
@click.argument("premio")
@click.argument("preco")
def cli(premio, preco):
    """Calcula a taxa da venda coberta."""
    premio = float(premio)
    preco = float(preco)
    risco = kt_taxa.risco(premio, preco)
    taxa = kt_taxa.taxa(premio, risco)
    click.echo("%.2f%%" % taxa)
