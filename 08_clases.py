"""Creación de una clase
class Usuario:
    pass
"""
class Usuario:
    def __init__(self):
        self.nombre = "Joaquin"
        self.apellido = "Navarrete"
        self.email = "joaco@gmail.com"
        self.edad = 17 
#Instanciar o crear un objeto
juan = Usuario()
juan.nombre = "Juan"
print(juan.nombre)


