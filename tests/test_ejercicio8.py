################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se prueba un valor primo, uno no primo y el uno y el cero que no son primos.
Se evalua que se cumpla la poscondicion
"""

import pytest

from src.ejercicio8 import es_primo

def test_es_primo_0():
    """
    Esta funcion prueba un valor primo
    Tambien chequea que el tipo de dato que devuelve al funcion se corresponda con la poscondicion
    """
    resultado = es_primo(17)
    assert resultado == True
    assert isinstance(resultado, bool)

def test_es_primo_1():
    """
    Esta funcion prueba un valor no primo
    Tambien chequea que el tipo de dato que devuelve al funcion se corresponda con la poscondicion
    """
    resultado = es_primo(10)
    assert resultado == False
    assert isinstance(resultado, bool)

def test_es_primo_2():
    """
    Esta funcion prueba el cero
    Tambien chequea que el tipo de dato que devuelve al funcion se corresponda con la poscondicion
    """
    resultado = es_primo(0)
    assert resultado == False
    assert isinstance(resultado, bool)

def test_es_primo_3():  
    """
    Esta funcion prueba el uno
    Tambien chequea que el tipo de dato que devuelve al funcion se corresponda con la poscondicion
    """
    resultado = es_primo(1)
    assert resultado == False
    assert isinstance(resultado, bool)

def test_es_primo_4():  
    """
    Esta funcion prueba tipo de dato que no es un numero entero
    Tambien chequea que el tipo de dato que devuelve al funcion se corresponda con la poscondicion
    """
    resultado = es_primo(True)
    assert resultado == "El parametro ingresado no es un numero entero"
    assert isinstance(resultado, str)
    
    