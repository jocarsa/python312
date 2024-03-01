import tkinter as tk

def hazNada():
    pass

def insertarCliente():
    print("Voy a insertar un cliente")
    print("el nombre es:",nombre.get())
    print("el email es:",email.get())
    print("el telefono es:",telefono.get())

ventana = tk.Tk()
ventana.title("Programa de gestión v0.2")
ventana.geometry("600x600+20+20")
ventana.iconbitmap("../../jv.ico")

menu = tk.Menu(ventana)
ventana.config(menu=menu)

tablas = tk.Menu(menu)
menu.add_cascade(label="Tablas",menu=tablas)
tablas.add_command(label="Clientes",command=hazNada)

tk.Label(text="Insertamos un cliente").pack(padx=50,pady=50)
tk.Label(text="Indica el nombre del cliente").pack(padx=50,pady=5)
nombre = tk.Entry()
nombre.pack(padx=50,pady=5)

tk.Label(text="Indica el email del cliente").pack(padx=50,pady=5)
email = tk.Entry()
email.pack(padx=50,pady=5)

tk.Label(text="Indica el teléfono del cliente").pack(padx=50,pady=5)
telefono = tk.Entry()
telefono.pack(padx=50,pady=5)

tk.Button(text="Insertar nuevo registro",command=insertarCliente).pack(padx=50,pady=5)

ventana.mainloop()
