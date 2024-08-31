# Superclase
class Vehiculo:
    def __init__(self, marca): # Atributo
        self.marca = marca
        
    def acelerar(self): # Metodo
        return 'El vehiculo está acelerando.'
    
# Hijos
class Coche(Vehiculo): 
    def __init__(self, marca):  
        super().__init__(marca) # Atributo del padre pasado al hijo
        
    # def tocar_claxon(self): # Metodo
    def accion(self): # Metodo
        # return '¡Beep beep!'
        return 'hace ¡Beep beep!'
    
class Motocicleta(Vehiculo):
    def __init__(self, marca): 
        super().__init__(marca) # Atributo del padre pasado al hijo
        
    # def hacer_caballito(self): # Metodo
    def accion(self): # Metodo
        # return 'La motocicleta está haciendo un caballito.'
        return 'está haciendo un caballito.'

# Polimorfismo
def accion(vehiculo):
    print(f'Mi {vehiculo.marca}, {vehiculo.accion()}\n{vehiculo.acelerar()}\n')


# mi_coche = Coche('Tesla')
# mi_motocicleta = Motocicleta('Honda')
# # print(f'Mi coche {mi_coche.marca}, hace {mi_coche.tocar_claxon()}.\nMi motocicleta {mi_motocicleta.marca}, hace {mi_motocicleta.hacer_caballito()}.')

# # Aplicación del Polimorfismo
# accion(mi_coche)
# accion(mi_motocicleta)