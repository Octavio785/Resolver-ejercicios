#Definir variables y otros
print("Ejercicio")
#Datos de entrada
a=int(input("Precio:"))
#Proceso
if a>=200:
 print("Se le descuenta el 15%")
elif a>100:
 print("Se le descuenta el 12%")
elif a<=100:
 print("Se le descuenta el 10%")