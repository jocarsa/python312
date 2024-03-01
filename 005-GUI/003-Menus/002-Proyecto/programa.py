import tkinter as tk

def hazNada():
    pass

ventana = tk.Tk()
ventana.title("Programa de gestión v0.2")
ventana.geometry("600x600+20+20")
ventana.iconbitmap("../../jv.ico")

menu = tk.Menu(ventana)
ventana.config(menu=menu)

tablas = tk.Menu(menu)
menu.add_cascade(label="Tablas",menu=tablas)
tablas.add_command(label="Clientes",command=hazNada)

ventana.mainloop()
