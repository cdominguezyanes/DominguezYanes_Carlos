#Haz un programa que pida una frase y cuenta cuantas letras tiene la frase, sin contar espacios.
frase=input ("Escribe una frase: ")
frase_sin_espacios=frase.replace("", "")
longitud=len(frase_sin_espacios)
print("La frase tiene", longitud, "letras sin contar espacios.")
