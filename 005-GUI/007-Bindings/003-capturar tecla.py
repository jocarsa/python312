import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

def vaciar(self):
    print(entrada.get())
    entrada.delete(0, tk.END)

def teclaA(self):
    print("Has pulsado la tecla A")
entrada = ttk.Entry()
entrada.pack(padx=50,pady=50)

entrada.bind("<Return>",vaciar)
entrada.bind("<a>",teclaA)

ventana.mainloop()
