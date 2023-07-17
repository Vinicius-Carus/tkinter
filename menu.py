import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Menu')

menu = tk.Menu(window)

file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='New', command= lambda: print('New file'))
file_menu.add_command(label='Open', command= lambda: print('open file'))
file_menu.add_separator()
menu.add_cascade(label='File', menu = file_menu)

help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label='Help entry', command= lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label= 'check', onvalue='on', offvalue='off', variable=help_check_string)

menu.add_cascade(label='Help', menu=help_menu)

exercise_menu = tk.Menu(menu, tearoff=False)
exercise_menu.add_command(label='exercise 1')
menu.add_cascade(label='Exercise', menu=exercise_menu)

exercise_sub_menu = tk.Menu(menu, tearoff=False)
exercise_menu.add_cascade(label='more', menu=exercise_sub_menu)
exercise_sub_menu.add_command(label='exercise sub menu')

window.configure(menu=menu)

menu_button = ttk.Menubutton(window, text='Menu button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label='entry', command=lambda: print('test1'))
button_sub_menu.add_checkbutton(label='check 1')

#menu_button.configure(menu = button_sub_menu)

menu_button['menu'] = button_sub_menu

window.mainloop()
