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
       pass


   def cambiar_suscripcion(self, nueva_suscripcion):
       """Cambia el tipo de suscripción del usuario."""
       pass


   def mostrar_info_usuario(self):
       """Muestra la información del usuario y su lista de reproducción."""
       pass