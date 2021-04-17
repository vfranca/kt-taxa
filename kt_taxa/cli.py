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
@click.option("--aquisicao-descontada", "-ad", is_flag=True)
@click.option("--version", is_flag=True, help="Exibe a versao")
def cli(premio, strike, cotacao, aquisicao_descontada, version):
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
    if aquisicao_descontada:
        click.echo("%.2f" % aquisicao)
        return 0
    click.echo("%.2f%%" % taxa)
    return 0
