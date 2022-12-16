 # ENTERO a, b, c ;
#INICIO
primer_numero=float(input("Dame el primer número"))
segundo_numero=float(input("Dame el segundo número"))
tercer_numero=float(input("Dame el tercer número"))

if (primer_numero< segundo_numero) and (segundo_numero < tercer_numero):
     print("En orden asedente")
else: 
    if(primer_numero>segundo_numero) and tercer_numero>primer_numero and segundo_numero>primer_numero:
         print("En orden no creciente")
    else:
        print("se ingresaron desordenados")


     

