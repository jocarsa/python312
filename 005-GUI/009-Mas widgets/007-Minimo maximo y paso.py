import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

slider = ttk.Scale(ventana, from_=0, to=10).pack(padx=5,pady=5)




ventana.mainloop()
