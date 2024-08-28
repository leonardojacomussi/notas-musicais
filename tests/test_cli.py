from pytest import mark
from typer.testing import CliRunner

from notas_musicais.cli import app

runner = CliRunner()


def test_escala_cli_should_return_0_from_stdout():
    result = runner.invoke(app, ['escala'])
    assert result.exit_code == 0


@mark.parametrize('nota', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_escala_cli_should_contain_notes_in_response(nota):
    result = runner.invoke(app, ['escala'])
    assert nota in result.stdout


@mark.parametrize('nota', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])
def test_escala_cli_should_contain_notes_in_response_of_fa(nota):
    result = runner.invoke(app, ['escala', 'F'])
    assert nota in result.stdout


@mark.parametrize('grau', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_escala_cli_should_contain_all_degrees(grau):
    result = runner.invoke(app, ['escala', 'F'])
    assert grau in result.stdout


@mark.parametrize('nota', ['C', 'E', 'G'])
def test_acorde_cli_should_contain_notes_in_response(nota):
    result = runner.invoke(app, ['acorde'])
    assert nota in result.stdout


@mark.parametrize('grau', ['I', 'III', 'V'])
def test_acorde_cli_should_contain_all_degrees(grau):
    result = runner.invoke(app, ['acorde', 'F'])
    assert grau in result.stdout


# @mark.parametrize('grau', ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°'])
# def test_campo_harmonico_cli_should_contain_all_degrees(grau):
#     result = runner.invoke(app, ['campo-harmonico', 'C'])
#     assert grau in result.stdout


# @mark.parametrize('cifra', ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B°'])
# def test_campo_harmonico_cli_should_contain_all_chords(cifra):
#     result = runner.invoke(app, ['campo-harmonico', 'C'])
#     assert cifra in result.stdout
