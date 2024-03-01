import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

marco = ttk.Frame(ventana)
marco.pack(padx=50,pady=50)

ttk.Button(marco,text="Pulsame 1").grid(row=0, column=0)
ttk.Button(marco,text="Pulsame 2").grid(row=0, column=1)
ttk.Button(marco,text="Pulsame 3").grid(row=0, column=2)


ventana.mainloop()
