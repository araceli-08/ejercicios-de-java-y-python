#Inicio del programa:

cantida_docena=float(input("Inserte la cantidad de docena"))

precio_producto=float(input("Inserte el precio del producto"))
# Calcula el monto de la compra
montocompra = cantida_docena* precio_producto
#Calcula el monto del descuento
if(cantida_docena >= 6):
      montodes = 0.15 * montocompra
else:
    montodes = 0.10 * montocompra
# Calcula el monto a pagar
montopag = montocompra - montodes
# Calcula el número de lapiceros de obsequio
if(cantida_docena >= 30):
      obsequio_lapiseros = 2*(cantida_docena/3)
else:
      obsequio_lapiseros = 0
# Salida de resultados
 
print("El número de lapiceros a regalar es",obsequio_lapiseros)

print("El monto total de la compra es",montocompra)

print("El monto de descuento es",montodes)


print("El monto a pagar es",montopag)







