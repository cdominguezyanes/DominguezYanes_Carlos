#Haz un programa que pida un numero entenero N, y calcula la suma de todos los numeros del 1 al N.
numero=int(input("Escribe un numero entero N: "))
suma=0
for i in range(1, numero+1):
    suma+=i
    print("La suma de los numeros del 1 al", numero, "es:", suma)