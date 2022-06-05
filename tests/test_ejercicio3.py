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

def test_compara():
    """
    Esta funcion compara las 3 posibilidades: si el primer numero es mayor que el segundo, al revés o si son iguales.
    Tambien se prueba lo que sucede cuando un parametro ingresado no es un numero.
    """


    resultado1 = compara(3, 2)
    resultado2 = compara(2, 2)    
    resultado3 = compara(2, 3)    
    resultado4 = compara("hola", 2)
    
    assert resultado1 == 1
    assert resultado2 == 0
    assert resultado3 == -1
    assert resultado4 == "Uno o ambos parametros ingresado no es un numero"
    assert isinstance(resultado1, int)
