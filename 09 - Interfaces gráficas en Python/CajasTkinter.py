'''
Ejemplo de uso avanzado del gestor de geometría de Tkinter
'''

import tkinter as tk

ventana = tk.Tk()
ventana.title('Ejercicio Gestor Geometría')
ventana.geometry("300x200")

label1 = tk.Label(ventana, text='Box 1', bg="red", fg="white")
label1.pack(ipadx=10, ipady=10, fill=tk.X)

label2 = tk.Label(ventana, text='Box 2', bg="green", fg="white")
label2.pack(ipadx=10, ipady=10, fill=tk.X)

label3 = tk.Label(ventana, text='Box 3', bg="blue", fg="white")
label3.pack(ipadx=10, ipady=10, fill=tk.X)

label4 = tk.Label(ventana, text='Left', bg="cyan", fg="black")
label4.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH, side=tk.LEFT)

label5 = tk.Label(ventana, text='Center', bg="magenta", fg="black")
label5.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH, side=tk.LEFT)

label6 = tk.Label(ventana, text='Right', bg="yellow", fg="black")
label6.pack(ipadx=10, ipady=10, expand=True, fill=tk.BOTH, side=tk.LEFT)

ventana.mainloop()
