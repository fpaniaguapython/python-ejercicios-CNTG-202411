def is_open(window):
    print(f'Evaluando si {window} está abierta') 
    return False

# Si una de las expresiones es True, no evalua la siguiente
if (is_open('Ventana1')) or (is_open('Ventana2')):
    print('Hay una ventana abierta')

# Evalua todas las expresiones
if (is_open('Ventana3')) | (is_open('Ventana4')):
    print('Hay una ventana abierta')

# Si una de las expresiones es False, no evalua la siguiente
if (is_open('Ventana5')) and (is_open('Ventana6')):
    print('Todas las ventanas están abiertas')

# Evalua todas las expresiones
if (is_open('Ventana7')) & (is_open('Ventana8')):
    print('Todas las ventanas están abiertas')