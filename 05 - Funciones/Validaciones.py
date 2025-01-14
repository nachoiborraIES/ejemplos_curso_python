# Programa que valida datos de distintos tipos usando captura y 
# propagación de excepciones

def pedir_entero(n1, n2):
    correcto = False
    resultado = 0
    while not correcto:
        try:
            resultado = int(input())
            if resultado >= n1 and resultado <= n2:
                correcto = True
            else:
                print("Valor incorrecto")                
        except:
            print("Número incorrecto")
    return resultado

def pedir_texto():
    resultado = input()
    if resultado == "":
        raise Exception("El texto no puede estar vacío")
    return resultado

# Programa principal

print("Escribe tu edad:")
edad = pedir_entero(18, 60)
try:
    print("Dime tu nombre:")
    nombre = pedir_texto()
    print(f"Hola {nombre}, tienes {edad} años")
except Exception as e:
    print("Error:", str(e))
