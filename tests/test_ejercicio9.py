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

def test_factores_primos_0():
    """
    Esta funcion testea un numero no primo
    Verifica que el tipo de dato que devuelve la funcion se corresponda con la poscondicion
    """
    resultado = factores_primos(1000)
    assert resultado == (2, 5)
    assert isinstance(resultado, tuple)

def test_factores_primos_1():
    """
    Esta funcion testea un numero primo
    Verifica que el tipo de dato que devuelve la funcion se corresponda con la poscondicion
    """
    resultado = factores_primos(3)
    assert resultado == (3, )
    assert isinstance(resultado, tuple)
    
def test_factores_primos_2():
    """
    Esta funcion prueba el numero cero
    Verifica que el tipo de dato que devuelve la funcion se corresponda con la poscondicion
    """
    
    resultado = factores_primos(0)
    assert resultado == ()
    assert isinstance(resultado, tuple)

def test_factores_primos_3():
    """
    Esta funcion prueba un valor que no es un numero entero
    Verifica que el tipo de dato que devuelve la funcion se corresponda con la poscondicion
    """
    resultado = factores_primos("test")
    assert resultado == "El parametro ingresado no es un numero entero"
    assert isinstance(resultado, str)