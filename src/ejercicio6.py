################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que a partir de tres variables de tipo entero
retorne una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
"""

try:
    from ejercicio1 import es_int
except ImportError as exc:
    from src.ejercicio1 import es_int



def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Esta funcion ordena tres numeros dentro de una tupla de mayor a menor
    
    Precondicion: tres numeros enteros
    Poscondicion: una tupla o un string
    """
    
    if es_int(uno) and es_int(dos) and es_int(tres):
        if uno >= dos and uno >= tres:
            if dos >= tres:
                resultado = (uno, dos, tres)
            else:
                resultado = (uno, tres, dos)
        elif dos >= tres and dos >= uno:
            if uno >= tres:
                resultado = (dos, uno, tres)
            else:
                resultado = (dos, tres, uno)
        else:
            if uno >= dos:
                resultado = (tres, uno, dos)
            else:
                resultado = (tres, dos, uno)
    else:
        resultado = "Alguno de los parametros ingresados no es un numero entero"
    return resultado
            
    
def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Esta funcion ordena tres numeros dentro de una tupla de menor a mayor
    
    Precondicion: tres numeros enteros
    Poscondicion: una tupla
    """

    if es_int(uno) and es_int(dos) and es_int(tres):        
        if uno >= dos and uno >= tres:
            if dos >= tres:
                resultado = (tres, dos, uno)
            else:
                resultado = (dos, tres, uno)
        elif dos >= tres and dos >= uno:
            if uno >= tres:
                resultado = (tres, uno, dos)
            else:
                resultado = (uno, tres, dos)
        else:
            if uno >= dos:
                resultado = (dos, uno, tres)
            else:
                resultado = (uno, dos, tres)
    else:
        resultado = "Alguno de los parametros ingresados no es un numero entero"
    return resultado


def principal():
    numero1 = int(input("Ingrese un numero entero: "))
    numero2 = int(input("Ingrese otro numero entero: "))
    numero3 = int(input("Ingrese otro numero entero: "))
    
    caso1 = ordenar_mayor_a_menor(numero1, numero2, numero3)
    caso2 =ordenar_menor_a_mayor(numero1, numero2, numero3)
    print(caso1)
    print(caso2)


if __name__ == "__main__":
    principal()

