#Definir variables y otros
print("Ejercicio")
monto=0
#Datos de entrada
a=int(input("Cantidad de carros:"))
b=int(input("Horas de servicio:"))
#Proceso
if b<=2:
 monto=5*a
elif b<=5:
  monto=4*a
elif b<=10:
  monto=3*a
elif b>=10:
  monto=2*a
#Datos de salida
print("La tarifa es de:", monto)