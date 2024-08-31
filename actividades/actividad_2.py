"""
NOTA: Particularidad de python que imprime None al momento de iterar sobre una lista de 
objostos y querer imprimirlo. Imprimir desde el metodo de la clase para evitar el problema.
"""
#Superclase
class Animal:
    def hacer_sonido(self): # Metodo no implementado
        pass

# Hijos
class Perro(Animal):
    def hacer_sonido(self): # Rewrite del metodo del padre
        print('¡Gua gua!')
     
class Gato(Animal):
    def hacer_sonido(self): # Rewrite del metodo del padre
        print ('¡Miau miau!')

# Metodo externo para llamada de los hijos
def hacer_ruido(animal):
    animal.hacer_sonido() # Impresion del sonido de los hijos

# Llamada de los metodos
# subclass = [Gato(), Perro()]
# for index in subclass:
#     hacer_ruido(index)
