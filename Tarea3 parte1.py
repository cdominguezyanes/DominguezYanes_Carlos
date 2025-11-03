#Haz un programa que calcule cuantos numeros del 1 al 100 son divisibles entre 3 y entre 5.
contador = 0
for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        contador += 1

print(f"Entre 1 y 100 hay {contador} números que son divisibles entre 3 y 5.") 