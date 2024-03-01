import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

def vaciar(self):
    print(entrada.get())
    entrada.delete(0, tk.END)

def teclaA(self):
    print("Has pulsado la tecla A")

def enfoca(self):
    print("Has entrado")

def desenfoca(self):
    print(entrada.get())
    entrada.delete(0, tk.END)
    
def entra(self):
    print("Tu raton esta sobre el elemento")
    
def sal(self):
    print("Tu raton ha salido del elemento")
    
entrada = ttk.Entry()
entrada.pack(padx=50,pady=50)

entrada2 = ttk.Entry()
entrada2.pack(padx=50,pady=50)

entrada.bind("<Return>",vaciar)
entrada.bind("<a>",teclaA)
entrada.bind("<FocusIn>", enfoca)
entrada.bind("<FocusOut>", desenfoca)
entrada.bind("<Enter>", entra)
entrada.bind("<Leave>", sal)
ventana.mainloop()
