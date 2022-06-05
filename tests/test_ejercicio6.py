################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se prueban todos los casos posibles de entrada variando el orden en el que se ingresan los parametros
Tambien se prueba que la poscondicion se cumpla
"""

import pytest

from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor

def test_ordenar_mayor_a_menor():
    resultado1 = ordenar_mayor_a_menor(1, 2, 3)
    resultado2 = ordenar_mayor_a_menor(1, 3, 2)
    resultado3 = ordenar_mayor_a_menor(2, 1, 3)
    resultado4 = ordenar_mayor_a_menor(2, 3, 1)
    resultado5 = ordenar_mayor_a_menor(3, 2, 1)
    resultado6 = ordenar_mayor_a_menor(3, 1, 2)
    resultado7 = ordenar_mayor_a_menor(1, 1, 2)
    resultado8 = ordenar_mayor_a_menor("hola", 1, 3)    
    
    assert resultado1 == (3, 2, 1)
    assert resultado2 == (3, 2, 1)
    assert resultado3 == (3, 2, 1)
    assert resultado4 == (3, 2, 1)
    assert resultado5 == (3, 2, 1)
    assert resultado6 == (3, 2, 1)
    assert resultado7 == (2, 1, 1)
    assert resultado8 == "Alguno de los parametros ingresados no es un numero entero"
    assert isinstance(resultado1, tuple) 
    
    
    
def test_ordenar_menor_a_mayor():
    resultado1 = ordenar_menor_a_mayor(1, 2, 3)
    resultado2 = ordenar_menor_a_mayor(1, 3, 2)
    resultado3 = ordenar_menor_a_mayor(2, 1, 3)
    resultado4 = ordenar_menor_a_mayor(2, 3, 1)
    resultado5 = ordenar_menor_a_mayor(3, 2, 1)
    resultado6 = ordenar_menor_a_mayor(3, 1, 2)
    resultado7 = ordenar_menor_a_mayor(1, 1, 2)
    resultado8 = ordenar_menor_a_mayor("hola", 4, 2)
    
    assert resultado1 == (1, 2, 3)
    assert resultado2 == (1, 2, 3)
    assert resultado3 == (1, 2, 3)
    assert resultado4 == (1, 2, 3)
    assert resultado5 == (1, 2, 3)
    assert resultado6 == (1, 2, 3)
    assert resultado7 == (1, 1, 2)
    assert resultado8 == "Alguno de los parametros ingresados no es un numero entero"
    assert isinstance(resultado1, tuple) 
    
    