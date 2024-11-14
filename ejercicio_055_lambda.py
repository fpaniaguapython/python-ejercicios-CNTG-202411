capitales = [('A Coruña',245_000), ('Lugo',98_000), ('Ourense',105_000), ('Pontevedra', 85_000)]

grandes_capitales = filter(lambda ciudad : ciudad[1]>100_000, capitales)
print(list(grandes_capitales))

capitales_mayuscula = map(lambda ciudad : (ciudad[0].upper(), ciudad[1]), capitales)
print(list(capitales_mayuscula))