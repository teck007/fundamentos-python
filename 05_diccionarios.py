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
