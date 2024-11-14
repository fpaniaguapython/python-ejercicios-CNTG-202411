class ConflictoError(ArithmeticError):
    def __init__(self, *args, usuario):
        ArithmeticError.__init__(self, *args)
        self.usuario = usuario
    def get_user_name(self):
        return 'Soy ' + self.usuario

def sumar(s1, s2):
    if (s1==s2):
        raise ConflictoError('Hay un conflicto','No sé qué hacer',usuario='Fernando')
    return s1+s2

try:
    sumar(3,3)
except ConflictoError as ce:
    print(ce) # <class '__main__.ConflictoError'>: Contiene la excepcion
    print(ce.args) # tuple: Contiene la tupla de argumentos posicionales suministrados al constructor
    print(ce.usuario)
    print(ce.get_user_name())






