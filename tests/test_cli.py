from kt_taxa.cli import cli
from click.testing import CliRunner


def test_exibicao_da_taxa():
    runner = CliRunner()
    res = runner.invoke(cli, ["1.00", "20.00"])
    assert res.output == "5.26%\n"
    assert res.exit_code == 0
