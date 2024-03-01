import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# Create a Tkinter window
ventana = tk.Tk()

# Create a ttkbootstrap style
style = Style(theme="minty")

# Apply the style to the window
style.master_style()

# Create a label with styled text
label = ttk.Label(ventana, text="Hello, ttkbootstrap!", style="TLabel")
label.pack(padx=20, pady=20)

# Run the application
ventana.mainloop()
