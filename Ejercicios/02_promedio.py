"""
Ejercicio N2
Usuario debe ingresar nombre y 3 notas, el programa debe mostrar su nombre y promedio
"""

nombre = input("Ingrese su nombre: ")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"{nombre}, tu promedio es: {promedio}")
