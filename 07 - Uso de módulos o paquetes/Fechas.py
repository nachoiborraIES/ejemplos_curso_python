# Programa de cálculo con fechas

import datetime

texto = input("Dime tu fecha de nacimiento(d/m/a):\n")
fecha_nacimiento = datetime.datetime.strptime(texto, '%d/%m/%Y')

ahora = datetime.datetime.now()

# Calcular edad
edad = (ahora - fecha_nacimiento).total_seconds() // (3600 * 24 * 365)
print("Tienes", edad, "años")

# Calcular fecha del próximo cumpleaños
proximo_cumple = datetime.datetime(ahora.year, fecha_nacimiento.month, 
    fecha_nacimiento.day)
if proximo_cumple < ahora:
    proximo_cumple = datetime.datetime(ahora.year+1, fecha_nacimiento.month, 
        fecha_nacimiento.day)
print("Tu próximo cumpleaños es:", proximo_cumple.strftime('%d/%m/%Y'))

# Calcular cuántos días faltan para el próximo cumpleaños
dias_cumple = (proximo_cumple - ahora).total_seconds() // (3600 * 24)
print("Faltan", dias_cumple, "días para tu próximo cumpleaños")
