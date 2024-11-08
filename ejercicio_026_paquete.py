# from calculadora import programa # Opción 1
from calculadora.programa import restar, maximo, _minimo, __privado # Opción 2
from ejercicio_027_paquete import saludar
# programa.restar() # Opción 1
restar() # Opción 2
saludar()
# Opción 1
# print(programa.maximo)
# print(programa._minimo) # Mal
# print(programa.__privado) # Mal
# Opción 2
print(maximo)
print(_minimo) # Mal
print(__privado) # Mal