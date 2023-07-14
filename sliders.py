import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title('Sliders')

scale_float = tk.DoubleVar(value=15)
scale = ttk.Scale(window, command= lambda value: progress.stop(), 
                  from_=0, 
                  to=25, 
                  length= 300, 
                  orient='vertical',
                  variable=scale_float)
scale.pack()

progress = ttk.Progressbar(window, variable=scale_float, maximum=25, mode='indeterminate')
progress.pack()

#progress.start(1000)

scrolled_text = scrolledtext.ScrolledText(window, height=5)
scrolled_text.pack()

window.mainloop()