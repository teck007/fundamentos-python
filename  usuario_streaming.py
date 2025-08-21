class UsuarioStreaming:
   def __init__(self, nombre, email, suscripcion="Gratis"):
       self.nombre = nombre
       self.email = email
       self.suscripcion = suscripcion
       self.lista_reproduccion = []


   def agregar_a_lista(self, titulo):
       self.lista_reproduccion.append(titulo)
       pass


   def ver_contenido(self, titulo):
       pos = self.lista_reproduccion.index(titulo)
       if pos == None:
           print("El contenido no se encuentra en la lista de reproducción")
           return
       print("Se esta reproduciendo:", self.lista_reproduccion[pos])
       pass


   def cambiar_suscripcion(self, nueva_suscripcion):
       """Cambia el tipo de suscripción del usuario."""
       pass


   def mostrar_info_usuario(self):
       """Muestra la información del usuario y su lista de reproducción."""
       pass
   
juan = UsuarioStreaming("Juan", "juan@gmail.com")
juan.agregar_a_lista("Canción 1")
juan.agregar_a_lista("Canción 2")
juan.ver_contenido("Canción 10")
   