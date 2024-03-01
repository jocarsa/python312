import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

mayoredad = tk.StringVar()
sexo = tk.StringVar()

ttk.Label(ventana,text="¿Eres mayor de edad?").pack(padx=5,pady=5)
ttk.Radiobutton(ventana,text="si",value='si',variable=mayoredad).pack(padx=5,pady=5)
ttk.Radiobutton(ventana,text="no",value='no',variable=mayoredad).pack(padx=5,pady=5)

ttk.Label(ventana,text="¿Sexo en el DNI?").pack(padx=5,pady=5)
ttk.Radiobutton(ventana,text="hombre",value='hombre',variable=sexo).pack(padx=5,pady=5)
ttk.Radiobutton(ventana,text="mujer",value='mujer',variable=sexo).pack(padx=5,pady=5)


ventana.mainloop()
