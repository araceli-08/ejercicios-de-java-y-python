#ejercicio3
#inici de lo sdatos a leer
kilometros= float (input("Escriba la cantidad en de kilometros 1tramo:" ))
pies= float (input("Escriba la cantidad en de pies 2tramo:" ))
millas= float (input("Escriba la millas en de pies 3tramo:" ))

#opercion 
metros=kilometros*1000.0
pies=pies/3.281
millas=millas*1609

total_de_metros=metros+pies+millas
#salida de los datos
print("total recorrida en metros",total_de_metros,"metros" ) 
yardas=total_de_metros*1094
print("total recorrida en yardas",yardas,"yardas" ) 