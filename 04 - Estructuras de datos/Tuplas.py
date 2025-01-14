# Programa que almacena los datos de una dirección postal en una tupla y
# luego los muestra uno a uno

calle = input("Nombre de la calle:\n")
numero = int(input("Número:\n"))
piso = int(input("Piso:\n"))

direccion = (calle, numero, piso)

print("Dirección postal:")
print("Calle %s" % (direccion[0]))
print("Número %d" % (direccion[1]))
print("Piso %d" % (direccion[2]))

