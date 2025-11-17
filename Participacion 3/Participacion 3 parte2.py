#Pide números hasta que el usuario escriba 0. Guarda los pares en una lista y los impares en otra. Al final, muestra cuantos números hay en cada lista. Ordena la lista en orden ascendente y recorre las listas para mostrar cada número uno por uno.
pares = []
impares = []
while True:
    numero = int(input("Introduce un número (escribe 0 para terminar): "))
    if numero == 0:
        break
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Ordenar las listas en orden ascendente
pares.sort()
impares.sort()

# Mostrar cantidades
print(f"\nCantidad de números pares: {len(pares)}")
print(f"Cantidad de números impares: {len(impares)}")

# Mostrar números pares
print("Números pares:")
for numero in pares:
    print(numero)

# Mostrar números impares
print("\nNúmeros impares:")
for numero in impares:
    print(numero)

