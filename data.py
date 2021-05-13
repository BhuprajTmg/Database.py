from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox

root = Tk()

root.title("Students Data")

ico = PhotoImage(file = "stat.png")
root.iconphoto(False, ico)

conn = sqlite3.connect()

root.mainloop()