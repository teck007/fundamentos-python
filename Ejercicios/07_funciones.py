#Funciones
#Definir función
def mi_funcion():
    print("Esto es una función")

#Llamar a la función
mi_funcion()
mi_funcion()

# Función con parametros de entrada
def multiplicacion(num1, num2):
    resultado = num1 * num2
    print(resultado)
    
multiplicacion(3, 5)

# Función con parametros de entrada
# además retorna un valor
def multiplicacion2(num1, num2):
    resultado = num1 * num2
    return resultado

print(multiplicacion2(4, 7))