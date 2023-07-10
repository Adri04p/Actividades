# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 07:50:08 2023

@author: SYSTEMarket
"""

acl=int(input("Ingrese el # de ACL "))
if acl>=2 and acl<=99:
    print("la acl es estandar")
elif acl>=100 and acl<=199:
    print("la acl es extendida")
else:
    print("el # ingresado no es de acl")