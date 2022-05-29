################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un número entero es multiplo de otro, utilizando sumas y restas.
"""

from ejercicio4 import es_int



def es_multiplo(numero, multiplo):
    """
    Esta funcion calclula si un numero es multiplo de otro a través de restas sucesivas
    
    Precondicion: un numero entero
    Poscondicion: un valor booleano
    """
    
    
    numero = es_int(numero)
    multiplo = es_int(multiplo)
    
    
    while multiplo - numero >= 0:
        multiplo = multiplo - numero;
    
    if multiplo == 0:
        res = True
    else:
        res = False
    
    return res


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero1 = input("Ingrese un numero: ")
    numero2 = input("Ingrese otro numero: ")
    
    print(es_multiplo(numero1, numero2))
          

if __name__ == "__main__":
    principal()

