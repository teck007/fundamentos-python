"""
Ejercicio N1
El usuario ingresa peso y altura y el programa muestre el valor del indice de masa corporal IMC
imc = peso/(altura²)
"""
peso = float(input("Ingrese peso en kilos"))
altura = float(input("Ingrese altura en metros"))
print("Su IMC es:", peso/altura**2)