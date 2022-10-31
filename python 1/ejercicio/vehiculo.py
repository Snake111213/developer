import pickle

class vehiculo:
    marca = ''
    placa = ''

    def __init__(self, marca,placa):
        self.marca=marca
        self.placa=placa
    def getMarca(self):
        return self.marca
v=vehiculo('Honda', '454684841f')

datos=open('carros.bin','wb')
pickle.dump(v, datos)
datos.close()

datos=open('carros.bin', 'rb')
p=pickle.load(datos)
datos.close()

print(p.getMarca(), p.placa)