# Función con argumento con valor por defecto
def sumar(sumando_1 : int, sumando_2 : int = 10) -> int:
    resultado = sumando_1 + sumando_2
    return resultado

print(sumar(3,2))
print(sumar(8))

# Relación indeterminada de parámetros 
def saludar(*args : str):
    print(args)

saludar()
saludar('uno')
saludar('uno','dos')
saludar('uno','dos','tres')