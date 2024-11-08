'''
Crear una lista de palabras prohibidas
Pedir una palabra al usuario
Comprobar si la palabra está en las palabras prohibidas
'''
lista = ['brócoli', 'lechuga', 'puerro']

# Función que elimina las tildes
def eliminar_tilde(palabra : str) -> str:
    palabra = palabra.replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U')
    return palabra

# Comprensión de listas
lista_mayusculas = [eliminar_tilde(elemento.upper()) for elemento in lista]

ingrediente = input('Introduce un ingrediente:')

if (eliminar_tilde(ingrediente.upper()) in lista_mayusculas):
    print('Está')
else:
    print('No está')

