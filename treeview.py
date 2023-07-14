import tkinter as tk
from tkinter import ttk
from random import choice

window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

first_names = ['Jin', 'Yato', 'Haten', 'Akira', 'Yuta']
last_names = ['Kerman', 'Lepli', 'Mortonium', 'Blake', 'Leandro']

table = ttk.Treeview(window, columns=('first', 'last', 'email'), show = 'headings')
table.heading('first', text='First Name')
table.heading('last', text='Last Name')
table.heading('email', text='Email')
table.pack(fill='both', expand= True)

for i in range(100):
    first = choice(first_names)
    last =  choice(last_names)
    email = f'{first.lower()}{last.lower()}@gmail.com'
    data = (first, last, email)
    table.insert(parent='', index=0, values= data)

table.insert(parent='', index=tk.END, values=('AAAAAA', 'EEEEEEEE', 'PPPPP'))

def item_select(_):
    for i in table.selection():
        print(table.item(i)['values'])

table.bind('<<TreeviewSelect>>', item_select)

def delete_items(_):
    for item in table.selection():
        table.delete(item)

        
table.bind('<Delete>', delete_items)

window.mainloop()