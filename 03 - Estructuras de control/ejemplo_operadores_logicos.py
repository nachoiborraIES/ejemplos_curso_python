'''
Ejemplos de uso de los operadores lógicos
'''

numero = int(input("Dime un número: "))

# Y lógica
print("Está entre 0 y 10:", numero >= 0 and numero <= 10)

# O lógica
print("Es un 0 o un 5:", numero == 0 or numero == 5)

# Negación
print("No está entre 0 y 10:", not(numero >= 0 and numero <= 10))
