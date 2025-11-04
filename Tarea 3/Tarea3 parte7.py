#Haz un programa que pida un numero, y calcule la suma de todos los numeros, desde el 1 hasta ese numero. Por ejemplo, si ingresas 5, deberas sumar 1+2+3+4+5.
numero = int(input("Introduce un número: "))

if numero < 0:
    print("Por favor, introduce un número positivo")
else:
    suma = sum(range(1, numero + 1))
    # Creamos la expresión para mostrar la suma (ej: "1+2+3+4+5")
    expresion = "+".join(str(i) for i in range(1, numero + 1))
    print(f"La suma de {expresion} = {suma}")
