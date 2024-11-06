'''
Crear un módulo con las funciones (dos números enteros):
- sumar
- restar
- multiplicar
- dividir

Crear un pograma Python que importe de manera EXPLÍCITA cada 
una de las funciones y haga uso de alguna de ellas.

Utilizar la estructura if __name__=='__main__'
'''

def sumar(operando_1 : int, operando_2 : int) -> int:
    '''
    Suma dos números
    '''
    resultado = operando_1 + operando_2
    return resultado

def restar(operando_1 : int, operando_2 : int) -> int:
    '''
    Resta dos números
    '''
    resultado = operando_1 - operando_2
    return resultado

def multiplicar(operando_1 : int, operando_2 : int) -> int:
    '''
    Multiplica dos números
    '''
    resultado = operando_1 * operando_2
    return resultado

def dividir(operando_1 : int, operando_2 : int) -> int:
    '''
    Divide dos números
    '''
    resultado = operando_1 / operando_2
    return resultado