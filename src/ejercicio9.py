################
# Nombre - @BrunoMayo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
"""
try:
    from ejercicio1 import es_int
    from ejercicio8 import es_primo
except ImportError as exc:
    from src.ejercicio1 import es_int
    from src.ejercicio8 import es_primo

def factores_primos(numero):
    """
    Esta funcion calcula los factores primos de un numero ingresado
    
    Precondicion: un numero entero
    Poscondicion: una tupla o un string
    """
    
    if es_int(numero):    
        if es_primo(numero):
            resultado = (numero)
        else:
            index = 1
            resultado = ()
            while index <= numero:
                if es_primo(index):
                    if numero % index == 0:
                        resultado = resultado + (index,)
                    else:
                        pass
                    index = index + 1
                else:
                    index = index + 1
    else: 
        resultado = "El parametro ingresado no es un numero entero"
    return resultado



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un numero: "))
    caso1 = factores_primos(numero)

    print(f"Los factores primos del numero ingresado son: {caso1}")

if __name__ == "__main__":
    principal()

