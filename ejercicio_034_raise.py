def sumar(s1 : int, s2 : int):
    if (not isinstance(s1, int)):
        raise TypeError('El sumando debe ser de tipo int')
    resultado = s1 + s2
    return resultado

try:
    print(sumar(1,2))
    print(sumar('Uno','Dos'))
    print(sumar(True, True))
except TypeError as te:
    print(te)