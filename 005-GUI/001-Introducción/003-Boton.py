import tkinter as tk

ventana = tk.Tk()

entrada = tk.Entry(ventana)
entrada.pack(padx=20,pady=20)

boton = tk.Button(ventana,text="Pulsame")
boton.pack(padx=20,pady=20)

ventana.mainloop()
