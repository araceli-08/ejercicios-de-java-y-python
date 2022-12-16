import os
#inicio de los datos
cuota = float (input ('Ingresa el valor de cuota: '))
dia_de_pago = float (input ('Ingresa el valor de dia de pago: '))
#"operacion"
descuento=0
recargo=0
if dia_de_pago<=10:
    descuento=cuota*0.02
if dia_de_pago<=10 and descuento<5:
    descuento=5
if dia_de_pago>20:
    recargo=cuota*0.03
if dia_de_pago>20 and recargo<10:
    recargo=10
importe_total_a_pagar=cuota-descuento+recargo
#salida de los datos
print ('Valor de descuento: ' + repr (descuento))
print ('Valor de importe total a pagar: ' + repr (importe_total_a_pagar))
print ('Valor de recargo: ' + repr (recargo))
print ()
os.system ('pause')