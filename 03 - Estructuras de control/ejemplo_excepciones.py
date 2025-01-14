'''
Ejemplo de uso de excepciones
Tomamos como base un programa que le pide al usuario dos números e intenta dividirlos
'''

try:
    a = int(input("Introduce el valor de a: "))
    b = int(input("Introduce el valor de b: "))
    if b == 0:
        raise Exception("No se puede dividir entre cero")
    resultado = a / b
    print(f"La división de {a} entre {b} es {resultado:.2f}")
except Exception as e:
    print("Error:", str(e))

print("Fin del programa")
