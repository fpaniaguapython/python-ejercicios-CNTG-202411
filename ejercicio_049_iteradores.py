class Componente:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return self.nombre

class Ordenador:
    def __init__(self):
        self.__index = 0
        self.__componentes = []

    def add_component(self, componente : Componente):
        self.__componentes.append(componente)

    def __iter__(self): # RECORDAR
        return self

    def __next__(self): # RECORDAR
        if (self.__index == len(self.__componentes)):
            self.__index = 0
            raise StopIteration # RECORDAR
        componente = self.__componentes[self.__index]
        self.__index+=1
        return componente

mi_ordenador = Ordenador()
cpu = Componente('Intel i5')
ram = Componente('128 Gbytes')
hd = Componente('2 TB SSD')
mi_ordenador.add_component(cpu)
mi_ordenador.add_component(ram)
mi_ordenador.add_component(hd)

for componente in mi_ordenador:
    print(componente)

for componente in mi_ordenador:
    print(componente)    
