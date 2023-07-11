import tkinter as tk
from tkinter import ttk


def button_func():
    #get the content of the entry
    entry_text = entry.get()
    if entry_text:
        #update the label
        label['text'] = entry_text
        entry['state'] = 'disabled'


def button_edit():
    label['text'] = 'Type something'
    entry['state'] = 'normal'

window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry('300x200')

label = ttk.Label(window, text='Type something')
label.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text='Get text', command=button_func)
button.pack()

edit_button = ttk.Button(window, text='Reset', command=button_edit)
edit_button.pack()
window.mainloop()