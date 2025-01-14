# Programa que define una función con valores por defecto
# La función se invoca desde el programa principal tomando los datos de 
# línea de comandos. Según el número de parámetros recibidos, se activarán
# los valores por defecto asignados

import sys

def contar(inicio=1, fin=10):
	if inicio < fin:
		for i in range(inicio, fin+1):
			print(i)
	else:
		for i in range(inicio, fin-1, -1):
			print(i)

# Programa principal

if len(sys.argv) == 3:
	contar(int(sys.argv[1]), int(sys.argv[2]))
elif len(sys.argv) == 2:
	contar(int(sys.argv[1]))
elif len(sys.argv) == 1:
	contar()