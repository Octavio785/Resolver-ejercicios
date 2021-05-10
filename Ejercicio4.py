#Definir variables y otros
print("Ejercicio")
Pago=0
#Datos de entrada
a=int(input("Horas de trabajo:"))
b=int(input("Pago por hora:"))
#Proceso
if a<=45:
 Pago=2*(a-40)+(a*b)
elif a<=50:
 Pago=3*(a-45)+2*(a-40-(a-45))+(a*b)
elif a>50:
 Pago=3*(a-45)+2*(a-40-(a-45))+(a*b)
elif a<=40:
 Pago=(a*b)
#Datos de salida
print("El pago es de:", Pago)