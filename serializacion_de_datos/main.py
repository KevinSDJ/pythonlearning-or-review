# -*- coding: utf-8 -*-
# pickle
import pickle

class Vehiculo :
    ruedas=''
    puertas=0
    color=''
    modelo=''
    def setDatabook(self,ruedas,puertas,color,modelo):
        self.ruedas=ruedas
        self.puertas=puertas
        self.color=color
        self.modelo=modelo


s=open('data.bin','wb')
pickle.dump(Vehiculo,s)
s.close()

data=open('data.bin','rb')
vehiculo=pickle.load(data)()
data.close()
print(vehiculo)