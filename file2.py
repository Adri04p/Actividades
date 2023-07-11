# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 19:20:57 2023

@author: SYSTEMarket
"""

archivo=open("devices.txt")
for elemento in archivo:
    elemento=elemento.strip("Cisco")
    print(elemento)
archivo.close()
