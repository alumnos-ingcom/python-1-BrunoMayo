################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir un programa que permita transformar un número solicitado
expresado en grados, minutos y segundos a segundos a segundos.
Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.

Recuerden que un grado son 60 minutos y un minuto son 60 segundos.
"""

from ejercicio4 import es_int

def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Convierte un numero de grados, minutos y segundos a segundos
    
    Precondicion: tres numeros enteros
    Poscondicion: un numero entero
    """
    horas = es_int(horas)
    minutos = es_int(minutos)
    segundos = es_int(segundos)
    
    return (horas * 3600) + (minutos * 60) + segundos


def decimal_a_sexadecimal(numero):
    """
    Convierte un numero a grados, minutos y segundos
    
    Precondicion: un numero entero
    Poscondicion: una tupla
    """
    numero = es_int(numero)

    grados = 0;
    minutos = 0;
    while numero - 3600 >= 0:
        grados = grados + 1
        numero = numero - 3600
    while numero - 60 >= 0:
        minutos = minutos + 1
        numero = numero - 60
    segundos = numero
    return (grados, minutos, segundos)

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    grados = input("Ingrese los grados: ")
    minutos = input("Ingrese los minutos: ")
    segundos = input("Ingrese los segundos: ")
    
    print(sexadecimal_a_decimal(grados, minutos, segundos))
    
    segundos_a_sexadecimal = input("Ingrese un numero: ")
    
    print(decimal_a_sexadecimal(segundos_a_sexadecimal))

if __name__ == "__main__":
    principal()

