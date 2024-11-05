numeros = (1,2,3,4,-8)

for numero in numeros:
    print(numero*2,end='-') 


#Hacer una lista con 5 nombres propios
nombres = ['Alberto', 'Pedro', 'Anna', 'Raquel', 'Rosa', 'Francisco']

for nombre in nombres:
    if nombre.upper().find('A')>-1:
        print(nombre)

