#Haz un programa que pida al usuario ingresar un nombre y una edad, verifica si la persona ingresada tiene la edad suficiente para votar(Tomando en cuenta que se puede votar a partir de los 18 años), si puede votar imprime un mensaje indicado que se puede votar, en caso de que no se pueda, imprime un mensaje indicado que no se puede votar y los años que le faltan para llegar poder votar.

nombre=input("Ingrese su nombre:")
edad=int(input("ingrese su edad:"))

if edad >=18:
    print(f"{nombre},usted tiene {edad}años y no puede votar.")
else:
    años_faltantes=18-edad
    print(f"{nombre},usted tiene {edad}años y no puede votar. Le falta{años_faltantes}años para poder votar.")
    