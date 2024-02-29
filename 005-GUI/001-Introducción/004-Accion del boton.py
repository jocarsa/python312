import tkinter as tk

def hazAlgo():
    print("Has pulsado el boton")

ventana = tk.Tk()

entrada = tk.Entry(ventana)
entrada.pack(padx=20,pady=20)

boton = tk.Button(ventana,text="Pulsame",command=hazAlgo)
boton.pack(padx=20,pady=20)

ventana.mainloop()
