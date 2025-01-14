'''
Programa que le pide 3 notas al usuario y le muestra un mensaje u otro según si llegan al 5 o no
'''

n1 = int(input("Nota 1: "))
n2 = int(input("Nota 2: "))
n3 = int(input("Nota 3: "))

if n1 >= 5 and n2 >= 5 and n3 >= 5:
    print("Has aprobado")
elif n1 >= 5 or n2 >= 5 or n3 >= 5:
    print("No se sabe si has aprobado o has suspendido")
else:
    print("Has suspendido")

'''
elif n1 < 5 and n2 < 5 and n3 < 5:
    print("Has suspendido")
'''