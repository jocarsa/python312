import tkinter as tk
from tkinter import ttk

def diHola():
    print("hola")

ventana = tk.Tk()

ttk.Button(ventana,text="Pulsame",command=diHola).pack(padx=50,pady=50)

ventana.mainloop()
