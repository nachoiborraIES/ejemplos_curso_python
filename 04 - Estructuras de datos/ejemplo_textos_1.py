'''
Uso básico de cadenas de texto
'''

# Creación y uso básico de strings o textos
texto = "Hola, buenas"
nombre = input("Dime tu nombre: ")
print("Hola,", nombre)

# Longitud de textos
print("El texto tiene", len(texto), "caracteres")

# Acceso a los caracteres del texto
print("La letra de la tercera posición es", texto[2])
for i in range(0, len(nombre)):
    print(nombre[i])
for i in nombre:
    print(i)

# Concatenar y convertir textos
print(texto + " " + nombre)
anyo = 2000
print(nombre + str(anyo))

# Buscar textos
if "buenas" in texto:
    print("El texto contiene la palabra buenas")
if "na" in texto:
    print("El texto contiene el texto na")
print("La palabra buenas está en la posición", texto.find("buenas"))
print("La palabra programa está en la posición", texto.find("programa"))

# Comparación de textos
print("hola" > "adios")
print("Hola" < "adios")