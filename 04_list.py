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

print(mi_lista + mi_otra_lista)  # Imprime la concatenación de las dos listas
mi_otra_lista.append("Complejo principe de gales")  # Agregar un elemento al final de la lista
print(mi_otra_lista)  # Imprime la lista completa después de agregar un nuevo elemento
mi_otra_lista.insert(1, "Rojo")  # Agregar un elemento en la posición 1 de la lista
print(mi_otra_lista)  # Imprime la lista completa después de agregar un nuevo elemento

mi_otra_lista[1] = "Azul"  # Cambiar el elemento en la posición 1 de la lista
print(mi_otra_lista)  # Imprime la lista completa después de cambiar un elemento
mi_otra_lista[3]= "Patricio"  # Cambiar el elemento en la posición 3 de la lista
mi_otra_lista[4]= "Renault"  # Cambiar el elemento en la posición 4 de la lista
print(mi_otra_lista)  # Imprime la lista completa después de cambiar un elemento

mi_otra_lista.remove("Azul") # Eliminar un elemento de la lista
print(mi_otra_lista)# imprime la lista completa

print(mi_lista)
mi_lista.remove(18) # elimina un elemento de la lista
print(mi_lista)# Imprime la lista completa
mi_lista.pop() #Eliminar el ultimo elemento de la lista
print(mi_lista) # Imprime la lista completa

mi_nueva_lista = mi_lista.copy() # Copiar la lista

del mi_lista[2] # Elimina el elemento de la lista en la posicion 2 de la lista
print(mi_lista) # Imprime la lista completa

print(mi_nueva_lista)

mi_lista.clear() #Eliminar todos los elmentos de la lista
print(mi_lista)

print(mi_nueva_lista.reverse()) # Invertir la lista
print(mi_nueva_lista) #Imprime la lista completa

mi_nueva_lista.sort() # Ordenar la lista
print(mi_nueva_lista) #Imprime la lista completa