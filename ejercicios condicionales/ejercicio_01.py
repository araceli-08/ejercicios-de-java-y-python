# datos propuestos 

cantidad_de_unidades = int(input("ingrese la cantidad de unidades: "))

#operacio

if cantidad_de_unidades>=1: 
    cantidad_de_unidades <=25
    precio_unitario = 27 * cantidad_de_unidades
if cantidad_de_unidades>=26:
    cantidad_de_unidades <=50
    precio_unitario = 25 * cantidad_de_unidades
if cantidad_de_unidades>=51:
    precio_unitario = 23 * cantidad_de_unidades
    

if cantidad_de_unidades > 50:
    descuento = 0.15 * precio_unitario
if  cantidad_de_unidades <= 50:
    descuento = 0.05 * precio_unitario

totalpagar = precio_unitario - descuento  

#respuesta al problema

print("Importe de la Compra:",precio_unitario)
print("Importe de Descuento:",descuento)
print("Importe a Pagar:",totalpagar)
    

    