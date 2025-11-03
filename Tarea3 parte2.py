#Haz un programa que solicite numeros al usuario hasta que ingrese un cero. Al final, imprime cuantos numeros positivos y negativos introdujo.
positivos = 0
negativos = 0
while True:
    numero = int(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    elif numero > 0:
        positivos += 1
    else:
        negativos += 1

print(f"Has introducido {positivos} números positivos y {negativos} números negativos.")

