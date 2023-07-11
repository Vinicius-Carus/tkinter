import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('Button pressed')

window = tk.Tk()
window.title("Tkinter variables")

string_var = tk.StringVar(value='start value')

label = ttk.Label(master=window, text='label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

buton = ttk.Button(master=window, text="button", command=button_func)
buton.pack()



window.mainloop()