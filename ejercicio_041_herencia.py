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

seat = Automovil('Seat')
seat.arrancar()