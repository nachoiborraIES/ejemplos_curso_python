# Programa que procesa una lista de contactos para ordenarlos y filtrarlos
# empleando expresiones lambda

contactos = [
    { 'nombre': 'Nacho', 'edad': 45, 'telefono': '611223344' },
    { 'nombre': 'Juan', 'edad': 70, 'telefono': '961234567' },
    { 'nombre': 'Ana', 'edad': 40, 'telefono': '699887766' }
]

contactos.sort(key=lambda x: x['edad'])
print("Contactos ordenados por edad:")
print(contactos)

contactos_mas_40 = list(filter(lambda x: x['edad'] > 40, contactos))
print("Contactos mayores de 40:")
print(contactos_mas_40)