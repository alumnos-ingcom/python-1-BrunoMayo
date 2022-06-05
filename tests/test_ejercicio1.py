################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
En los test de las funciones de conversión de grados se van a testear valores para ver que la
conversion sea correcta y tamben se va a chequear que el resultado obtenido sea del tipo que lo requiere la
poscondicion
"""

import pytest

from src.ejercicio1 import convertir_a_fahrrenheit, convertir_a_centigrados


def test_convertir_a_fahrrenheit():
    """
    Esta funcion chequea dos valores, uno negativo y uno positivo para ver que su conversion sea correcta.
    Tambien prueba un caso en donde el parametro de entrada no es un numero decimal.
    """

    resultado1 = convertir_a_fahrrenheit(-10)
    resultado2 = convertir_a_fahrrenheit(25)
    resultado3 = convertir_a_fahrrenheit("Hola")

    assert resultado1 == 14.0 
    assert resultado2 == 77.0
    assert resultado3 == "El parametro ingresado no es un numero natural"
    assert isinstance(resultado1, float)
    assert isinstance(resultado2, float)
    assert isinstance(resultado3, str)
    


def test_convertir_a_centigrados():
    """
    Esta funcion chequea dos valores, uno negativo y uno positivo para ver que su conversion sea correcta.
    Tambien prueba un caso en donde el parametro de entrada no es un numero decimal.
    """

    resultado1 = convertir_a_centigrados(14)
    resultado2 = convertir_a_centigrados(77)
    resultado3 = convertir_a_centigrados("Hola")
    
    assert resultado1 == -10.0
    assert resultado2 == 25.0
    assert resultado3 == "El parametro ingresado no es un numero natural"
    assert isinstance(resultado1, float)
    assert isinstance(resultado2, float)
    assert isinstance(resultado3, str)
    
    
