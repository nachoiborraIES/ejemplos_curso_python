'''
Funciones específicas para listas con expresiones lambda
'''

libros = [
    ("El juego de Ender", 7.95),
    ("El señor de los Anillos", 11.15),
    ("La tabla de Flandes", 6.58),
]

# Ordenación de listas de datos complejos

libros.sort(key=lambda x: x[1], reverse=True)
print(libros)

# Mapear valores de una lista

titulos = list(map(lambda x: x[0], libros))
print(titulos)

numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

# Filtrar valores

libros_menos_10 = list(filter(lambda x: x[1] < 10, libros))
print(libros_menos_10)