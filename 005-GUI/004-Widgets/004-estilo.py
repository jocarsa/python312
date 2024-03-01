import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

boton = ttk.Button(ventana, text="Pulsame")
boton.pack(padx=50, pady=50)

# Now configure the colors
boton.configure(background='red')

ventana.mainloop()
