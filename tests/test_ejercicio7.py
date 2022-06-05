################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
En el caso de sexadecimal a decimal se preuban diversos casos, uno en el que se le da un valor a grados, a minutos y a segundos y despues cada valor por separado.
En el caso de decimal a sexadecimal se prueban los valores que otorgo la funcion anterior.
Se prueba que en cada funcion se cumpla la poscondicion
"""

import pytest

from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal

def test_sexadecimal_a_decimal_0():
    """
    Esta funcion testea un valor en grados, minutos y segundos asegurandose que la conversion sea correcta
    Tambien chequea que el tipo de dato que devuelve sea correcto
    """
    resultado = sexadecimal_a_decimal(1, 1, 1)
    assert resultado == 3661
    assert isinstance(resultado, int)
    

def test_sexadecimal_a_decimal_1():   
    """
    Esta funcion testea el caso en donde un valor de entrada no es un numero entero
    Tambien chequea que el tipo de dato que devuelve sea correcto
    """
    resultado = sexadecimal_a_decimal("test", 0, 1)
    assert resultado == "Alguno de los parametros ingresados no es un numero entero"
    assert isinstance(resultado, str)



def test_decimal_a_sexadecimal_0():    
    """
    Esta funcion testea que se realize correctamenta la conversion de segundos a grados, minutos y segundos
    Tambien chequea que el tipo de dato que devuelve sea correcto
    """
    resultado = decimal_a_sexadecimal(3661)
    assert resultado == (1, 1, 1)
    assert isinstance(resultado, tuple)

def test_decimal_a_sexadecimal_1():    
    """
    Esta funcion testea el caso en donde el parametro de entrada no es un numero entero
    Tambien chequea que el tipo de dato que devuelve sea correcto
    """
    resultado = decimal_a_sexadecimal("test")
    assert resultado == "Alguno de los parametros ingresados no es un numero entero"
    assert isinstance(resultado, str)