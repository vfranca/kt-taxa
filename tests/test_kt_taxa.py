from kt_taxa import __version__
from kt_taxa import kt_taxa


def test_version():
    assert __version__ == "0.1.0"


def test_calcula_o_risco():
    assert kt_taxa.risco(0.7, 27.10) == 26.40


def test_calcula_a_taxa():
    assert kt_taxa.taxa(1.0, 20.0) == 5.0
