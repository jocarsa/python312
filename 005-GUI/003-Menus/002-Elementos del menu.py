import tkinter as tk

ventana = tk.Tk()

menu = tk.Menu(ventana)
ventana.config(menu=menu)

archivo = tk.Menu(menu)
menu.add_cascade(label="Archivo",menu=archivo)


ventana.mainloop()
