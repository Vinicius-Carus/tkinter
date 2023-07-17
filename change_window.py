import tkinter as tk
from tkinter import ttk

window = tk.Tk()


window.title('More on the window')
#window.geometry(f'600x400+{midle_width}+{midle_height}')
window.iconbitmap('python.ico')

window_width = 1200
window_height = 700

midle_width = int(window.winfo_screenwidth() / 2 - window_width / 2)
midle_height = int(window.winfo_screenheight() / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{midle_width}+{midle_height}')

window.minsize(200, 100)

#window.maxsize(800, 700)
#window.resizable(False, False)


window.attributes('-alpha', 1)
#window.attributes('-topmost', True)

#security event
window.bind('<KeyPress-p>', lambda event: window.quit())

#window.attributes('-disable', True)
#window.attributes('-fullscreen', True)

window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx=1.0, rely=1.0, anchor='se')

window.mainloop()