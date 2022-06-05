################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.
"""

try:
    from ejercicio1 import es_int
except ImportError as exc:
    from src.ejercicio1 import es_int





def division_lenta(dividendo, divisor):
    """
    Esta funcion realiza la division de dos numeros mediante restas
    
    Precondicion: dos numeros reales donde el segundo debe ser mayor a 0
    Poscondicion: una tupla de dos enteros o un string
    """
    if (es_int(divisor) and es_int(dividendo)):
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
    else: 
        resultado = "Alguno de los parametros ingresados no es un numero entero"
    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    dividendo = int(input("Ingrese un numero: "))
    divisor = int(input("Ingrese otro numero: "))
    print(division_lenta(dividendo, divisor))


if __name__ == "__main__":
    principal()

