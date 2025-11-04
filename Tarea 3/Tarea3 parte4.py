#Haz un programa que sume todos los numeros impares del 1 al 50.
suma = 0
for numero in range(1, 51, 2):  # Empezamos en 1 y vamos de 2 en 2 hasta 50
    suma += numero

print(f"La suma de todos los números impares del 1 al 50 es: {suma}")
