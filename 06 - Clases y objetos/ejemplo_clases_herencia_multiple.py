'''
Herencia múltiple
'''

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar(self):
        return f"{self.nombre}, {self.edad} años"

class Empleado:

    def __init__(self, numSS, salario):
        self.numSS = numSS
        self.salario = salario
    
    def mostrar(self):
        return f"Num S.S. {self.numSS}, {self.salario} eur/año"

class Programador(Persona, Empleado):

    def __init__(self, nombre, edad, numSS, salario, lenguaje):
        Persona.__init__(self, nombre, edad)
        Empleado.__init__(self, numSS, salario)
        self.lenguaje = lenguaje

    def mostrar(self):
        return Persona.mostrar(self) + "\n" + Empleado.mostrar(self) + "\n" + \
            "Lenguaje: " + self.lenguaje

# Programa principal

persona1 = Persona("Nacho", 45)
prog1 = Programador("Juan", 50, 121334412, 32000, "Python")

print(persona1.mostrar())
print(prog1.mostrar())
