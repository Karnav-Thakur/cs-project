import datetime
from tkinter import messagebox
import mysql.connector
import pytz

class MySQL:
    def __init__(self,host,user,db,pw):
        self.db = mysql.connector.connect(host=host,user=user,passwd=pw,database=db)
        self.c = self.db.cursor()

    def start_new(self):
        try:
            self.c.execute('CREATE TABLE patient (id int PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(45), last_name VARCHAR(45), age int, gender VARCHAR(45), phone_number bigint, email VARCHAR(45), type VARCHAR(45), disease VARCHAR(45),last_visit date);') # patient table
        
        except mysql.connector.errors.ProgrammingError:
            pass

        try:
            self.c.execute('CREATE TABLE doctor (ppin int PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(45), last_name VARCHAR(45), age int, gender VARCHAR(45), phone_number bigint, email VARCHAR(45), speciality VARCHAR(45), shift_start TIME,shift_end TIME);') # doctor table
        
        except mysql.connector.errors.ProgrammingError as e:
            pass
            
        try:
            self.c.execute('CREATE TABLE medicine (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(45), dose VARCHAR(10), price bigint, disease VARCHAR(50));')
        except mysql.connector.errors.ProgrammingError:
            pass

        try:
            self.c.execute('CREATE TABLE history (id int PRIMARY KEY AUTO_INCREMENT, patient_id int, FOREIGN KEY(patient_id) REFERENCES patient(id), disease VARCHAR(45), last_visit date);')
        except mysql.connector.errors.ProgrammingError:
            pass

        try:
            self.c.execute('CREATE TABLE admin (name VARCHAR(45), pass VARCHAR(45));')
        except mysql.connector.errors.ProgrammingError:
            pass

    def search_doc(self,*name):
        self.c.execute('SELECT * FROM doctor WHERE first_name = %s AND last_name = %s',name)
        data = []
        for x in self.c:
            data.append(x)
        return data

    def search_patient(self,*name):
        print(name)
        self.c.execute('SELECT * FROM patient WHERE first_name= %s AND last_name = %s',name)
        data = []
        for x in self.c:
            data.append(x)
        return data

    def add_patient(self,visited_before,*args):
        self.c.execute('SELECT * FROM patient ')

        correct_patient = []

        for x in self.c:
            if args[0] == x[1] and args[1] == x[2]:
                correct_patient.append(x)
                break
        
            


        if visited_before == 1:
            self.c.execute('INSERT INTO history (patient_id,disease,last_visit) VALUES (%s,%s,%s)',(correct_patient[0][0],args[7],args[8]))
            self.c.execute('UPDATE patient SET disease = %s , last_visit = %s, type = %s WHERE id = %s',(args[7],args[8],args[6], correct_patient[0][0]))
            self.db.commit()
            return
        
        self.c.execute('INSERT INTO patient (first_name,last_name,age,gender,phone_number,email,type,disease,last_visit) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',args)
        self.db.commit()

    def history(self,patient):
        self.c.execute('SELECT * FROM history WHERE patient_id = %s',(int(patient),))

        result = []

        for x in self.c:
            result.append(x)
        
        return result

    def free_doc(self):
        tz_india = pytz.timezone('Asia/Kolkata')
        
        now = datetime.datetime.now(tz_india)
                
        self.c.execute('SELECT * FROM doctor WHERE shift_end < %s',(now,))
        data = []

        for x in self.c:
            data.append(x)
        
        return data
    
    def docs(self):
        self.c.execute("SELECT * FROM doctor")
        data = []
        for x in self.c:
            data.append(x)
        
        return data

    def add_doc(self,*args):
        self.c.execute('SELECT * FROM doctor')
        for x in self.c:
            if x[1] ==  args[4]:
                return Exception("Please use a different mobile number")
        
        self.c.execute('INSERT INTO doctor (ppin,first_name,last_name,age,gender,phone_number,email ,speciality,shift_start time ,shift_end time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',args)

    def check_admin(self,*cred):
        self.c.execute('SELECT * FROM admin WHERE name= %s AND pass = %s',cred)
        result = []
        for x in self.c:
            result.append(x)
        
        if result == []:        
            return 0
        
        else:
            return x

    def suggest_medicine(self,disease):

        self.c.execute('SELECT * FROM medicine WHERE disease = %s ',(disease,))

        meds = []

        for x in self.c:
            meds.append(x)
        
        return meds

    def add_med(self,*args):
        self.c.execute('SELECT * FROM medicine WHERE name = %s',(args[0],))
        if self.c.fetchall() == []: 
            self.c.execute('INSERT INTO medicine (name,dose,price,disease) VALUES (%s,%s,%s,%s)',args)
            self.db.commit()
        else:
            messagebox.showerror(title='Error Occured',message='Medicine Already Exists')



if __name__ == "__main__":
    ms = MySQL(host='localhost',user='root',db='hms',pw='12345678')
    ms.add_med('Aptio',"1",2000,'xyz')