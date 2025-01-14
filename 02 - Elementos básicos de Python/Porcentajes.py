'''
Programa que calcula el porcentaje de perros y gatos en una protectora
según la información introducida por el usuario
'''

perros = int(input("Indica la cantidad de perros: "))
gatos = int(input("Indica la cantidad de gatos: "))

total = perros + gatos
porcentaje_perros = 100 * perros / total
porcentaje_gatos = 100 * gatos / total

print(f"Porcentaje de perros: {porcentaje_perros: .2f}%")
print(f"Porcentaje de gatos: {porcentaje_gatos: .2f}%")
# print("Porcentaje de gatos: %.2f%%" % (porcentaje_gatos))
