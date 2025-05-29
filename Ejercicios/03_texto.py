"""
Ejercicio N3
El usuario debe ingresar un texto y el programa debe mostrar la cantidad 
de letras que contiene y mostrar la letra inicial y la letra final
"""
texto = input("Ingrese un texto: ").strip()
cantidad_letras = len(texto)
letra_inicial = texto[:1]
letra_final = texto[-1:]
print(f"Cantidad de letras: {cantidad_letras}")
print(f"Letra inicial: {letra_inicial}")
print(f"Letra final: {letra_final}")
