import sqlite3

#this creates a file
conn = sqlite3.connect('database.db')

#this commits it to memory, dissapears when the program closes
# conn=sqlite3.connection(':memory:')

cur= conn.cursor()

name_list=[
    ('Thayer','Prime'),
    ('Marios','Kosofidis')
]

cur.execute("""CREATE TABLE IF NOT EXISTS data 
              (first_name TEXT, 
              last_name TEXT)""")

cur.executemany("""INSERT INTO data (first_name, last_name) VALUES (?,?)""", name_list)

conn.commit()

cur.close()
conn.close()