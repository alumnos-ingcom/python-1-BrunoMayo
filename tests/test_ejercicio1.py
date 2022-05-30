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

    resultado1 = convertir_a_fahrrenheit(0)
    resultado2 = convertir_a_fahrrenheit(25)

    assert resultado1 == 32.0
    assert resultado2 == 77.0
    assert isinstance(resultado1, float)
    assert isinstance(resultado2, float)



def test_convertir_a_centigrados():

    resultado1 = convertir_a_centigrados(32)
    resultado2 = convertir_a_centigrados(77)
    
    assert resultado1 == 0
    assert resultado2 == 25.0
    assert isinstance(resultado1, float)
