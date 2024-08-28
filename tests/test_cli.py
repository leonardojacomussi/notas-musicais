from pytest import mark
from typer.testing import CliRunner

from notas_musicais.cli import app

runner = CliRunner()


def test_escala_cli_should_return_0_from_stdout():
    result = runner.invoke(app)
    assert result.exit_code == 0


@mark.parametrize('nota', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_escala_cli_should_contain_notes_in_response(nota):
    result = runner.invoke(app)
    assert nota in result.stdout


@mark.parametrize('nota', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])
def test_escala_cli_should_contain_notes_in_response_of_fa(nota):
    result = runner.invoke(app, ['F'])
    assert nota in result.stdout


@mark.parametrize('grau', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_escala_cli_should_contain_all_degrees(grau):
    result = runner.invoke(app, ['F'])
    assert grau in result.stdout
