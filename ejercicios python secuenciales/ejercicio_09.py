#inicio d los datos

n = int(input("Poner el un número de cuatro cifras propuestas : "))
#operacion
suma= 0
while n > 0:
    suma = suma + (n % 10)
    n = n // 10
    
print("La suma total de los dígitos",suma)