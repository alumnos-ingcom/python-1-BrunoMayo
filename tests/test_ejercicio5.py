################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se prueban casos de division donde el resto sea 0, el resto sea un numero mayor a 0 y donde el divisor es mayor que el dividendo.
Tambien se chequea la poscondicion
"""

import pytest

from src.ejercicio5 import division_lenta

def test_division_lenta():
    """
    Esta funcion testea division con y sin resto, division por cero y tambien caso en el que un parametro no es un numero entero
    """
    resultado1 = division_lenta(20, 2)
    resultado2 = division_lenta(20, 3)
    resultado3 = division_lenta(20, 0)
    resultado4 = division_lenta("Hola", 20)
    
    
    assert resultado1 == (10, 0)
    assert resultado2 == (6, 2)
    assert resultado3 == "No se puede realizar la operacion ya que el divisor es 0"
    assert resultado4 == "Alguno de los parametros ingresados no es un numero entero"
    assert isinstance(resultado1[0], int)
    assert isinstance(resultado1[1], int)
