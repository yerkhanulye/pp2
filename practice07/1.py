from connect import connect
import os

def inserting_data_from_console():
    name = input("Name: ")
    phone = input("Phone: ")
    
    
    conn = connect()
    cur = conn.cursor()
    cur.execute ("Insert INTO phonebook (name, phone) Values (%s, %s)", (name, phone))
    
    conn.commit()
    cur.close()
    conn.close()
    print()

inserting_data_from_console()
    


