#Diccionarios
#Definir diccionario
datos = {}
datos = {"nombre": "Axel", "apellido": "Pincheira", "edad": 37}

#Mostrar diccionario
print(datos)

#Mostrar un dato en concreto
print(datos["nombre"])

#Ingresar un dato
datos["sexo"]="masculino"

#Ingresa un dato y verifica si existe la clave
datos.setdefault("sexo", "femenino")
print(datos)

del datos["sexo"]  # Eliminar un dato
print(datos)

datos["Lenguajes"] = ("html", "Java", "C++")  # Agregar una tupla de lenguajes
# Ejemplo: agregar más valores a la clave "Lenguajes"
datos["Lenguajes"] = list(datos["Lenguajes"])  # Convertir a lista si es tupla
datos["Lenguajes"].append("JavaScript")  # Agregar un nuevo lenguaje

print(datos["Lenguajes"])  # Ahora muestra todos los lenguajes

print("Pincheria" in datos)  # Verifica si la clave "Pincheria" está en el diccionario
print("apellido" in datos)  # Verifica si la clave "apellido" está en el diccionario

print(datos.items())  # Muestra todos los items del diccionario
print(datos.keys())  # Muestra todas las claves del diccionario
print(datos.values())  # Muestra todos los valores del diccionario
