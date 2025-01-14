'''
Herencia entre clases
'''

class Persona:

    def __init__(self, n, e):
        self.nombre = n
        self.edad = e
    
    def mostrar(self):
        return f"{self.nombre}, {self.edad} años"

class Programador(Persona):

    def __init__(self, n, e, l):
        super().__init__(n, e)
        self.lenguaje = l

    def mostrar(self):
        return super().mostrar() + "\nLenguaje: " + self.lenguaje

# Programa principal

persona1 = Persona("Nacho", 45)
prog1 = Programador("Juan", 50, "Python")

print(persona1.mostrar())
print(prog1.mostrar())

personas = list()
personas.append(persona1)
personas.append(prog1)
personas.append(Programador("Ana", 40, "Java"))

for p in personas:
    print(p.mostrar())