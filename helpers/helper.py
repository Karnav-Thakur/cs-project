import mysql.connector

def start_new(host,user,db,pw):
    db = mysql.connector.connect(host=host,user=user,passwd=pw,database=db)
    c = db.cursor()
    c.execute()