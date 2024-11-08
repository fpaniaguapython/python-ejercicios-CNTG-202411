try:
    numero = int(input('Numero:'))
except ValueError as ve:
    print('Ha ocurrido un error:',ve)

# Pedir al usuario dos números y dividirlos
# Capturar la excepción ZeroDivisionError que se producirá
# si el divisior es 0

try:
    dividendo = int(input('Dividendo:'))
    divisor = int(input('Divisor:'))
    resultado = dividendo / divisor
    print("Resultado:", resultado)
except ZeroDivisionError as zde:
    print("Error:", zde)
except ValueError as ve:
    print("Error:", ve)
except BaseException as ae:
    print("Error:", ae)
else:
    print("Si no hay excepción, se ejecuta")
finally:
    print("Siempre se ejecuta")


try:
    pass
except:
    print("Se capturan todos los errores sin identificar")





