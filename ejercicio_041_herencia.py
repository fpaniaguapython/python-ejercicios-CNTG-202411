'''
Crear la clase Vehiculo, con los métodos arrancar y parar
Crear las clases derivadas Automovil, Barco, Avion
Sobreescribir los métodos de arrancar y parar
Programar los métodos avanzar (todas las clases derivadas), 
    aparcar, atracar y aterrizar
Crear una instancia de cada clase derivada.
Arrancar y utilizar alguno de los métodos específicos
'''
class Vehiculo:
    def __init__(self, nombre) -> None:
        print('En el init de Vehiculo')
        self.nombre = nombre
    def arrancar(self):
        print('Soy un Vehiculo y estoy arrancando')
    def parar(self):
        print('Soy un Vehiculo y estoy parando')

class Automovil(Vehiculo):
    def arrancar(self):
        super().arrancar()
        # Vehiculo.arrancar(self) # Notación alternativa
        print('Soy un Automovil y estoy arrancando')
    def parar(self):
        print('Soy un Automovil y estoy parando')
    def avanzar(self):
        print('Soy un Automovil y estoy avanzando')

class Barco(Vehiculo):
    astillero = 'Lo que sea'
    def __init__(self, nombre, eslora):
        super().__init__(nombre)
        self.eslora = eslora
    def arrancar(self):
        print('Soy un Barco y estoy arrancando')
    def parar(self):
        print('Soy un Barco y estoy parando')
    def avanzar(self):
        print('Soy un Barco y estoy avanzando')        

seat = Automovil('Seat')
seat.arrancar()

yate = Barco('MiYate', 30)
yate.avanzar()
print(yate.nombre)
print(yate.eslora)

# Introspección
# isinstance --> Determina si un objeto es instancia de una clase
print(isinstance(yate, Barco)) # True
print(isinstance(yate, Vehiculo)) # True
print(isinstance(yate, object)) # True
print(isinstance(yate, Automovil)) # False

# issubclass --> Determina si una clase es clase derivada de otra clase
print(issubclass(Barco, Vehiculo)) # True
print(issubclass(Vehiculo, Barco)) # False
print(issubclass(Barco, object)) # True

# hasattr
print(hasattr(seat, 'eslora')) # False
print(hasattr(yate, 'eslora')) # True
print(hasattr(yate, 'astillero')) # True (consulta de un atributo de clase)
print(hasattr(yate, 'arrancar')) # True (arrancar es un método)

# Atributo __dict__
# print(Barco.__dict__) # Aplicado a una clase proporciona (diccionario) métodos y atributos de clase
print(yate.__dict__) # Aplicado a un objeto proporciona (diccionario) atributos de instancia

# Atributo __name__
# Aplica a clases
print(Barco.__name__) # Proporciona un str con el nombre de la clase
# print(yate.__name__) # Error

# Atributo __module__
# Aplica a clases y objetos
print(Barco.__module__) # '__main__' o el nombre del módulo si no es el principal
print(yate.__module__) # '__main__' o el nombre del módulo si no es el principal

# from ejercicio_040_pila import Pila
# print(Pila.__module__) # 'ejercicio_040_pila' ya que no está en el módulo principal

# Atributo __bases__
# Aplica a clases. Proporciona las superclases directas
print(Barco.__bases__) # (<class '__main__.Vehiculo'>,)