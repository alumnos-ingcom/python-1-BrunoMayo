################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se prueban casos de division donde el resto sea 0, el resto sea un numero mayor a 0 y donde el divisor es mayor que el dividendo.
Tambien se chequea la poscondicion
"""

import pytest

from src.ejercicio5 import division_lenta

def test_division_lenta():
    resultado1 = division_lenta(20, 2)
    resultado2 = division_lenta(20, 3)
    resultado3 = division_lenta(0, 20)
    
    assert resultado1 == (10, 0)
    assert resultado2 == (6, 2)
    assert resultado3 == (0, 20)
    assert isinstance(resultado1[0], int)
    assert isinstance(resultado1[1], int)
