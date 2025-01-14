'''
Usos avanzados de la cláusula "if"
'''

numero = int(input("Escribe un número: "))

if numero >= 10:
    print("El número es mayor o igual que 10")
elif numero >= 0:
    print("El número es mayor o igual que 0 y menor que 10")
elif numero >= -10:
    print("El número es mayor o igual que -10 y menor que 0")
else:
    print("El número es menor que -10")

nota = int(input("Dime la nota del examen: "))
'''
if nota >= 5:
    resultado = "APROBADO"
else:
    resultado = "SUSPENSO"
'''
resultado = "APROBADO" if nota >= 5 else "SUSPENSO"
print("Resultado de tu examen:", resultado)