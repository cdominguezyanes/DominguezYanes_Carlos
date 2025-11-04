#Haz un programa en python que pida una cantidad y la convierte de grados celsius a fahrenheit
celsius=float(input("Ingrese la cantidad de grados celsius:"))
fahrenheit=(celsius*9/5)+32
print(f"{celsius}grados celsius son {fahrenheit}grados fahrenheit")
cantidad=float(input("Ingrese la cantidad de grados fahrenheit:"))
celsius=(cantidad-32)*5/9
print(f"{cantidad}grados fahrenheit son {celsius}grados celsius")

