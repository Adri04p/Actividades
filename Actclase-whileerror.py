# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 09:22:42 2023

@author: SYSTEMarket

"""
while True:
    x=input("Ingrese un número a contar: ")
    if x=="q" or x=="quit":
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
        