"""
Ejercicio N11
1. Pedir al usuario su año de nacimiento (input).
2. Definir año actual en una variable .
3. Calcular la edad restando el año de nacimiento al año actual.
4. Determinar el rango etario usando condicionales:
   - Si la edad está entre 1 y 17: "Menor de edad"
   - Si la edad está entre 18 y 25: "Adulto joven"
   - Si la edad está entre 26 y 59: "Adulto"
   - Si la edad está entre 60 y 100: "Adulto mayor"
5. Mostrar al usuario su edad y rango etario (print).
Utilizar condicionales, mayor o igual >=     menor o igual <=
"""
fecha_nac = int(input("Ingrese su año de nacimiento: "))
anio_actual = 2025
edad = anio_actual - fecha_nac

if 1 <= edad <= 17:
    rango = "Menor de edad"
elif 18 <= edad <= 25:
    rango = "Adulto joven"
elif 26 <= edad <= 59:
    rango = "Adulto"
elif 60 <= edad <= 100:
    rango = "Adulto mayor"
else:
    rango = "Edad fuera de rango"

print(f"Tienes {edad} años. Rango etario: {rango}.")