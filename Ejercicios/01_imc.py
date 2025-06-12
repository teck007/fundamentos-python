"""
Ejercicio N1
El usuario ingresa peso y altura y el programa muestre el valor del indice de masa corporal IMC
imc = peso/(altura²)
"""
def imc(peso, altura):
    resultado = peso/altura**2
    return resultado

peso = float(input("Ingrese peso en kilos"))
altura = float(input("Ingrese altura en metros"))
print("Su IMC es:", imc(peso, altura))