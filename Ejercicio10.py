#Definir variables y otros
print("Ejercicio")
Sueldo1=0
#Datos de entrada
a=int(input("Años de trabajo:"))
b=int(input("Sueldo de trabajo:"))
#Proceso
#Por años de trabajo
if a<5:
 print("el bono es de 20%")
elif a>=5:
 print("el bono es de 30%")
#Por sueldo
if b<=1000:
 print("el bono es de 25%")
elif b<3500:
 print("el bono es de 15%")
elif b>=3500:
 print("el bono es de 10%")
