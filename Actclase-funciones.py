# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 13:58:18 2023

@author: SYSTEMarket
"""
#funciones saludo
def saludo(nombre):
    print("hola",nombre)
saludo("Ana")
saludo("José")
saludo("Dillan")


#funciones 2 parámetros
def saludo2(nombre,apellido):
    print("Hola",nombre,apellido)
saludo2("MISHELL","PARRA")


#funciones ejemplo delivery
def delivery(ciudad,barrio,calle):
    print("La entrega será en ",ciudad,"en el barrio",barrio,"en la calle",calle)
ci=input("Ingrese ciudad ")
ba=input("Ingrese barrio ")
ca=input("Ingrese calles ")
delivery(ci,ba,ca)


#funcion resta primera forma
def resta(a,b):
    print(a-b)
resta(5,2) 

#funcion resta segunda forma
def resta1(a1,b1):
    print(a1-b1)
resta(a=10,b=15)

#funcion resta tercera forma
def resta1(a1,b1):
    print(a1-b1)
resta(10,b=6)

#funcion no type con return
def multiply(x,y):
    print(x*y)
    return x*y
resultado=multiply(3,6)


#funcion lista
def lista1(lista):
    for item in lista:
        print("hola",item)    
lista1(["Juan"])
lista1(["Juan","Ana"])
lista1(["Juan","Dorian","Dillan"])

#funcion lista * recibe datos 
#de una tupla
def lista1(*lista):
    for item in lista:
        print("hola",item)
        print(type(lista1))
    print("\n")
lista1(1,2,3,4)

    