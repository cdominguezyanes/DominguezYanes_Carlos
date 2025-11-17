#Crea un diccionario con clave y valor producto : precio. Luego, pide una lista de productos comprados y muestra el total de la compra. Si el producto no existe, muestra una advertencia.
productos_precios={"manzana":0.5, "banana":0.3, "leche":1.2, "pan":1.0, "huevos":2.5}
entrada=input("Introduce una lista de productos comprados: ")
productos_comprados=entrada.split()
total_compra=0.0
for producto in productos_comprados:
    producto=producto.strip()
    if producto in productos_precios:
        total_compra+=productos_precios[producto]
    else:
        print(f"Advertencia: El producto '{producto}' no existe en el diccionario.")
        print(f"El total de la compra es: ${total_compra:.2f}")