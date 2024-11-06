# Función con argumentos y retorno
def sumar(sumando_1 : int, sumando_2 : int) -> int : 
    '''
    (docstring)
    Suma dos números enteros y devuelve el resultado
    '''
    resultado = sumando_1 + sumando_2
    return resultado

rdo = sumar(sumando_1=10, sumando_2=3) # Keywords arguments
rdo = sumar(3, 8) # Positional arguments

# Función con argumentos y SIN retorno
def saludar(nombre):
    print(f'Hola {nombre}')

# Función SIN argumentos y SIN retorno
def escribe_hola():
    print('Hola')



