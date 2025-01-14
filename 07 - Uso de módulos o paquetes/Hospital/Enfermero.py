# Enfermeros/as del hospital

from Personal import Personal

class Enfermero(Personal):
       
    def __init__(self, dni, nombre, direccion, telefono, numeroPlanta): 
        super().__init__(dni, nombre, direccion, telefono)
        self.numeroPlanta = numeroPlanta
        
    def mostrar(self):
        return "Enfermero/a " + super().mostrar() + " (" + \
			str(self.numeroPlanta) + "ª planta)"