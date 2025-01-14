# Aplicacion TKinter con una calculadora sencilla
# Añadimos colores y tamaños a algunos controles

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

# El botón tiene fondo azul y tamaño algo más grande
btn_calcular = tk.Button(ventana, text="Calcular", background="#61dbf1",
    width=10, height=2)
btn_calcular.pack()
# La etiqueta tiene texto verde algo más grande de lo normal
lbl_resultado = tk.Label(ventana, text='Resultado', foreground="green",
    font=("Arial", 12))
lbl_resultado.pack()

ventana.mainloop()
