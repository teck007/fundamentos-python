"""
Ejercicio: Sistema de Cobro de entradas parque de diversiones Fullpark

Se necesita un sistema automatizado para el cobro de entradas. El programa debe cumplir con los siguientes requisitos:

1. Mostrar un mensaje de bienvenida al usuario.
   Ejemplo: "Bienvenido a Fullpark, el mejor lugar para disfrutar de tus juegos favoritos."
2. Preguntar cuántas personas ingresarán al recinto.
3. Solicitar el nombre, edad y tiempo de permanencia en horas (se debe guardar una lista de diccionarios).
4. Definir las siguientes categorías de entrada y sus precios:
    - Menor de 4 años: Entrada gratuita
    - Entre 4 y 17 años: Entrada a $3.000 x hora
    - Adulto (18 años o más): Entrada a $5.000 x hora
5. Mostrar el resumen de costos.
6. Al final, mostrar el total a pagar por todo el grupo.

Utiliza estructuras de control como bucles for, listas y diccionarios para resolver el ejercicio.
"""
print("Bienvenido a Fullpark, el mejor lugar para disfrutar de tus juegos favoritos")

def calcular_precio(edad):
    monto = 0
    if 4 <= edad < 18:
            monto = 3000
    elif edad >= 18:
            monto = 5000
    return monto

cantidad_personas = int(input("Ingrese cantidad de personas del grupo"))
monto_total = 0
for i in range(cantidad_personas):
    nombre = input("Ingrese nombre, persona " + str(i+1))
    edad = int(input("Ingrese edad" + str(i+1)))
    monto_total = monto_total + calcular_precio(edad)

tiempo = int(input("Ingrese tiempo de permanencia en horas"))
monto_total = monto_total * tiempo
print("El total a pagar es:", monto_total)