#Haz un programa que pida 5 nombres y luego pregunte uno; si está en la lista, muestra “Encontrado”.
nombres=[]
for _ in range(5):
    nombre=input("Introduce un nombre: ")
    nombres.append(nombre)
    buscar=input("Introducde un nombre para buscar: ")
    if buscar in nombres: 
        print("Encontrado")
    else:
        print("No encontrado")