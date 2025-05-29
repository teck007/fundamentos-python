"""
Ejercicio N5 
1. Crear una lista llamada vegetales con al menos 5 nombres de vegetales.
2. Imprime la lista completa y su longitud.
3. Imprime el primer y el ultimo elemento de la lista.
4. Agrega un nuevo vegetal al final de la lista.
5. Inserta un vegetal en la segunda posición.
6. reemplaza el vegetal en la tercera posicion por otro.
7. Elimina un vegetal por su nombre.
8. Elimina el ultimo vegetal usando .pop().
9. Crea una copia de la lista ordenada alfabeticamente.
10. Imprime una sublista con los elementos del indice 1 a 3.
"""
# 1. Crear la lista
vegetales = ["zanahoria", "lechuga", "tomate", "pepino", "espinaca"]

# 2. Imprime la lista completa y su longitud
print("Lista completa:", vegetales)
print("Longitud de la lista:", len(vegetales))

# 3. Imprime el primer y el último elemento
print("Primer vegetal:", vegetales[0])
print("Último vegetal:", vegetales[-1])

# 4. Agrega un nuevo vegetal al final
vegetales.append("brócoli")
print("Después de agregar brócoli:", vegetales)

# 5. Inserta un vegetal en la segunda posición
vegetales.insert(1, "apio")
print("Después de insertar apio en la segunda posición:", vegetales)

# 6. Reemplaza el vegetal en la tercera posición por otro
vegetales[2] = "calabaza"
print("Después de reemplazar el tercer vegetal por calabaza:", vegetales)

# 7. Elimina un vegetal por su nombre
vegetales.remove("pepino")
print("Después de eliminar pepino:", vegetales)

# 8. Elimina el último vegetal usando .pop()
vegetales.pop()
print("Después de eliminar el último vegetal:", vegetales)

# 9. Crea una copia de la lista ordenada alfabéticamente
vegetales_ordenados = sorted(vegetales)
print("Lista ordenada alfabéticamente:", vegetales_ordenados)

# 10. Imprime una sublista con los elementos del índice 1 a 3
print("Sublista de índice 1 a 3:", vegetales[1:4])