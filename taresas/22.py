#!/usr/bin/python3
 
lista = []
 
salir = False
 
while(not salir):
    numero = int(input("Dame un numero: "))
    if(numero == 0):
        salir=True
    else:
        lista.append(numero)
 
lista.sort() #ordena la lista
 
print(lista)
