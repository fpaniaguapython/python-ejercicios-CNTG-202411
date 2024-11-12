'''
(1) Crear un aula con 3 alumnos.
(2) Agregar un método mostrar_alumnos en el Aula que muestre los datos 
de los alumnos.
(Después...)
(3) Añadir un nuevo alumno al aula
(4) Mostrar los alumnos
'''
class Alumno:
    fondo_comun = 10 # Variable (atributo) de clase
    def __init__(self, nombre, email):
        self.nombre = nombre # Variable (atributo) de instancia
        self.email = email

    def mostrar(self):
        print(f'{self.nombre}-{self.email}-{Alumno.fondo_comun}')

class Aula:
    def __init__(self, identificador, capacidad, alumnos):
        self.identificador = identificador
        self.capacidad = capacidad
        self.__alumnos = alumnos # _Aula__alumnos

    def mostrar_alumnos(self):
        for alumno in self.__alumnos:
            alumno.mostrar()

    def __metodo_privado(self):
        pass

    def agregar_alumno(self, alumno):
        if (len(self.__alumnos)<self.capacidad):
            self.__alumnos.append(alumno)
        else:
            raise Exception('El aula ha alcanzado su máximo de capacidad')


alumno_1 = Alumno('Diego', 'diego@gmail.com')
alumno_2 = Alumno('Nahir', 'nahir@outlook.com')
alumno_3 = Alumno('Marta', 'marta@hotmail.com')

lista_alumnos = [alumno_1, alumno_2, alumno_3]

aula_1 = Aula('005', 20, lista_alumnos)
aula_1.mostrar_alumnos()

alumno_4 = Alumno('Óscar', 'oscar@telefonica.net')

aula_1.mostrar_alumnos()