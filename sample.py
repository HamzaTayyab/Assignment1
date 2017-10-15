#imporitng every thing from tkinter
from Tkinter import *
import tkMessageBox
import sqlite3
from query import  *
from Quizer import *
from student import *

#Library for profiling
import yappi


class Users:
    def __init__(self,window):
        self.window=window
        self.window.title("Online Quiz Form!")
        window.configure(background="black")
        window.geometry("640x480")

        self.l1=Label(window,text="Username",background="black",foreground="white")
        self.l1.place(x=100,y=100)
        self.l2=Label(window,text="Password",background="black",foreground="white")
        self.l2.place(x=100, y=120)


        self.E1 = Entry(self.window,bd=2)
        self.E1.place(x=160,y=100)
        self.E2 = Entry(window,bd=2,textvariable="password", show='*')
        self.E2.place(x=160, y=120)

        self.button = Button(window, text="Log IN", command=self.login)
        self.button.place(x=160, y=170)


    def login(self):
        u_name=self.E1.get()
        password=self.E2.get()

        for x in result:
            if (x[0]==u_name and x[1]==password):
                if(x[2]=="faculty"):
                    tkMessageBox.showinfo("LoggedIn!")
                    self.clear()
                    addQ(window)
                    break
                elif(x[2]=="student"):
                    self.clear()
                    Welcome(window)
                    break
        else:
            tkMessageBox.showinfo("NotLoggedIn!", "Incorrect user Id or Password")


                # Function to clear Window
    def clear(self):
        self.l1.place_forget()
        self.l2.place_forget()

        self.E1.place_forget()
        self.E2.place_forget()

        self.button.place_forget()
        return  True

yappi.start()

if __name__=="__main__":
    window = Tk()
    obj = Users(window)
    window.mainloop()

yappi.get_func_stats().print_all()

yappi.get_thread_stats().print_all()
print yappi.get_mem_usage()