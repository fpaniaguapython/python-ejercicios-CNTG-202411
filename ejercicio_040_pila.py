class Pila:
    def __init__(self) -> None:
        self.__items = list()

    def push(self, item) -> None:
        self.__items.append(item)

    def pop(self) -> any:
        return self.__items.pop()
    
    def __str__(self) -> str:
        cadena = ''
        for item in self.__items:
            cadena+=f'| {item} |\n'
        return cadena

    def __repr__(self) -> str:
        cadena = ''
        for item in self.__items:
            cadena+=f'{item},'
        return cadena

    '''
    def push_artesanal(self, item) -> None:
        self.__items.insert(0, item)

    def pop_artesanal(self) -> any:
        item = self.__items[0]
        del self.__items[0]
        return item
    '''

class PilaContadora(Pila):
    contador = 0
    
    def mostrar_contador(self):
        print(PilaContadora.contador)

    #Sobreescritura (override) de método
    def push(self, item) -> None:
        PilaContadora.contador+=1
        #super().push(item) # Opción 1
        Pila.push(self, item) # Opción 2

    def pop(self):
        PilaContadora.contador-=1
        return super().pop()

pila = PilaContadora()
pila2 = PilaContadora()

pila.push('1')
pila.push('2')
pila2.push('1')
pila2.push('2')
pila2.push('2')
pila2.pop()
pila.mostrar_contador()