import os
os.system("cls")
#inicio
print("")
num_segundos=int(input("digite en numero expresados en segundos:"))
#operacion de los datos 
dias=((num_segundos//60)//60)//24
horas=((num_segundos//60)//60)%24
minutos=(num_segundos//60)%60
segundos=num_segundos%60
#salida de los datos
print("dias",dias)
print("horas",horas)
print("minutos",minutos)
print("segundos",segundos)
print("")