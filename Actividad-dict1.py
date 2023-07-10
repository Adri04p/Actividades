# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 19:09:20 2023

@author: SYSTEMarket
"""


dict={"azul":"blue","rojo":"red","verde":"green"}
print(dict["azul"])
print(dict["rojo"])
#agregué un elemento al diccionario
dict["amarillo"]="yellow"
print(dict)
#modificar un elemento al diccionario
dict["azul"]="BLUE"
print(dict)
#eliminar un elemento al diccionario con funcion del
del(dict["verde"])
print(dict)



#dentro de un diccionario se puede agregar listas , tuplas , diccionarios
dict1={"Alejandro":[22,1.73],"Jose":[21,1.75],"Maria":[22,1.75],"Maria":[22,1.67]}
print(dict1["Alejandro"])
