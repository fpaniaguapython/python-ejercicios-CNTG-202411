capitales = [('A Coruña',245_000), ('Lugo',98_000), ('Ourense',105_000), ('Pontevedra', 85_000)]

def es_grande(ciudad):
    return ciudad[1]>100_000

grandes_capitales = filter(es_grande, capitales)
print(list(grandes_capitales))

def contiene_a(ciudad):
    return 'a' in ciudad[0]

ciudades_con_a = filter(contiene_a, capitales)
print(list(ciudades_con_a))