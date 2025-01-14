'''
Clase Persona
'''

class Persona:

    def __init__(self, n, e, t):
        self.nombre = n
        self.edad = e
        self.telefono = t
    
    def mostrar(self):
        print(f"{self.nombre}, {self.edad} años, {self.telefono}")
