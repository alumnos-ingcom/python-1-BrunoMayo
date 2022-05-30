################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se testea que se obtengan los resultados esperados usando un valor negarivo, cero y un valor positivo.
Ademas, se analiza que la poscondicion se cumpla
"""

import pytest

from src.ejercicio2 import signo

def test_signo():
    resultado1 = signo(10)
    resultado2 = signo(0) 
    resultado3 = signo(-10)
    
    assert resultado1 == "positivo"
    assert resultado2 == "cero"
    assert resultado3 == "negativo"
    assert isinstance(resultado1, str)
