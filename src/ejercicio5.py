################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.
"""

from ejercicio4 import es_int



def division_lenta(dividendo, divisor):
    """
    Esta funcion realiza la division de dos numeros mediante restas
    
    Precondicion: dos numeros reales donde el segundo debe ser mayor a 0
    Poscondicion: una tupla de dos enteros
    """
    dividendo = es_int(dividendo)
    divisor = es_int(divisor)
    
    if divisor == 0:
        resultado = "No se puede realizar la operacion ya que el divisor es 0"
    elif divisor > dividendo:
        cociente = 0
        resto = divisor
        resultado = cociente, resto
    else:
        cociente = 0
        resto = dividendo
        while resto - divisor >= 0:
            resto = resto - divisor
            cociente = cociente + 1
        resultado = cociente, resto
    
    print(f"Cociente: {cociente} Resto: {resto}")
        
    return resultado
        


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    dividendo = input("Ingrese un numero: ")
    divisor = input("Ingrese otro numero: ")
    print(division_lenta(dividendo, divisor))
    resul = division_lenta(dividendo, divisor)

if __name__ == "__main__":
    principal()

