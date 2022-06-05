
# Ejercicio 1
import math

# coding=utf-8

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


#Leccion 6 , Ejercicio 1

def triangleArea(altura,base):
   print("------------Triangle area-------------")
   return (base*altura)/2
def circleRadio(radio):
    print("------------Circle area-------------")
    return (radio*math.pi)**2

circleRadio(20)