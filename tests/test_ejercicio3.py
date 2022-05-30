################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se prueban los casos en donde el primer numero es mayor que el segundo, cuando son iguales y cuando el segundo es mayor que el primerio.
Tambien se testea que la poscondicion se cumpla.
"""

import pytest

from src.ejercicio3 import compara

def test_compara():
    resultado1 = compara(3, 2)
    resultado2 = compara(2, 2)    
    resultado3 = compara(2, 3)    
    
    
    assert resultado1 == 1
    assert resultado2 == 0
    assert resultado3 == -1
    assert isinstance(resultado1, int)
