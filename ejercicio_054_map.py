capitales = [('A Coruña',245_000), ('Lugo',98_000), ('Ourense',105_000), ('Pontevedra', 85_000)]

def convertir_mayusculas(ciudad):
    return (ciudad[0].upper(), ciudad[1])

capitales_mayuscula = map(convertir_mayusculas, capitales)
print(list(capitales_mayuscula))