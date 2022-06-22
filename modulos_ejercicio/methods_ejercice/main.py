# -*- coding: utf-8 -*-
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
print(listcountries)