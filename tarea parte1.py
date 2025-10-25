#Haz un programa en Python que pida tres calificaciones y calcule su promedio con dos decimales. (Investiga la funcion round() en Python.)
# solicita las calificaciones al usuario
calificacion1=float(input("Ingresa la primera calificacion:"))
calificacion2=float(input("Ingresa la segunda calificacion:"))
calificacion3=float(input("Ingresa la tercera calificacion:"))
# calcula el promedio
promedio=(calificacion1+calificacion2+calificacion3)/3
# muestra el promedio redondeado a dos decimales
print("El promedio es:", round(promedio,2))
#Recuerda usar la funcion round() para redondear el promedio a dos decimales.