# Aplicacion TKinter con una calculadora sencilla
# Añadimos la gestión de eventos
# Añadimos la encapsulación en una clase

import tkinter as tk
from tkinter import ttk, messagebox

class Calculadora(tk.Frame):
    
    def __init__(self, ventana):
        super().__init__(ventana)
        self.master = ventana
        self.pack()
        self.crear_elementos()
    
    def crear_elementos(self):

        # Etiquetas y cuadros de texto

        lbl_numero1 = tk.Label(ventana, text="Número 1")
        self.txt_numero1 = tk.Entry(ventana)
        lbl_numero2 = tk.Label(ventana, text="Numero 2")
        self.txt_numero2 = tk.Entry(ventana)
        lbl_numero1.pack()
        self.txt_numero1.pack()
        lbl_numero2.pack()
        self.txt_numero2.pack()

        # Desplegable con operaciones

        lbl_operaciones = tk.Label(ventana, text="Operación")
        lbl_operaciones.pack()

        self.operacion_seleccionada = tk.StringVar()
        operaciones = ttk.Combobox(ventana, textvariable=self.operacion_seleccionada)
        operaciones['values'] = ['+', '-', '*', '/']
        operaciones.pack()

        # Botón de calcular y resultado

        btn_calcular = tk.Button(ventana, text="Calcular", background="#61dbf1",
            width=10, height=2, command=self.calcular)
        btn_calcular.pack()

        self.resultado_operacion = tk.StringVar()
        lbl_resultado = tk.Label(ventana, textvariable=self.resultado_operacion,
            foreground="green", font=("Arial", 12))
        lbl_resultado.pack()

    def calcular(self):
        numero1 = self.txt_numero1.get()
        numero2 = self.txt_numero2.get()
        operacion = self.operacion_seleccionada.get()
        if numero1 == '' or numero2 == '' or operacion == '':
            messagebox.showerror("Error", "Los campos no pueden estar vacíos")
        else:
            if operacion == '+':
                self.resultado_operacion.set(int(numero1) + int(numero2))
            elif operacion == '-':
                self.resultado_operacion.set(int(numero1) - int(numero2))
            elif operacion == '*':
                self.resultado_operacion.set(int(numero1) * int(numero2))
            elif operacion == '/':
                self.resultado_operacion.set(int(numero1) / int(numero2))

# Programa principal

ventana = tk.Tk()
ventana.title('Calculadora')
ventana.geometry('400x250+200+200')
c = Calculadora(ventana)
ventana.mainloop()
