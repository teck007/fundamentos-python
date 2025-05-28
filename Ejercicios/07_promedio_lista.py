"""
Ejercicio N7
1. Usuario debe ingresar nombre
2. Usuario debe ingresar 4 notas y estas notas guardarlas 
   como elemento en una lista llamada notas
3. Calcular promedio final y guardarlo en una variable promedio
4. Mostrar nombre y promedio con un mensaje
   ejemplo de mensaje "Joaquin usted tiene un promedio: "
"""
nombre = input("Ingrese su nombre")
notas = []
notas.append(float(input("Ingrese primera nota")))
notas.append(float(input("Ingrese segunda nota")))
notas.append(float(input("Ingrese tercera nota")))
notas.append(float(input("Ingrese cuarta nota")))
promedio = (notas[0]+notas[1]+notas[2]+notas[3])/4
print("Su promedio es:", promedio)