# Médicos/as del hospital

from Personal import Personal

class Medico(Personal):
       
    def __init__(self, dni, nombre, direccion, telefono, especialidad): 
        super().__init__(dni, nombre, direccion, telefono)
        self.especialidad = especialidad
        
    def mostrar(self):
        return "Doctor/a " + super().mostrar() +  " (" + \
			self.especialidad + ")"