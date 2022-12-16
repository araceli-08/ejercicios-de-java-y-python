import os
os.system("cls")
#inicio
print("")
#operacion
numero1=int(input("Inserte  el numero 1: "))
numero2=int(input("Inserteel numero 2: "))
numero1_c1=numero1//100
numero1_c2=numero1%100//10
numero1_c3=numero1%10

numero2_c1=numero2//100
numero2_c2=numero2%100//10
numero2_c3=numero2%10
#salida de los datos
print("---numeros intercambiados---")
print("numero 1",(numero2_c3*100)+(numero1_c2*10)+(numero2_c1))
print("numero 2",(numero1_c3*100)+(numero2_c2*10)+(numero1_c1))