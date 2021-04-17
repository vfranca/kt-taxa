"""
Testes funcionais
"""
from kt_taxa.cli import cli
from click.testing import CliRunner
import mock


runner = CliRunner()


def test_exibe_a_taxa_de_financiamento_no_exercicio():
    res = runner.invoke(cli, ["0.61", "27.18", "26.06"])
    assert res.output == "6.80%\n"
    assert res.exit_code == 0


def test_saida_sem_parametros():
    res = runner.invoke(cli, [])
    assert res.output == "Usage: tx [OPTIONS] [PREMIO] [STRIKE] [COTACAO]\n"
    assert res.exit_code == 0
