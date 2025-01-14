'''
Funciones específicas para listas
'''

def ordenar_por_precio(libro):
    return libro[1]

def obtener_nombre(libro):
    return libro[0]

def cuadrado(numero):
    return numero ** 2

def libros_baratos(libro):
    return libro[1] < 10

libros = [
    ("El juego de Ender", 7.95),
    ("El señor de los Anillos", 11.15),
    ("La tabla de Flandes", 6.58),
]

# Ordenación de listas de datos complejos

libros.sort(key=ordenar_por_precio, reverse=True)
print(libros)

# Mapear valores de una lista

titulos = list(map(obtener_nombre, libros))
print(titulos)

numeros = [1, 2, 3, 4]
cuadrados = list(map(cuadrado, numeros))
print(cuadrados)

# Filtrar valores

libros_menos_10 = list(filter(libros_baratos, libros))
print(libros_menos_10)