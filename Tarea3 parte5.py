#Haz un programa que pida una edad, y dependiendo del rango, muestre una categoria: - Menor de 13 años -> "Niño" - 13 a 17 años -> "Adolescente" - 18 a 64 años -> "Adulto" - 65 o mas -> "Adulto mayor".
edad = int(input("Introduce tu edad: "))

if edad < 0:
    print("La edad no puede ser negativa")
elif edad < 13:
    print("Categoría: Niño")
elif edad < 18:
    print("Categoría: Adolescente")
elif edad < 65:
    print("Categoría: Adulto")
else:
    print("Categoría: Adulto mayor") 