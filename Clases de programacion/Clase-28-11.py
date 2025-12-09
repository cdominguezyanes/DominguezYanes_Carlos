#Funcion para agregar un estudiante 
def agregar_estudiante(lista_estudiantes):
    nombre=input("Ingrese el nombre del estudiante: ")
    apellido=input("Ingrese el apellido del estudiante: ")
    promedio=float(input("Ingrese el promedio del estudiante: "))
    lista_estudiantes.append({"nombre": nombre, "apellido": apellido, "promedio": promedio})
    print(f"Estudiante {nombre} {apellido} agregado exitosamente.")