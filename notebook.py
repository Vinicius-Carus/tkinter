import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title("Tab Widget")

notebook = ttk.Notebook(window)

tab1 = ttk.Frame(notebook)

label1 = ttk.Label(tab1, text='Text in tab 1')
label1.pack()

button1 = ttk.Button(tab1, text='Button')
button1.pack()

tab2 = ttk.Frame(notebook)

label2 = ttk.Label(tab2, text='Text in tab 2')
label2.pack()

entry2 = ttk.Entry(tab2)
entry2.pack()

tab3 = ttk.Frame(notebook)

label3 = ttk.Label(tab3, text="This is the exercise!")
label3.pack()

entry3 = ttk.Entry(tab3)
entry3.pack()

button3 = ttk.Button(tab3, text='Button exercise')
button3.pack()


notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.add(tab3, text='Tab 3 - Exercise')
notebook.pack()

window.mainloop()