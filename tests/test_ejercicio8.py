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
    """
    Esta funcion prueba un valor primo, uno no primo, el uno, el cero y tabien un parametro con el tipo de dato que no corresponde
    """
    resultado1 = es_primo(17)
    resultado2 = es_primo(10)
    resultado3 = es_primo(0)
    resultado4 = es_primo(1)
    resultado5 = es_primo(True)
    
    assert resultado1 == True
    assert resultado2 == False
    assert resultado3 == False
    assert resultado4 == False
    assert resultado5 == "El parametro ingresado no es un numero entero"
    assert isinstance(resultado1, bool)
    
    