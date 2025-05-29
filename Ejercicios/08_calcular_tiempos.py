"""
Ejercicio N8
El usuario debe ingresar su nombre y 4 tiempos minutos de ida y vuelta
en un tramo especifico, el programa debe ordenar los tiempos de
menor a mayor y debe mostrar el promedio de tiempo, asi como
el tiempo menor y mayor. 
"""
tiempos = []
nombre = input("Ingrese nombre")
tiempos.append(float(input("Ingrese primer tiempo")))
tiempos.append(float(input("Ingrese segundo tiempo")))
tiempos.append(float(input("Ingrese tercer tiempo")))
tiempos.append(float(input("Ingrese cuarto tiempo")))
promedio = (sum(tiempos)/len(tiempos))
tiempos.sort()
print("Hola", nombre, "te dejo a continuación tus datos")
print("El promedio es:", promedio)
print("Tu mejor tiempo es:", tiempos[0])
print("El peor tiempo es:", tiempos[-1])