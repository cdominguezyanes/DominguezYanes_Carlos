#Haz un programa en python que pida tres numeros y muestre si los tres son iguales (solo mostrando true o false).
# solicita los numeros al usuario
num1=float(input("Ingresa el primer numero:"))
num2=float(input("Ingresa el segundo numero:"))
num3=float(input("Ingresa el tercer numero:"))
# verifica si los tres numeros son iguales
resultado=(num1==num2==num3)
# muestra el resultado
print("¿Los tres numeros son iguales?", resultado)