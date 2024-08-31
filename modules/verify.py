# comprobaciones de los datos de entrada
from re import match

# Comprobación de correo electrónico
def verify_email(email):
    # Expresión regular para validar un correo electrónico
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if match(patron, email):
        return email
    else:
        return False

# Comprobación de nieveles premium
def verify_premium(nivel):
    if nivel == 1:
        return 'Oro'
    
    elif nivel == 2:
        return 'Plata'
    
    elif nivel == 3:
        return 'Bronce'
    
    else:
        return False
