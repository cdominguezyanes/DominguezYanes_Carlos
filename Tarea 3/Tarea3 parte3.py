#Haz un programa que pida un numero y muestre si es divisible entre 2, 3 o ambos.
numero = int(input("Introduce un número: "))

divisible_2 = numero % 2 == 0
divisible_3 = numero % 3 == 0

if divisible_2 and divisible_3:
    print(f"{numero} es divisible entre 2 y 3")
elif divisible_2:
    print(f"{numero} es divisible entre 2")
elif divisible_3:
    print(f"{numero} es divisible entre 3")
else:
    print(f"{numero} no es divisible ni entre 2 ni entre 3")
