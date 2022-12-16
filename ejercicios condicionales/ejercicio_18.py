#donación, salud, comedor, bolsa
#leer donación
donacion=float(input("Inserte  la cantidad de donacion"))
if(donacion>= 10000):
    centro_salud = 0.30  * donacion
    comedor = 0.50  * donacion
    bolsa = 0.20  * donacion
else:
    centro_salud = 0.25  * donacion
comedor = 0.60  * donacion
bolsa = 0.15  * donacion
# Salida de resultados
 
print("catidad de donacion del centro de salud es",centro_salud)

print("cantidad de donacion en el comedor es",comedor)

print("lo que sobra en bolsa",bolsa)
