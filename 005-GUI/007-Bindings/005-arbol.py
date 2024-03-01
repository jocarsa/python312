import tkinter as tk
from tkinter import ttk

def arbolSeleccionado(event):
    seleccionado = arbol.selection()[0]
    print("El registro seleccionado es:",seleccionado)
    valores = arbol.item(seleccionado, "values")
    print("Sus valores son:", valores)

ventana = tk.Tk()
ventana.geometry("800x800")

arbol = ttk.Treeview()
arbol.pack(padx=50,pady=50)

arbol["columns"] = ("1", "2", "3")

arbol.heading("#0", text="Identificador")
arbol.heading("1", text="Nombre")
arbol.heading("2", text="Email")
arbol.heading("3", text="Teléfono")

arbol.insert("", tk.END, text="0", values=("Jose Vicente", "info@jocarsa.com", "452354"))
arbol.insert("", tk.END, text="1", values=("Juan", "Juan@jocarsa.com", "5235235"))
arbol.insert("", tk.END, text="2", values=("Jorge", "Jorge@jocarsa.com", "234534534"))

arbol.bind("<<TreeviewSelect>>", arbolSeleccionado)

ventana.mainloop()
