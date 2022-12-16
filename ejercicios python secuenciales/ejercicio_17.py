#ejercicio17 
import os
os.system("cls")
#inicio 
donacion=float(input(" monto de la donacion"))
centro_de_salud=donacion*0.25
comedor_infantil=donacion*0.35
escuela_infantil=donacion*0.25
asilo_ancianos=donacion*0.15

print("el centro de salud recibe S/.",format(centro_de_salud,"2f"))
print("el comedor infantil recibe S/.",format(comedor_infantil,"2f"))
print("la escuela infantil recibe S/.",format(escuela_infantil,"2f"))
print("el asilo de ancianos recibe S/.",format(asilo_ancianos,"2f"))