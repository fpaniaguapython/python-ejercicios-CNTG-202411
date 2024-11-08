姓名 = "Fernando"
print(f'Mi nombre es {姓名}')

# with open('datos.txt',mode='w') as fichero: # No escribe la tilde
with open('datos.txt', mode='w', encoding='utf-8') as fichero: #OK
    fichero.write('Línea 1')

