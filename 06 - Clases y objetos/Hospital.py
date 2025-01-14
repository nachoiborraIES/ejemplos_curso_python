'''
Programa que simula con clases y objetos la gestión de pacientes de
un hospital
'''

# Clase padre Persona, de la que deriva el personal del hospital y pacientes

class Persona:

    def __init__(self, dni, nombre, direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    
    def mostrar(self):
        return f"{self.nombre} ({self.dni})"

# Personal del hospital

class Personal(Persona):

    def __init__(self, dni, nombre, direccion, telefono):
        super().__init__(dni, nombre, direccion, telefono)
    
class Administrativo(Personal):

    def __init__(self, dni, nombre, direccion, telefono): 
        super().__init__(dni, nombre, direccion, telefono)

class Medico(Personal):
       
    def __init__(self, dni, nombre, direccion, telefono, especialidad): 
        super().__init__(dni, nombre, direccion, telefono)
        self.especialidad = especialidad
        
    def mostrar(self):
        return "Doctor/a " + super().mostrar() +  " (" + \
			self.especialidad + ")"

class Enfermero(Personal):
       
    def __init__(self, dni, nombre, direccion, telefono, numeroPlanta): 
        super().__init__(dni, nombre, direccion, telefono)
        self.numeroPlanta = numeroPlanta
        
    def mostrar(self):
        return "Enfermero/a " + super().mostrar() + " (" + \
			str(self.numeroPlanta) + "ª planta)"

# Paciente

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
        
        return resultado;

# Clase Prueba médica

class Prueba:
        
    def __init__(self, fecha, descripcion, medico):
        self.fecha = fecha
        self.descripcion = descripcion
        self.medico = medico
        
    def mostrar(self):
        return self.descripcion + ", realizada por " + \
            self.medico.mostrar() + " el " + self.fecha

# Programa principal

personal = []
personal.append(Medico("11223344A", "Juan Pérez", "C/Dolor de tripa, 3", \
	"611223344", "Endocrinología"))
personal.append(Medico("55667788B", "Elena Suárez", \
	"C/Tendón de Aquiles, 5", "600998877", "Traumatología"))
personal.append(Medico("98765432C", "María Ripoll", "C/Bisturí, 12", \
	"699885544", "Cirugía"))
personal.append(Enfermero("55667788D", "Mario Martínez", "C/Vacuna, 23", \
	"666771122", 3))

paciente = Paciente("48112233D", "Dolores Fuertes", \
	"C/ Hipocondria, 22", "666554433")
paciente.nuevaPrueba(Prueba("12/1/2019", "Radiografía", personal[1]))
paciente.nuevaPrueba(Prueba("23/3/2019", "Ecografía", personal[0]))

print(paciente.mostrar())