class Factura:
    numeros_facturas = 32
    def __init__(self, id) -> None:
        self.id = id

f = Factura(1000)

#getattr (a nivel objeto)
print(getattr(f,'id')) # Es lo mismo que hacer f.id
#print(getattr(f,'importe')) # AttributeError

#setattr (a nivel objeto)
setattr(f,'id',1001) # Es lo mismo que hacer f.id=1001
setattr(f,'importe',200_000)
print(f.__dict__) # {'id': 1001, 'importe': 200000}

#getattr (a nivel de clase)
print(getattr(f,'numeros_facturas')) # 32
print(getattr(Factura,'numeros_facturas')) #32

#setattr (a nivel de clase)
setattr(Factura, 'localidad', 'Palencia') #Factura.localidad = 'Palencia'
print(Factura.localidad) # Palencia
