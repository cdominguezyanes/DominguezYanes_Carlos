#Haz un programa que pida un numero, y muestre si es primo o no.
def es_primo(n):
    # Los números menores o iguales a 1 no son primos
    if n <= 1:
        return False
    # Verificamos divisibilidad desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Introduce un número: "))

if es_primo(numero):
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo") 
