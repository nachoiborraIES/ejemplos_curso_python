# Programa que usa Pillow para redimensionar la imagen que diga el usuario

from PIL import Image

fichero_imagen = input("Indica la imagen a procesar: ")

try:
    imagen = Image.open(fichero_imagen)
    imagen_redimensionada = imagen.resize((50, 50))
    imagen_redimensionada.save("50_50_" + fichero_imagen)
except:
    print("Error procesando imagen")
