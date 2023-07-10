# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 19:30:34 2023

@author: Adriana Parra
"""
#Listas-colecciones



Lista=["Lunes","Martes","Miércoles","Jueves"]
print(Lista[-4])
#En la lista podemos imprimir en rango
print(Lista[0:3])
#Agregar en la lista otra lista

lista1=["Lunes","Martes","Miércoles","Jueves",40,40.5,[1,2,3]]

#Agregar un elemento más en las listas apped-FINAL
lista1.append("ADRIUX")
print(lista1)

#Agregar un elemento más en las listas insert-INICIO
lista1.insert(2,"MICHU")
print(lista1)

#Para ver si hay algun elemento en la lista utilizo in
print("Lunes" in lista1)
lista3=["manzana","pera","durazno","pera"]
#Para buscar el valor del indice index
print(lista3.index("pera"))

#Cuantos valores hay en una lista
print(lista3.count("pera"))

