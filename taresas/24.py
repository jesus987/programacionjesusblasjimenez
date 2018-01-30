#!/usr/bin/python3
 
cadena = input("Dame una cadena: ")
 
print(cadena)
 
lista = []
 
for c in cadena:
    if(c not in lista):
        lista.append(c)
 
print(lista)
