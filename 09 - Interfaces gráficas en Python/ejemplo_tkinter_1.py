'''
Uso básico de TKinter
'''

import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ventana de prueba")
# Ventana de 600 x 400
# ubicada en x = 100, y = 200
ventana.geometry("600x400+100+200")

lbl_nombre = ttk.Label(ventana, text="Nombre:")
lbl_nombre.pack()

btn_aceptar = ttk.Button(ventana, text="Aceptar")
btn_aceptar.pack()

ventana.mainloop()