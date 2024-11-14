class Paleta:
    def __init__(self) -> None:
        self.__index = 0
        self.__colores = ['Rojo', 'Verde', 'Negro', 'Blanco', 'Azul']

    def __iter__(self):
        return self

    def __next__(self):
        if (self.__index==len(self.__colores)):
            self.__index=0
            raise StopIteration()
        else:
            color = self.__colores[self.__index]
            self.__index+=1
            return color

paleta = Paleta()

for color in paleta:
    print(color)

for color in paleta:
    print(color)