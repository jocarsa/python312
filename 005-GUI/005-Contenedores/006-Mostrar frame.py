import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

def ocultar():
    marco.pack_forget()

def mostrar():
    marco.pack(padx=50,pady=50)

boton = ttk.Button(ventana,text="Oculta Frame",command=ocultar)
boton.pack()
boton2 = ttk.Button(ventana,text="Muestra Frame",command=mostrar)
boton2.pack()

marco = ttk.Frame(ventana)
marco.pack(padx=50,pady=50)

ttk.Label(marco,text="Leyenda 1").grid(row=0, column=0)
ttk.Label(marco,text="Leyenda 2").grid(row=0, column=1)
ttk.Label(marco,text="Leyenda 3").grid(row=0, column=2)

ttk.Button(marco,text="Pulsame 1").grid(row=1, column=0)
ttk.Button(marco,text="Pulsame 2").grid(row=1, column=1)
ttk.Button(marco,text="Pulsame 3").grid(row=1, column=2)




ventana.mainloop()
