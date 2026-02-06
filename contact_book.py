# SQLITE IS: Embedded, Serverless, File-Based, Zero-Configuration
# connect → cursor → execute → fetch → commit → close

import sqlite3 # build in python module to which let python to talk to database

DB_Name = "contact.db"


def get_connection():
    return sqlite3.connect(DB_Name) # connect establish a connect and create a .db file if not present


def create_table():
    conn = get_connection()
    cursor = conn.cursor() # cursor is an object that send SQL commands and receive result

    cursor.execute( 
        """
                   CREATE TABLE IF NOT EXISTS contact(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       email TEXT UNIQUE,
                       phone TEXT,
                       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )
                   """
    )

    conn.commit() # permanently store in db (file)
    conn.close()


def add_contact(name, email, phone):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
                       INSERT INTO contact (name,email,phone)
                       VALUES (?,?,?)
                       """,
            (name, email, phone),
        )
        conn.commit()
        print("Contact Added")
    except sqlite3.IntegrityError:
        print("Something went wrong...!")
        
    finally:
        conn.close()


def list_contacts():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email, phone  FROM contact") # run query - db has prepared the data
    rows = cursor.fetchall() # python collects data
    
    if not rows:
        print("No contacts available")
    else:
        print("\n Contacts: ")
        for row in rows:
            print(row)
    
    conn.close()
    
    
def search_contacts(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM contact WHERE name LIKE ? OR email LIKE ? ", (f"%{keyword}%", f"%{keyword}%"))
    
    rows = cursor.fetchall()
    
    if not rows:
        print("Contact not found")
    else:
        for row in rows:
            print(row)
    
    conn.close()
    
def update_contact(contact_id,name,email,phone):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("UPDATE contact SET name = ?, email = ?, phone = ? WHERE id = ?",(name,email,phone,contact_id))

    if cursor.rowcount == 0:
        print("Contact not found")
    else:
        conn.commit()
        print("Contact updated")
    
    
    conn.close()
    
def delete_contact(contact_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE contact WHERE id = ?",(contact_id))
    
    if cursor.rowcount == 0:
        print("Contact not found")
    else:
        conn.commit()
        print("Contact deleted")
    
    conn.close()   