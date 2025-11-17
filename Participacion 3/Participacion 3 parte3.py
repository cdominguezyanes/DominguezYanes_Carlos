#Haz un programa que pida "Nombre" y "Calificación". Almacena todos estos datos en un diccionario. Posteriormente muestra: Promedio general, cantidad de aprobados y cantidad de reprobados.
diccionario_alumnos={}
for i in range(10):
    nombre=input("Introduce el nombre del alumno: ")
    calificacion=float(input(f"Introduce la calificacion de {nombre}: "))
    while(calificacion < 0 or calificacion > 10):
        calificacion= float(input(f"Calificacion invalida. Introduce la calificacion de {nombre} entre 0 y 10: "))
    diccionario_alumnos[nombre] = calificacion

print(diccionario_alumnos)

for clave, valor in diccionario_alumnos.items():
    print(f"La calificacion de {clave} es: {valor}")

suma_calificaciones=sum(diccionario_alumnos.values())
promedio=suma_calificaciones/len(diccionario_alumnos)
print(f"El promedio de las calificaciones es: {promedio}")
