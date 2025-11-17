# Pide nombres hasta que el usuario escriba la palabra "Fin". Al final muestra cuantos nombres ingresó, y cuál es el primero y el último.
nombre_ususario = []

while True:
    nombre = input("Introduce un nombre (escribe 'Fin' para terminar): ")
    if nombre == "fin": 
        break
    nombre_ususario.append(nombre)

# Mostrar los resultados
if nombre_ususario:
    print(f"Total de nombres ingresados: {(nombre_ususario)}")
    print(f"Primer nombre: {nombre_ususario}")
    print(f"Último nombre: {nombre_ususario}")
else:
    print("No se ingresaron nombres") 