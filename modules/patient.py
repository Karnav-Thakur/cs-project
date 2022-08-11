import tkinter as tk

def add_patient(win):
    
    instruction = tk.Label(win,text='Add a Patient in The Database')
    instruction.pack()
    
    name = tk.Label(win,text='Name')
    name.pack()
    
    name_box = tk.Text(win,height=5,width=20)
    name_box.pack()

    def ok():
        label = tk.Label(win,text='Added Patient in Database')
        label.pack()
        # win.destroy()


    ok_button = tk.Button(win,text='Add User',command=ok)
    ok_button.pack()



if __name__ == '__main__':
    pass