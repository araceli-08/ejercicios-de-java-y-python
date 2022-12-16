
#Inicio

moto_Tvendido = float(input("COLOQUE EL MONTO TOTAL  VENDIDO: "))
categoria=float(input("escriba la categoria: "))
sbasico=250

if  (categoria==1):
 comision = 0.1425*moto_Tvendido
if (categoria== 2):
 comision = 0.1300 *moto_Tvendido
if (categoria == 3):
 comision = 0.1175 *moto_Tvendido
#Calcular el sueldo bruto del vendedor
sbruto = sbasico + comision
#Calcular el descuento del vendedor
if (sbruto > 3500):
 descuento = 0.15 * sbruto
else: 
 descuento = 0.08 * sbruto
# Calcular el sueldo neto del vendedor
sneto = sbruto-descuento
#solucion
print("sueldo basico",sbasico)
print("comision",comision)
print("sueldo bruto",sbruto)
print("descuento",descuento)
print("sueldo neto",sneto) 