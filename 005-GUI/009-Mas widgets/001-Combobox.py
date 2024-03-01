import tkinter as tk
from tkinter import ttk


ventana = tk.Tk()

desplegable = ttk.Combobox(ventana)
desplegable.pack(padx=50,pady=50)

ventana.mainloop()
