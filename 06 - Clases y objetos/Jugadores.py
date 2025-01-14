# Programa que define una clase Jugador con varios objetos de esa clase

class Jugador:
	
	def __init__(self, d, n):
		self.dorsal = d
		self.nombre = n
	
	def mostrar(self):
		return str(self.dorsal) + ". " + self.nombre 

# Programa principal
jugador1 = Jugador(8, "John Lambda")
jugador2 = Jugador(16, "Pau Gasol")
print(jugador1.mostrar())
print(jugador2.mostrar())

