from tkinter import *
import sqlite3
from tkinter.messagebox import showinfo

root = Tk()
root.title("Database")

# database# Creating a database or connect to one
# c = conn.cursor()
conn = sqlite3.connect("student_data.db")
# Creating cursor
c = conn.cursor()


# Cursor Class is an instance using which you can invoke methods that
# Execute SQLITE statements, fetch data fro the result sets of the quries.

#Creating Table
'''
c.execute("""CREATE TABLE addresses(
             first_name text,
             last_name text,
             city text,
             state text ,
             zipcode integer

 )
 """)
print("Table created Successfully")
'''

def submit():
    conn = sqlite3.connect(("addressBook.db"))
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES (:first_name,:last_name,:city,:state,:zipcode)", {
        'first_name': first_Name1.get(),
        'last_name': second_Name1.get(),
        'city': city1.get(),
        'state': state1.get(),
        'zipcode': zipcode1.get()
    }

              )
    print("Address insterted Successfully")

    conn.commit()
    conn.close()
    first_Name1.delete(0, END)
    second_Name1.delete(0, END)
    city1.delete(0, END)
    state1.delete(0, END)
    zipcode1.delete(0, END)


# Creating Input Field
first_Name = Label(root, text="First Name:").grid(row=0, column=0)

first_Name1 = Entry(root, borderwidth=5, width=35)
first_Name1.grid(row=0, column=1)

second_Name = Label(root, text="Second Name:").grid(row=1, column=0)

second_Name1 = Entry(root, borderwidth=5, width=35)
second_Name1.grid(row=1, column=1)

city_name = Label(root, text="City:").grid(row=2, column=0)

city1 = Entry(root, borderwidth=5, width=35)
city1.grid(row=2, column=1)

state_name = Label(root, text="State:").grid(row=3, column=0)

state1 = Entry(root, borderwidth=5, width=35)
state1.grid(row=3, column=1)

zipcode = Label(root, text="Zip Code:").grid(row=3, column=0)

zipcode1 = Entry(root, borderwidth=5, width=35)
zipcode1.grid(row=3, column=1)

addbutton = Button(root, text="Add Contact", width=20, command=submit).grid(row=4, column=1, pady=5)
displaybutton = Button(root, text="Show Values", width=20).grid(row=5, column=1, pady=10)
deleteLabel = Label(root, text="Select ID: ").grid(row=7, column=0)
deletefield = Entry(root, width=35, borderwidth=5)
deletefield.grid(row=7, column=1, pady=10)
deletebutton = Button(root, text="Delete Items", width=20)
deletebutton.grid(row=8, column=1, pady=10)
updatebutton = Button(root, text="Update Data", width=20)
updatebutton.grid(row=10, column=1, pady=10)




conn.commit()
conn.close()
root.mainloop()