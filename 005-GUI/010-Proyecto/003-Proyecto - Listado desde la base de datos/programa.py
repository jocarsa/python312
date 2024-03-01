import tkinter as tk
from tkinter import ttk

from importaciones.interfaz import *

ventana = tk.Tk()
configurarVentana(ventana)
marco = ttk.Frame(ventana)
marcolistado = ttk.Frame(ventana)
miMenu(ventana,marco,marcolistado)
marcoInsertar(marco,marcolistado)
marcoListado(marco,marcolistado)

ventana.mainloop()
