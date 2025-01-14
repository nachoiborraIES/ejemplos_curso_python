# Programa que rellena una lista con los números que escribe el usuario y 
# luego le indica en qué posiciones está el número que él diga

numeros = list()
print ("Escribe números. Escribe 0 para terminar")
numero = int(input())
while numero != 0:
    numeros.append(numero)
    numero = int(input())

numeroABuscar = int(input("Indica el número que quieres buscar:\n"))
veces = 0
for i in range(0, len(numeros)):
    if numeros[i] == numeroABuscar:
        print("Encontrado en posición", i+1)
        veces += 1
if veces == 0:
    print("Número no encontrado")