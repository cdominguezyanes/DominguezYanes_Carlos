#Haz un programa en python que pida el radio y la altura de un cilindro y muestre su volumen.
import math
# solicita el radio y la altura al usuario
radio=float(input("Ingresa el radio del cilindro:"))
altura=float(input("Ingresa la altura del cilindro:"))
# calcula el volumen
volumen=math.pi*radio**2*altura
# muestra el volumen del cilindro
print("El volumen del cilindro es:", volumen)