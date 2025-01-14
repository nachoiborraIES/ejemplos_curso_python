'''
Uso básico de Pillow
'''

from PIL import Image

imagen = Image.open('logo_python.png')

imagen_rotada = imagen.rotate(45)

imagen_rotada.save('logo_rotado.png')