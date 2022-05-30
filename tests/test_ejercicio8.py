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

def test_es_primo():
    resultado1 = es_primo(17)
    resultado2 = es_primo(10)
    resultado3 = es_primo(0)
    resultado4 = es_primo(1)
    
    assert resultado1 == True
    assert resultado2 == False
    assert resultado3 == False
    assert resultado4 == False
    assert isinstance(resultado1, bool)
    
    