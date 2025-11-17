# Haz un programa que pida el nombre de un contacto y su teléfono, y los agregue a un diccionario.
contactos={}
while True:
    nombre=input("Introduce el nombre del contacto: ")
    if nombre.lower():
        break
    telefono=input("Introduce el teléfono del contacto: ")
    contactos[nombre]=telefono
    print("Contactos guardados:", contactos)