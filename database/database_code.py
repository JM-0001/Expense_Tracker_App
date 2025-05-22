import sqlite3 as sql


conn = sql.connect("database.db")
cursor = conn.cursor()

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
user TEXT NOT NULL,
amount REAL NOT NULL,
category TEXT NOT NULL,
date DATE NOT NULL,
time TIME NOT NULL,
description TEXT)''')


# def insert_new_user(user:dict):
#     # user dict contains the ff. keys: username, last_name, first_name (optional), password
#     pass

# def insert_expense(username:str, amount:float, category:str, date, time, desc:str):
#     pass

# def delete_expense(expense_id:int):
#     pass

# def remove_user():
#     pass


# username = input("username: ")
# password = input("password: ")

# cursor.execute("INSERT INTO UserAuthentication VALUES (:username, :password)", {'username': username, 'password': password})

conn.commit()

# for row in cursor.execute("SELECT * FROM UserAuthentication"):
#     print(row)

conn.close()