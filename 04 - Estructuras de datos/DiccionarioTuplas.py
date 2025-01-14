# Programa que almacena los datos postales de un conjunto de usuarios
# en un diccionario y luego le pide al usuario buscar uno de ellos

direcciones = {}

# Rellenamos 4 datos
for i in range(4):
    dni = input("DNI del usuario %d:\n" % (i+1))
    calle = input("Nombre de la calle:\n")
    numero = int(input("Número:\n"))
    piso = int(input("Piso:\n"))
    direcciones[dni] = (calle, numero, piso)

dniABuscar = input("Introduce un DNI a buscar:\n")
if dniABuscar in direcciones:
    print("Dirección postal:")
    print("Calle %s" % (direcciones[dniABuscar][0]))
    print("Número %d" % (direcciones[dniABuscar][1]))
    print("Piso %d" % (direcciones[dniABuscar][2]))
else:
    print("El DNI no se encuentra almacenado")

