import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Combo and Spin")

items = ('Ice cream', 'Pizza', 'Brocoli')
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_string)
combo['values'] = items
combo.pack()

combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text=f'Selected value: {food_string.get()}'))

combo_label = ttk.Label(window, text = 'a label')
combo_label.pack()

spin_int = tk.IntVar()
spin = ttk.Spinbox(window, from_ = 3, to=20, increment=3, command= lambda: print(spin_int.get()), textvariable=spin_int)
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down') )
spin.pack()

spin2_letter = tk.StringVar()
spin2 = ttk.Spinbox(window, textvariable=spin2_letter)
spin2['values'] = ("A","B","C","D","E")
spin2.bind("<<Decrement>>", lambda event: print(spin2_letter.get()))
spin2.pack()
window.mainloop()