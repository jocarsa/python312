import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

deportes1 = tk.StringVar()
deportes2 = tk.StringVar()
deportes3 = tk.StringVar()
deportes4 = tk.StringVar()

deportes1.set(1)

ttk.Label(ventana,text="Indica tus deportes favoritos").pack(padx=5,pady=5)
ttk.Checkbutton(ventana,text="Futbol",variable=deportes1).pack(padx=5,pady=5)
ttk.Checkbutton(ventana,text="Baloncesto",variable=deportes2).pack(padx=5,pady=5)
ttk.Checkbutton(ventana,text="Ski",variable=deportes3).pack(padx=5,pady=5)
ttk.Checkbutton(ventana,text="Patinaje",variable=deportes4).pack(padx=5,pady=5)




ventana.mainloop()
