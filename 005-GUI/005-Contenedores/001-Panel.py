import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

marco = ttk.Frame(ventana)
marco.pack(padx=50,pady=50)

ttk.Button(marco,text="Pulsame").pack()


ventana.mainloop()
