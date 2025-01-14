'''
Programa que discrimina el login del usuario para mostrarle un mensaje u otro
'''

login = input("Introduce tu login: ")

if login == 'admin':
    print("Tienes permisos de administrador")
elif login == 'user':
    print("Tienes permisos de usuario")
else:
    print("No tienes permisos de acceso a la aplicación")