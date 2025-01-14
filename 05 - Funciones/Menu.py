# Programa que muestra repetidamente un menú de opciones al usuario
# empleando una función "menu"

def menu():
    print("1. Dar los buenos días")
    print("2. Dar las buenas tardes")
    print("3. Terminar")

# Programa principal
opcion = 0
while opcion != 3:
    menu()
    print("Elige una opción del menú:")
    opcion = int(input())
    if opcion == 1:
        print("Buenos días")
    elif opcion == 2:
        print("Buenas tardes")
