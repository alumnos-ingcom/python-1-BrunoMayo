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

def test_sexadecimal_a_decimal():
    """
    Esta funcion testea casos donde se ingresa un numero positivo en cada valor, cada valor individualmente y un 
    caso en el que un parametro no es un numero entero
    """

    resultado1 = sexadecimal_a_decimal(1, 1, 1)
    resultado2 = sexadecimal_a_decimal(1, 0, 0)
    resultado3 = sexadecimal_a_decimal(0, 1, 0)
    resultado4 = sexadecimal_a_decimal(0, 0, 1)
    resultado5 = sexadecimal_a_decimal("test", 0, 1)
    
    assert resultado1 == 3661
    assert resultado2 == 3600
    assert resultado3 == 60
    assert resultado4 == 1
    assert resultado5 == "Alguno de los parametros ingresados no es un numero entero"
    assert isinstance(resultado1, int)
    
    
    
def test_decimal_a_sexadecimal():    
    """
    Esta funcion testea distintos valores y prueba un caso donde el parametro no es valido
    """

    resultado1 = decimal_a_sexadecimal(3661)
    resultado2 = decimal_a_sexadecimal(3600)
    resultado3 = decimal_a_sexadecimal(60)
    resultado4 = decimal_a_sexadecimal(1)
    resultado5 = decimal_a_sexadecimal("test")
    
    assert resultado1 == (1, 1, 1)
    assert resultado2 == (1, 0, 0)
    assert resultado3 == (0, 1, 0)
    assert resultado4 == (0, 0, 1)
    assert resultado5 == "Alguno de los parametros ingresados no es un numero entero"
    assert isinstance(resultado1, tuple)