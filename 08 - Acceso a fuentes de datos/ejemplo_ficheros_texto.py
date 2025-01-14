'''
Uso de ficheros de texto
'''

lectura = open("datos.txt", "r", encoding='UTF-8')
lineas = lectura.readlines()
for linea in lineas:
    print(linea.strip())
lectura.close()

escritura = open("datos2.txt", "a")
escritura.write("CCCCC\n")
escritura.write("DDDDD\n")
escritura.close()

with open("datos.txt", "r", encoding='UTF-8') as lectura:
    for linea in lectura:
        print(linea.strip())

print("Proceso finalizado")