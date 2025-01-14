'''
Ejemplo sencillo de consulta sobre BD de contactos
'''

import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="contactos"
)

cursor = bd.cursor()
edad_max = int(input("Elige la edad máxima de filtrado: "))

sql = "SELECT nombre, telefono, edad FROM contactos WHERE edad < %s"
valores = (edad_max,)
cursor.execute(sql, valores)
resultados = cursor.fetchall()
for r in resultados:
    print("Nombre:", r[0])
    print("Telefono:", r[1])
    print("Edad:", r[2])

cursor.close()
bd.close()