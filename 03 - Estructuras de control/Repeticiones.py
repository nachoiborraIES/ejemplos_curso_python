'''
Programa que escribe textos las veces que diga el usuario.
El programa termina cuando el usuario escriba un texto vacío
'''

texto = " "

while texto != "":
    texto = input("Escribe un texto: ")
    if texto != "":
        veces = int(input("Indica las veces que hay que repetirlo: "))
        for n in range(veces):
            print(texto, end="")
        print()
