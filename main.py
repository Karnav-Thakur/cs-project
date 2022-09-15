import os
import tkinter as tk

window = tk.Tk()
# window.maxsize(width=1366,height=728)
window.attributes('-fullscreen',True)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()


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

        typ = tk.Label(window,text='Type (OPD or IPD)')
        typ.pack()

        typ_box = tk.Text(window,height=1,width=20)
        typ_box.pack()
        
        disease = tk.Label(window,text='Disease')
        disease.pack()

        disease_box = tk.Text(window,height=1,width=20)
        disease_box.pack()
        
        def ok():
            label = tk.Label(window,text='Added Patient in Database')
            label.pack()
            label.after(3000,func=clear_item)
            ok_button.after(4000,func=recover_wid)
            

            # print(name_box.get('1.0','end-1c')) # this is how to get data (temoporary until database added)

        ok_button = tk.Button(window,text='Add Patient',command=ok)
        ok_button.pack()
        
    def search_patient(self): #search for a new patient
        search = tk.Label(window,text='Enter name of patient')
        search.pack()

        search_box = tk.Text(window,height=1,width=20)
        search_box.pack()

        def search():
            name = search_box.get('1.0','end-1c')
            print(name)


        search_button = tk.Button(window,text='Search',command=search)
        search_button.pack()






class Doctor:
    
    def doc_list(self): # get the list of all the doctors in the database
        pass

    def free_doc(self): #get the list of available doctors
        pass

    def new_doc(self): #add a new doctor
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

        time = tk.Label(window,text='Consultancy Time')
        time.pack()

        time_box = tk.Text(window,height=1,width=20)
        time_box.pack()
        
        def ok():
            label = tk.Label(window,text='Added Doctor in Database')
            label.pack()
            label.after(3000,func=clear_item)
            ok_button.after(4000,func=recover_wid)

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
        methods_drop.pack()

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
        methods_drop.pack()


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


