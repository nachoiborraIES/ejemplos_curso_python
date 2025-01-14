# Personal del hospital

from Persona import Persona

class Personal(Persona):

    def __init__(self, dni, nombre, direccion, telefono):
        super().__init__(dni, nombre, direccion, telefono)