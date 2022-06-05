################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero utilizando sumas y restas.
"""    


try:
    from ejercicio1 import es_float
    from ejercicio1 import es_int
except ImportError as exc:
    from src.ejercicio1 import es_float
    from src.ejercicio1 import es_int



def signo(numero):
    """
    Esta funcion calcula si un numero es positivo, negativo o cero.

    Precondicion: un numero real
    Poscondicion: un numero o un string
    """
    resultado = ""

    if es_float(numero) or es_int(numero):
        valor_absoluto = abs(numero)
        if numero == 0:
            resultado = 0
        elif numero - valor_absoluto == 0:
            resultado = 1
        else:
            resultado = -1
    else:
        resultado = "El parametro ingresado no es un numero"

    
    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = float(input("Ingrese un numero: "))
    
    if signo(numero) == 0:
        print("El numero ingresado es Cero")
    elif signo(numero) == 1:
        print("El numero ingresado es Positivo")
    else:
        print("El numero ingresado es Negativo")
    

if __name__ == "__main__":
    principal()

