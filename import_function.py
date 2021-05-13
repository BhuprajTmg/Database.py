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
frame.grid(row=0, column=0, columnspan=2)

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
frame1.grid(row=1, column=0, pady=20)

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




##########################
frame4=Frame(root,bg = "gray",bd=10,width=400,height=540)
frame4.grid(row = 0, column = 2, rowspan = 2)


name =Label(frame4, text = " search ")
name.grid(row = 0, column = 0)

entry_name = Entry(frame4, width = 50, borderwidth = 10)
entry_name.grid(row = 0, column =1,ipady = 2)

search_button = Button(frame4, text = "Search")
search_button.grid(row = 1, column =1 )

my_image = ImageTk.PhotoImage(Image.open("experi.jpg"))
my_lable = Label(frame4, image = my_image)
my_lable.grid(row = 2, column = 0, columnspan = 2)

frame5=Frame(root,bg = "gray",bd=10,width=400,height=540)
frame5.grid(row = 1, column = 2, rowspan = 2)

button_ji = Button(frame5, text = "Reatire")
button_ji.grid(row = 0, column = 0)


conn.commit()
conn.close()
root.mainloop()