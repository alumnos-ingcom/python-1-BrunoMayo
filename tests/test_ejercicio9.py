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
    """
    Esta funcion testea un numero primo, uno no primo, el cero y un paramentro de 
    entreada no correcto
    """
    resultado1 = factores_primos(1000)
    resultado2 = factores_primos(3)
    resultado3 = factores_primos(0)
    resultado4 = factores_primos("test")
    
    assert resultado1 == (2, 5)
    assert resultado2 == (3)
    assert resultado3 == ()
    assert resultado4 == "El parametro ingresado no es un numero entero"
    assert isinstance(resultado1, tuple)