#Definir variables y otros
print("Ejercicio")
Sueldo=0
#Datos de entrada
a=int(input("Años de trabajo:"))
b=int(input("Sueldo de trabajo:"))
#Proceso
if a>=4:
 Sueldo=((b*25)/100)+b
elif b<=2000:
 Sueldo=((b*25)/100)+b
elif a<=4:
 Sueldo=((b*20)/100)+b
elif b>=2000:
 Sueldo=((b*20)/100)+b
#Datos de salida
print("El sueldo de navidad es:", Sueldo)