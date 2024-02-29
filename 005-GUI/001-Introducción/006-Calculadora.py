import tkinter as tk

def hazAlgo():
    operando1 = int(entrada1.get())
    operando2 = int(entrada2.get())
    suma = operando1 + operando2
    resultado.config(text=str(suma))

ventana = tk.Tk()

entrada1 = tk.Entry(ventana)
entrada1.pack(padx=20,pady=20)

entrada2 = tk.Entry(ventana)
entrada2.pack(padx=20,pady=20)

boton = tk.Button(ventana,text="Pulsame",command=hazAlgo)
boton.pack(padx=20,pady=20)

resultado = tk.Label(text="Resultado")
resultado.pack(padx=20,pady=20)

ventana.mainloop()
