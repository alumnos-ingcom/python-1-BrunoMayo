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

def test_compara_0():
    """
    Esta funcion compara el caso donde el primero es mayor que el segundo.
    Tambien chequea que el tipo que devuelve la funcion corresponda a la poscondicion
    """
    resultado = compara(3, 2)
    assert resultado == 1
    assert isinstance(resultado, int)

def test_compara_1():
    """
    Esta funcion compara el caso donde ambos numeros son iguales
    Tambien chequea que el tipo que devuelve la funcion corresponda a la poscondicion
    """
    resultado = compara(2, 2)  
    assert resultado == 0    
    assert isinstance(resultado, int)

def test_compara_2():
    """
    Esta funcion compara el caso donde el segundo es mayor que el segundo.
    Tambien chequea que el tipo que devuelve la funcion corresponda a la poscondicion
    """
    resultado = compara(2, 3)    
    assert resultado == -1
    assert isinstance(resultado, int)

def test_compara_3():
    """
    Esta funcion compara el caso donde uno de los parametros no es un numero
    Tambien chequea que el tipo que devuelve la funcion corresponda a la poscondicion
    """
    resultado = compara("hola", 2)
    assert resultado == "Uno o ambos parametros ingresado no es un numero"
    assert isinstance(resultado, str)