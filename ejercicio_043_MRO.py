class Animal:
    def comer(self):
        print('Soy un Animal y estoy comiendo')

class Mamifero(Animal):
    def comer(self):    
        print('Soy un Mamifero y estoy comiendo')

class BichoVolador(Animal):
    def comer(self):
        print('Soy un BichoVolador y estoy comiendo')
   
#class Murcielago(Animal, BichoVolador): # TypeError: Cannot create a consistent method resolution order (MRO) for bases Animal, BichoVolador
#    pass

class Murcielago(Mamifero, BichoVolador):
    pass

# ¿Cómo come un Murciélago que tiene método comer?
# Con su propio método

# ¿Cómo come un Murciélago que no tiene método comer?
# Si hay método comer en todas las superclases, elige la primera de 
# las que hereda directamente (empieza por la izquierda) en la que 
# encuentra el método.
#
# Si en las superclases directas no tiene el método, se va a las
# superclases de estas

# Si la clase derivada hereda de la superclase y de una de clases
# derivadas de esta, da un error MRO: class Murcielago(Animal, BichoVolador) 

batman = Murcielago()
batman.comer()