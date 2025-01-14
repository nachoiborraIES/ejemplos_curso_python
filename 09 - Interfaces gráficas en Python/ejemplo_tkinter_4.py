'''
Uso básico de TKinter
Eventos y cuadros de diálogo
'''

import tkinter as tk
from tkinter import messagebox, filedialog

def aceptar():
    texto_aceptar.set("Has pulsado Aceptar")

def entrada_raton(evento):
    lbl_evento_mouse.configure(bg='green')

def salida_raton(evento):
    lbl_evento_mouse.configure(bg='red')

def mensaje():
    messagebox.showwarning("Cuidado", "Has pulsado un botón de la aplicación")

def abrir():
    nombre_fichero = filedialog.askopenfile(initialdir='.', title="Elige fichero",
        filetypes=(("Ficheros Python", "*.py"),))
    if nombre_fichero:
        texto_fichero.set(nombre_fichero.name)

ventana = tk.Tk()
ventana.title("Prueba de eventos")
ventana.geometry("600x400+100+200")

btn_aceptar = tk.Button(ventana, text="Aceptar", command=aceptar)
texto_aceptar = tk.StringVar()
lbl_aceptar = tk.Label(ventana, text="", textvariable=texto_aceptar)
btn_aceptar.pack()
lbl_aceptar.pack()

lbl_evento_mouse = tk.Label(ventana, text="Etiqueta de prueba", bg='red')
lbl_evento_mouse.bind('<Enter>', entrada_raton)
lbl_evento_mouse.bind('<Leave>', salida_raton)
lbl_evento_mouse.pack()

btn_mensaje = tk.Button(ventana, text="Mostrar mensaje", command=mensaje)
btn_mensaje.pack()

btn_abrir_fichero = tk.Button(ventana, text="Abrir fichero", command=abrir)
texto_fichero = tk.StringVar()
lbl_nombre_fichero = tk.Label(ventana, text="", textvariable=texto_fichero)
btn_abrir_fichero.pack()
lbl_nombre_fichero.pack()

ventana.mainloop()