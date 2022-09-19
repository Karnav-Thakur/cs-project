import tkinter as tk

window = tk.Tk()
window.attributes('-fullscreen',True)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
dimensions = (screenwidth,screenheight)
canvas = tk.Canvas(window,width=dimensions[0],height=dimensions[1])
canvas.pack(fill='both',expand=True)
canvas.create_image(0,0,anchor='nw')

y = 150
gap = 25

mail = tk.Label(window,text='Email')
canvas.create_window(screenwidth//2,y+11*gap,window=mail)

mail_box = tk.Text(window,height=1,width=20)
canvas.create_window(screenwidth//2,y+12*gap,window=mail_box)

time = tk.Label(window,text='Consultancy Time')        
canvas.create_window(screenwidth//2,y+13*gap,window=time)

time_box = tk.Text(window,height=1,width=20)
canvas.create_window(screenwidth//2,y+14*gap,window=time_box)

print(canvas.find_all())
# canvas.delete(1)
canvas.delete(2)
canvas.delete(3)
canvas.delete(4)
window.mainloop()