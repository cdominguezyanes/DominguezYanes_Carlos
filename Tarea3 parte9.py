#Pide una cantidad de productos y su precio uno por uno, luego muestra el total con IVA del 16%.
cantidad_productos = int(input("¿Cuántos productos deseas registrar? "))
total = 0

for i in range(cantidad_productos):
    precio = float(input(f"Introduce el precio del producto {i + 1}: $"))
    total += precio

# Calcular el IVA y el total con IVA
iva = total * 0.16
total_con_iva = total + iva

# Mostrar los resultados con formato de 2 decimales
print(f"\nSubtotal: ${total:.2f}")
print(f"IVA (16%): ${iva:.2f}")
print(f"Total con IVA: ${total_con_iva:.2f}")
