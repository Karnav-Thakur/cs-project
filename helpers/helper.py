import mysql.connector

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
            print(e)
            
        try:
            self.c.execute('CREATE TABLE medicine (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(45), dose VARCHAR(10), price bigint);')
            # self.c.execute('CREATE TABLE report (id int PRIMARY KEY AUTO_INCREMENT, patient_first_name VARCHAR(45), patient_last_name VARCHAR(45), doctor_first_name VARCHAR(45), doctor_last_name VARCHAR(45), ')
        except mysql.connector.errors.ProgrammingError:
            pass

    def search_doc(self,table,ppin):
        # self.c.execute('SELECT ppin FROM {} WHERE ppin={}'.format((table,ppin)))
        self.c.execute('SELECT * FROM doctor WHERE ppin = 1')
        for x in self.c:
            return x


if __name__ == "__main__":
    ms = MySQL(host='localhost',user='root',db='hms',pw='12345678')
    ms.start_new()
    print(ms.search_doc(table="doctor",ppin=1))