from ejercicio_020_importaciones import dividir as divi, multiplicar, restar, sumar

if __name__=='__main__':
    numero_1 = int(input('Número 1:'))
    numero_2 = int(input('Número 2:'))
    operacion = int(input('Operación (0-Sumar, 1-Restar):'))
    if operacion==0:
        resultado = sumar(numero_1, numero_2)
    elif operacion==1:
        resultado = restar(numero_1, numero_2)
    print(resultado)