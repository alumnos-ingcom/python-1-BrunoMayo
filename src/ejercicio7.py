################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir un programa que permita transformar un número solicitado
expresado en grados, minutos y segundos a segundos a segundos.
Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.

Recuerden que un grado son 60 minutos y un minuto son 60 segundos.
"""
try:
    from ejercicio1 import es_int
except ImportError as exc:
    from src.ejercicio1 import es_int


def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Convierte un numero de grados, minutos y segundos a segundos
    
    Precondicion: tres numeros enteros
    Poscondicion: un numero entero o un string
    """
    if es_int(horas) and es_int(minutos) and es_int(segundos):
        resultado = (horas * 3600) + (minutos * 60) + segundos
    else:
        resultado = "Alguno de los parametros ingresados no es un numero entero"
    return resultado 


def decimal_a_sexadecimal(numero):
    """
    Convierte un numero a grados, minutos y segundos
    
    Precondicion: un numero entero
    Poscondicion: una tupla o un string
    """
    
    if es_int(numero):
        grados = 0;
        minutos = 0;
        while numero - 3600 >= 0:
            grados = grados + 1
            numero = numero - 3600
        while numero - 60 >= 0:
            minutos = minutos + 1
            numero = numero - 60
        segundos = numero
        resultado = (grados, minutos, segundos)
    else: 
        resultado = "Alguno de los parametros ingresados no es un numero entero"
    return resultado

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    grados = int(input("Ingrese los grados: "))
    minutos = int(input("Ingrese los minutos: "))
    segundos = int(input("Ingrese los segundos: "))
    
    caso1 = sexadecimal_a_decimal(grados, minutos, segundos) 
    
    print(caso1)
    
    segundos_a_sexadecimal = int(input("Ingrese un numero: "))
    
    caso2 = decimal_a_sexadecimal(segundos_a_sexadecimal)
    print(caso2)

if __name__ == "__main__":
    principal()

