print(3+4)#7 - int
print('3'+'4') #'34' - str
print(3,4) #3 4
print(3,4,sep='ratón')

nombre='Fernando'
numero_caracteres = len(nombre)
print(numero_caracteres)

#Fernando tiene 8 caracteres
print(nombre,'tiene',numero_caracteres,'caracteres')
print(nombre+' tiene '+str(numero_caracteres)+' caracteres ')

#f-string
print(f'{nombre} tiene {numero_caracteres} caracteres') 
