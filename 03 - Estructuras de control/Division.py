'''
Programa que le pide al usuario dos números a y b y los divide siempre que b no sea 0
'''

a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))

if b != 0:
    resultado = a / b
    print(f"La división de {a} entre {b} es {resultado:.2f}")
else:
    print("No se puede dividir entre 0")