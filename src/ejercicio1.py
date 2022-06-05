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
    """
    Esta funcion chequea que el numero ingresado sea de tipo float y devuelve True si lo es o False si no lo es
    
    Precondicion: cualquier parametro
    Poscondicion: un valor booleano
    """
    return type(numero) == float
            
def es_int(numero):
    """
    Esta funcion chequea que el numero ingresado sea de tipo int y devuelve True si lo es o False si no lo es
    
    Precondicion: cualquier parametro
    Poscondicion: un valor booleano
    """
    return type(numero) == int
        


def convertir_a_fahrrenheit(centigrados):
    """
    Esta función toma una temperatura expresada en grados centigrados 
    y la devuelve expresada en grados farenheit
    
    Precondicion: numero decimal
    Poscondicion: numero de tipo float o un string
    """
    
    if es_float(centigrados) or es_int(centigrados):
        resultado = (centigrados * 9/5) + 32
    else:
        resultado = "El parametro ingresado no es un numero natural"
    
    return resultado
    



def convertir_a_centigrados(fahrenheit):
    """
    Esta función toma una temperatura expresada en grados farenheit
    y la devuelve expresada en grados centigrados
    
    Precondicion: numero decimal
    Poscondicion: numero de tipo float o un string
    """
    if es_float(fahrenheit) or es_int(fahrenheit):
        resultado = (fahrenheit - 32) * 5/9
    else:
        resultado = "El parametro ingresado no es un numero natural"
    
    return resultado
    

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero1 = float(input("Ingrese una temperatura en centigrados: "))
    print(f"La temperatura ingresada equivale a {convertir_a_fahrrenheit(numero1)} grados fahrenheit")
    numero2 = float(input("Ingrese una temperatura en fahrenheit: "))
    print(f"La temperatura ingresada equivale a {convertir_a_centigrados(numero2)} grados centigrados")
    
    

if __name__ == "__main__":
    principal()

