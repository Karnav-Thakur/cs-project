import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',passwd='Kartavya2908',database='hms ')
c = db.cursor()

c.execute('CREATE TABLE patient (id int PRIMARY KEY, first_name VARCHAR(45), last_name VARCHAR(45), age int, gender VARCHAR(45), phone_number bigint, email VARCHAR(45), type VARCHAR(45), disease VARCHAR(45));')