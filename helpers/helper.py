import mysql.connector

def start_new(host,user,db,pw):
    db = mysql.connector.connect(host=host,user=user,passwd=pw,database=db)
    c = db.cursor()
    c.execute('CREATE TABLE patient (id int PRIMARY KEY, first_name VARCHAR(45), last_name VARCHAR(45), age int, gender VARCHAR(45), phone_number bigint, email VARCHAR(45), type VARCHAR(45), disease VARCHAR(45));') # patient table
    c.execute('CREATE TABLE doctor (ppin int PRIMARY KEY. first_name VARCHAR(45), last_name VARCHAR(45), age int, gender VARCHAR(45). phone_number bigint, email VARCHAR(45), speciality VARCHAR(45), free_hours ') # doctor table
    c.execute('')
