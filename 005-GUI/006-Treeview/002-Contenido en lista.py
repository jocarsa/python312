import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("800x800")

arbol = ttk.Treeview()
arbol.pack(padx=50,pady=50)

arbol["columns"] = ("1", "2", "3")

arbol.heading("#0", text="Identificador")
arbol.heading("1", text="Nombre")
arbol.heading("2", text="Email")
arbol.heading("3", text="Teléfono")


ventana.mainloop()
