#Pide una palabra y reemplazaa todas las vocales por el simbolo *
palabra=input("Escribe una palabra: ")
palabra_modificada=palabra.replace("a","*").replace("e","*").replace("i","*").replace("o","*").replace("u","*").replace("A","*").replace("E","*").replace("I","*").replace("O","*").replace("U","*")
print("La palabra modificada es:", palabra_modificada)