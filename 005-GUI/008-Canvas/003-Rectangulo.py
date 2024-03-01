import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

lienzo = tk.Canvas()
lienzo.pack()

lienzo.create_oval(50, 50, 150, 150, outline="blue", fill="cyan")
lienzo.create_rectangle(200, 50, 300, 150, outline="red", fill="pink")

ventana.mainloop()
