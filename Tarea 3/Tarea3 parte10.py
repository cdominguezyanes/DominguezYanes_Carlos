#Haz un programa que simule una calculadora basica con opciones de suma, resta, multiplicacion y division, que se repita hasta que el usuario elija salir.
while True:
    print("Calculadora Básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    opcion = input("Elige una opción (1-5):")
    
    if opcion == '5':
        print("Gracias por usar la calculadora")
        break
    
    if opcion not in ['1', '2', '3', '4']:
        print("Opción no válida. Por favor, elige una opción del 1 al 5.")
        continue
    
    num1 = float(input("Introduce el primer número:"))
    num2 = float(input("Introduce el segundo número:"))
    
    if opcion == '1':
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif opcion == '2':
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    elif opcion == '3':
        resultado = num1 * num2
        print(f"{num1} × {num2} = {resultado}")
    elif opcion == '4':
        if num2 == 0:
            print("Error: No se puede dividir entre cero")
        else:
            resultado = num1 / num2
            print(f"{num1} ÷ {num2} = {resultado}") 
