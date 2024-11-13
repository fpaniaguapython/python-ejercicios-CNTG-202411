class Animal:
    def comer(self):
        pass

class Mamifero(Animal):
    def mamar(self):
        pass

class BichoVolador(Animal):
    def volar(self):
        pass

class Gaviota(BichoVolador):
    pass

class Murcielago(Mamifero, BichoVolador):
    pass

print(Animal.__bases__) # (<class 'object'>,)
print(Murcielago.__bases__) # (<class '__main__.Mamifero'>, <class '__main__.BichoVolador'>)   
print(Murcielago.__base__) # <class '__main__.Mamifero'>

# Crear una instancia de Gaviota y un Murcielago
# Crear una función amamantar(animal)
# Determinar si el animal puede o no puede mamar. Si no puede, lanza un error

def amamantar(animal):
    if not isinstance(animal, Mamifero):
        raise TypeError('El animal no es un mamífero')
    elif not hasattr(animal, 'mamar'):
        raise AttributeError('El animal no puede mamar')
    else:
        print('El animal puede mamar')
        animal.mamar()
        

gaviota = Gaviota()
batman = Murcielago()

try:
    # amamantar(gaviota)
    amamantar(batman)
except Exception as e:
    print(e)