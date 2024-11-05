lista = ['luns', 'martes', 'mercores', 'xoves', 'venres', 'sabado', 'domingo']
lista = []
lista = list()
tupla = (3,4,5)
lista = list(tupla)

lista[1] = 6 # Asignación - 3,6,5
lista.insert(1,10) # Inserción - 3, 10, 6, 5
lista.append(20) # Añadir - 3, 10, 6, 5, 20
print(lista) # [3, 10, 6, 5, 20]

#lista.sort() # Modifica la lista
#print(lista) # [3, 5, 6, 10, 20]
lista_ordenada = sorted(lista) # Genera una nueva lista ordenada
print(lista) # [3, 10, 6, 5, 20]
print(lista_ordenada) # [3, 5, 6, 10, 20]
lista_ordenada.sort(reverse=True)
print(lista_ordenada) # [20, 10, 6, 5, 3]

# Slicing
print(lista) # [3, 10, 6, 5, 20]
print(lista[0:2]) # [3, 10]
print(lista[1:2]) # [10]
print(lista[:3]) # [3, 10, 6]
print(lista[3:]) # [5, 20]
print(lista[:]) # [3, 10, 6, 5, 20]
print(lista[0:4:2]) # [3, 6]
print(lista[-1:]) # [20]
print(lista[-2:]) # [5, 20]
print(lista[-3:-1]) # [6, 5]

mi_slice = slice(0,2)
print(lista[mi_slice])# [3,10]

lista.reverse() #Invierte la lista

print(3 in lista) # True
print(3 not in lista) # False

