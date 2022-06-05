
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
def prim_or_not_prim(number):
    print('-------Numbero primo------')
    isPrim= (number%2==0) and 'not' or'yes'
    return isPrim
print(prim_or_not_prim(3))