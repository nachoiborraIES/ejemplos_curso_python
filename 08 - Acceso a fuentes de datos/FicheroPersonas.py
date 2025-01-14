# Programa que lee datos personales de un fichero y muestra por pantalla
# los datos de la persona más vieja y más joven

fichero = open("personas.txt", "r")
lineas = fichero.readlines()
personas = list()

# Almacenamos datos en una lista (nombre y edad)
for linea in lineas:
    datos = linea.split(';')
    if len(datos) == 2:
        personas.append([datos[0], int(datos[1])])

fichero.close()

# Buscar persona más joven y más vieja  
personas.sort(key=lambda x: x[1])
print("Persona más joven: %s (%d años)" % (personas[0][0], personas[0][1]))
print("Persona más vieja: %s (%d años)" % (personas[-1][0], personas[-1][1]))
