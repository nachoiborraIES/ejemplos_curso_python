# Programa que procesa una lista de contactos para ordenarlos y filtrarlos

def ordenar_edad(contacto):
    return contacto['edad']

def mayores_40(contacto):
    return contacto['edad'] > 40

contactos = [
    { 'nombre': 'Nacho', 'edad': 45, 'telefono': '611223344' },
    { 'nombre': 'Juan', 'edad': 70, 'telefono': '961234567' },
    { 'nombre': 'Ana', 'edad': 40, 'telefono': '699887766' }
]

contactos.sort(key=ordenar_edad)
print("Contactos ordenados por edad:")
print(contactos)

contactos_mas_40 = list(filter(mayores_40, contactos))
print("Contactos mayores de 40:")
print(contactos_mas_40)