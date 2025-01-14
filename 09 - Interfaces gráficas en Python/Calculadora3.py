# Aplicacion TKinter con una calculadora sencilla
# Definimos eventos para completar funcionamiento

import tkinter as tk
from tkinter import ttk, messagebox

def calcular():
    numero1 = txt_numero1.get()
    numero2 = txt_numero2.get()
    operacion = operacion_seleccionada.get()
    if numero1 == '' or numero2 == '' or operacion == '':
        messagebox.showerror("Error", "Los campos no pueden estar vacíos")
    else:
        if operacion == '+':
            resultado_operacion.set(int(numero1) + int(numero2))
        elif operacion == '-':
            resultado_operacion.set(int(numero1) - int(numero2))
        elif operacion == '*':
            resultado_operacion.set(int(numero1) * int(numero2))
        elif operacion == '/':
            resultado_operacion.set(int(numero1) / int(numero2))

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

operacion_seleccionada = tk.StringVar()
operaciones = ttk.Combobox(ventana, textvariable=operacion_seleccionada)
operaciones['values'] = ['+', '-', '*', '/']
operaciones.pack()

# Botón de calcular y resultado

btn_calcular = tk.Button(ventana, text="Calcular", background="#61dbf1",
    width=10, height=2, command=calcular)
btn_calcular.pack()

resultado_operacion = tk.StringVar()
lbl_resultado = tk.Label(ventana, text='Resultado', textvariable=resultado_operacion,
    foreground="green", font=("Arial", 12))
lbl_resultado.pack()

ventana.mainloop()
