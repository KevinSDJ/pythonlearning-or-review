
# Ejercicio 1
edad=int(input('Ingresa tu edad: '))
if edad <18:
    print("Eres un crio")
else:
    print("Bienvenido señor")



#Ejercicio 2

inicial=int(input('Valor de inicio: '))
final= int(input('Valor de finalzacion: '))


for number in range(inicial,final):
    if number%2!=0:
        print(number)