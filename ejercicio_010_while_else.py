import random

numero_intentos = 0
numero_secreto = random.randint(1,10)
# print(numero_secreto)
numero = -1
while (numero!=numero_secreto):
    numero = input('Introduce un número (1-10):')
    numero = int(numero)
    #numero_intentos = numero_intentos + 1
    numero_intentos+=1
    if (numero_secreto == numero):
        print(f'Eres un adivino. Has necesitado {numero_intentos} intentos')
    else:
        print('Prueba de nuevo')
else:
    print("Se muestra cuando la condición del while se deja de cumplir")       
