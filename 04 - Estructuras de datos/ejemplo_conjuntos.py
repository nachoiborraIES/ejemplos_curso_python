'''
Uso de conjuntos
'''

# Operaciones básicas: crear, añadir, borrar, buscar, listar

conjunto_1 = set(["Uno", "Dos", "Tres", "Uno"])
print(conjunto_1)

conjunto_1.add("Cuatro")
conjunto_1.add("Dos")
print(conjunto_1)

conjunto_1.remove("Tres")
print(conjunto_1)
conjunto_1.discard("Cinco")
print(conjunto_1)

if "Uno" in conjunto_1:
    print("Uno está en el conjunto")

for elemento in conjunto_1:
    print(elemento)

# Operaciones específicas de conjuntos

conjunto_1 = set(["Uno", "Dos", "Tres", "Cuatro"])
conjunto_2 = set(["Cuatro", "Cinco", "Seis"])
conjunto_3 = set(["Uno", "Dos"])

union = conjunto_1.union(conjunto_2)
print(union)

interseccion = conjunto_1.intersection(conjunto_2)
print(interseccion)

diferencia = conjunto_1.difference(conjunto_3)
print(diferencia)

if conjunto_3.issubset(conjunto_1):
    print("C3 es subconjunto de C1")

if conjunto_1.issuperset(conjunto_3):
    print("C1 es superconjunto de C3")