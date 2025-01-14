# Clase padre Persona, de la que deriva el personal del hospital y pacientes

class Persona:

    def __init__(self, dni, nombre, direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    
    def mostrar(self):
        return f"{self.nombre} ({self.dni})"