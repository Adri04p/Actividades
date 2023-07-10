# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 07:38:35 2023

@author: SYSTEMarket
"""

numero=int(input("ingresa un numero: "))
numero1=int(input("ingresa otro numero: "))

if numero==numero1:
    print("numeros iguales")
else:
    print("numeros diferentes")
    if numero<numero1:
        print("el numero", numero , "es menor que " , numero1)
    if numero>numero1:
        print("el numero", numero, "es mayor que ", numero1)
