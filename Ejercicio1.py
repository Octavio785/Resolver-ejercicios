#Definir variables y otros
print("Ejercicios 01")
montoP=0
#Datos de entrada
b=int(input("Sueldo por hora:"))
d=int(input("Horas trabajadas:"))
#Proceso
if d>=40:
 montoP=2*(d-40)+(b*d)
else:
  montoP=(b*d)
#Datos de salida
print("El monto a pagar es:", montoP)