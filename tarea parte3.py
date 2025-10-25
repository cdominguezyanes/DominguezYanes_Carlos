#Haz un programa en Python que calcule el perimetro de una circunferencia con base en su radio.
import math
# solicita el radio al usuario
radio=float(input("Ingresa el radio de la circunferencia:"))
# calcula el perimetro
perimetro=2*math.pi*radio
# muestra la circunferfencia 
print("El perimetro de la circunferencia es:",(perimetro))