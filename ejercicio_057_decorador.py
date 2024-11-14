def saludador(funcion_decorada):
    def inner_function(*args, **kwargs):
        print("¡Hola!")
        return funcion_decorada(*args, **kwargs)
    return inner_function

@saludador
def sumar(s1, s2):
    return s1+s2

print(sumar(3,8))