#Ejercicio: Registro y búsqueda de libros en una biblioteca
#Descripción del ejercicio:
#Desarrolla un programa en Python que permita registrar libros en una biblioteca, mostrando luego la lista completa de libros y permitiendo buscar un libro por su título.
#Requisitos:
#Debes crear una lista llamada biblioteca para almacenar los libros.
#Cada libro será representado como un diccionario con las claves: "titulo", "autor" y "anio".
#Implementa las siguientes funciones:
#agregar_libro(biblioteca, titulo, autor, anio): Agrega un libro a la lista.
#mostrar_libros(biblioteca): Muestra todos los libros registrados.
#buscar_libro(biblioteca, titulo): Busca un libro por su título y muestra su información si lo encuentra.
#Usa un ciclo for para mostrar todos los libros almacenados.

biblioteca = []

def agregar_libro(biblioteca, titulo, autor, anio):
    datos = {"titulo": titulo, "autor": autor, "año": anio}
    biblioteca.append(datos)
    
def mostrar_libros(biblioteca):
    print(biblioteca)

agregar_libro(biblioteca, "El senor de los anillos", "JRR Tolkien", 1954)
print(biblioteca)