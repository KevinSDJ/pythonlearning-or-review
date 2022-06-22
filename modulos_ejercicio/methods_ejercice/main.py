# -*- coding: utf-8 -*-
import functools

#Ejercicio 1
print("Ingresa una lista de paises")

listcountries=set()
start=True

while start:
    country=input("Pais: ")
    listcountries.add(country)
    ask= input('Quieres ingresar mas: y o n ...')
    if ask.lower().startswith('n'):
        start=False
                              
    
listcountries= sorted(list(listcountries),reverse=False)
print('Lista de paises ingresados:´')
print(listcountries)
print('\n')

#Ejercicio 2
print('Ejercicio 2 \n')

def filterAndsum(lista):
    entrytype=type(lista) == type([])
    if entrytype:
        pass
    else:
        print('Debes pasar una lista como argumento')
        return
    checkcontent=all([type(element)==type(4) for element in lista])
    if checkcontent:
        pass
    else:
        print('La lista solo debe contener numeros')
    lista= filter(lambda x: x%2!=0,lista)
    sum= functools.reduce(lambda x,b: x+b ,lista)
    print(sum)

filterAndsum([2,3,43,1])

