#Condicionales
#False=falso  True=verdadero
condicion = False
condicion = True

if condicion:
    print("hola")

#Condiciónal simple    
numero = 5 * 2
if numero == 10:
    print("número es igual a 10")
    print("chao")

# IF ELIF ELSE
numero = 5  
if numero > 5:
    print("Número mayor a 5")
elif numero < 5:
    print("Número menor a 5")
else:
    print("Número es igual a 5")
"""
Doble condición:
and = requiere que todas las condiciones sean 
verdaderas
or = requiere que una de las condiciones sean verdaderas
"""
numero = 10
if numero > 5 and numero < 10:
    print("Número es mayor que 5 y menor a 10")
elif numero < 5:
    print("Número es menor a 5")
elif numero > 10:
    print("Número es mayor a 10")
elif numero == 10:
    print("Número es igual a 10")
else:
    print("Número es igual a 5")

# IF NOT
numero = 5
if not numero == 5:
    print("numero no es igual a 5")
    
texto = "hola"
if texto == "hola":
    print("Es igual a hola")
else:
    print("No es hola")