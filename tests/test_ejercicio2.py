################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se testea que se obtengan los resultados esperados usando un valor negativo, cero y un valor positivo.
Ademas, se analiza que la poscondicion se cumpla
"""

import pytest

from src.ejercicio2 import signo

def test_signo():
    """
    Esta funcion analiza que se devuelva lo esperado con un valor negarivo, uno positivo y cero.
    También se prueba un caso en el que el parametro no es del tipo esperado
    """


    resultado1 = signo(10)
    resultado2 = signo(0) 
    resultado3 = signo(-10.23)
    resultado4 = signo("Test")
    
    assert resultado1 == 1
    assert resultado2 == 0
    assert resultado3 == -1
    assert resultado4 == "El parametro ingresado no es un numero"
    assert isinstance(resultado1, int)
    assert isinstance(resultado2, int)
    assert isinstance(resultado3, int)
    assert isinstance(resultado4, str)
