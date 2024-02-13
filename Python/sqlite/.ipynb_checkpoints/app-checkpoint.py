import sqlite3

#this creates a file
conn = sqlite3.connect('database.db')

#this commits it to memory, dissapears when the program closes
# conn=sqlite3.connection(':memory:')


cur= conn.cursor()


conn.close()