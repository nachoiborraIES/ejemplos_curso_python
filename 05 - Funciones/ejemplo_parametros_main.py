'''
Ejemplo de paso de parámetros al programa principal
'''
import sys

for i in range(1, len(sys.argv)):
    print(f"El parámetro {i} es {sys.argv[i]}")