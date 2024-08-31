# Añadir la ruta absoluta de la carpeta 'modulos' al sistema de rutas de Python
import sys, os

# Añadir la ruta relativa de la carpeta 'modulos' al sistema de rutas de Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modules')) # importe de ruta relativa comprobada en chatgpt

from verify import *

# Importar mimodulo

# Superclase
class Usuario:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def mostrar_info(self):
        return print(f'User: {self.username}\nEmail: {self.email}')

# Hijo
class UsuarioPremium(Usuario):
    def __init__(self, username, email, nivel_premium):
        super().__init__(username, email)
        self.nivel_premium = nivel_premium

# Polimorfismo
def mostrar_informacion_usuario(usuario):

    if verify_email(usuario.email) == False or verify_premium(usuario.nivel_premium) == False:
        print('Error: Correo electrónico o el nivel premium invalido.')

    else:
        usuario.mostrar_info()
        print(f'Nivel Premium: {verify_premium(usuario.nivel_premium)}\n')

# Aplicación del Polimorfismo
# usuario = UsuarioPremium('Perez', 'coso@gmail.com', 1)
# mostrar_informacion_usuario(usuario) # Imprime la información del usuario

# usuario = UsuarioPremium('Perez', 'fhgesiufghieg', 1)
# mostrar_informacion_usuario(usuario) # Imprime un error

# usuario = UsuarioPremium('Perez', 'coso@gmail.com', 0)
# mostrar_informacion_usuario(usuario) # Imprime un error