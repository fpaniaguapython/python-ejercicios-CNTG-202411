import time
'''
# Solución tradicional. Hasta que no están todos los elementos de la lista
# no comienza el proceso

def get_numeros():
    numeros = []
    for numero in range(3):
        time.sleep(2)
        numeros.append(numero)
    return numeros

print('Empezando...')
numeros = get_numeros()
for numero in numeros:
    print('Procesando:',numero)
    time.sleep(2)
'''

# Solución mediante generador
# Se procesa cada elemento según va generándose
def get_numeros_generador():
    for numero in range(3):
        time.sleep(2)
        yield numero

print('Empezando...')
for numero in get_numeros_generador():
    print('Procesando:',numero)
    time.sleep(2)

