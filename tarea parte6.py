# Haz un programa en python que pida tres numeros y muestre si se cumple la expresion A<B<C(solo mostrando el resultado logico.)
# solicita los numeros al usuario
A=float(input("Ingresa el valor de A:"))
B=float(input("Ingresa el valor de B:"))
C=float(input("Ingresa el valor de C:"))
# verifica si se cumple la expresion A<B<C
resultado=A<B<C
# muestra el resultado logico
print("¿Se cumple la expresion A<B<C?", resultado)