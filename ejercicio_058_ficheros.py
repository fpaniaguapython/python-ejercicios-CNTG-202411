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
print(fichero.read()) # Todo el fichero, str
fichero.close()