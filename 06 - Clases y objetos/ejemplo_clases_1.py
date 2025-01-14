'''
Definición básica de clases y objetos
'''

class Persona:

    def __init__(self, n, e, t):
        self.nombre = n
        self.edad = e
        self.telefono = t
    
    def mostrar(self):
        print(f"{self.nombre}, {self.edad} años, {self.telefono}")

# Programa principal

persona1 = Persona("Nacho", 45, "611223344")
persona1.mostrar()

personas = list()
personas.append(Persona("Juan", 70, "9612345678"))
personas.append(Persona("Ana", 40, "699887766"))

for p in personas:
    p.mostrar()