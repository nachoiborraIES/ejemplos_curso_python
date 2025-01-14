# Programa que define una clase Jugador y otra Equipo, y asocia un 
# equipo a cada jugador

class Equipo:
	
	def __init__(self, n):
		self.nombre = n
            
	def mostrar(self):
		return self.nombre

class Jugador:
	
	def __init__(self, d, n, e):
		self.dorsal = d
		self.nombre = n
		self.equipo = e
	
	def mostrar(self):
		return str(self.dorsal) + ". " + self.nombre + \
			" (" + self.equipo.mostrar() + ")"

equipo1 = Equipo("Python FC")
jugador1 = Jugador(8, "John Lambda", equipo1)
print(jugador1.mostrar())

