'''
Uso básico de TKinter
Contenedores y gestor de geometría
'''

import tkinter as tk

ventana = tk.Tk()
ventana.title("Ventana con contenedores")
ventana.geometry("800x600+100+200")

# Contenedores

f1 = tk.LabelFrame(ventana, text="Frame 1", background='white', 
    width='500', height='150')
f1.pack(pady = 10)
f1.pack_propagate(False)

f2 = tk.Frame(ventana, background='yellow', width='500', height='150')
f2.pack(ipadx = 50, pady = 10)
f2.grid_propagate(False)

f3 = tk.LabelFrame(ventana, text="Frame 3", background='green', 
    width='500', height='150')
f3.pack()

# Gestor "pack" sobre primer frame

l1 = tk.Label(f1, text="Etiqueta 1", background='black', foreground='white')
l1.pack(fill = tk.X, side = tk.LEFT)
l2 = tk.Label(f1, text="Etiqueta 2", background='blue', foreground='white')
l2.pack(side = tk.LEFT)
l3 = tk.Label(f1, text="Etiqueta 3", background='green', foreground='white')
l3.pack(expand = True, side = tk.LEFT)
l4 = tk.Label(f1, text="Etiqueta 4", background='red', foreground='white')
l4.pack(anchor = tk.W, side = tk.LEFT)

# Gestor "grid" sobre segundo frame

l5 = tk.Label(f2, text="Etiqueta 5", background='black', foreground='white')
l5.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
l6 = tk.Label(f2, text="Etiqueta 6", background='blue', foreground='white')
l6.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
l7 = tk.Label(f2, text="Etiqueta 7", background='green', foreground='white')
l7.grid(row=1, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")
l8 = tk.Label(f2, text="Etiqueta 8", background='red', foreground='white')
l8.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")
l9 = tk.Label(f2, text="Etiqueta 9", background='white')
l9.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
l10 = tk.Label(f2, text="Etiqueta 10", background='white')
l10.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

# Gestor "place" sobre tercer frame

l11 = tk.Label(f3, text="Etiqueta 11", background='black', foreground='white')
l11.place(x = 50, y = 10)
l12 = tk.Label(f3, text="Etiqueta 12", background='blue', foreground='white')
l12.place(relx = 0.5, rely = 0.5)
l13 = tk.Label(f3, text="Etiqueta 13", background='red', foreground='white')
l13.place(relx=0.5, rely=0.9, anchor = tk.S)

ventana.mainloop()