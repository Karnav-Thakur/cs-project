import datetime
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
            self.c.execute('CREATE TABLE medicine (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(45), dose VARCHAR(10), price bigint);')
            # self.c.execute('CREATE TABLE report (id int PRIMARY KEY AUTO_INCREMENT, patient_first_name VARCHAR(45), patient_last_name VARCHAR(45), doctor_first_name VARCHAR(45), doctor_last_name VARCHAR(45), ')
        except mysql.connector.errors.ProgrammingError:
            pass

    def search_doc(self,*name):
        self.c.execute('SELECT * FROM doctor WHERE first_name = %s AND last_name = %s',name)
        data = []
        for x in self.c:
            data.append(x)
        return data

    def search_patient(self,*name):
        self.c.execute('SELECT * FROM patient WHERE first_name= %s AND last_name = %s',name)
        data = []
        for x in self.c:
            data.append(x)
        return data

    def add_patient(self,*args):
        self.c.execute('SELECT * FROM patient')

        for x in self.c:
            if x[5] == int(args[4]):
                return Exception('Please use a different mobile number')
        
        self.c.execute('INSERT INTO patient (first_name,last_name,age,gender,phone_number,email,type,disease,last_visit) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',args)
        self.db.commit()

    def free_doc(self):
        tz_india = pytz.timezone('Asia/Kolkata')
        
        now = datetime.datetime.now(tz_india)
                
        self.c.execute('SELECT * FROM doctor WHERE shift_end < %s',(now,))
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
                


if __name__ == "__main__":
    ms = MySQL(host='localhost',user='root',db='hms',pw='12345678')
    # ms.start_new()
    # print(ms.search_doc(table="doctor",ppin=1))
    # print(ms.add_doc())
    print(ms.free_doc())