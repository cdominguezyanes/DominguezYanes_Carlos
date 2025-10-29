#Haz un programa en Python que convierta una cantidad de minutos a horas.
# solicita los minutos al usuario
minutos=int(input("Ingresa la cantidad de minutos:"))
# calcula las horas
horas=minutos/60
# solicita la cantidad restante de minutos
minutos_restantes=minutos%60
# muestra el resultado
print(f"{minutos} minutos son {int(horas)} horas y {minutos_restantes} minutos.") 