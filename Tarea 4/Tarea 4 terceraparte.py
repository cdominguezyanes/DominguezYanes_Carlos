#Haz un programa que pida al usuario una contraseña. Verifica que: La contraseña tenga al menos 8 caracteres, y que contenga al menos una mayúscula y un número.
contraseña=input("Introduce una contraseña: ")
tiene_mayuscula=False
tiene_numero=False
if len(contraseña)>=8:
    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula=True
        if caracter.isdigit():
            tiene_numero=True
            if tiene_mayuscula and tiene_numero:
                break
            if tiene_mayuscula and tiene_numero:
                print("Contraseña valida.")
            else:
                print("La contraseña debe contener al menos una mayuscula y un numero. ")
        else:
            print("La contraseña debe tener al menos 8 caracteres. ")