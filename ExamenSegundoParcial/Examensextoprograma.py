#Pide al usuario ingresar 10 productos y alamacenalos en una lista. Luego muestra la lista ordenada alafabeticamente.
productos=[]
for i in range(10):
    producto=input(f"Escribe el nombre del producto {i+1}: ")
    productos.append(producto)
    productos.sort()
    print("La lista de productos ordenada alfabeticamente es:")
    for producto in productos:
        print(producto)