import tkinter as tk
import tkinter.ttk as ttk

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')

window = tk.Tk()
window.geometry('600x500')
window.title("Event biding")

text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text='A button')
button.pack()

button.bind('<Alt-KeyPress-a>', lambda event: print("event"))
text.bind('<Motion>', get_pos)

window.bind('<KeyPress>', lambda event: print(f'A button was pressed ({event.char})'))

entry.bind('<FocusIn>', lambda event:print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

text.bind('<Shift-MouseWheel>', lambda event: print('MouseWheel'))

window.mainloop()