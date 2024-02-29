import tkinter as tk

def hazAlgo():
    print("Has pulsado el boton")
    entrada_content = entrada.get()
    print("Contenido de la entrada:", entrada_content)

ventana = tk.Tk()

entrada = tk.Entry(ventana)
entrada.pack(padx=20,pady=20)

boton = tk.Button(ventana,text="Pulsame",command=hazAlgo)
boton.pack(padx=20,pady=20)

ventana.mainloop()
