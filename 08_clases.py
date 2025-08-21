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
        self.limite_credito = 500000 #500 lucas
        self.saldo_pagar = 0
        
    def hacer_compra(self, monto):
        if monto > self.limite_credito - self.saldo_pagar:
            print("Cupo insuficiente")
        else:
            self.saldo_pagar += monto
            print("Compra realizada")
    
    def hacer_pago(self, monto):
        self.saldo_pagar -= monto
        
juan = Usuario("Juan", "Ruiz", "juan@gmail.com", 35)
juan.hacer_compra(1000000) 
        
        
        
        
        
        
        
    

    


