# Haz un programa en python que pida un precio y muestre el total con IVA de 16%.
# solicita el precio al usuario
precio=float(input("Ingresa el precio del producto:"))
# calcula el IVA
iva=precio*0.16
# calcula el total con IVA
total=precio+iva
# muestra el total con IVA
print("El total con IVA es:",(total))