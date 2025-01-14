'''
Ejemplo de uso del bucle while
'''

n = 1
while n <= 10:
    print(n)
    n += 1
print("Fin del programa")

n = int(input("Escribe un número positivo: "))
while n >= 0:
    n = int(input("Escribe un número positivo: "))
print("Has escrito un número negativo")
