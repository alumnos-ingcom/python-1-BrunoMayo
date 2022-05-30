################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""
from ejercicio1 import es_float
from ejercicio2 import signo


def compara(numero, otro_numero):
    """
    Esta funcion compara dos numeros ingresados y devuelve 1 si el primero
    es mayor que el segundo, -1 si el segundo es mayor que el primero o 0 si
    ambos numeros son iguales.
    
    Precondicion: dos numeros reales
    Poscondicion: un numero entero (1, -1 o 0)
    """
    numero = es_float(numero)
    otro_numero = es_float(otro_numero)
    
    resultado = numero - otro_numero
    if signo(resultado) == "positivo":
        resultado = 1
    elif signo(resultado) == "negativo":
        resultado = -1
    else:
        resultado = 0
    return resultado
    



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero1 = input("Ingrese un numero: ")
    numero2 = input("Ingrese otro numero: ")

    print(compara(numero1, numero2))

if __name__ == "__main__":
    principal()

