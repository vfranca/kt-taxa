"""
Testes unitários
"""
from kt_taxa import __version__
from kt_taxa import kt_taxa


def test_version():
    assert __version__ == "0.3.0"


def test_calcula_o_preco_de_aquisicao_no_exercicio():
    assert kt_taxa.aquisicao_exercicio(0.61, 26.06) == 25.45


def test_lucro_no_exercicio():
    assert kt_taxa.lucro_exercicio(27.18, 25.45) == 1.73


def test_calcula_taxa_no_exercicio():
    assert kt_taxa.taxa_exercicio(25.44, 1.73) == 6.80
