import datetime
import os
import tkinter as tk
from tkinter import messagebox,ttk
from PIL import Image,ImageTk
from helpers import helper

window = tk.Tk()
window.attributes('-fullscreen',True)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
dimensions = (screenwidth,screenheight)

y = 100
gap = 25

ms = helper.MySQL('localhost','root','hms','12345678')

bg = ImageTk.PhotoImage(Image.open('templates/bg.png').resize(dimensions))



canvas = tk.Canvas(window,width=dimensions[0],height=dimensions[1])
canvas.pack(fill='both',expand=True)
canvas.create_image(0,0,image=bg,anchor='nw')


def clear_item():
    for item,ids in enumerate(canvas.find_all()):
        if ids == 1:
            continue
        canvas.delete(ids)



def recover_wid():
    canvas.pack(fill='both',expand=True)
    canvas.create_window(0,0,anchor='nw',window=button1)
    canvas.create_window(screenwidth//2,0,anchor='n',window=dropdown)  



class Patient:
    
    def history(self): #check the medical history of the patient with our hospital
        search = tk.Label(window,text='Enter name of patient')
        canvas.create_window(screenwidth//2,y+gap,window=search)

        search_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+2*gap,window=search_box)

        def search():
            text = search_box.get('1.0','end-1c').split(' ')
            if text == ['']:
                messagebox.showwarning(title='Error Occured',message='Please enter name of the patient to search')
                return
            
            results = ms.search_patient(*text)

            if results == []:
                messagebox.showerror(title="Error Occured",message='Patient Not Found')
                return
            
            patient_id = results[0][0]       

            history = ms.history(patient_id)

            clean_history = []

            for x in history:
                new_x = (x[0],x[1],x[2],str(x[3]))
                clean_history.append(new_x)

            label = tk.Label(window,text=f'Results Found\n {clean_history}')
            
            canvas.create_window(screenwidth//2,y+4*gap,window=label)

        search_button = tk.Button(window,text='Search',command=search)
        canvas.create_window(screenwidth//2,y+3*gap,window=search_button)

            

    def last_visited(self): #check when the patient last visited
        search = tk.Label(window,text='Enter name of patient')
        canvas.create_window(screenwidth//2,y+gap,window=search)

        search_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+2*gap,window=search_box)

        def search():
            text = search_box.get('1.0','end-1c').split(' ')
            if text == ['']:
                messagebox.showwarning(title='Error Occured',message='Please enter name of the patient to search')
                return
            
            results = ms.search_patient(*text)
            clean_result = []

            if results == []:
                messagebox.showerror(title="Error Occured",message='Patient Not Found')
                return

            for i in results:
                last_visit = str(i[9])
                new_doc_data = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],last_visit)
                clean_result.append(new_doc_data)


            label = tk.Label(window,text=f'Results Found\n {clean_result}')
            
            canvas.create_window(screenwidth//2,y+4*gap,window=label)

        search_button = tk.Button(window,text='Search',command=search)
        canvas.create_window(screenwidth//2,y+3*gap,window=search_button)


    def add_patient(self): #add new patient

        first_name = tk.Label(window,text='First Name')
        canvas.create_window(screenwidth//2,y+gap,window=first_name)

        first_name_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+2*gap,window=first_name_box)
        
        last_name = tk.Label(window,text='Last Name')
        canvas.create_window(screenwidth//2,y+3*gap,window=last_name)

        last_name_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+4*gap,window=last_name_box)
        
        age = tk.Label(window,text='Age')
        canvas.create_window(screenwidth//2,y+5*gap,window=age)
        
        age_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+6*gap,window=age_box)

        gender = tk.Label(window,text='Gender')
        canvas.create_window(screenwidth//2,y+7*gap,window=gender)
        
        gender_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+8*gap,window=gender_box)

        pn = tk.Label(window,text='Phone Number')
        canvas.create_window(screenwidth//2,y+9*gap,window=pn)
        
        pn_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+10*gap,window=pn_box)

        mail = tk.Label(window,text='Email')
        canvas.create_window(screenwidth//2,y+11*gap,window=mail)
        
        mail_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+12*gap,window=mail_box)

        typ = tk.Label(window,text='Type (OPD or IPD)')
        canvas.create_window(screenwidth//2,y+13*gap,window=typ)

        typ_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+14*gap,window=typ_box)
        
        disease = tk.Label(window,text='Disease')
        canvas.create_window(screenwidth//2,y+15*gap,window=disease)

        disease_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+16*gap,window=disease_box)

        visit = tk.Label(window,text='Last Visit')
        canvas.create_window(screenwidth//2,y+17*gap,window=visit)

        visit_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+18*gap,window=visit_box)
        

        def ok():
        
            try:
                int(age_box.get('1.0','end-1c'))
                int(pn_box.get('1.0','end-1c'))
                datetime.datetime.strptime(visit_box.get('1.0','end-1c'),'%d/%m/%Y')

            except Exception as e:
                messagebox.showerror('Error Occured', 'One or more arguments are put incorrectly')
                return

            first_name_box_text = first_name_box.get('1.0','end-1c').title().strip()
            last_name_box_text = last_name_box.get('1.0','end-1c').title().strip()
            age_box_text = int(age_box.get('1.0','end-1c').strip())
            gender_box_text = gender_box.get('1.0','end-1c').title().strip()
            pn_box_text = int(pn_box.get('1.0','end-1c').strip())
            mail_box_text = mail_box.get('1.0','end-1c').title().strip()
            typ_box_text = typ_box.get('1.0','end-1c').title().strip()
            disease_box_text = disease_box.get('1.0','end-1c').title().strip()
            visit_box_text = datetime.datetime.strptime(visit_box.get('1.0','end-1c').strip(),'%d/%m/%Y')
            visited_before = intvar.get()

            data = [first_name_box_text,last_name_box_text,age_box_text,gender_box_text,pn_box_text,mail_box_text,typ_box_text,disease_box_text,visit_box_text]

            if len(first_name_box_text) > 45 or len(last_name_box_text) > 45 or len(str(pn_box_text)) > 10:
                messagebox.showerror(title="Error Occured",message='Text arguments have exceeded the word limit')
        
            label = tk.Label(window,text='Added Patient in Database')
            canvas.create_window(screenwidth//2,y+19*gap,window=label)
            label.after(3000,func=clear_item)
            ok_button.after(4000,func=recover_wid)

            
            # try:
            ms.add_patient(visited_before,*data)
            # except Exception as e:
            #     print(e)
            #     messagebox.showerror(title='Error Occured',message=e)
            #     return


        ok_button = tk.Button(window,text='Add Patient',command=ok)
        # ok_button.pack()
        canvas.create_window(screenwidth//2,y+20*gap,window=ok_button)

        visited_before = tk.Checkbutton(window,text='Visited Before',onvalue=1,offvalue=0,variable=intvar,height=1,width=20)
        print(intvar.get())
        canvas.create_window(screenwidth//2,y+21*gap,window=visited_before)
        
        
    def search_patient(self): #search for a new patient
        search = tk.Label(window,text='Enter name of patient')
        canvas.create_window(screenwidth//2,y+gap,window=search)

        search_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+2*gap,window=search_box)

        def search():
            text = search_box.get('1.0','end-1c').split(' ')
            if text == ['']:
                messagebox.showwarning(title='Error Occured',message='Please enter name of the patient to search')
                return
            
            results = ms.search_patient(*text)


            if results == []:
                messagebox.showerror(title="Error Occured",message='Patient Not Found')
                return

            label = tk.Label(window,text=f'Results Found\n {results}')
            
            canvas.create_window(screenwidth//2,y+4*gap,window=label)







        search_button = tk.Button(window,text='Search',command=search)
        canvas.create_window(screenwidth//2,y+3*gap,window=search_button)
        
class Doctor:
    
    def doc_list(self): # get the list of all the doctors in the database
        label = tk.Label(window,text='Click the button to get list of all doctors in the hospital')
        canvas.create_window(screenwidth//2,y+gap,window=label)

        clean_results = []

        def cmd():
            results = ms.docs()
            for i in results:
                start_time = str(i[8])
                end_time = str(i[9])
                new_doc_data = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],start_time,end_time)
                clean_results.append(new_doc_data)
            lab = tk.Label(window,text=f'{clean_results}')
            canvas.create_window(screenwidth//2, y+3*gap,window=lab)



        button = tk.Button(window,text='Click Me',command=cmd)
        canvas.create_window(screenwidth//2,y+2*gap,window=button)



    def free_doc(self): #get the list of available doctors
        
        label = tk.Label(window,text='Click the button to find out which doctors are free')
        canvas.create_window(screenwidth//2,y+gap,window=label)

        results = ms.free_doc()

        if results == []:
            messagebox.showerror(title="Error Occured",message='doctor Not Found')
            return

        clean_results = []

        for i in results:
            start_time = str(i[8])
            end_time = str(i[9])
            new_doc_data = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],start_time,end_time)
            clean_results.append(new_doc_data)

        def cmd():
            result = tk.Label(window,text=f'{new_doc_data}')
            canvas.create_window(screenwidth//2,y+3*gap,window=result)

        button = tk.Button(window,text='Search',command=cmd)
        canvas.create_window(screenwidth//2,y+2*gap,window=button)


    def search_doc(self):
        search = tk.Label(window,text='Enter name of doctor')
        canvas.create_window(screenwidth//2,y+gap,window=search)

        search_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+2*gap,window=search_box)

        def search():
            text = search_box.get('1.0','end-1c').split(' ')
            if text == ['']:
                messagebox.showwarning(title='Error Occured',message='Please enter name of the doctor to search')
                return
            
            results = ms.search_doc(*text)

            if results == []:
                messagebox.showerror(title="Error Occured",message='doctor Not Found')
                return

            clean_results = []

            for i in results:
                start_time = str(i[8])
                end_time = str(i[9])
                new_doc_data = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],start_time,end_time)
                clean_results.append(new_doc_data)

            

            label = tk.Label(window,text=f'Results Found\n {clean_results}')
            
            canvas.create_window(screenwidth//2,y+4*gap,window=label)







        search_button = tk.Button(window,text='Search',command=search)
        canvas.create_window(screenwidth//2,y+3*gap,window=search_button)

    def new_doc(self): #add a new doctor

        first_name = tk.Label(window,text='First Name')
        canvas.create_window(screenwidth//2,y+gap,window=first_name)

        first_name_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+2*gap,window=first_name_box)

        last_name = tk.Label(window,text='Last Name')
        canvas.create_window(screenwidth//2,y+3*gap,window=last_name)

        last_name_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+4*gap,window=last_name_box)
        
        age = tk.Label(window,text='Age')
        canvas.create_window(screenwidth//2,y+5*gap,window=age)
        
        age_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+6*gap,window=age_box)

        gender = tk.Label(window,text='Gender')
        canvas.create_window(screenwidth//2,y+7*gap,window=gender)
        
        gender_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+8*gap,window=gender_box)

        pn = tk.Label(window,text='Phone Number')
        canvas.create_window(screenwidth//2,y+9*gap,window=pn)
        
        pn_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+10*gap,window=pn_box)

        mail = tk.Label(window,text='Email')
        canvas.create_window(screenwidth//2,y+11*gap,window=mail)
        
        mail_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+12*gap,window=mail_box)

        start_time = tk.Label(window,text='Shift Start Time')        
        canvas.create_window(screenwidth//2,y+13*gap,window=start_time)

        start_time_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+14*gap,window=start_time_box)
        
        end_time = tk.Label(window,text='Shift End Time')        
        canvas.create_window(screenwidth//2,y+15*gap,window=end_time)

        end_time_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+16*gap,window=end_time_box)
        
        spec = tk.Label(window,text='Speciality')        
        canvas.create_window(screenwidth//2,y+17*gap,window=spec)

        spec_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+18*gap,window=spec_box)
        
        def ok():

            try:
                int(age_box.get('1.0','end-1c'))
                int(pn_box.get('1.0','end-1c'))
                datetime.datetime.strptime(start_time_box.get('1.0','end-1c'),'%h:%M')
                datetime.datetime.strptime(end_time_box.get('1.0','end-1c'),'%h:%M')

            except Exception as e:
                messagebox.showerror('Error Occured', 'One or more arguments are put incorrectly')
                return

            first_name_box_text = first_name_box.get('1.0','end-1c').title()
            last_name_box_text = last_name_box.get('1.0','end-1c').title()
            age_box_text = int(age_box.get('1.0','end-1c'))
            gender_box_text = gender_box.get('1.0','end-1c').title()
            pn_box_text = int(pn_box.get('1.0','end-1c'))
            mail_box_text = mail_box.get('1.0','end-1c').title()
            start_time_text = datetime.datetime.strptime(start_time_box.get('1.0','end-1c'),'%d/%m/%Y')
            end_time_text = datetime.datetime.strptime(end_time_box.get('1.0','end-1c'),'%d/%m/%Y')
            spec_box_text = datetime.datetime.strptime(spec_box.get('1.0','end-1c'),'%d/%m/%Y')

            data = [first_name_box_text,last_name_box_text,age_box_text,gender_box_text,pn_box_text,mail_box_text,spec_box_text,start_time_text,end_time_text,spec_box_text]

            if len(first_name_box_text) > 45 or len(last_name_box_text) > 45 or len(str(pn_box_text)) > 10:
                messagebox.showerror(title="Error Occured",message='Text arguments have exceeded the word limit')

            label = tk.Label(window,text='Added Doctor in Database')
            canvas.create_window(screenwidth//2,y+19*gap,window=label)
            label.after(3000,func=clear_item)
            ok_button.after(4000,func=recover_wid)

            try:
                ms.add_doc(*data)
            except Exception as e:
                messagebox.showerror(title='Error Occured',message=e)
                return
            


        ok_button = tk.Button(window,text='Add Doctor',command=ok)
        ok_button.pack()
        canvas.create_window(screenwidth//2,y+20*gap,window=ok_button)

class Admin:
    
    def user(self):
        cred = tk.Label(window,text='Enter admin details, sepereate username and password by a space')
        canvas.create_window(screenwidth//2,y,window=cred)

        cred_text = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+gap,window=cred_text)

        def cmd():
            result = ms.check_admin(*cred_text.get('1.0','end-1c').split(' '))
            if result == 0:
                messagebox.showerror(title="Error Occured",message='Username or Password is incorrect')
            else:
                label = tk.Label(window,text='Login Successful')
                canvas.create_window(screenwidth//2,y+3*gap,window=label)

        ok_button = tk.Button(window,text='Login',command=cmd)
        canvas.create_window(screenwidth//2,y+2*gap,window=ok_button)
        



class Prescription:
    def suggest_meds(self):
        dis = tk.Label(window,text='Enter Disease')
        canvas.create_window(screenwidth//2,y,window=dis)

        dis_box = tk.Text(window,height=1,width=20)
        canvas.create_window(screenwidth//2,y+gap,window=dis_box)

        def cmd():
            print(dis_box.get('1.0','end-1c').lower())
            result = ms.suggest_medicine(dis_box.get('1.0','end-1c').lower())

            if result == [] or not result:
                messagebox.showerror(title='Error Occured',message='No Medicine with that disease was found, please enter the medicine name in the database')
            else:
                rows = len(result)
                columns = len(result[0])

                for i in range(rows):
                    for j in range(columns):
                        
                        table = tk.Entry(window, width=20, fg='blue',
                                    font=('Arial',16,'bold'))
                        


                        table.grid(row=i, column=j,sticky=tk.NSEW)
                        # canvas.create_window(0,y+2*gap,row=)
                        table.insert(tk.END, result[i][j])
        
        ok_button = tk.Button(window,text='Suggest',command=cmd)
        canvas.create_window(screenwidth//2,y+2*gap,window=ok_button)
        
        

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
            elif meths.get() == 'search_doc':
                doctor.search_doc()


        methods_drop = tk.OptionMenu(window,meths,*methods,command=cho)
        canvas.create_window(screenwidth//2,dropdown.winfo_height()+50,window=methods_drop)

    elif stringvar.get() == 'Home':

        main = tk.Label(window, text= 'HOSPITAL MANAGEMENT SYSTEM',font=('Franklin Gothic Demi',25))
        canvas.create_window(screenwidth//2,screenheight//2,window=main)

        made_by = tk.Label(window,text='Made by- Kartavya Bang \nClass - 12th A',font=('Franklin Gothic Demi',15))
        canvas.create_window(screenwidth-200,screenheight-23,window=made_by)

    elif stringvar.get() == 'Admin':
        admin = Admin()

        methods = [attr for attr in dir(Admin) if attr.startswith('__') is False]

        meths = tk.StringVar(window,methods[0])

        def cho(event):
            clear_item()
            recover_wid()
            if meths.get() == 'user':
                admin.user()
            # elif meths.get() == 'history':
            #     patient.history()
            # elif meths.get() == 'last_visited':
            #     patient.last_visited()
            # elif meths.get() == 'search_patient':
            #     patient.search_patient()


        methods_drop = tk.OptionMenu(window,meths,*methods,command=cho)
        canvas.create_window(screenwidth//2,dropdown.winfo_height()+50,window=methods_drop)

    elif stringvar.get() == 'Prescription':
        pres = Prescription()

        methods = [attr for attr in dir(pres) if attr.startswith('__') is False]
        
        meths = tk.StringVar(window,methods[0])

        def cho(event):
            clear_item()
            recover_wid()
            if meths.get() == 'suggest_meds':
                pres.suggest_meds()


        methods_drop = tk.OptionMenu(window,meths,*methods,command=cho)
        canvas.create_window(screenwidth//2,dropdown.winfo_height()+50,window=methods_drop)

mods = []
for i in os.listdir('./modules'):
    if i.endswith('.py'):
        mods.append(i.split('.py')[0].title())

mods.sort()

stringvar = tk.StringVar(window,mods[2])
intvar = tk.IntVar(window)
button1 = tk.Button(window,command=winquit, text = "Exit",font=('Segoe UI',18,'bold'))


canvas.create_window(0,0,anchor='nw',window=button1)

dropdown = tk.OptionMenu(window,stringvar,*mods,command=choice)
canvas.create_window(screenwidth//2,0,anchor='n',window=dropdown)  

choice('opt')

window.mainloop()


