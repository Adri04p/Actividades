# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 10:37:02 2023

@author: SYSTEMarket
"""

#Estructura de control While
#suma de los números múltiplos de 5 menores a 50
numero=0
suma=0
while numero<=50:
    suma=suma+numero
    numero += 5 # numero de paso
    print(numero)
print("la suma es: ", suma)

#solicitar numero limite al usuario
suma=0
i=0
numer=int(input("Ingrese un número límite: "))

while i<numer:
    suma=i+numero
    numero += 5 # numero de paso
    print(numero)
print("la suma es: ", suma)