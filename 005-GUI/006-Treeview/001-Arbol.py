import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("800x800")

arbol = ttk.Treeview()
arbol.pack(padx=50,pady=50)


ventana.mainloop()
