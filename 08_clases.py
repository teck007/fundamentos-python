"""Creación de una clase
class Usuario:
    pass
"""
class Usuario:
    def __init__(self, nombre, apellido, email, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad
        self.limite_credito = 30000
        self.saldo_pagar = 0
    def hacer_compra(self, monto):
        self.saldo_pagar += monto
#Instanciar o crear un objeto
juan = Usuario("Juan", "Rojo", "juan@gmail.com", 30)
juan.hacer_compra(1000)
juan.hacer_compra(1000)
print(juan.nombre, juan.saldo_pagar)


