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

def test_division_lenta_0():
    """
    Esta funcion testea la division sin resto
    Tambien chequea que el tipo que devuelve la funcion se conrresponda con la poscondicion
    """
    resultado = division_lenta(20, 2)
    assert resultado == (10, 0)
    assert isinstance(resultado, tuple)
    

def test_division_lenta_1():
    """
    Esta funcion testea la division con resto
    Tambien chequea que el tipo que devuelve la funcion se conrresponda con la poscondicion
    """
    resultado = division_lenta(20, 3)
    assert resultado == (6, 2)
    assert isinstance(resultado, tuple) 

def test_division_lenta_2():
    """
    Esta funcion testea la division por cero
    Tambien chequea que el tipo que devuelve la funcion se conrresponda con la poscondicion
    """
    resultado = division_lenta(20, 0)
    assert resultado == "No se puede realizar la operacion ya que el divisor es 0"
    assert isinstance(resultado, str)


def test_division_lenta_3():
    """
    Esta funcion testea el caso donde uno de los parametros no es un numero entero
    Tambien chequea que el tipo que devuelve la funcion se conrresponda con la poscondicion
    """
    resultado = division_lenta("Hola", 20)
    assert resultado == "Alguno de los parametros ingresados no es un numero entero"
    assert isinstance(resultado, str)