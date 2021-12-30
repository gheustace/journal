import sqlite3

connection = sqlite3.connect("data.db")

def create_table():
    connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")
    connection.commit()

def add_entry(content, date):
    connection.execute("INSERT INTO entries VALUES (?, ?);",
    (content, date))
    connection.commit()

def get_entries():
    return connection.execute("SELECT * FROM entries")
