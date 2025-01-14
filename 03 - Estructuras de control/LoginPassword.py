'''
Programa que le pide al usuario su login y su password repetidamente
hasta que escriba los correctos: login "admin" y password "1234"
'''

login = ""
password = ""

while login != 'admin' or password != '1234':
    login = input("Login: ")
    password = input("Password: ")

print("Credenciales correctas")