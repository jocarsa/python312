import tkinter as tk
from tkinter import ttk
from importaciones.operacionessql import *

def hazNada():
    pass

def mostrarInsertar(marco):
    marco.pack(padx=50,pady=50)

def mostrarListado(marcolistado):
    print("ok voy a mostrar el listado")
    marcolistado.pack(padx=50,pady=50)

def miMenu(ventana,marco,marcolistado):
    menu = tk.Menu(ventana)
    ventana.config(menu=menu)
    tablas = tk.Menu(menu)
    menu.add_cascade(label="Tablas",menu=tablas)
    tablas.add_command(label="Clientes",command=hazNada)

    operaciones = tk.Menu(menu)
    menu.add_cascade(label="Operaciones",menu=operaciones)
    operaciones.add_command(label="Listado",command=lambda:mostrarListado(marcolistado))
    operaciones.add_command(label="Insertar",command=lambda:mostrarInsertar(marco))
    operaciones.add_command(label="Actualizar",command=hazNada)
    operaciones.add_command(label="Eliminar",command=hazNada)

def configurarVentana(ventana):
    ventana.title("Programa de gestión v0.2")
    ventana.geometry("600x600+20+20")
    ventana.iconbitmap("../../jv.ico")

def marcoInsertar(marco):
    tk.Label(marco,text="Insertamos un cliente").grid(row=0,column=0, columnspan=4)
    tk.Label(marco,text="Indica el nombre del cliente").grid(row=1,column=0)
    nombre = tk.Entry(marco)
    nombre.grid(row=2,column=0)

    tk.Label(marco,text="Indica el email del cliente").grid(row=1,column=1)
    email = tk.Entry(marco)
    email.grid(row=2,column=1)

    tk.Label(marco,text="Indica el teléfono del cliente").grid(row=1,column=2)
    telefono = tk.Entry(marco)
    telefono.grid(row=2,column=2)

    boton = tk.Button(marco,text="Insertar nuevo registro",command=lambda:insertarCliente(nombre,email,telefono))
    boton.grid(row=2,column=4)
    
def marcoListado(marcolistado):
    print("ok vamos")
    arbol = ttk.Treeview(marcolistado)
    arbol.pack(padx=50,pady=50)

    arbol["columns"] = ("1", "2", "3")

    arbol.heading("#0", text="Identificador")
    arbol.heading("1", text="Nombre")
    arbol.heading("2", text="Email")
    arbol.heading("3", text="Teléfono")

    arbol.insert("", tk.END, text="0", values=("Jose Vicente", "info@jocarsa.com", "452354"))

