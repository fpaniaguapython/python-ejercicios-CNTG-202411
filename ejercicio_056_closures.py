def convertir(nombre):
    def funcion_interna():
        return nombre.upper()
    return funcion_interna

nombre = 'python'
funcion = convertir(nombre)
nombre = 'java'
print(funcion()) # PYTHON

