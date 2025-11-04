#Haz un programa que pida 5 numeros (Tecnicamente podriamos almacenarnos en un arreglo, pero no hemos llegando ahi, asi que no lo hagas asi, debes pedir los numeros y almacenarlos en variables diferentes)de los 5 numeros integrados, muestra cuantos fueron mayores que 10.

num1=float(input("Ingrese numero 1: "))
num2=float(input("Ingrese numero 2: "))
num3=float(input("Ingrese numero 3: "))
num4=float(input("Ingrese numero 4: "))
num5=float(input("Ingrese numero 5: "))

conteo_mayores_10 = 0

# Verificamos cada número si es mayor a 10
if num1 > 10:
    conteo_mayores_10 += 1
if num2 > 10:
    conteo_mayores_10 += 1
if num3 > 10:
    conteo_mayores_10 += 1
if num4 > 10:
    conteo_mayores_10 += 1
if num5 > 10:
    conteo_mayores_10 += 1

# Mostramos el resultado
print(f"\nCantidad de números mayores a 10: {conteo_mayores_10}")
