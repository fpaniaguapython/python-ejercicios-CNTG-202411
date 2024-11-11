try:
    # Este bloque de código puede
    # potencialmente lanzar una excepción
    # como consecuencia de una operación fallida
    pass
except:
    pass

try:
    # Este bloque de código puede
    # potencialmente lanzar una excepción
    # como consecuencia de una operación fallida
    pass
except BaseException:
    pass


try:
    # Este bloque de código puede
    # potencialmente lanzar una excepción
    # como consecuencia de una operación fallida
    pass
except BaseException as be:
    pass


try:
    # Este bloque de código puede
    # potencialmente lanzar una excepción
    # como consecuencia de una operación fallida
    pass
except ZeroDivisionError as zde:
    pass
except ArithmeticError as ae:
    pass
except Exception as e:
    pass
except BaseException as be:
    pass


try:
    # Este bloque de código puede
    # potencialmente lanzar una excepción
    # como consecuencia de una operación fallida
    pass
except (ValueError, TypeError) as ae:
    pass


try:
    # Este bloque de código puede
    # potencialmente lanzar una excepción
    # como consecuencia de una operación fallida
    pass
except (ValueError, TypeError) as ae:
    pass
finally: #Siempre se ejecuta
    pass

try:
    # Este bloque de código puede
    # potencialmente lanzar una excepción
    # como consecuencia de una operación fallida
    pass
except (ValueError, TypeError) as ae:
    pass
else: # Se ejecuta si no hay excepción
    pass