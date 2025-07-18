"""
https://learning.skillnest.com/cursos/python-full-stack-b2u-4-medio-principe-de-gales-2025/leccion/fundamentos-de-python-funciones-basicas-2-practica-14/
"""
# ejercicio 1
def multiplicax2(num1):
    resultado = []
    for i in range(num1+1):
      resultado.append(i*2)
    return resultado  

print(multiplicax2(5))

# ejercicio 2
def suma_resta(a, b):
  print(a + b)
  return a - b

print(suma_resta(5, 4))