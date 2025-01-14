# Paciente del hospital

from Persona import Persona

class Paciente(Persona):

    def __init__(self, dni, nombre, direccion, telefono):
        super().__init__(dni, nombre, direccion, telefono)
        self.pruebas = []
        
    def nuevaPrueba(self, p):
        self.pruebas.append(p)
        
    def mostrar(self):
        resultado = super().mostrar() + "\n";
        if len(self.pruebas) > 0:
            resultado += "Pruebas realizadas:\n";
            for prueba in self.pruebas:
                resultado += "\t" + prueba.mostrar() + "\n";
        else:
            resultado += "No tiene pruebas realizadas\n";
        
        return resultado