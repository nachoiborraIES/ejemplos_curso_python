'''
Definición básica de clases y objetos con visibilidad y encapsulamiento
'''

class Persona:

    def __init__(self, n, e, t):
        self.__nombre = n
        self.__edad = e
        self.__telefono = t
    
    def mostrar(self):
        print(f"{self.__nombre}, {self.__edad} años, {self.__telefono}")
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def telefono(self):
        return self.__telefono
    
    @nombre.setter
    def nombre(self, n):
        self.__nombre = n
    
    @edad.setter
    def edad(self, e):
        if e >= 0:
            self.__edad = e
    
    @telefono.setter
    def telefono(self, t):
        self.__telefono = t

# Programa principal

persona1 = Persona("Nacho", 45, "611223344")
persona1.nombre = "Pepe"
persona1.edad = 30
persona1.edad = -10
persona1.mostrar()
