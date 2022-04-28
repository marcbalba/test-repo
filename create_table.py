import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE if NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" #for id, to auto increment, use INTEGER PRIMARY KEY instead of data type int
cursor.execute(create_table)

create_table = "CREATE TABLE if NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)" #for table name items
cursor.execute(create_table)


connection.commit()
connection.close()
