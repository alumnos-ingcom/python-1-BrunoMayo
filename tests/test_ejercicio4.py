################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se prueba la suma de dos numeros negarivos, dos positivos y un negativo con un positivo.
Tambien se chequea que se cumpla la poscondicion
"""

import pytest

from src.ejercicio4 import suma_lenta

def test_suma_lenta_0():
    """
    Esta funcion analiza el caso de suma de dos numeros enteros positivos
    Tambien chequea que el tipo de dato que devuelve la funcion corresponda con la poscondicion
    """
    resultado = suma_lenta(5, 3)
    assert resultado == 8
    assert isinstance(resultado, int)


def test_suma_lenta_1():
    """
    Esta funcion analiza el caso de suma de un numero entero positivo y uno negativo
    Tambien chequea que el tipo de dato que devuelve la funcion corresponda con la poscondicion
    """
    resultado = suma_lenta(5, -3)
    assert resultado == 2
    assert isinstance(resultado, int)

def test_suma_lenta_2():
    """
    Esta funcion analiza el caso de suma de dos numeros enteros negativos
    Tambien chequea que el tipo de dato que devuelve la funcion corresponda con la poscondicion
    """
    resultado = suma_lenta(-5, -3)
    assert resultado == -8
    assert isinstance(resultado, int)

def test_suma_lenta_3():
    """
    Esta funcion analiza el caso de suma donde un valor no es un numero entero
    Tambien chequea que el tipo de dato que devuelve la funcion corresponda con la poscondicion
    """
    resultado = suma_lenta(2.3, 4)
    assert resultado =="Alguno de los parametros ingresados no es un numero entero"
    assert isinstance(resultado, str)