from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox

root = Tk()
conn = sqlite3.connect("test_student_data.db")

cursor = conn.cursor()

'''
cursor.execute("""CREATE TABLE test_students(
                first name,
                last_name,
                temporary_address,
                permanent_address,
                course_applied,
                contact_number,
                twelve_grade

                )""")
'''

# creating the frame for studennts derails
frame = LabelFrame(root, text="                   STUNDET DETAIL                    ", bg="skyblue")
frame.grid(row=0, column=0, columnspan=5)

# Detail about the students
first_name = Label(frame, text="         First Name       ")
last_name = Label(frame, text="       Last Name         ")
temp_address = Label(frame, text=" Temporary Address")
perm_address = Label(frame, text=" Permanent Address")
course_applied = Label(frame, text="     course Applied    ")
contact_num = Label(frame, text="  Contact Number   ")
twelve_grade = Label(frame, text="           +2 grade        ")

# griding or labelng of the form
first_name.grid(row=0, column=0)
last_name.grid(row=1, column=0)
temp_address.grid(row=2, column=0)
perm_address.grid(row=3, column=0)
course_applied.grid(row=4, column=0)
contact_num.grid(row=5, column=0)
twelve_grade.grid(row=6, column=0)

# Creating the entry box where user give the input
entry1 = Entry(frame, width=50, borderwidth=10)
entry2 = Entry(frame, width=50, borderwidth=10)
entry3 = Entry(frame, width=50, borderwidth=10)
entry4 = Entry(frame, width=50, borderwidth=10)
entry5 = Entry(frame, width=50, borderwidth=10)
entry6 = Entry(frame, width=50, borderwidth=10)
entry7 = Entry(frame, width=50, borderwidth=10)

entry7.grid(row=6, column=1, ipady=2)
entry6.grid(row=5, column=1, ipady=2, pady=10)
entry5.grid(row=4, column=1, ipady=2)
entry4.grid(row=3, column=1, ipady=2, pady=10)
entry3.grid(row=2, column=1, ipady=2)
entry2.grid(row=1, column=1, ipady=2, pady=10)
entry1.grid(row=0, column=1, ipady=2)

# cheating a new frame for the parents details

frame1 = LabelFrame(root, text="              PARENTS DETAILS               ", bg="skyblue")
frame1.grid(row=1, column=0, pady=20, columnspan=5)

first_name1 = Label(frame1, text="         First Name        ")
last_name1 = Label(frame1, text="        Last Name         ")
occupation = Label(frame1, text="        Occupation        ")
contact = Label(frame1, text="            Contact          ")

first_name1.grid(row=0, column=0)
last_name1.grid(row=1, column=0)
occupation.grid(row=2, column=0)
contact.grid(row=3, column=0)

# Creating the entry box where user give the input
entry1_1 = Entry(frame1, width=50, borderwidth=10)
entry2_2 = Entry(frame1, width=50, borderwidth=10)
entry3_3 = Entry(frame1, width=50, borderwidth=10)
entry4_4 = Entry(frame1, width=50, borderwidth=10)

entry4_4.grid(row=3, column=1, ipady=2)
entry3_3.grid(row=2, column=1, ipady=2)
entry2_2.grid(row=1, column=1, ipady=2)
entry1_1.grid(row=0, column=1, ipady=2)

# importing a frame for parents details

button1 = Button(root, text="Import", padx=30, pady=10)
button2 = Button(root, text="delete", padx=30, pady=10)
button3 = Button(root, text="Update", padx=30, pady=10)
button4 = Button(root, text="delete", padx=30, pady=10)

button1.grid(row=2, column=0, columnspan=1)
button2.grid(row=2, column=2, columnspan=1)
button3.grid(row=2, column=4, columnspan=1)
button4.grid(row=2, column=5)

# creating a frame for displaying the icon of the collage
frame2 = LabelFrame(root, text="DISPLAYING DETAILS")
frame2.grid(row=0, column=5)

name = Label(frame2, text=" search ")
name.grid(row=0, column=0)

entry_name = Entry(frame2, width=50, borderwidth=10)
entry_name.grid(row=0, column=1, ipady=2)

my_image = ImageTk.PhotoImage(Image.open("database_soft (2).jpg"))
my_lable = Label(frame2, image=my_image)
my_lable.grid(row=2, column=0, columnspan=2)

search_button = Button(frame2, text="Search")
search_button.grid(row=1, column=1)

conn.commit()
conn.close()
root.mainloop()