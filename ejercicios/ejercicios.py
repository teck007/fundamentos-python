#Ejercicio N1
#calculadora de IMC
#peso/(altura²)

peso = float(input("Ingrese peso en kilos"))
altura = float(input("Ingrese altura en metros"))
print("Su IMC es:", peso/altura**2)

#Ejercicio N2
#Usuario debe ingresar nombre y 3 notas, el programa
#debe mostrar su nombre y promedio
nombre = input("Ingrese su nombre")
nota1 = float(input("Ingrese la primera nota"))
nota2 = float(input("Ingrese la segunda nota"))
nota3 = float(input("Ingrese la tercera nota"))
#Calculo de promedio
promedio = (nota1+nota2+nota3)/3
#Promedio con 1 decimal
print("Su promedio es:", round(promedio, 1))