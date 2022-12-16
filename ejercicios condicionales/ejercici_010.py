
#elimina las notas de mayor y menor puntaje
#inicio 
primner_nota =  int(input("INGRESE PRIMER NOTA: "))
segunda_nota =  int(input("INGRESE segunda NOTA: "))
tercer_nota =  int(input("INGRESE tercer NOTA: "))
cuarta_nota =  int(input("INGRESE cuarta NOTA: "))
#operacion
if primner_nota<segunda_nota:
   primner_nota<tercer_nota
   primner_nota<cuarta_nota
   elimine=primner_nota
else:
    if segunda_nota<primner_nota:
       segunda_nota<tercer_nota
       segunda_nota<cuarta_nota
       elimine=segunda_nota
    else:
        elimine=tercer_nota

total_de_promedio=(primner_nota+segunda_nota+tercer_nota+cuarta_nota-elimine)/3
#salida
print("su premedio fue",total_de_promedio)
print("y la nota eliminada ",elimine)


