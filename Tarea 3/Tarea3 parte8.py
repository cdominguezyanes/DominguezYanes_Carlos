#Pide dos numeros y muestra todos los numeros entre ellos que sean multiplos de 7.
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Asegurarnos que num1 sea el menor y num2 el mayor
if num1 > num2:
    num1, num2 = num2, num1

# Encontrar el primer múltiplo de 7 mayor o igual a num1
primer_multiplo = ((num1 + 6) // 7) * 7

print(f"Los múltiplos de 7 entre {num1} y {num2} son:")
for numero in range(primer_multiplo, num2 + 1, 7):
    print(numero) 
