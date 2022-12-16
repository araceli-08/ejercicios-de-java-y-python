import os
os.system("cls")

#20.	Desarrolle el programa que lea tres números a, b, c y determine si los números fueron ingresados en orden ascendente, descendente o en desorden.'''
print("")
n = int(input("ingresar"))

a = int (input("ingrese el primer numero a"))
b = int (input("ingrese el primer numero b"))
c = int (input("ingrese el primer numero c"))
#operacion 
if a < b < c :
     print("los numeros a-b-c estan ordenado de forma ascendente")
elif a > b > c :
     print("los numeros a-b-c estan ordenado de forma desendente")
else:
     print("los numeros estan desordenados")
     

