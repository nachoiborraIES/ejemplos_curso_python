'''
Uso de módulos incorporados en Python
'''

# Módulo con propiedades del sistema
import os
# Módulo con componentes matemáticos. Incorporamos sólo la constante PI y 
# la raíz cuadrada
from math import pi, sqrt

print("Carpeta actual:", os.path.abspath(os.getcwd()))
print(pi)
print(sqrt(81))