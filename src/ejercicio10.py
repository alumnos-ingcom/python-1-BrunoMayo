################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo.
Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.
"""


def remover_espacios(texto):
    """
    Esta funcion remueve los espacios en el texto
    
    Precondicion: Un string
    Poscondicion: Un string
    """
    i = 0
    nuevo_texto = ""
    while i < len(texto):
        if texto[i] != " ":
            nuevo_texto = nuevo_texto + texto[i]
            i = i + 1
        else:
            i = i + 1
    return nuevo_texto

def es_palindromo(texto):
    """
    Esta funcion toma un texto y analiza si es palindromo
    
    Precondiciones: un string
    Poscondicion: un valor booleano
    """
    texto = remover_espacios(texto)
    texto = texto.lower()
    longitud = len(texto) - 1
    indice = 0
    resultado = True
    while indice < int(longitud // 2):
        if texto[indice] != texto[longitud - indice]:
            resultado = False
            break;
        else:
            indice = indice + 1
    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    texto = input("Ingrese un texto: ")
    caso1 = es_palindromo(texto)
    print(caso1)

if __name__ == "__main__":
    principal()

