#Pide al usuario una lista de palabras (separadas por comas, por ejemplo Hola, Mario, Python, Programación). Elimina los elementos repetidos y los que sean menores a 3 letras. Muestra la nueva lista e imprímela en pantalla. 
entrada=input("Introduce una lista de palabras separadas por comas: ")
palabras=entrada.split(",") 
palabras_limpias=set()
for palabra in palabras:
    palabra=palabra.strip() 
    if len(palabra)>=3:
        palabras_limpias.add(palabra)
        nueva_lista=list(palabras_limpias)
        print("Lista sin elementos repetidos y con palabras de al menos 3 letras:", nueva_lista)