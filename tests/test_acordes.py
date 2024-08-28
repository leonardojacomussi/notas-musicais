from pytest import mark

from notas_musicais import acorde

"""
Entrada
acorde Cm

Esperado:
I - III - V
C    E    G

{'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}
"""


@mark.parametrize(
    'nota,esperado',
    [
        ('C', ['C', 'E', 'G']),
        ('Cm', ['C', 'D#', 'G']),
        ('C°', ['C', 'D#', 'F#']),
        ('C+', ['C', 'E', 'G#']),
        ('Cm+', ['C', 'D#', 'G#']),
        ('F#', ['F#', 'A#', 'C#']),
    ],
)
def test_acorde_shoud_expected_notas(nota, esperado):
    notas, _ = acorde(nota).values()

    assert esperado == notas


@mark.parametrize(
    'cifra,esperado',
    [
        ('C', ['I', 'III', 'V']),
        ('Cm', ['I', 'III-', 'V']),
        ('C°', ['I', 'III-', 'V-']),
        ('C+', ['I', 'III', 'V+']),
        ('Cm+', ['I', 'III-', 'V+']),
    ],
)
def test_acorde_shoud_expected_graus(cifra, esperado):
    _, graus = acorde(cifra).values()

    assert esperado == graus
