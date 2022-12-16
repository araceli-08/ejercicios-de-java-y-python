#inicio
monVendido=float(input("monto vendido"))
#calculamos la operacion
comisión = monVendido*0.09
sbruto = 300 + comisión
descuento = sbruto * 0.11
sneto = sbruto - descuento
#salida

print("comision ",comisión)
print("sueldo bruto",sbruto,)
print("descuento ",descuento)
print("sueldo neto ",sneto)