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

def test_ordenar_mayor_a_menor_0():
    """
    Se testea una de las posibles 6 formas de entrada con respecto a el orden de ingreso de los parametros
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_mayor_a_menor(1, 2, 3)
    assert resultado == (3, 2, 1)
    assert isinstance(resultado, tuple)

def test_ordenar_mayor_a_menor_1():
    """
    Se testea una de las posibles 6 formas de entrada con respecto a el orden de ingreso de los parametros
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_mayor_a_menor(1, 3, 2)
    assert resultado == (3, 2, 1)
    assert isinstance(resultado, tuple)

def test_ordenar_mayor_a_menor_2():
    """
    Se testea una de las posibles 6 formas de entrada con respecto a el orden de ingreso de los parametros
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_mayor_a_menor(2, 1, 3)
    assert resultado == (3, 2, 1)
    assert isinstance(resultado, tuple)

def test_ordenar_mayor_a_menor_3():
    """
    Se testea una de las posibles 6 formas de entrada con respecto a el orden de ingreso de los parametros
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_mayor_a_menor(2, 3, 1)
    assert resultado == (3, 2, 1)
    assert isinstance(resultado, tuple)

def test_ordenar_mayor_a_menor_4():
    """
    Se testea una de las posibles 6 formas de entrada con respecto a el orden de ingreso de los parametros
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_mayor_a_menor(3, 2, 1)
    assert resultado == (3, 2, 1)
    assert isinstance(resultado, tuple)

def test_ordenar_mayor_a_menor_5():
    """
    Se testea una de las posibles 6 formas de entrada con respecto a el orden de ingreso de los parametros
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_mayor_a_menor(3, 1, 2)
    assert resultado == (3, 2, 1)
    assert isinstance(resultado, tuple)

def test_ordenar_mayor_a_menor_6():
    """
    Se testea una de las posibles 6 formas de entrada con respecto a el orden de ingreso de los parametros
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_mayor_a_menor(1, 1, 2)
    assert resultado == (2, 1, 1)
    assert isinstance(resultado, tuple)

def test_ordenar_mayor_a_menor_7():
    """
    Se testea el caso donde un parametro de entrada no es un numero entero
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_mayor_a_menor("hola", 1, 3)    
    assert resultado == "Alguno de los parametros ingresados no es un numero entero"
    assert isinstance(resultado, str) 
    
    
    
def test_ordenar_menor_a_mayor_0():
    """
    Se testea una de las posibles 6 formas de entrada con respecto a el orden de ingreso de los parametros
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_menor_a_mayor(1, 2, 3)
    assert resultado == (1, 2, 3)
    assert isinstance(resultado, tuple) 

def test_ordenar_menor_a_mayor_1():
    """
    Se testea una de las posibles 6 formas de entrada con respecto a el orden de ingreso de los parametros
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_menor_a_mayor(1, 3, 2)
    assert resultado == (1, 2, 3)
    assert isinstance(resultado, tuple) 

def test_ordenar_menor_a_mayor_2():
    """
    Se testea una de las posibles 6 formas de entrada con respecto a el orden de ingreso de los parametros
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_menor_a_mayor(2, 1, 3)
    assert resultado == (1, 2, 3)
    assert isinstance(resultado, tuple) 
    
def test_ordenar_menor_a_mayor_3():
    """
    Se testea una de las posibles 6 formas de entrada con respecto a el orden de ingreso de los parametros
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_menor_a_mayor(2, 3, 1)
    assert resultado == (1, 2, 3)
    assert isinstance(resultado, tuple) 

def test_ordenar_menor_a_mayor_4():
    """
    Se testea una de las posibles 6 formas de entrada con respecto a el orden de ingreso de los parametros
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_menor_a_mayor(3, 2, 1)
    assert resultado == (1, 2, 3)
    assert isinstance(resultado, tuple) 

def test_ordenar_menor_a_mayor_5():
    """
    Se testea una de las posibles 6 formas de entrada con respecto a el orden de ingreso de los parametros
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_menor_a_mayor(3, 1, 2)
    assert resultado == (1, 2, 3)
    assert isinstance(resultado, tuple) 

def test_ordenar_menor_a_mayor_6():
    """
    Se testea una de las posibles 6 formas de entrada con respecto a el orden de ingreso de los parametros
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_menor_a_mayor(1, 1, 2)
    assert resultado == (1, 1, 2)
    assert isinstance(resultado, tuple) 

def test_ordenar_menor_a_mayor_7():
    """
    Se testea el caso donde un parametro de entrada no es un numero entero
    Tambien se chequea que el tipo de dato que devuelve la funcion se correpsonda con la poscondicion
    """
    resultado = ordenar_menor_a_mayor("hola", 4, 2)
    assert resultado == "Alguno de los parametros ingresados no es un numero entero"
    assert isinstance(resultado, str) 
    
    
    
    
    
    
    
    
    
    