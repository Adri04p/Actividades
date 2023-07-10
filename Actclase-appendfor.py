# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 22:48:39 2023

@author: SYSTEMarket
"""
router=[]
switches=[]
puntos=[]
letrasr=[]
dispositivos=[]

lista=["R1","R2","R3","S1","S2","S3","AP1","FW1","Pc","Consolas","impresoras"]

for i in lista:
    if "R" in i:
        router.append(i)
    elif "S" in i:
        switches.append(i)
    elif "A" in i:
        puntos.append(i)
    elif "A" in i:
        puntos.append(i)
else:
    dispositivos.append(i) 
print(router,switches,puntos,letrasr,dispositivos)