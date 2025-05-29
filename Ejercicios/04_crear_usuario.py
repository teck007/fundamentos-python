"""
Ejercicio N4
El usuario debe ingresar nombre, nickname y edad, el programa debe
generar un nombre de usuario utilizando los datos ingresados
"""
nombre = input("Ingresa tu nombre: ")
nickname = input("Ingresa tu nickname: ")
edad = input("Ingresa tu edad: ")

# Generar nombre de usuario: primera letra del nombre + nickname + edad
usuario = nombre[0].lower() + nickname.lower() + edad

print(f"Tu nombre de usuario es: {usuario}")