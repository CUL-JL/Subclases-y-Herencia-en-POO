# Superclase
class Usuario:
    def __init__(self, user):
        self.user = user

# Hijos
class UsuarioPremium(Usuario):
    def __init__(self, user, nivel_premium):
        super().__init__(user)
        self.nivel_premium = nivel_premium

    def obtener_descuento(self):
        if self.nivel_premium == "Oro":
            return 20
        elif self.nivel_premium == "Plata":
            return 15
        elif self.nivel_premium == "Bronce":
            return 10
        else:
            return 0

# Polimorfismo
def impresion(user):
    print(f'El usuario {user.user}, es de nivel {user.nivel_premium}. \nDescuento: {user.obtener_descuento()}%')

# Aplicación del Polimorfismo
# usuario = UsuarioPremium("Juan", "Oro")
# impresion(usuario)
# usuario = UsuarioPremium("Pedro", "Plata")
# impresion(usuario)