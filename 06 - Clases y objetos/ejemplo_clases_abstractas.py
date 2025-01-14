'''
Ejemplo de uso de clases abstractas
'''

from abc import ABC, abstractmethod

# Clase padre abstracta Animal

class Animal(ABC):

    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def hablar():
        pass

    @abstractmethod
    def dibujar():
        pass

# Subclase abstracta Ave
class Ave(Animal):

    pass

# Subclase de Animal: Perro
class Perro(Animal):

    def hablar(self):
        print("Guau!")
    
    def dibujar(self):
        print(' -._,-.')
        print('\\/)\"(\\/')
        print(' (_o_)')
        print('  / \\')
        print('(|| ||')
        print(' oo-oo')

# Subclase de Animal: Conejo
class Conejo(Animal):

    def hablar(self):
        print("...")
    
    def dibujar(self):
        print(" ()()")
        print("=(';')=")
        print(" (\")(\")")

# Subclase de Ave: Buho
class Buho(Ave):

    def hablar(self):
        print("Uhuuuu!")
    
    def dibujar(self):
        print('/╲ ︵ ╱\\')
        print('(◉) (◉)|')
        print('\︶V︶/')
        print(' /↺↺↺↺\\')
        print(' ↺↺↺↺↺')
        print(' \\↺↺↺↺/')
        print('  /\/\ ')

# Programa principal

animales = list()
animales.append(Perro("Bobby"))
animales.append(Conejo("Bugs Bunny"))
animales.append(Buho("Owl"))

for a in animales:
    a.dibujar()
    a.hablar()

# Esto daría error al ser una clase abstracta
# ave = Ave("Ave 1")