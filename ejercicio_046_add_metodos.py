class Factura:
    def __init__(self, importes):
        self.importes = importes

def obtener_total(self):
    return sum(self.importes)

f = Factura([1,2,3,4,5])

Factura.dame_total = obtener_total

print(f.dame_total())