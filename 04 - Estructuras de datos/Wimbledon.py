# Programa que usa conjuntos para determinar los ganadores de las últimas
# 10 ediciones del torneo de Wimbledon masculino, sin mostrar repetidos

ganadores = set()

print("Escribe los nombres de los últimos 10 ganadores de Wimbledon:")
for i in range(10):
    ganadores.add(input())

print("Listado de ganadores sin repetir:")
for tenista in ganadores:
    print(tenista)
