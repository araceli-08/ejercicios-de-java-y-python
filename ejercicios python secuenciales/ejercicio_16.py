#Inicio
   #Declaración de variables

horasTrab=float(input("Inserte las horas de trabajo: "))
tarifaHor=float(input("Inserte la tarifa de horas: "))
   # Proceso de cálculo
sueldoBas = horasTrab*tarifaHor
montoBoni = 0.20*sueldoBas
sueldoBru = sueldoBas+montoBoni
montoDesc = 0.10*sueldoBru
sueldoNet = sueldoBru-montoDesc
   # Salida de resultados
print("sueldo basico ",sueldoBas)
print("sueldo bruto ",sueldoBru)
print("sueldo neto" ,sueldoNet)
