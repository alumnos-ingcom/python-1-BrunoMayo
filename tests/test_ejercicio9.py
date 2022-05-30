################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se evalua un numero no primo, uno primo y el cero.
También se chequea que se cumpla la poscondicion
"""

import pytest

from src.ejercicio9 import factores_primos

def test_factores_primos():
    resultado1 = factores_primos(1000)
    resultado2 = factores_primos(3)
    resultado3 = factores_primos(0)
    
    assert resultado1 == (2, 5)
    assert resultado2 == (3)
    assert resultado3 == ()
    assert isinstance(resultado1, tuple)