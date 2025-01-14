'''
Otros usos de funciones
'''

def mostrar_datos(nombre, apellidos="García", dia=1):
    print(f"Hola {nombre} {apellidos}, hoy es día {dia}")

def sumar_numeros(num1, *numeros):
    suma = num1
    for num in numeros:
        suma += num
    return suma

def mostrar_notas(**notas):
    for clave in notas:
        print(clave, ":", notas[clave])

def funcion_pendiente():
    pass

# Programa principal

# Parámetros con nombre y valores por defecto
mostrar_datos("Nacho", "Iborra", 7)
mostrar_datos("Juan", "Pérez")
mostrar_datos("Ana")
mostrar_datos("Mario", dia=10)
mostrar_datos(apellidos="Pérez", dia=15, nombre="Laura")

# Parámetros variables
total = sumar_numeros(1, 2, 3, 4, 5)
print("Suma total =", total)
total2 = sumar_numeros(10)
print("Suma total =", total2)
mostrar_notas(nacho=8, ana=6, juan=9)

funcion_pendiente()