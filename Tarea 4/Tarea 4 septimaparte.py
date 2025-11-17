#Haz un programa en Python que pida repetidamente el nombre de una persona y su respuesta ("Si" o "No"). Guarda cada respuesta en un diccionario, donde la clave sea el nombre y el valor la respuesta. El programa debe terminar cuando el usuario escriba "Fin" como nombre. Al finalizar, muestra cuántas personas respondieron "Si", y cuántas respondieron "No"
respuesta={}
while True:
    nombre=input("Introduce el nombre de una persona (o 'Fin' para terminar): ")
    if nombre.lower()=="fin":
        break
    resp=input("Introduce la respuesta ('Si' o 'No'): ")
    respuesta[nombre]=resp
contador_si=0
contador_no=0
for resp in respuesta.values():
    if resp.lower()=="si":
        contador_si+=1
    elif resp.lower()=="no":
        contador_no+=1
print(f"Cantidad de personas que respondieron 'Si': {contador_si}")
print(f"Cantidad de personas que respondieron 'No': {contador_no}")