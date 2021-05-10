#Definir variables y otros
print("Ejercicio")
bono=0
#Datos de entrada
a=int(input("Años de trabajo:"))
#Proceso
if a==1:
 bono=100
elif a==2:
 bono=200
elif a==3:
 bono=300
elif a==4:
 bono=400
elif a==5:
 bono=500
elif a>5:
 bono=1000
#Datos de salida
print("El pago es de:", bono)