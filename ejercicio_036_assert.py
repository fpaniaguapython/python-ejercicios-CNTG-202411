'''
Crear la función contratar que recibe los argumentos:
nombre (tipo str, longitud>0)
edad (tipo int, >=18)

Comprobar con assert que los tipos y los valores
de nombre y edad son correctos
'''
def contratar(nombre : str, edad : int):
    assert (isinstance(nombre, str)), 'El nombre debe ser un str'
    nombre = nombre.strip()
    assert (len(nombre)>0), 'Longitud incorrecta'
    assert (isinstance(edad, int)), 'La edad debe ser un int'
    assert (edad >= 18), 'La edad deber mayor o igual a 18'

contratar('Ricardo', 23)