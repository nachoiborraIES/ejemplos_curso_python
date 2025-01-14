'''
Lanzamiento de excepciones desde funciones
'''

def pedir_precio():
    print("Escribe el precio del articulo")
    try:
        precio = int(input())
        if precio <= 0:
            raise Exception()
        return precio
    except:
        raise Exception("Precio invalido")

# Programa principal

try:
    precio_usuario = pedir_precio()
    print("El precio introducido es de", precio_usuario)
except Exception as e:
    print("Error:", str(e))