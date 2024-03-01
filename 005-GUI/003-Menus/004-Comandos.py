import tkinter as tk
import sys

def salir():
    sys.exit()

ventana = tk.Tk()

menu = tk.Menu(ventana)
ventana.config(menu=menu)

archivo = tk.Menu(menu)
menu.add_cascade(label="Archivo",menu=archivo)

archivo.add_command(label="Salir",command=salir)

editar = tk.Menu(menu)
menu.add_cascade(label="Editar",menu=editar)

tablas = tk.Menu(menu)
menu.add_cascade(label="Tablas",menu=tablas)

ayuda = tk.Menu(menu)
menu.add_cascade(label="Ayuda",menu=ayuda)


ventana.mainloop()
