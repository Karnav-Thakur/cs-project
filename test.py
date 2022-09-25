import tkinter as tk
import pyglet

win = tk.Tk()

# pyglet.font.add_file('./fonts/ANNAI.TTF')

label = tk.Label(win,text='Test',font=('Bradley Hand ITC',25))
label.pack()

win.mainloop()