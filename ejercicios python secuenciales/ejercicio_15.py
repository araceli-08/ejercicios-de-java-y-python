import os
os.system("cls")
#inicio de los datos 
print("")
dinero_juan=float(input("ingrese el dinero de juan: $"))
dinero_rosa=float(input("ingrese el dinero de rosa: $"))
dinero_daniel=float(input("ingrese el dinero de daniel: S/. "))
#operacion
dolares_daniel=dinero_daniel/3
capital_total=dinero_juan+dinero_rosa+dolares_daniel
porcentaje_juan=(dinero_juan*100)/capital_total
porcentaje_rosa=(dinero_rosa*100)/capital_total
porcentaje_danie=(dolares_daniel*100)/capital_total
#salida delos datos
print("el capital total: $",format(capital_total,".2f"))
print("juan aporto",format(porcentaje_juan,".2f"),"%")
print("rosa aporto",format(porcentaje_rosa,".2f"),"%")
print("daniel aporto",format(porcentaje_danie,".2f"),"%")
