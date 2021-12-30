from database import create_table, add_entry, get_entries
from datetime import datetime

menu = """Select on of the following options:
1) Add new entry
2) View Entries
3) Exit

Your Selection: """

print("Welcome to the journal!")

user_input = input(menu)

def new_entry():
    entry = input("What would you like to journal? ")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    add_entry(entry, dt_string)

def view_entries(entries):
    for e in entries:
            print(f"{e[1]}\n{e[0]}\n")

create_table()

while user_input != "3":
    if user_input == "1":
        new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("Invalid, enter 1, 2, or 3")
    user_input = input(menu)

print("Program closed")
