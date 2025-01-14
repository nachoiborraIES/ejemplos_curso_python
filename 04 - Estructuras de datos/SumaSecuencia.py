'''
Programa que le pide al usuario una secuencia de números separados por espacios
y muestra el resultado de su suma
'''

secuencia = input("Escribe la secuencia de números separados por espacios:\n")
partes = secuencia.split(" ")
total = 0
for parte in partes:
    total += int(parte)

print("Total:", total)
