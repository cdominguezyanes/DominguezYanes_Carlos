#Pide una frase, divídela en palabras y guarda una lista solo las que tengan más de 5 letras. Muestra la lista resultante.
frase=input("Introduce una frase: ")
palabras=frase.split()
lista_mas_de_5_letras=[palabra for palabra in palabras if len(palabra)>5]
print("Palabras con mas de 5 letras:", lista_mas_de_5_letras)