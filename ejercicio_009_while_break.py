import random

numero_intentos = 0
numero_secreto = random.randint(1,10)
# print(numero_secreto)
while (True):
    numero = input('Introduce un número (1-10):')
    numero = int(numero)
    #numero_intentos = numero_intentos + 1
    numero_intentos+=1
    if (numero_secreto == numero):
        print(f'Eres un adivino. Has necesitado {numero_intentos} intentos')
        break
    else:
        print('Prueba de nuevo')
