'''
Paso de parámetros a funciones y tipos de retorno
'''

def saludar(nombre):
    print("Hola,", nombre)

def mostrar_suma(n1, n2):
    print(f"La suma de {n1} y {n2} es {n1+n2}")

def calcular_suma(n1, n2):
    resultado = n1 + n2
    return resultado

saludar("Nacho")
saludar("Ana")
mostrar_suma(7, 3)
mostrar_suma(20, 30)
num1 = int(input("Escribe un número: "))
num2 = int(input("Escribe otro número: "))
mostrar_suma(num1, num2)
suma = calcular_suma(7, 1)
print("La suma de la función calcular_suma es", suma)
print("Otro ejemplo de calcular_suma:", calcular_suma(10, 9))