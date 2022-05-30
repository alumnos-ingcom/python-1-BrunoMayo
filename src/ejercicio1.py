################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.
Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un número decimal, 
utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. Y viceversa.
"""

def es_float(numero):
    
    return float(numero)



def convertir_a_fahrrenheit(centigrados):
    """
    Esta función toma una temperatura expresada en grados centigrados 
    y la devuelve expresada en grados farenheit
    
    Precondicion: numero real
    Poscondicion: numero de tipo float
    """
    
    centigrados = es_float(centigrados)
    return (centigrados * 9/5) + 32



def convertir_a_centigrados(fahrenheit):
    """
    Esta función toma una temperatura expresada en grados farenheit
    y la devuelve expresada en grados centigrados
    
    Precondicion: numero real
    Poscondicion: numero de tipo float
    """
    fahrenheit = es_float(fahrenheit)
    return (fahrenheit - 32) * 5/9


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    temperatura_cel = input("Ingrese una temperatura en celcius: ")
    print(f"La temperatura ingresada equivale a {convertir_a_fahrrenheit(temperatura_cel)} grados fahrenheit")
    temperatura_far = input("Ingrese una temperatura en fahrenheit: ")
    print(f"La temperatura ingresada equivale a {convertir_a_centigrados(temperatura_far)} grados centigrados")
    

if __name__ == "__main__":
    principal()

