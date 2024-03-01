import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("800x800")

boton = ttk.Button(ventana,text="Oculta Frame")
boton.place(x=250, y=50)


ventana.mainloop()
