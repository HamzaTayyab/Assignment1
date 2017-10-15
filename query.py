import sqlite3
from Tkinter import *


#Setting connection with the data base
conn=sqlite3.connect("Quizer.db")
curr=conn.cursor()

#Getting data from the Users Table
curr.execute("Select * from users")
result=curr.fetchall()

curr.execute("select * from quiz")
quiz=curr.fetchall()