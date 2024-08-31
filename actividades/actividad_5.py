# Añadir la ruta absoluta de la carpeta 'modulos' al sistema de rutas de Python
import sys, os

# Añadir la ruta relativa de la carpeta 'modulos' al sistema de rutas de Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modules')) # importe de ruta relativa comprobada en chatgpt

from verify import verify_email # Importamos la funcion verify_email para 

# Superclase
class Pago:
    def procesar_pago(self):
        pass

# Hijos
class PagoTarjeta(Pago):
    def __init__(self, numero_tarjeta, monto):
        self.numero_tarjeta = numero_tarjeta
        self.monto = int(monto)


    def procesar_pago(self):
        if len(self.numero_tarjeta) != 16:
            raise ValueError('Error: El email no es valido.\n')
        
        return f'Pago aceptado. Se ha realizado un pago de {self.monto}$ con la tarjeta {self.numero_tarjeta}.\n'

        
class PagoPaypal(Pago):
    def __init__(self, email, monto):
        self.email = email
        self.monto = int(monto)

    def procesar_pago(self):
        if not verify_email(self.email):
            raise ValueError('Error: El email no es valido.\n')
        
        return f'Pago aceptado. Se ha realizado un pago de {self.monto}$ con el email {self.email}.\n'
    
class PagoCriptomoneda(Pago):
    def __init__(self, wallet, monto):
        self.wallet = wallet
        self.monto = int(monto)

    def procesar_pago(self):
        if len(self.wallet) != 4:
            raise Exception('Error: La wallet no es valida.\n')
        
        return f'Pago aceptado. Se ha realizado un pago de {self.monto}$ con la wallet {self.wallet}.\n'

# Polimorfismo
def procesar_pagos(pagos):
    print(pagos.procesar_pago())

# Instancias
# pago1 = PagoTarjeta('1234567891234567', 100)
# procesar_pagos(pago1)
# pago2 = PagoPaypal('coso@gmail.com', 200)
# procesar_pagos(pago2)
# pago3 = PagoCriptomoneda('1234', 300)
# procesar_pagos(pago3)
        
