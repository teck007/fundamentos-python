#Se definen variables
nombre = "Axel"
apellido = "Pincheira"
edad = 37

#Mostrar cantidad de carácteres entre 1 y 3
print(len(nombre))

#Se muestra los carácteres entre 1 y 3 en mayuscula
print(nombre.upper())

#Se muestra los carácteres entre 1 y 3 en minuscula
print(nombre.lower())

#Se muestra cantidad de carácteres entre 1 y 3 que coincida
print(apellido.count("a"))

#Devuelve un true si es un número
edad = "37"
print(edad.isnumeric())

#División
#Mostrar carácteres entre 1 y 3
print(nombre[1:3])
#Mostrar carácteres de la posición 1 en adelante 
print(nombre[1:])
#Mostrar carácteres a la inversa la posición 2 
print(nombre[-2])

#Concatenar o unir
edad = 37
print("Mis datos son " + nombre + " " +  apellido + " " + str(edad))

#Concatenar o unir en una variable
datos = nombre + " " +  apellido + " " + str(edad)
print(datos)

datos = nombre + "\n" +  apellido + "\n" + str(edad)
print(datos)