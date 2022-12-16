#inicio
capacidad_en_GB = float (input ('Insertar el valor de capacidad en GB: '))
#operacion de los datos 
capacidad_en_MB=capacidad_en_GB*1024
capacidad_en_KB=capacidad_en_MB*1024
capacidad_en_B=capacidad_en_KB*1024
#salida de los datos
print ('Valor de capacidad en B: ' + repr (capacidad_en_B))
print ('Valor de capacidad en KB: ' + repr (capacidad_en_KB))
print ('Valor de capacidad en MB: ' + repr (capacidad_en_MB))