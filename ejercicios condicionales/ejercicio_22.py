#Inicio

#Leer unidadesA, unidadesB
unidadA=float(input("UNIDAD A"))
unidadB=float(input("UNIDAD B "))
   # Determina los importes para el proveedor A
impcomA = unidadA*25.0
if( unidadA > 50 ):
       impdesA = 0.15*impcomA
else:
     impdesA = 0
     imppagA = impcomA - impdesA
 
   # Determina los importes para el proveedor B
impcomB = unidadB*27.5
if( unidadB > 35 ):
       impdesB = 0.10*impcomB
else:
    impdesB = 0
    imppagB = impcomB - impdesB
 #Determina los importes totales
impcomtot = impcomA + impcomB
impdestot = impdesA + impdesB
imppagtot = imppagA + imppagB
 # Salida de resultados
print("importe bruto",impcomtot) 
print("importe del descuento",impdestot)
print("importe total a pagar",imppagtot) 
#Fin