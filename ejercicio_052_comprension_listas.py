def triplicar(numero):
    return numero*3

numeros = [1, 2, 3, 4, 5]
dobles = [numero*2 for numero in numeros]
triples = [triplicar(numero) for numero in numeros]
doble_pares = [numero*2 for numero in numeros if numero%2==0]
dobles_impares = [numero*2 if numero%2==1 else 'ERROR' for numero in numeros ]

# Comprensión de listas utilizando paréntesis
generador = (numero*2 for numero in numeros)
print(generador) # <generator object <genexpr> at 0x000001B934D6A8E0>
lista_generada = list(generador)
print(lista_generada) # [2, 4, 6, 8, 10]