lista1 = [1, 2, 3]
lista2 = lista1
# Modificar el 2º elemento de lista 1
# ¿Cómo quedan lista1 y lista2?
lista1[1]=10
print(lista1) # [1, 10, 3]
print(lista2) # [1, 10, 3]
print(lista1 is lista2) # True, son el mismo objeto

lista1 = [1, 2, 3]
lista2 = lista1[:]
lista1[1]=10
print(lista1) # [1, 10, 3]
print(lista2) # [1, 2, 3]
print(lista1 is lista2) # False

lista1 = [1, 2, [3, 4]]
lista2 = lista1[:]
lista1[0]=8
lista1[2][0]=10
print(lista1) # [8, 2, [10, 4]]
print(lista2) # [1, 2, [10, 4]]

import copy
lista1 = [1, 2, [3, 4]]
lista2 = copy.deepcopy(lista1) # SOLUCIÓN, DEEPCOPY
lista1[0]=8
lista1[2][0]=10
print(lista1) # [8, 2, [10, 4]]
print(lista2) # [1, 2, [3, 4]]
