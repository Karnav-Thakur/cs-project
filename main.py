import os
import time
import tkinter as tk
import asyncio
# from modules import patient,admin,home,prescription,report,tests,doctor

window = tk.Tk()
# window.maxsize(width=1366,height=728)
window.attributes('-fullscreen',True)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

# parts = {"patient":patient,"doctor":doctor,"home":home,"admin":admin,"prescription":prescription,"report":report,"tests":tests}

def clear_item():
    for item in window.winfo_children():
        item.forget()


def recover_wid():
    button1.pack(anchor='nw')
    dropdown.pack(anchor='n')


class Patient:
    
    def history(): #check the medical history of the patient with our hospital
        pass

    def last_visited(): #check when the patient last visited
        pass

    def add_patient(self): #add new patient

        instruction = tk.Label(window,text='Add a Patient in The Database\nRequired Information: Name,Age,Sex,Phone Number,Email\nPress "Enter" to enter different data in order')
        instruction.pack()
        
        name = tk.Label(window,text='Name')
        name.pack()

        name_box = tk.Text(window,height=1,width=20)
        name_box.pack()
        
        age = tk.Label(window,text='Age')
        age.pack()
        
        age_box = tk.Text(window,height=1,width=20)
        age_box.pack()

        gender = tk.Label(window,text='Gender')
        gender.pack()
        
        gender = tk.Text(window,height=1,width=20)
        gender.pack()

        pn = tk.Label(window,text='Phone Number')
        pn.pack()
        
        pn_box = tk.Text(window,height=1,width=20)
        pn_box.pack()

        mail = tk.Label(window,text='Email')
        mail.pack()
        
        mail_box = tk.Text(window,height=1,width=20)
        mail_box.pack()
        
        def ok():
            label = tk.Label(window,text='Added Patient in Database')
            label.pack()
            label.after(3000,func=clear_item)
            ok_button.after(4000,func=recover_wid)
            

            # print(name_box.get('1.0','end-1c')) # this is how to get data (temoporary until database added)

        ok_button = tk.Button(window,text='Add Patient',command=ok)
        ok_button.pack()
        





class Doctor:
    
    def doc_list(self): # get the list of all the doctors in the database
        pass

    def free_doc(self): #get the list of available doctors
        pass

    def new_doc(self): #add a new doctor
        instruction = tk.Label(window,text='Add a Doctor in The Database\nRequired Information: Name,Age,Sex,Phone Number,Email,Visiting Hours\nPress "Enter" to enter different data in order')
        instruction.pack()
        
        name = tk.Label(window,text='Name')
        name.pack()
        
        name_box = tk.Text(window,height=1,width=20)
        name_box.pack()
        
        def ok():
            label = tk.Label(window,text='Added Doctor in Database')
            label.pack()
            time.sleep(2)
            ok_button.destroy()
            
            label.destroy()

        ok_button = tk.Button(window,text='Add Doctor',command=ok)
        ok_button.pack()

class Admin:
    def __init__(self,user,password):
        self.user = user
        self.pw = password

class Prescription:
    def __init__(self,name,date,medicine):
        self.name = name
        self.date = date
        self.medicine = medicine

class Report:
    def __init__(self,name,date,visit_after):
        self.name = name
        self.date = date
        self.visit_after = visit_after


class Tests:
    def __init__(self,name):
        self.name = name


def winquit():
    window.quit()

def choice(event):
    clear_item()
    recover_wid()
    if stringvar.get() == 'Patient':
        patient = Patient()
        patient.add_patient()
    elif stringvar.get() == 'Doctor':
        doctor = Doctor()
        doctor.new_doc()


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


