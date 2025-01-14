# Aplicacion TKinter con una calculadora sencilla

import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Calculadora')
ventana.geometry('400x250+200+200')

# Etiquetas y cuadros de texto
lbl_numero1 = tk.Label(ventana, text="Número 1")
txt_numero1 = tk.Entry(ventana)
lbl_numero2 = tk.Label(ventana, text="Numero 2")
txt_numero2 = tk.Entry(ventana)
lbl_numero1.pack()
txt_numero1.pack()
lbl_numero2.pack()
txt_numero2.pack()

# Desplegable con operaciones

lbl_operaciones = tk.Label(ventana, text="Operación")
lbl_operaciones.pack()
operaciones = ttk.Combobox(ventana)
operaciones['values'] = ['+', '-', '*', '/']
operaciones.pack()

# Botón de calcular y resultado

btn_calcular = tk.Button(ventana, text="Calcular")
btn_calcular.pack()
lbl_resultado = tk.Label(ventana, text='Resultado')
lbl_resultado.pack()

ventana.mainloop()
