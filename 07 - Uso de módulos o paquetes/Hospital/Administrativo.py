# Personal administrativo del hospital

from Personal import Personal

class Administrativo(Personal):

    def __init__(self, dni, nombre, direccion, telefono): 
        super().__init__(dni, nombre, direccion, telefono)