import os
import tkinter as tk
from PIL import Image,ImageTk
from helpers import helper

window = tk.Tk()
# window.maxsize(width=1366,height=728)
window.attributes('-fullscreen',True)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
dimensions = (screenwidth,screenheight)

y = 100
gap = 25


bg = ImageTk.PhotoImage(Image.open('templates/bg.png').resize(dimensions))

canvas = tk.Canvas(window,width=dimensions[0],height=dimensions[1])
canvas.pack(fill='both',expand=True)
canvas.create_image(0,0,image=bg,anchor='nw')

def clear_item():
    for item in canvas.winfo_children():
        item.forget()

def recover_wid():
    # button1.pack(anchor='nw')
    canvas.create_window(0,0,anchor='nw',window=button1)
    canvas.create_window(screenwidth//2,0,anchor='n',window=dropdown)  

    # dropdown.pack(anchor='n')


class Patient:
    
    def history(): #check the medical history of the patient with our hospital
        pass

    def last_visited(): #check when the patient last visited
        pass

    def add_patient(self): #add new patient

        name = tk.Label(window,text='Name')
        canvas.create_window(screenwidth//2,y+gap,window=name)

        name_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+2*gap,window=name_box)
        
        age = tk.Label(window,text='Age')
        canvas.create_window(screenwidth//2,y+3*gap,window=age)
        
        age_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+4*gap,window=age_box)

        gender = tk.Label(window,text='Gender')
        canvas.create_window(screenwidth//2,y+5*gap,window=gender)
        
        gender_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+6*gap,window=gender_box)

        pn = tk.Label(window,text='Phone Number')
        canvas.create_window(screenwidth//2,y+7*gap,window=pn)
        
        pn_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+8*gap,window=pn_box)

        mail = tk.Label(window,text='Email')
        canvas.create_window(screenwidth//2,y+9*gap,window=mail)
        
        mail_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+10*gap,window=mail_box)

        typ = tk.Label(window,text='Type (OPD or IPD)')
        canvas.create_window(screenwidth//2,y+11*gap,window=typ)

        typ_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+12*gap,window=typ_box)
        
        disease = tk.Label(window,text='Disease')
        canvas.create_window(screenwidth//2,y+13*gap,window=disease)

        disease_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+14*gap,window=disease_box)
        
        def ok():
            label = tk.Label(window,text='Added Patient in Database')
            # label.pack()
            canvas.create_window(screenwidth//2,y+15*gap,window=label)
            label.after(3000,func=clear_item)
            ok_button.after(4000,func=recover_wid)
            

            # print(name_box.get('1.0','end-1c')) # this is how to get data (temoporary until database added)

        ok_button = tk.Button(window,text='Add Patient',command=ok)
        ok_button.pack()
        canvas.create_window(screenwidth//2,y+16*gap,window=ok_button)
        
    def search_patient(self): #search for a new patient
        search = tk.Label(window,text='Enter name of patient')
        # search.pack()
        canvas.create_window(screenwidth//2,y+gap,window=search)

        search_box = tk.Text(window,height=1,width=20)
        # search_box.pack()
        canvas.create_window(screenwidth//2,y+2*gap,window=search_box)

        def search():
            name = search_box.get('1.0','end-1c')
            print(name)


        search_button = tk.Button(window,text='Search',command=search)
        # search_button.pack()
        canvas.create_window(screenwidth//2,y+3*gap,window=search_button)
        
class Doctor:
    
    def doc_list(self): # get the list of all the doctors in the database
        pass

    def free_doc(self): #get the list of available doctors
        pass

    def new_doc(self): #add a new doctor
        y = 100
        gap = 25

        name = tk.Label(window,text='Name')
        canvas.create_window(screenwidth//2,y+gap,window=name)

        name_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+2*gap,window=name_box)
        
        age = tk.Label(window,text='Age')
        canvas.create_window(screenwidth//2,y+3*gap,window=age)
        
        age_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+4*gap,window=age_box)

        gender = tk.Label(window,text='Gender')
        canvas.create_window(screenwidth//2,y+5*gap,window=gender)
        
        gender_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+6*gap,window=gender_box)

        pn = tk.Label(window,text='Phone Number')
        canvas.create_window(screenwidth//2,y+7*gap,window=pn)
        
        pn_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+8*gap,window=pn_box)

        mail = tk.Label(window,text='Email')
        canvas.create_window(screenwidth//2,y+9*gap,window=mail)
        
        mail_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+10*gap,window=mail_box)

        time = tk.Label(window,text='Consultancy Time')        
        canvas.create_window(screenwidth//2,y+11*gap,window=time)

        time_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+12*gap,window=time_box)
        
        def ok():
            label = tk.Label(window,text='Added Doctor in Database')
            # label.pack()
            canvas.create_window(screenwidth//2,y+13*gap,window=label)
            label.after(3000,func=clear_item)
            ok_button.after(4000,func=recover_wid)
            

            # print(name_box.get('1.0','end-1c')) # this is how to get data (temoporary until database added)

        ok_button = tk.Button(window,text='Add Patient',command=ok)
        ok_button.pack()
        canvas.create_window(screenwidth//2,y+16*gap,window=ok_button)

class Admin:
    def __init__(self,user,password):
        self.user = user
        self.pw = password

class Prescription:
    def __init__(self,name,date,medicine):
        self.name = name
        self.date = date
        self.medicine = medicine

class Report(Patient):
    pass


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

        methods = [attr for attr in dir(Patient) if attr.startswith('__') is False]

        meths = tk.StringVar(window,methods[0])

        def cho(event):
            clear_item()
            recover_wid()
            if meths.get() == 'add_patient':
                patient.add_patient()
            elif meths.get() == 'history':
                patient.history()
            elif meths.get() == 'last_visited':
                patient.last_visited()
            elif meths.get() == 'search_patient':
                patient.search_patient()


        methods_drop = tk.OptionMenu(window,meths,*methods,command=cho)
        # methods_drop.pack()
        canvas.create_window(screenwidth//2,dropdown.winfo_height()+50,window=methods_drop)

    elif stringvar.get() == 'Doctor':
        doctor = Doctor()

        methods = [attr for attr in dir(doctor) if attr.startswith('__') is False]
        
        meths = tk.StringVar(window,methods[0])

        def cho(event):
            clear_item()
            recover_wid()
            if meths.get() == 'doc_list':
                doctor.doc_list()
            elif meths.get() == 'free_doc':
                doctor.free_doc()
            elif meths.get() == 'new_doc':
                doctor.new_doc()


        methods_drop = tk.OptionMenu(window,meths,*methods,command=cho)
        # methods_drop.pack()
        canvas.create_window(screenwidth//2,dropdown.winfo_height()+50,window=methods_drop)



mods = []
for i in os.listdir('./modules'):
    if i.endswith('.py'):
        mods.append(i.split('.py')[0].title())

mods.sort()

stringvar = tk.StringVar(window,mods[0])

button1 = tk.Button(window,command=winquit, text = "Exit",font=('Segoe UI',18,'bold'))

# button1.pack(anchor='nw')

canvas.create_window(0,0,anchor='nw',window=button1)

dropdown = tk.OptionMenu(window,stringvar,*mods,command=choice)
# dropdown.pack(anchor='n')
canvas.create_window(screenwidth//2,0,anchor='n',window=dropdown)  
# limg = tk.Label(window,image=bg)
# limg.pack()

window.mainloop()


