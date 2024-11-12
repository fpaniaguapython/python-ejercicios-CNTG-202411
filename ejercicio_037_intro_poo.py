class Alumno:
    def __init__(self, nombre, email, poblacion : str ='Santiago de Compostela') -> None:
        print('En el método __init__ de Alumno')
        self.nombre = nombre # Definición de atributo
        self.email = email
        self.poblacion = poblacion
        self.activo = True
    
    # Método
    def presentar(self):
        print(f'Soy {self.nombre} y mi dirección de correo es {self.email}')

# Instanciación, creación de objeto, creación de instancia
alba = Alumno('Alba', 'alba@gmail.com', 'Pontevedra')
# Acceso a atributo
print(alba.nombre)
# Invocación a un método
alba.presentar()


