'''
Uso de tuplas
'''

datos_personales = ("Nacho", 611223344, "C/Mayor 12")
print(datos_personales[1])
nombre, telefono, direccion = datos_personales
print(nombre)

tupla = 1, 5, 10
print(tupla[2])
# Error: tupla[0] = 0
print(5 in tupla)       # True
print(max(tupla))       # 10
print(len(tupla))       # 3