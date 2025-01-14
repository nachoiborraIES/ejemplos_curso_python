'''
Programa que calcula la tabla de multiplicar del número que diga el usuario
'''

# Pedimos al usuario un número del 1 al 10

numero = 0

while numero < 1 or numero > 10:
    numero = int(input("Escribe un número del 1 al 10: "))

print("Has elegido el número", numero)

# Construir la tabla de multiplicar

for i in range(0, 11):
    print(f"{numero} x {i} = {numero * i}")