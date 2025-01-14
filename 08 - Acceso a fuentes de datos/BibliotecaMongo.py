'''
Ejemplo de conexión y uso de bases de datos MongoDB
'''

import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017")
bd = cliente["biblioteca"]
coleccion = bd["libros"]

# Añadir documento(s)
'''
libros = [
    {'titulo': 'La tabla de Flandes', 'autor': 'Arturo Pérez Reverte',
		'paginas': 312},
    {'titulo': 'El juego de Ender', 'autor': 'Orson Scott Card',
		'paginas': 452}
]
coleccion.insert_many(libros)

otro_libro = {'titulo': 'Momo', 'autor': 'Michael Ende', 'paginas': 380}
coleccion.insert_one(otro_libro)
'''
# Borrar documento(s)
'''
coleccion.delete_one({'titulo': 'Momo'})
'''
# Actualizar documento(s)
'''
coleccion.update_one({'titulo': 'El juego de Ender'}, 
    {'$set': {'paginas': 391}})
'''

# Búsquedas

'''
resultado = coleccion.find({'titulo': 'El juego de Ender'})
for r in resultado:
    print(r)
'''

# Ampliación: insertar el libro que diga el usuario y buscar libros de
# más de 400 páginas

titulo = input("Título del nuevo libro: ")
autor = input("Autor: ")
paginas = int(input("Páginas: "))

coleccion.insert_one({'titulo': titulo, 'autor': autor, 'paginas': paginas})

libros_400 = coleccion.find({'paginas': {'$gt': 400}})
for r in libros_400:
	print(r['titulo'], r['paginas'], 'páginas')