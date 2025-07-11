import datetime
mes_actual = datetime.datetime.now().month
año_actual = datetime.datetime.now().year
año_nacimiento = int(input("Ingrese su año de nacimiento"))
mes_nacimiento = int(input("Ingrese su mes de nacimiento"))
if (mes_actual > mes_nacimiento): # meses mayores octubre
    edad = año_actual - año_nacimiento
else: # meses menores a octubre
    edad = (año_actual - año_nacimiento) - 1
nombre = "Joaquin Navarrete"
print("Mi edad es:", edad)





print("Mi nombre es:", nombre.upper(), "y mi edad es:", edad)
notas = []
notas.append(70) #Matemática
notas.append(55) #Lenguaje
notas.append(65) #Programación
notas.append(60) #Filosofía
print("Mis notas son:", notas)
promedio = sum(notas)/len(notas)
print("Mi promedio es: ", promedio)
#mostrar mensaje dependiendo el promedio
if (promedio >= 40):
    print("Nota azul")
else:
    print("Nota roja")

