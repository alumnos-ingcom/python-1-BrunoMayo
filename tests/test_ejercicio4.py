################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se prueba la suma de dos numeros negarivos, dos positivos y un negativo con un positivo.
Tambien se chequea que se cumpla la poscondicion
"""

import pytest

from src.ejercicio4 import suma_lenta

def test_suma_lenta():
    resultado1 = suma_lenta(5, 3)
    resultado2 = suma_lenta(5, -3)
    resultado3 = suma_lenta(-5, -3)
    resultado4 = suma_lenta(2.3, 4)
    
    assert resultado1 == 8
    assert resultado2 == 2
    assert resultado3 == -8
    assert resultado4 =="Alguno de los parametros ingresados no es un numero entero"
    assert isinstance(resultado1, int)
