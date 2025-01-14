'''
Algunas opciones adicionales sobre los controles de Tkinter
'''

import tkinter as tk
from PIL import Image, ImageTk

def nuevo():
    print("Menú Nuevo")

def abrir():
    print("Menú Abrir")

ventana = tk.Tk()
ventana.title("Ventana de prueba")
ventana.geometry("600x400+100+200")

# Imágenes

imagen = ImageTk.PhotoImage(Image.open('python.png').resize((200, 200)))
lbl_imagen = tk.Label(ventana)
lbl_imagen.configure(image=imagen)
lbl_imagen.pack()

# Menús

menu = tk.Menu(ventana)
ventana.config(menu = menu)

menu_archivo = tk.Menu(menu, tearoff=False)
menu_editar = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Archivo", menu=menu_archivo)
menu.add_cascade(label="Editar", menu=menu_editar)

menu_archivo.add_command(label="Nuevo", command=nuevo)
menu_archivo.add_command(label="Abrir", command=abrir)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)

# Colores y fuentes

etiqueta = tk.Label(ventana, text='Etiqueta', 
    background='blue', foreground='white', font=('Arial', 20), 
    width=20, height=10)
etiqueta.pack()

ventana.mainloop()