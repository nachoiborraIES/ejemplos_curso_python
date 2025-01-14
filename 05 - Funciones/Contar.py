# Programa que define dos funciones:
# contar(n1, n2): muestra por pantalla un conteo desde n1 hasta n2
# mcd(n1, n2): devuelve el máximo común divisor de n1 y n2

def contar(n1, n2):
	if n1 < n2:	
		for i in range(n1, n2+1):
			print(i)
	else:
		for i in range(n1, n2-1, -1):
			print(i)

def mcd(n1, n2):
	menor = min(n1, n2)
	while n1 % menor != 0 or n2 % menor != 0:
		menor -= 1
	return menor

# Programa principal
print("Conteo de 1 a 10:")
contar(1, 10)
print("Conteo de 30 a 15")
contar(30, 15)
print("MCD de 20 y 12 =", mcd(20, 12))
print("MCD de 20 y 12 =", mcd(30, 15))
