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


try:
    from ejercicio1 import es_float
    from ejercicio1 import es_int
    from ejercicio2 import signo
except ImportError as exc:
    from src.ejercicio1 import es_float
    from src.ejercicio1 import es_int
    from src.ejercicio2 import signo





def compara(numero, otro_numero):
    """
    Esta funcion compara dos numeros ingresados y devuelve 1 si el primero
    es mayor que el segundo, -1 si el segundo es mayor que el primero o 0 si
    ambos numeros son iguales.
    
    Precondicion: dos numeros reales
    Poscondicion: un numero entero (1, -1 o 0) o un string
    """
    if (es_float(numero) or es_int(numero)) and (es_float(otro_numero) or es_int(otro_numero)):
        temp = numero - otro_numero
        resultado = signo(temp)
    else:
        resultado = "Uno o ambos parametros ingresado no es un numero"
    return resultado
    



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))

    if compara(numero1, numero2) == 1:
        print("El primer numero es mayor que el segundo")
    elif compara(numero1, numero2) == -1:
        print("El primer numero es menor que el segundo")
    else:
        print("Ambos numeros son iguales")


if __name__ == "__main__":
    principal()

