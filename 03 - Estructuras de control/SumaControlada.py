'''
Programa que trata de sumar dos números introducidos por el usuario, 
avisándole si alguno no es correcto
'''

try:
    num1 = int(input("Escribe un número: "))
    num2 = int(input("Escribe otro número: "))
    if num1 < 0 or num2 < 0:
        raise Exception("Los números no pueden ser negativos")
    print("La suma es:", num1+num2)
except Exception as e:
    print("Error:", str(e))

print("Fin del programa")
