import sqlite3 as sql

con = sql.connect("database.db")
cursor = con.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS UserAuthentication (
username TEXT PRIMARY KEY,
password TEXT NOT NULL)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS UserProfiles (
user_id TEXT PRIMARY KEY,
last_name TEXT NOT NULL,
first_name TEXT)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Categories (
category_type TEXT PRIMARY KEY,
category_description TEXT NOT NULL)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Expenses (
expense_id INT PRIMARY KEY,
amount TEXT NOT NULL,
category TEXT NOT NULL,
date DATE NOT NULL,
time TIME NOT NULL
description TEXT,
user TEXT NOT NULL)''')

data = [("ass", "cheeks"), ("cock", "sucker")]

cursor.executemany('''INSERT INTO UserAuthentication (username, password) VALUES (?, ?)''', data)

con.commit()

# for row in cursor.execute("SELECT * FROM UserAuthentication"):
#     print(row)

con.close()