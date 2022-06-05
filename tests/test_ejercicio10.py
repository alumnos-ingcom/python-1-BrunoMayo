################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se evalua un palindromo en minusculas, uno con mayusculas y minusculas, uno con espacios y un no palindromo.
También se evalua la poscondicion
"""

import pytest

from src.ejercicio10 import es_palindromo

def test_es_palindromo_0():
    """
    Esta funcion testea un string todo en minusculas y junto
    Tambien chequea que el tipo de dato que retorna de la funcion se corresponda con la poscondicion
    """
    resultado = es_palindromo("neuquen")
    assert resultado == True
    assert isinstance(resultado, bool)

def test_es_palindromo_1():
    """
    Esta funcion testea un string con espacios en el medio de la palabra
    Tambien chequea que el tipo de dato que retorna de la funcion se corresponda con la poscondicion
    """
    resultado = es_palindromo("neu quen")
    assert resultado == True
    assert isinstance(resultado, bool)

def test_es_palindromo_2():
    """
    Esta funcion testea un string que mezcla minusculas y mayusculas
    Tambien chequea que el tipo de dato que retorna de la funcion se corresponda con la poscondicion
    """
    resultado = es_palindromo("neUQueN")
    assert resultado == True
    assert isinstance(resultado, bool)
    
def test_es_palindromo_3():
    """
    Esta funcion testea un string que no es palindromo
    Tambien chequea que el tipo de dato que retorna de la funcion se corresponda con la poscondicion
    """
    resultado = es_palindromo("No soy palindromo")
    assert resultado == False
    assert isinstance(resultado, bool)