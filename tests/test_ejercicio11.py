################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se analiza un caso con multiplos, uno donde no son multiplos y casos en donde alguno de los valores es cero.
Se chequea que se cumpla la poscondicion
"""

import pytest

from src.ejercicio11 import es_multiplo

def test_es_multiplo():
    """
    Esta funcion testea caso donde sucede que un numero es multiplo de otro, uno donde no,
    casos con 1 y 0 y un caso donde un parametro no es un numero
    """
    resultado1 = es_multiplo(3, 9)
    resultado2 = es_multiplo(9, 3)
    resultado3 = es_multiplo(1, 0)
    resultado4 = es_multiplo(0, 1)
    resultado5 = es_multiplo("test", 2)
    
    assert resultado1 == True
    assert resultado2 == False
    assert resultado3 == True
    assert resultado4 == False
    assert resultado5 == "El parametro ingresado no es un numero entero"
    assert isinstance(resultado1, bool)
    