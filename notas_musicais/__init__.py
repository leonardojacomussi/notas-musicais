# isort: skip_file
from .escalas import ESCALAS, NOTAS, escala
from .acordes import acorde, semitom, triade

__version__ = '0.0.1'

__all__ = [
    'acorde',
    'NOTAS',
    'ESCALAS',
    'escala',
    'semitom',
    'triade',
]
