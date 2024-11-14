# Tipos básicos de apertura según el uso: 
# r-lectura, 
# w-escritura con borrado,
# a-escritura a continuación (append)
#
#Tipos básicos de apertura según el tipo de dato:
# t-texto
# b-binary
#
# Por defecto: mode='rt'
# Por defecto, siempre texto (t)
fichero = open('C:/Users/usuario/Documents/borrar.txt', mode='w', encoding='utf-8')
fichero.write('Hola')
fichero.close()

fichero = open('./poema.txt', mode='rt', encoding='utf-8')
#print(fichero.read()) # Todo el fichero, str
#print(fichero.read(10)) # Hay dulzur, str
#print(fichero.read(10)) # a infantil, str
#fichero.seek(0) # Pone el puntero en la posición 0
#print(fichero.read(10)) # Hay dulzur, str
#print(f'#{fichero.readline()}#') # Incluye los saltos de línea
#print(f'#{fichero.readline().replace('\n','')}#') # #En la mañana quieta.#
#print(fichero.readlines()) # Todo, list (incluye los saltos de línea)
#print(fichero.readlines(200)) # Devuelve líneas enteras hasta completar el número de bytes
fichero.close()
