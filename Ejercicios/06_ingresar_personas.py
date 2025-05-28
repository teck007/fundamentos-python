"""
Ejercicio N6
1. Permite al usuario ingresar 3 nombres.
2. Guarda cada nombre como elemento en una lista llamada personas
3. Ordena los nombres por orden alfabetico
4. Muestra todos los nombres en pantalla
"""
personas = []
personas.append(input("Ingrese el primer nombre"))
personas.append(input("Ingrese el segundo nombre"))
personas.append(input("Ingrese el tercer nombre"))
personas.sort()
print(personas)
