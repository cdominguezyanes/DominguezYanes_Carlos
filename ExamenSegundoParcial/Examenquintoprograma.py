#Haz un programa que pida al usuario solicitar 5 calificaciones, solo acepta numeros del 1 al 10 (Si se permite decimales). Almacena estas 5 calificaciones en un arreglo, y posteriormente calcula el promedio de las calificaciones, nuestra solamente 2 decimales. Si el alumno tiene una calificacion promedio mayor que 6, imprime un mensaje de "Aprobado", si tiene una calificacion menor que 6 imprime "Reprobado", y si tiene una calificacion de 10, imprime "Excelente".
calificaciones=[]
for i in range(5):
    while True:
        try:
            calificacion=float(input(f"Escribe la calificacion {i+1} (entre 1 y 10): "))
            if 1 <= calificacion <= 10:
                calificaciones.append(calificacion)
                break
            else:
                print("Calificacion invalida. Debe estar entre 1 y 10.")
        except ValueError:
            print("Entrada invalida. Por favor ingresa un numero.")
            promedio=sum(calificaciones)/len(calificaciones)
            print(f"El promedio de las calificaciones es: {promedio:.2f}")
            if promedio == 10:
                print("Excelente")
            elif promedio >= 6:
                print("Aprobado")
            else:
                print("Reprobado")