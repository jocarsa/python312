import tkinter as tk

ventana = tk.Tk()

menu = tk.Menu(ventana)
ventana.config(menu=menu)

archivo = tk.Menu(menu)
menu.add_cascade(label="Archivo",menu=archivo)

editar = tk.Menu(menu)
menu.add_cascade(label="Editar",menu=editar)

tablas = tk.Menu(menu)
menu.add_cascade(label="Tablas",menu=tablas)

ayuda = tk.Menu(menu)
menu.add_cascade(label="Ayuda",menu=ayuda)


ventana.mainloop()
