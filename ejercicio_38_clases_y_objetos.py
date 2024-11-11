from gtts import gTTS
import os

class Factura:
    def __init__(self, numero, empresa, cliente) -> None:
        self.numero = numero
        self.empresa = empresa
        self.cliente = cliente

    def guardar(self):
        with open(f'{self.numero}.txt', mode='w', encoding='utf-8') as fichero:
            fichero.write(self.numero)
            fichero.write('\n')
            fichero.write(self.empresa)
            fichero.write('\n')
            fichero.write(self.cliente)
            fichero.write('\n')
            
    def hacer_locucion(self, idioma):
        self.idioma = idioma # Crea un atributo en tiempo de ejecución
        cadena_locucion = f'Factura {self.numero} del cliente {self.cliente}'
        tts = gTTS(cadena_locucion, lang=self.idioma)
        tts.save('factura.mp3')
        os.system('start factura.mp3')


factura_1 = Factura('001','Empresa 1','Cliente 1')
factura_2 = Factura('002','Empresa 2','Cliente 3')
factura_1.pagado = True # Crea un atributo en tiempo de ejecución
factura_1.guardar()
factura_2.guardar()
factura_2.hacer_locucion('es')