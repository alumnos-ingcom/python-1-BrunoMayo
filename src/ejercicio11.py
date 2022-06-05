################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un número entero es multiplo de otro, utilizando sumas y restas.
"""

try:
    from ejercicio1 import es_int
except ImportError as exc:
    from src.ejercicio1 import es_int


def es_multiplo(numero, multiplo):
    """
    Esta funcion calclula si un numero es multiplo de otro a través de restas sucesivas
    
    Precondicion: un numero entero
    Poscondicion: un valor booleano o un string
    """
    
    
    
    if es_int(numero) and es_int(multiplo):
        if multiplo == 0:
            res = True
        elif numero == 0:
            res = False
        else:            
            while multiplo - numero >= 0:
                multiplo = multiplo - numero;            
            res = (multiplo == 0)                
    else:
        res = "El parametro ingresado no es un numero entero"
    return res


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese otro numero: "))
    caso1 = es_multiplo(numero1, numero2)
    
    print(caso1)
          

if __name__ == "__main__":
    principal()

