import sqlite3
from Tkinter import *
from query import *

class addQ:
    def __init__(self,master):
        self.master = master
        master.configure(background="black")
        master.geometry("640x480")

        self.welcom = Label(self.master, text="Welcome to Faculty Mode!",font=("Courier", 20), bg="white", fg="black")
        self.welcom.place(x=150, y=50)
        self.label3 = Label(self.master, text='Enter the Subject',background="black",fg="white")
        self.label3.place(x=100,y=120)
        self.text1 = StringVar()
        self.text_entry = Entry(self.master, textvariable=self.text1)
        self.text_entry.place(x=210, y=120)

#buttons for MCQ's or True False

        self.label=Label(self.master,text="Select the Question type", background="black",foreground="white")
        self.label.place(x=100,y=180)
        self.button4 = Button(master, text="Questions",command=self.MCQ)
        self.button4.place(x=250, y=180)

    # function to add MCQ's
    def MCQ(self):
        # Replacing the above Window to get questions
        self.clear();
        # Label Tag for Questions
        self.label1 = Label(self.master, text='Enter Questions', background="black", fg="white")
        self.label1.place(x=50, y=120)
        # Getting Question
        self.q = StringVar()
        self.q_entry = Entry(self.master, textvariable=self.q, width=100)
        self.q_entry.place(x=150, y=120)
        # Label Tag for Correct OPtions for MCQ's
        self.crct = Label(self.master, text='Correct Option', background="black", fg="white")
        self.crct.place(x=50, y=140)

        # Label Tag for All OPtions
        self.lbe1 = Label(self.master, text='Options', background="black", fg="white")
        self.lbe1.place(x=50, y=160)

        # Getting Correct Options
        self.CO = StringVar()
        self.CO_entry = Entry(self.master, textvariable=self.CO)
        self.CO_entry.place(x=150, y=140)

        # Getting All Options
        self.O1 = StringVar()
        self.O1_entry = Entry(self.master, textvariable=self.O1)
        self.O1_entry.place(x=150, y=160)

        self.O2 = StringVar()
        self.O2_entry = Entry(self.master, textvariable=self.O2)
        self.O2_entry.place(x=270, y=160)

        self.O3 = StringVar()
        self.O3_entry = Entry(self.master, textvariable=self.O3)
        self.O3_entry.place(x=370, y=160)

        # Button to Exit
        self.Exit = Button(self.master, text="Exit", command=self.exit)
        self.Exit.place(x=260, y=180)

        # Button for True false
        self.button = Button(self.master,width="10", text="Skip -> T/F", command=self.T_F)
        self.button.place(x=500, y=300)
        # Button to Add more MCQ's
        self.Add = Button(self.master, text="Add", command= self.query)
        self.Add.place(x=290, y=180)

        self.Add = Button(self.master, text="Next", command=self.MCQ)
        self.Add.place(x=500, y=250)

 #function to clear window
    def clear(self):
        self.label.place_forget()
        self.label3.place_forget()
        self.text_entry.place_forget()
        self.button4.place_forget()

# Function to exit window
    def exit(self):
        self.master.destroy()

    def qryT(self):
        # for True False
        s = self.text_entry.get()
        tf = self.CO_tf.get()
        Q = self.qtf_entry.get()
        O1 = self.O1_entry.get()
        O2 = self.O2_entry.get()
        O3 = self.O3_entry.get()
        curr.execute("INSERT INTO  quiz values(?,?,?,?,?,?,'Truefalse')", (s,Q,O1,O2,O3,tf))
        conn.commit()

    def query(self):
        #for MCQ's
        s=self.text_entry.get()
        q=self.q_entry.get()
        O1= self.O1_entry.get()
        O2= self.O2_entry.get()
        O3 = self.O3_entry.get()
        CO=self.CO_entry.get()
        curr.execute("INSERT INTO  quiz values(?,?,?,?,?,?,'mcq')",(s,q,O1,O2,O3,CO))
        conn.commit()



    # function to add True False
    def T_F(self):
        # Replacing the above Window to get questions
        self.clear();
        self.lbe1.place_forget()
        self.O1_entry.place_forget()
        self.O3_entry.place_forget()
        self.O2_entry.place_forget()
        self.button.place_forget()


        # Label Tag for Questions
        self.label1 = Label(self.master, text='Enter Questions', background="black", fg="white")
        self.label1.place(x=50, y=120)
        # Getting Question
        self.qtf = StringVar()
        self.qtf_entry = Entry(self.master, textvariable=self.qtf, width=100)
        self.qtf_entry.place(x=150, y=120)
        # Label Tag for Correct OPtions for MCQ's
        self.crct = Label(self.master, text='Correct Option', background="black", fg="white")
        self.crct.place(x=50, y=140)


        # Getting Correct Options
        self.COtf = StringVar()
        self.CO_tf = Entry(self.master, textvariable=self.COtf)
        self.CO_tf.place(x=150, y=140)


        # Button to Exit
        self.Exit = Button(self.master, text="Exit", command=self.exit)
        self.Exit.place(x=260, y=180)

        # Button for True false
        self.button = Button(self.master,width="10", text="Skip -> MCQ's", command=self.MCQ)
        self.button.place(x=500, y=300)
        self.skip = self.button['text']

        # Button to Add more true False

        self.Add = Button(self.master, text="Add", command=self.qryT)
        self.Add.place(x=290, y=180)

        self.Add = Button(self.master, text="Next", command=self.T_F)
        self.Add.place(x=500, y=250)