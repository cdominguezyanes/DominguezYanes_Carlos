#Haz un programa en python que pida al usuario ingresa un numero, y muestre su tabla de multiplicar del 1 al 20, pero solo para los multiplos pares(Es decir, numero x 2, numero x 4, numero x 6, etc.)

numero=int(input("Ingrese un numero para ver su tabla de multiplicar(solo multiplos)"))
print(f"Tabla de multiplicar del{numero}(multiplica pares):")
for i in range(2, 21, 2):
    resultado=numero*i
    print(f"{numero}x{i}={resultado}")
    