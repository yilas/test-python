import pytest

from capital_growth.cli import main


def test_cli(capsys):
    assert main(["--initial", "100", "--target", "121", "--rate", "0.1"]) == 0
    output = capsys.readouterr().out
    assert "annee=2" in output
    assert "Annees necessaires: 2" in output


def test_cli_invalid(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["--rate", "0"])
    assert exc.value.code == 2
    assert "Rate must" in capsys.readouterr().err
