################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""

import pytest

from src.ejemplo1 import convertir_a_fahrrenheit, convertir_a_centigrados


def test_convertir_a_fahrrenheit():
    """
       Se testea que de acuerdo al valor ingresado en celcius se obtenga su equivalente en fahrenheit.
       Para realizar los test se utiliza el caso donde hay 0 grados celcius para ver que la diferencia en  la conver
       sion sea la debida, un caso en donde la temperatura sea en grados positivos y otra en grados negativos.
       Por otra parte se analiza un caso donde la entrada no es un valor numerico
    """
    caso1 = 0
    caso2 = 25
    caso3 = -25
    resultado1 = convertir_a_fahrrenheit(caso1)
    resultado2 = convertir_a_fahrrenheit(caso2)
    resultado3 = convertir_a_fahrrenheit(caso3)

    assert resultado1 == 32.0
    assert resultado2 == 77.0
    assert resultado3 == -13.0
    assert isinstance(resultado1, float)
    assert isinstance(resultado2, float)
    assert isinstance(resultado3, float)
