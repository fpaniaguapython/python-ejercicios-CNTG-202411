import ejercicio_016_calculadora_imc as calculadora

if __name__=='__main__':
    peso = float(input('Peso:'))
    altura = float(input('Altura:'))
    imc = calculadora.calcular_IMC(peso, altura)
    print(f'El IMC es {imc}')
    estado = calculadora.get_estado(imc)
    print(f'El estado del paciente es {estado}')