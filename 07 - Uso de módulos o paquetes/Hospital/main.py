'''
Programa que simula con clases y objetos la gestión de pacientes de
un hospital
'''

from Paciente import Paciente
from Prueba import Prueba
from Medico import Medico
from Enfermero import Enfermero

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