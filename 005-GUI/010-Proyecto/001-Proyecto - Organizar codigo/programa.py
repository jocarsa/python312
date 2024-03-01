import tkinter as tk
from tkinter import ttk

from importaciones.interfaz import *

ventana = tk.Tk()
configurarVentana(ventana)
marco = ttk.Frame(ventana)
miMenu(ventana,marco)
marcoInsertar(marco)

ventana.mainloop()
