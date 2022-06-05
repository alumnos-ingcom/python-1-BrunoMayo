################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un numero indicado es Primo.
"""
from unittest import result


try:
    from ejercicio1 import es_int
except ImportError as exc:
    from src.ejercicio1 import es_int


def es_primo(numero):
    """
    Esta funcion toma un numero y devuelve True si es primo y False si no lo es
    
    Precondicion: un numero entero
    Poscondicion: un valor booleano o un string
    """
    
    if es_int(numero):    
        if numero == 0 or numero == 1:
            return False
        else:
            indice = numero - 1
            resultado = True
            while indice > 1:
                if numero % indice == 0:
                    resultado = False
                    break
                else:
                    resultado = True
                    indice = indice - 1    
    else:
        resultado = "El parametro ingresado no es un numero entero"
    return resultado



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un numero: "))
    caso1 = es_primo(numero)
    print(caso1)

if __name__ == "__main__":
    principal()

