'''
Crear una lista
Pedir al usuario cuatro nombres y agregarlos a la lista
Mostrar la lista
Ordenar la lista
Mostrar la lista
Pedir al usuario un nombre y mostrar si está o no está en la lista
Si el nombre no existe, agregarlo en la primera posición
'''
nombres = list()

for index in range(4):
    nombre = input("Introduce el nombre:")
    nombre = nombre.capitalize()
    nombres.append(nombre)
print(nombres)

nombres.sort()
print(nombres)

nombre_a_buscar = input("Introduce el nombre a buscar:")
nombre_a_buscar = nombre_a_buscar.capitalize()
if (nombre_a_buscar in nombres):
    print(f'{nombre_a_buscar} está en la lista')
else:
    print(f'{nombre_a_buscar} NO está en la lista')
    nombres.insert(0,nombre_a_buscar)
print(nombres)    
