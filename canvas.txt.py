import tkinter as tk
from tkinter import ttk

def print_line(event):
    canvas2.create_oval((event.x - brush_size/2, event.y - brush_size/2, event.x + brush_size/2, event.y + brush_size/2), fill='green', outline='green')

brush_size = 4

window = tk.Tk()
window.geometry('600x600')
window.title('Canvas') 

canvas = tk.Canvas(window, bg='white')
canvas.pack()

canvas.create_rectangle((20,20,100,200), fill='red', width=10, dash= (255,20), outline='blue')
canvas.create_oval((110,10,210,110), fill='cyan')
canvas.create_line((100, 100, 200, 250), fill ='green')
canvas.create_window((150,100), window = ttk.Label(window, text="This is text"))

canvas2 = tk.Canvas(window, bg='white')
canvas2.pack(pady=10)
#canvas2.create_polygon((250,250,100,200,300,50), fill='gray')
#canvas2.create_arc((110,10,210,110), fill='cyan', start=90, extent=60, style= tk.ARC)
#canvas2.create_text((100,50), text='Some text', fill='green', width=10)

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4

    brush_size = max(0,min(brush_size, 50))

canvas2.bind("<Motion>", print_line)
canvas2.bind("<MouseWheel>", brush_size_adjust)
window.mainloop()

#https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html