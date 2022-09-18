import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',passwd='12345678')
c = db.cursor()

c.execute('CREATE DATABASE hms')
# c.execute('CREATE TABLE patient (id int PRIMARY KEY, first_name VARCHAR(45), last_name VARCHAR(45), age int, gender VARCHAR(45), phone_number bigint, email VARCHAR(45), type VARCHAR(45), disease VARCHAR(45));')