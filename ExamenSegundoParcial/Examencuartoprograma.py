#Haz un programa que pida una palabra y cuenta cuantas vocales tiene la palabra ingresada.
palabra=input("Escribe una palabra: ")
vocales="aeiouAEIOU"
contador=0
for letra in palabra:
    if letra in vocales:
        contador+=1
        print("La palabra tiene", contador , "vocales.")