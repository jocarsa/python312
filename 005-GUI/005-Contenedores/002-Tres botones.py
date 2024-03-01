import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

marco = ttk.Frame(ventana)
marco.pack(padx=50,pady=50)

ttk.Button(marco,text="Pulsame 1").pack()
ttk.Button(marco,text="Pulsame 2").pack()
ttk.Button(marco,text="Pulsame 3").pack()


ventana.mainloop()
