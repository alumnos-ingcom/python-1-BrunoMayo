################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que haga la suma entre dos números enteros sin hacer la operación de manera directa.
Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""


try:
    from ejercicio2 import signo
    from ejercicio1 import es_int
except ImportError as exc:
    from src.ejercicio2 import signo
    from src.ejercicio1 import es_int


def suma_lenta(numero, otro_numero):
    """
    Esta funcion suma dos numeros pero lo hace de una unidad a la vez

    Precondicion: dos numeros enteros
    Poscondicion: un numero entero o un string
    """
    if (es_int(numero) and es_int(otro_numero)):
        absoluto = abs(otro_numero)
        while absoluto > 0:
            if signo(otro_numero) == 1:
                print(f"{numero} + 1")
                numero = numero + 1
                absoluto = absoluto - 1
            else:
                print(f"{numero} - 1")
                numero = numero - 1
                absoluto = absoluto - 1
    else:
        numero = "Alguno de los parametros ingresados no es un numero entero"
    
    return numero
        


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))

    print(suma_lenta(numero2, numero1))
    


if __name__ == "__main__":
    principal()

