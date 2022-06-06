
# Ejercicio 1

import math


edad=int(input('Ingresa tu edad: '))
if edad <18:
    print('Eres un crio')
else:
    print('Bienvenido señor')

#Ejercicio 2
inicial=int(input('Valor de inicio: '))
final= int(input('Valor de finalzacion: '))

for number in range(inicial,final):
    if number%2!=0:
        print(number)


#Ejercicio 3

for number in range(100,1,-1):
    print(number)


##Tema 5 
# Ejercicio 1

def triangleArea(altura,base):
   print("------------Triagulo area-------------")
   return (base*altura)/2
def circleRadio(radio):
    print("------------Circulo area-------------")
    return (radio*math.pi)**2

# Ejercicio 2
def prim_or_not_prim(numero):
    print('-------Numbero primo------')
    isPrim= (numero%2==0) and 'not' or'yes'
    return isPrim
print(prim_or_not_prim(3))

# Ejercicio 3
def bisiest_year(año):
    isbisiesto =año % 400 == 0 and True or año% 100 == 0 and False or año % 4 == 0;
    print(isbisiesto)
  				
bisiest_year(2024)

##Tema 6

#Ejercicio 1 , Clases
class Vehiculo():
    _Color=''
    _Ruedas=0
    _Puertas=0
    def setRuedas(self,ruedas):
        self._Ruedas=ruedas
    def getRuedas(self):
        return self._Ruedas
    def setColor(self,color):
        self._Color=color
    def getColor(self):
        return self._Color
    def setPuertas(self,puertas):
        self._Puertas=puertas

class Coche(Vehiculo):
    _Velocidad=0
    _Cilindradas=0
    def setCilindradas(self,cilindradas):
        self._Cilindradas=cilindradas
    def setVelocidad(self,velocidad):
        self._Velocidad=velocidad

micoche= Coche()
print(micoche)
