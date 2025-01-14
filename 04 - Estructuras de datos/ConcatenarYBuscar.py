'''
Ejercicio que le pide al usuario tres textos, los concatena y busca:
- Cuántas "a" minúscula hay en todo el texto enlazado
- En qué posición aparece por primera vez la palabra "Python"
'''

texto = ""
print("Escribe 3 textos:")
for n in range(3):
    texto = texto + input()
print("Has escrito:", texto)

# Contar "a" minúsculas
total_a = 0
for letra in texto:
    if letra == 'a':
        total_a += 1
print("Total de letras a minúscula:", total_a)

# En qué posición aparece por primera vez "Python"
posicion = texto.find("Python")
if posicion >= 0:
    print("El texto Python está en la posición", posicion)
else:
    print("No se encuentra el texto Python")