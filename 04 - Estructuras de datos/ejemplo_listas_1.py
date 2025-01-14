'''
Uso básico de listas
'''

# Definición de listas
lista1 = list()
lista2 = ["Nacho", 14, "Juan", 70]

# Acceso a los elementos
print(lista2[0])        # "Nacho"
lista2[1] = 20
print(lista2)           # ["Nacho" 20 "Juan" 70]
print(lista2[-1])       # 70

# Añadir/Insertar elementos
lista1.append(3)
lista1.append(7)
lista1.append(2)
print(lista1)           # [3, 7, 2]
lista1.insert(1, 10)    
print(lista1)           # [3, 10, 7, 2]
lista1.extend([8, 4])
print(lista1)           # [3, 10, 7, 2, 8, 4]

# Borrado de elementos
lista1.append(7)        # [3, 10, 7, 2, 8, 4, 7]
lista1.remove(7)        
print(lista1)           # [3, 10, 2, 8, 4, 7]
del lista1[3]
print(lista1)           # [3, 10, 2, 4, 7]
valor = lista1.pop(0)
print("Eliminado el valor", valor)
print(lista1)           # [10, 2, 4, 7]
lista1.clear()
print(lista1)           # []

# Recorrido de listas
print("Recorrido 1 de lista2:")
for elemento in lista2:
    print(elemento)

print ("Recorrido 2 de lista2:")
for i in range(0, len(lista2)):
    print(lista2[i])