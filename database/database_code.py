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

con.commit()

# for row in cursor.execute("SELECT * FROM UserAuthentication"):
#     print(row)

con.close()