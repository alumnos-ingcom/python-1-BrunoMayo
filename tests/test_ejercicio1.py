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


def test_convertir_a_fahrrenheit_0():
    """
    Esta funcion testea un valor negativo y se asegura que la conversion sea correcta. 
    Tambien analiza que el tipo de salida sea el esperado en la poscondicion
    """
    resultado = convertir_a_fahrrenheit(-10)
    assert resultado == 14.0 
    assert isinstance(resultado, float)
    
    
def test_convertir_a_fahrrenheit_1():
    """
    Esta funcion testea un valor positivo y se asegura que la conversion sea correcta
    Tambien analiza que el tipo de salida sea el esperado en la poscondicion
    """
    resultado = convertir_a_fahrrenheit(25)
    assert resultado == 77.0
    assert isinstance(resultado, float)


def test_convertir_a_fahrrenheit_2():
    """
    Esta funcion prueba un valor de entrada que no es posible convertir
    Tambien analiza que el tipo de salida sea el esperado en la poscondicion
    """
    resultado = convertir_a_fahrrenheit("Hola")
    assert resultado == "El parametro ingresado no es un numero natural"
    assert isinstance(resultado, str)


def test_convertir_a_centigrados_0():
    """
    Esta funcion chequea la inversa de convertir_a_fahrrenheit_0 y determina que se obtenga el mismo resultado
    Tambien analiza que el tipo de salida sea el esperado en la poscondicion
    """
    resultado = convertir_a_centigrados(14)
    assert resultado == -10.0
    assert isinstance(resultado, float)
    
    

def test_convertir_a_centigrados_1():
    """
    Esta funcion chequea la inversa de convertir_a_fahrrenheit_1 y determina que se obtenga el mismo resultado
    Tambien analiza que el tipo de salida sea el esperado en la poscondicion
    """
    resultado = convertir_a_centigrados(77)
    assert resultado == 25.0
    assert isinstance(resultado, float)


def test_convertir_a_centigrados_2():
    """
    Esta funcion prueba un valor de entrada que no es posible convertir
    Tambien analiza que el tipo de salida sea el esperado en la poscondicion
    """
    resultado = convertir_a_centigrados("Hola")
    assert resultado == "El parametro ingresado no es un numero natural"
    assert isinstance(resultado, str)
