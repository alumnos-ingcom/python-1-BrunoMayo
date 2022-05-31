################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero utilizando sumas y restas.
"""    
from ejercicio1 import es_float

try:
    from ejercicio1 import es_float
except ImportError as exc:
    from src.ejercicio1 import es_float

def signo(numero):
    """
    Esta funcion calcula si un numero es positivo, negativo o cero.
    Precondicion: un numero real
    Poscondicion: un string
    """
    numero = es_float(numero)
    
    valor_absoluto = abs(numero)
    if numero == 0:
        resultado = "cero"
    elif numero - valor_absoluto == 0:
        resultado = "positivo"
    else:
        resultado = "negativo"
    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = input("Ingrese un numero: ")
    print(f"El numero ingresado es: {signo(numero)}")

if __name__ == "__main__":
    principal()

