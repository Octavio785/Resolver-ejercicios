#Definir variables y otros
print("Ejercicio")
Pasajes=0
#Datos de entrada
a=int(input("Cantidad de alumnos:"))
#Proceso
if a>100:
 Pasajes=20*a
elif a>=50:
 Pasajes=35*a
elif a>=20:
 Pasajes=40*a
elif a<20:
 Pasajes=70*a
#Datos de salida
print("El pasaje es de:", Pasajes)