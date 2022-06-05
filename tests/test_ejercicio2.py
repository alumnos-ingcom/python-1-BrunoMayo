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

def test_signo_0():
    """
    Esta funcion analiza el caso para un numero positivo
    También se prueba que el tipo devuelto corresponda a la poscondicion
    """
    resultado = signo(10)
    assert resultado == 1
    assert isinstance(resultado, int)
    
    
    
def test_signo_1():
    """
    Esta funcion analiza el caso para el cero
    También se prueba que el tipo devuelto corresponda a la poscondicion
    """
    resultado = signo(0) 
    assert resultado == 0
    assert isinstance(resultado, int)


def test_signo_2():
    """
    Esta funcion analiza el caso para un numero negativo
    También se prueba que el tipo devuelto corresponda a la poscondicion
    """
    resultado = signo(-10.23)
    assert resultado == -1
    assert isinstance(resultado, int)


def test_signo_3():
    """
    Esta funcion analiza el caso para un valor de entreada que no es un numero
    También se prueba que el tipo devuelto corresponda a la poscondicion
    """
    resultado = signo("Test")
    assert resultado == "El parametro ingresado no es un numero"
    assert isinstance(resultado, str)