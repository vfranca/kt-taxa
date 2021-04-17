"""
Scripts de console
"""
from kt_taxa import kt_taxa
from kt_taxa import __version__
import click


@click.command()
@click.argument("premio", type=float, required=False)
@click.argument("strike", type=float, required=False)
@click.argument("cotacao", type=float, required=False)
@click.option("--version", is_flag=True, help="Exibe a versao")
def cli(premio, strike, cotacao, version):
    """Calcula a taxa de financiamento no exercício de uma operação de venda coberta."""
    if version:
        click.echo("kt-taxa %s" % __version__)
        return 0
    if not premio:
        click.echo("Usage: tx [OPTIONS] [PREMIO] [STRIKE] [COTACAO]")
        return 0
    aquisicao = kt_taxa.aquisicao_exercicio(premio, cotacao)
    lucro = kt_taxa.lucro_exercicio(strike, aquisicao)
    taxa = kt_taxa.taxa_exercicio(aquisicao, lucro)
    click.echo("%.2f%%" % taxa)
