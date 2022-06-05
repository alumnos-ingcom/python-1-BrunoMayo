################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se analiza un caso con multiplos, uno donde no son multiplos y casos en donde alguno de los valores es cero.
Se chequea que se cumpla la poscondicion
"""

import pytest

from src.ejercicio11 import es_multiplo

def test_es_multiplo_0():
    """
    Esta funcion testea caso donde sucede que un numero es multiplo de otro.
    Tambien chequea que el tipo de dato que devuelve la funcion se corresponda con el de la poscondicion
    """
    resultado = es_multiplo(3, 9)
    assert resultado == True
    assert isinstance(resultado, bool)

def test_es_multiplo_1():
    """
    Esta funcion testea caso donde sucede que un numero NO es multiplo de otro.
    Tambien chequea que el tipo de dato que devuelve la funcion se corresponda con el de la poscondicion
    """
    resultado = es_multiplo(9, 3)
    assert resultado == False
    assert isinstance(resultado, bool)

def test_es_multiplo_2():
    """
    Esta funcion testea caso donde sucede que el multiplo es cero
    Tambien chequea que el tipo de dato que devuelve la funcion se corresponda con el de la poscondicion
    """
    resultado = es_multiplo(1, 0)
    assert resultado == True
    assert isinstance(resultado, bool)

def test_es_multiplo_3():
    """
    Esta funcion testea caso donde sucede que el numero es cero
    Tambien chequea que el tipo de dato que devuelve la funcion se corresponda con el de la poscondicion
    """
    resultado = es_multiplo(0, 1)
    assert resultado == False
    assert isinstance(resultado, bool)

def test_es_multiplo_4():
    """
    Esta funcion testea caso donde sucede que un valor no es un numero entero
    Tambien chequea que el tipo de dato que devuelve la funcion se corresponda con el de la poscondicion
    """
    resultado = es_multiplo("test", 2)
    assert resultado == "El parametro ingresado no es un numero entero"
    assert isinstance(resultado, str)
    