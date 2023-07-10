# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 11:14:33 2023

@author: SYSTEMarket
"""

contador=0
suma=0

num_max=int(input("Ingrese numero limite para sumarlos: "))

while contador<num_max:
    suma += contador
    contador +=5
print("la suma es: ", suma)