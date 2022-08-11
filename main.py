import os
import tkinter as tk
from modules import patient,admin,home,prescription,report,tests,doctor

window = tk.Tk()
# window.maxsize(width=1366,height=728)
window.attributes('-fullscreen',True)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

parts = {"patient":patient,"doctor":doctor,"home":home,"admin":admin,"prescription":prescription,"report":report,"tests":tests}

def winquit():
    window.quit()

def choice(event):
    if stringvar.get() == 'Patient':
        patient.add_patient(window)


mods = []
for i in os.listdir('./modules'):
    if i.endswith('.py'):
        mods.append(i.split('.py')[0].title())

mods.sort()

stringvar = tk.StringVar(window,mods[0])

button1 = tk.Button(window,command=winquit, text = "Exit",font=('Segoe UI',18,'bold'))

button1.pack(anchor='nw')

dropdown = tk.OptionMenu(window,stringvar,*mods,command=choice)
dropdown.pack(anchor='n')  



window.mainloop()