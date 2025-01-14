'''
Programa que cuenta desde el primer número que diga el usuario hasta
el segundo
'''

num1 = int(input("Escribe el primer número: "))
num2 = int(input("Escribe el segundo número: "))

if num1 < num2:
    for n in range(num1, num2 + 1):
        print(n)
else:
    for n in range(num1, num2 - 1, -1):
        print(n)
