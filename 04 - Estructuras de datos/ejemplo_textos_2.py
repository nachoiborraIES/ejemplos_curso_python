'''
Uso avanzado de cadenas de texto
'''

texto = "Hola, buenos días"

# Paso a mayúsculas/minúsculas
texto_mayus = texto.upper()
print(texto_mayus)
texto_minus = texto.lower()
print(texto_minus)

# Reemplazar texto
texto_replace1 = texto.replace("Hola", "Saludos")
print(texto_replace1)
texto_replace2 = texto.replace("o", "a")
print(texto_replace2)

# Separar y unir textos
partes = texto.split(" ")
print(partes)
texto_unido = "-".join(partes)
print(texto_unido)

# Extraer subcadenas
subcadena1 = texto[6:12]
print(subcadena1)
subcadena2 = texto[texto.index('buenos'):texto.index('buenos') + len('buenos')]
print(subcadena2)
subcadena3 = texto[-11:-5]
print(subcadena3)

# Limpiar textos
texto2 = "     Hola, buenas tardes   "
texto_limpio = texto2.strip()
print(texto_limpio)