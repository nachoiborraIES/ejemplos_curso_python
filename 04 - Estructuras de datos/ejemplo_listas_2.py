'''
Uso avanzado de listas
'''

lista1 = [1, 2]
lista2 = [3, 4]

# Concatenar y multiplicar
lista_concatenada = lista1 + lista2
print(lista_concatenada)                # [1, 2, 3, 4]
lista_multiplicada = lista1 * 3
print(lista_multiplicada)               # [1, 2, 1, 2, 1, 2]

# Conteos, máximos y mínimos
print(max(lista_concatenada))           # 4
print(min(lista_concatenada))           # 1
print(lista_multiplicada.count(2))      # 3

# Búsquedas
if 3 in lista_concatenada:
    print("El 3 está en la lista")
if 5 in lista_concatenada:
    print("El 5 está en la lista")

print(lista_multiplicada.index(2))      # 1
print(lista_multiplicada.index(2, 2))   # 3

# Ordenaciones
lista_multiplicada.sort()
print(lista_multiplicada)               # [1, 1, 1, 2, 2, 2]
lista_multiplicada.sort(reverse=True)
print(lista_multiplicada)               # [2, 2, 2, 1, 1, 1]
copia_lista = sorted(lista_concatenada, reverse=True)
print(lista_concatenada)                # [1, 2, 3, 4]
print(copia_lista)                      # [4, 3, 2, 1]

# Inversiones
lista = [1, 5, 7, 10]
lista.reverse()
print(lista)                            # [10, 7, 5, 1]
copia_invertida = lista[::-1]
print(lista)                            # [10, 7, 5, 1]
print(copia_invertida)                  # [1, 5, 7, 10]

# Copias y sublistas
copia_lista = lista.copy()
sublista1 = copia_lista[1:3]
print(sublista1)                        # [7, 5]
sublista2 = copia_lista[1:]
print(sublista2)                        # [7, 5, 1]
sublista3 = copia_lista[:2]
print(sublista3)                        # [10, 7]
sublista4 = copia_lista[:]
print(sublista4)                        # [10, 7, 5, 1]

# List comprehension

# Múltiplos de 5 y 7 entre el 0 y el 100
multiplos = [x for x in range(101) if x % 5 == 0 and x % 7 == 0]
print(multiplos)
# Números del 1 al 10
secuencia = list(range(1, 11))
print(secuencia)

# Listas multidimensionales
datos = [
    ["Nacho", 40, 185],
    ["Ana", 45, 178]
]

print(datos[0][1])          # 40
print(len(datos))           # 2 listas
print(len(datos[0]))        # 3