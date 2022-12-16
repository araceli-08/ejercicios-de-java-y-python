import os
os.system("cls")

#inicio de los datos
print("")
n = int(input("ingresar"))
n1 = int (input("ingrese el primer numero"))
n2 = int (input("ingrese el segundo numero"))
n3 = int (input("ingrese el tercer numero"))
#operacion 
if n1 < n2 < n3 :
    print("los numeros estan ordenados de forma creciente")
else:
    print("los numeros no estan ordenados de forma creciente")