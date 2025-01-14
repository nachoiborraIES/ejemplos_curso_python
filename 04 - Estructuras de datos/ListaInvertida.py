# Programa que invierte una lista de nombres separados por comas

print ("Escribe los nombres separados por comas:")
nombres = input().split(",")
nombres.reverse()
print(','.join(nombres))
