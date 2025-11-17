#Funcion en Python

#Definicion
def saludar():
    print("Hola, buenvenido a la clase de Python")

#Llamada a la funcion 
saludar()
saludar()
saludar()

#Funcion con parametros
def saludar_persona(nombre, apellido, edad):
    print(f"Hola {nombre} {apellido}, tienes {edad} años.")


#Llamada a la funcion con argumentos
saludar_persona("Carlos", "Dominguez", 29)
saludar_persona("Ana", "Lopez", 39)
saludar_persona("Luis", "Matinez", 49)

#Funcion con valor de retorno
def sumar(a, b):
    return a + b

print(sumar (3, 5))
resultado= sumar (10, 20) 
print("El resultado de la suma es:", resultado) 