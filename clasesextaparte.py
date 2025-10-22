#Haz un programa que pida dos numeros y muestre si el primero es mayor, menor o igual al segundo(Utiliza solo operadores de comparacion y logicos)
num1=float(input("Ingrese el primer numero:"))
num2=float(input("Ingrese el segundo numero:"))
esMayor=num1>num2
esMenor=num1<num2
esIgual=num1==num2
print(f"¿El primer numero es mayor que el segundo?{esMayor}")
print(f"¿El primer numero es menor que el segundo?{esMenor}")
print(f"¿El primer numero es igual al segundo?{esIgual}")

