# Ejercicio:
# Crear una función que calcule el Índice de Masa Corporal
# y retorne el resultado
# Utilizar en la llamada keywords arguments y añadir
# comentarios de tipo 'docstring' para explicar la función

def calcular_IMC(peso : float, altura : float) -> float :
    '''
    Calcula el Índice de Masa Corporal (IMC)

    El IMC es...
    '''
    imc = peso / ((altura / 100)**2)
    return imc

def get_estado(imc : float) -> str:
    '''
    Devuelve una cadena de caracteres con el estado del paciente
    '''
    if (imc < 18.5):
        return "Inferior al normal"
    elif (imc < 24.9):
        return "Normal"
    elif (imc < 29.9):
        return "Superior al normal"
    else:
        return "Obesidad"

