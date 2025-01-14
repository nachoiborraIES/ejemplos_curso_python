'''
Ejemplo sencillo de conexión a una base de datos MySQL
'''

import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="contactos"
)

cursor = bd.cursor()

# Inserciones
'''
sql = "INSERT INTO contactos (nombre, telefono, edad) VALUES(%s, %s, %s)"
valores = ("Pepe", "611223344", 48)
cursor.execute(sql, valores)
bd.commit()

filas_insertadas = cursor.rowcount
ultimo_id = cursor.lastrowid
if filas_insertadas > 0:
    print("Registro insertado correctamente con id = ", ultimo_id)
'''

# Borrados y modificaciones
'''
sql = "DELETE FROM contactos WHERE nombre = %s"
valores = ("Pepe", )
cursor.execute(sql, valores)
bd.commit()
print("Se han borrado", cursor.rowcount, "elementos")

sql = "UPDATE contactos SET edad=46 WHERE nombre=%s"
valores = ("Nacho Iborra", )
cursor.execute(sql, valores)
bd.commit()
print("Se han actualizado", cursor.rowcount, "elementos")
'''

# Consultas

sql = "SELECT nombre, edad FROM contactos"
cursor.execute(sql)
resultados = cursor.fetchall()
for r in resultados:
    print("Nombre:", r[0])
    print("Edad:", r[1])

# Cierre de la conexión
cursor.close()
bd.close()