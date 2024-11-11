
'''
Modos son (opcional, por defecto r):
- w (escritura -borra el anterior si lo hay-)
- a (escritura -añadiendo-)
- r (lectura)
Encoding (opcional):
- utf-8 
'''
fichero = open('salida.dat', mode='w', encoding='utf-8')
fichero.write('Este texto quiero quede escrito')
fichero.close()

with open('salida.ttr', mode='w', encoding='utf-8') as mi_fichero:
    mi_fichero.write('Esto también')