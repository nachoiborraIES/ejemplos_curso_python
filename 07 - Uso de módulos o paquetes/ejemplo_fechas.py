'''
Gestión de fechas y horas
'''

import datetime

# Crear fechas

fecha_actual = datetime.datetime.now()
print(fecha_actual)
fecha_actual2 = datetime.date.today()
print(fecha_actual2)
fecha_personalizada = datetime.datetime(2025, 10, 31)
print(fecha_personalizada)
fecha_personalizada2 = datetime.datetime(2026, 4, 7, 22, 30, 16)
print(fecha_personalizada2)

# Acceder a partes de la fecha

print("Mes fecha actual:", fecha_actual.month)
print("Minuto fecha personalizada:", fecha_personalizada2.minute)

# Formato de fechas

texto = input("Escribe una fecha (d/m/a):")
fecha_usuario = datetime.datetime.strptime(texto, '%d/%m/%Y')
print("Fecha procesada:", fecha_usuario)
print("Fecha personalizada", 
      datetime.datetime.strftime(fecha_personalizada2,'%d/%m/%Y %H:%M:%S'))

# Operaciones con fechas

diferencia = fecha_personalizada2 - fecha_personalizada
print(diferencia.days)
fecha_suma = fecha_actual + datetime.timedelta(days=10)
print(fecha_actual)
print(fecha_suma)