import os
os.system("cls")
#inicio :leer datos
cantidad_de_propruductos=float(input("cantidad de unidades adqueridas"))
precio_unitario=float(input("ingresar el precio del articulo"))
#operacion del problema
importe_compra=precio_unitario*cantidad_de_propruductos
primer_descuento=importe_compra*0.15
segundo_descuento=(importe_compra-primer_descuento)+0.15
importe_a_pagar= importe_compra-primer_descuento -segundo_descuento
#salida de los datos
print ('el importe de la compra: ',importe_compra,"S/")
print ('el importe del primer descuento : ',primer_descuento,"S/")
print ('el importe del primer segundo descuento : ',segundo_descuento,"S/")
print ('el importe a pagar  : ',importe_a_pagar,"S/")