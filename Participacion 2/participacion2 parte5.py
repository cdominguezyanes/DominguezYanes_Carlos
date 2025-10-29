#Haz un programa que sume todos los numeros pares del 1 al 100. Al final muestra el resultado de la suma.

# Inicializamos la variable para la suma
suma = 0

# Iteramos del 1 al 100
for numero in range(1, 101):
    # Verificamos si el número es par
    if numero % 2 == 0:
        suma += numero

# Mostramos el resultado
print(f"La suma de todos los números pares del 1 al 100 es: {suma}")
