# Programa que gestiona una lista de libros almacenada en un fichero de texto

import os

fichero = 'libros.txt'

def cargar_libros():
    global fichero
    libros = list()
    if os.path.exists(fichero):
        with open(fichero, "r", encoding="UTF-8") as lectura:
            for linea in lectura:
                partes = linea.strip().split(';')
                libros.append((partes[0], partes[1]))
    return libros

def guardar_libros(lista):
    global fichero
    with open(fichero, "w", encoding="UTF-8") as escritura:
        for libro in lista:
            escritura.write(f"{libro[0]};{libro[1]}\n")

# Programa principal

libros = cargar_libros()
respuesta = "s"

while respuesta.lower() == "s":
    respuesta = input("Quieres añadir más libros? (S/N): ").lower()
    if respuesta == "s":
        titulo = input("Título del nuevo libro: ")
        autor = input("Autor del libro: ")
        libros.append((titulo, autor))

print("Listado actual de libros:")
for libro in libros:
    print(f"{libro[0]} ({libro[1]})")

guardar_libros(libros)