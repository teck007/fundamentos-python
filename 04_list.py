### Definicion de listas ###    

mi_lista = list() # lista vacia
mi_otra_lista =[] # lista vacia

mi_lista = [38, 17, 17, 17, 18] # lista con elementos

print(mi_lista) # imprime la lista

print(len(mi_lista)) # longitud de la lista

# lista con diferentes tipos de datos
mi_otra_lista = [35, 1.77, "Axel", "Pincheira"] 

# imprime el tipo de la lista
print(type(mi_otra_lista)) 

# acceder a los elementos de la lista
print(mi_otra_lista[2])
print(mi_otra_lista[-2])
print(mi_otra_lista[0])

# Mostrar cantidad de veces que se repite un elemento
print(mi_lista.count(17))

#Devuelve un error de Index
#print(mi_otra_lista[4])

# Mostrar la posición de un elemento
print(mi_otra_lista.index("Pincheira", ))

# Crear tres variables con los elementos de la lista
edad, altura, nombre = mi_otra_lista[0], mi_otra_lista[1], mi_otra_lista[2]
print(edad)