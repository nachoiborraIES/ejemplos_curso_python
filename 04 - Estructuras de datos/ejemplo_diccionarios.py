'''
Uso de diccionarios o mapas
'''

# Definición y acceso a elementos

datos_personales = {
    'nombre': 'Nacho',
    'edad': 46,
    'telefono': '611223344'
}

print(datos_personales['edad'])     # 46
datos_personales['edad'] = 47

productos = {}
productos['22B'] = ('22B', 'Monitor', 'Benq', 103.45)
productos['11A'] = ('11A', 'Teclado', 'Logitech', 10.25)
productos['33C'] = ('33C', 'Impresora', 'HP', 201.95)

print(productos['33C'][3])          # 201.95
if '44D' in productos:
    print(productos['44D'][0])
else:
    print("El producto 44D no se encuentra")

print(productos.get('44D', 'El producto no se encuentra'))

# Recorrido de elementos

print("El catálogo de productos tiene", len(productos), "elementos")

print("Recorrido por clave")
for clave in productos:
    print(productos[clave][1])

print("Recorrido por valores")
for valor in productos.values():
    print(valor[1])

print("Recorrido por clave y valor")
for clave, valor in productos.items():
    print(valor[1])

# Ordenar diccionarios

print("Productos ordenados por clave")
for clave in sorted(productos.keys()):
    print(productos[clave])

# Borrar elementos del diccionario

del productos['11A']
print("Productos tras borrar 11A:")
print(productos)
producto_borrado = productos.pop('22B')
print("Productos tras borrar 22B")
print(productos)
print("Se ha borrado:", producto_borrado)

# Listas de diccionarios

contactos = list()
contactos.append({
    'nombre': 'Pepe',
    'edad': 60,
    'telefono': '699887766'
})
contactos.append({
    'nombre': 'Ana',
    'edad': 40,
    'telefono': '612345678'
})

print(contactos[0]['telefono'])     # 699887766

# Diccionarios con listas

pizza1 = {
    'nombre': 'Barbacoa',
    'precio': 17.05,
    'ingredientes': ['Mozarella', 'Salsa barbacoa', 'Carne']
}

print(pizza1['ingredientes'][1])    # Salsa barbacoa

# Diccionarios con diccionarios

contacto = {
    'nombre': 'Juan',
    'edad': 70,
    'telefono': '612983746',
    'direccion': {
        'calle': 'C/Mayor',
        'numero': 10,
        'piso': 3,
        'puerta': 'A'
    }
}

print(contacto['direccion']['piso'])    # 3