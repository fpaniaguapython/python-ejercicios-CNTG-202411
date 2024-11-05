# Lista
# Sí duplicados
# Sí orden
lista = [3, True, 'Hola', [3, 4, 'Adios', True]]
print(lista)
print(lista[0]) # 3 -> Acceso a un elemento concreto
for item in lista:
    print("ITEM:", item)
    print("Hola")
    print("Python")


# Tupla
# Sí duplicados
# Sí orden
tupla = (3, True, 'Hola', [3, 4, 'Adios', True])
print(tupla)
print(tupla[2]) # 'Hola' -> Acceso a un elemento concreto
tupla = (3,) # Ojo, de un solo elemento
for elemento in tupla:
    print(elemento)

# Conjunto
# No duplicados
# No orden
conjunto = {3, 4, 8, 10, 10, 10}
print(conjunto) # {8, 10, 3, 4}
print(10 in conjunto) # True -> Preguntamos si un elemento está en el conjunto
for elemento in conjunto:
    print("Conjunto:",elemento)

# Diccionario
# No claves duplicadas
# ¿Orden?
diccionario = {'nombre':'Fernando', 'edad':50, 'edad':48}
print(diccionario) # {'nombre': 'Fernando', 'edad': 48}
print(diccionario['edad']) # 48
for clave in diccionario.keys():
    print(clave)
for valor in diccionario.values():
    print(valor)
for clave, valor in diccionario.items():
    print(clave, valor)    


