# database.py

import sqlite3
from sqlite3 import Error
import os

def create_connection():
    conn = None
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "repairs.db")
    
    try:
        conn = sqlite3.connect(db_path)
    except Error as e:
        print(e)

    return conn

def init_database():
    conn = create_connection()
    
    if conn is not None:
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS repairs (
            id INTEGER PRIMARY KEY,
            Num TEXT NOT NULL,
            Date TEXT NOT NULL,
            Location TEXT NOT NULL,
            Description TEXT NOT NULL,
            Reporter TEXT NOT NULL,
            Phonenum TEXT NOT NULL,
            Solution TEXT,
            Stuff TEXT,
            Consumables TEXT,
            State TEXT
        );
        """

        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)
        
        conn.close()
    else:
        print("Error! Cannot create the database connection.")
