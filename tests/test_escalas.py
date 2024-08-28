"""
AAA - 3A - A3
Arrange - Act - Assert
"""
from pytest import mark, raises

from notas_musicais import ESCALAS, NOTAS, escala


def test_escala_should_work_with_lowercase_notas():
    # Arrange
    tonica = 'c'
    tonalidade = 'maior'
    # Act
    result = escala(tonica, tonalidade)
    # Assert
    assert result


def test_escala_should_return_an_error_message_with_invalid_tonica():
    # Arrange
    tonica = 'x'
    tonalidade = 'maior'
    message_error = f'Essa nota não existe, tente uma dessas {NOTAS}'
    # Act
    with raises(ValueError) as error:
        escala(tonica, tonalidade)
    # Assert
    assert message_error == error.value.args[0]


def test_escala_should_return_an_error_message_with_invalid_tonalidade():
    # Arrange
    tonica = 'C'
    tonalidade = 'x'
    message_error = (
        'Essa escala não existe ou não foi implementada. '
        f'Tente uma dessas {list(ESCALAS.keys())}'
    )
    # Act
    with raises(KeyError) as error:
        escala(tonica, tonalidade)
    # Assert
    assert message_error == error.value.args[0]


@mark.parametrize(
    'tonica,tonalidade, esperado',
    [
        ('C', 'maior', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'maior', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('D', 'maior', ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']),
        ('D#', 'maior', ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D']),
        ('E', 'maior', ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']),
        ('F', 'maior', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('F#', 'maior', ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F']),
        ('G', 'maior', ['G', 'A', 'B', 'C', 'D', 'E', 'F#']),
        ('G#', 'maior', ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']),
        ('A', 'maior', ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']),
        ('A#', 'maior', ['A#', 'C', 'D', 'D#', 'F', 'G', 'A']),
        ('B', 'maior', ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']),
        ('C', 'menor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', 'menor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('F', 'menor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
    ],
)
def test_should_return_the_expected_scale(tonica, tonalidade, esperado):
    result = escala(tonica, tonalidade)
    assert result['notas'] == esperado


def test_should_return_the_expected_degrees():
    tonica = 'c'
    tonalidade = 'maior'
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    result = escala(tonica, tonalidade)

    assert result['graus'] == esperado
