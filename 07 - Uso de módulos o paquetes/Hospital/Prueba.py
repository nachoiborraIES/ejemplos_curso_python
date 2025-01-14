# Clase Prueba médica

class Prueba:
        
    def __init__(self, fecha, descripcion, medico):
        self.fecha = fecha
        self.descripcion = descripcion
        self.medico = medico
        
    def mostrar(self):
        return self.descripcion + ", realizada por " + \
            self.medico.mostrar() + " el " + self.fecha