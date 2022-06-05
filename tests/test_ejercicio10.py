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

def test_es_palindromo():
    resultado1 = es_palindromo("neuquen")
    resultado2 = es_palindromo("neu quen")
    resultado3 = es_palindromo("neuqueN")
    resultado4 = es_palindromo("No soy palindromo")
    
    
    assert resultado1 == True
    assert resultado2 == True
    assert resultado3 == True
    assert resultado4 == False
    assert isinstance(resultado1, bool)