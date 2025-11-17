#Haz un programa que pida un texto y una palabra. Si la palabra está en el texto, muestra cuántas veces aparece.
texto=input("Introduce un texto: ")
palabra=input("Introduce una palabra a buscar en el texto: ")
contador=0
palabras=texto.split()
for p in palabras:
    if p==palabra:
        contador+=1
        print(f"La palabra '{palabra}' aparece {contador} veces en el texto.")