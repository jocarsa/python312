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

editar.add_command(label="Copiar",command=salir)
editar.add_command(label="Cortar",command=salir)
editar.add_command(label="Pegar",command=salir)

tablas = tk.Menu(menu)
menu.add_cascade(label="Tablas",menu=tablas)
tablas.add_command(label="Clientes",command=salir)
tablas.add_command(label="Productos",command=salir)
tablas.add_command(label="Pedidos",command=salir)

ayuda = tk.Menu(menu)
menu.add_cascade(label="Ayuda",menu=ayuda)
ayuda.add_command(label="Sobre esta aplicación",command=salir)


ventana.mainloop()
