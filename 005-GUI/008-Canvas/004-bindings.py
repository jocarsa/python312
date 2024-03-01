import tkinter as tk
from tkinter import ttk

def mover(event):
    print("ok")
    if event.keysym == "Up":
        lienzo.move(rectangulo, 0, -10)
    elif event.keysym == "Down":
        lienzo.move(rectangulo, 0, 10)
    elif event.keysym == "Left":
        lienzo.move(rectangulo, -10, 0)
    elif event.keysym == "Right":
        lienzo.move(rectangulo, 10, 0)

ventana = tk.Tk()

lienzo = tk.Canvas()
lienzo.pack()

lienzo.create_oval(50, 50, 150, 150, outline="blue", fill="cyan")
rectangulo = lienzo.create_rectangle(200, 50, 300, 150, outline="red", fill="pink")

lienzo.focus_set()

lienzo.bind("<Up>", mover)
lienzo.bind("<Down>", mover)
lienzo.bind("<Left>", mover)
lienzo.bind("<Right>", mover)

ventana.mainloop()
