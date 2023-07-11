import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Buttons') 
window.geometry('600x400')

def button_func():
    print('a basic button')
    print(radio_var.get())

button_string = tk.StringVar(value='Ab button with strin var')
button = ttk.Button(window, text='Button', command= button_func, textvariable=button_string)
button.pack()

check_var = tk.IntVar(value=10)
check = ttk.Checkbutton(window, 
                        text='Checkbox 1', 
                        command=lambda:print(check_var.get()), 
                        variable=check_var, 
                        onvalue=10, 
                        offvalue=5)
check.pack()

radio_var = tk.IntVar()
radio1 = ttk.Radiobutton(window, 
                         text='Radiobutton 1',
                         value=1,
                         variable=radio_var,
                         command=lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(window, 
                         text='Radiobutton 2',
                         value=2,
                         variable=radio_var) 
radio2.pack()

def radio_func():
    print(check_exercise_var.get())
    check_exercise_var.set(False)

check_exercise_var = tk.BooleanVar()
check_exercise = ttk.Checkbutton(window, text='Check exercise', variable=check_exercise_var, command=lambda:print(radio_exercise_var.get()))
check_exercise.pack()

radio_exercise_var = tk.StringVar()
radio_exercise = ttk.Radiobutton(window, text='Radiobutton exercise', value='A', command=radio_func,variable=radio_exercise_var)
radio_exercise.pack()

radio_exercise2 = ttk.Radiobutton(window, text='Radiobutton exercise 2', value='B', command=radio_func, variable=radio_exercise_var)
radio_exercise2.pack()

window.mainloop()