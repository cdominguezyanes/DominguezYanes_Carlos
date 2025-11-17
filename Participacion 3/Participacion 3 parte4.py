#Haz un programa que pida un número, y crea una nueva lista sin duplicados. Pide 10 números.
numeros = []

for i in range(10):
    numero = int(input(f"Introduce el número: "))
    numeros.append(numero)

# Crear una lista sin duplicados
sin_duplicados = list(set(numeros))

# Ordenar la lista sin duplicados
sin_duplicados.sort()

# Mostrar resultados
print(f"\nLista original: {numeros}")
print(f"Lista sin duplicados: {sin_duplicados}")
print(f"\nNúmeros únicos ingresados: {(sin_duplicados)}")
print("\nNúmeros sin duplicados (ordenados):")
for numero in sin_duplicados:
    print(numero)
