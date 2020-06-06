from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import pymysql
from tkcalendar import DateEntry


root=Tk()
root.title("College Management")
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
root.geometry("%dx%d"%(screen_width,screen_height))

def dbconfig():
    global mycurosor,con
    con=pymysql.connect(host="localhost",user="root",db="college_management")
    mycurosor=con.cursor()



def removeallwidget():
    #global root
    for widget in root.winfo_children():
        #print(widget)
        widget.grid_remove()

def mainheading():
    lab=Label(root,text="College Management System",bg="green",font=("Ariel",40,"bold"),padx=400)
    lab.grid(row=0,column=0,columnspan=10)

def back1():
    removeallwidget()
    student1()

def registeredstdata():
    print(dobentryv.get())

entrancenamev=StringVar(root,value="JEECUP")
totalmarksentryv=StringVar(root,value="600")
def conditional(event):
    a=admissiontypeentryv.get()
    if a=="Entrance":
        lab=Label(root,text="Entrance Exam Name",font=("Ariel",20))
        lab.grid(row=6,column=3)
        entrancename=Entry(root,state=DISABLED,textvar=entrancenamev)
        entrancename.grid(row=7,column=3)

        lab1=Label(root,text="Total Marks",font=("Ariel",20))
        lab1.grid(row=6,column=4)
        totalmarksentry=Entry(root,textvar=totalmarksentryv,state=DISABLED)
        totalmarksentry.grid(row=7,column=4)
        lab2=Label(root,text="Obtain Marks",font=("Ariel",20))
        lab2.grid(row=6,column=5)
        obtainmarksentry=Entry(root)
        obtainmarksentry.grid(row=7,column=5)
    elif a=="Direct":
        lab = Label(root, text="Entrance Exam Name", font=("Ariel", 20))
        lab.grid(row=6, column=3)
        entrancename = Entry(root, state=DISABLED)
        entrancename.grid(row=7, column=3)

        lab1 = Label(root, text="Total Marks", font=("Ariel", 20))
        lab1.grid(row=6, column=4)
        totalmarksentry = Entry(root,state=DISABLED)
        totalmarksentry.grid(row=7, column=4)
        lab2 = Label(root, text="Obtain Marks", font=("Ariel", 20))
        lab2.grid(row=6, column=5)
        obtainmarksentry = Entry(root,state=DISABLED)
        obtainmarksentry.grid(row=7, column=5)
    print(a)

admissiontypeentryv=StringVar()
nameentryv=StringVar()
fnameentryv=StringVar()
mnameentryv=StringVar()
dobentryv=StringVar()
qualificationentryv=StringVar()
addressentryv=StringVar()
passentryv=StringVar()


def studentregistration():
    removeallwidget()
    mainheading()
    btn=Button(root,text="Back",bd=5,font=("Ariel",10),command=back1)
    btn.grid(row=3,column=0)
    lab=Label(root,text="New Student Registration",font=("Ariel",20,"bold"))
    lab.grid(row=4,column=4)
    lab8=Label(root,text="Admission Type",font=("Ariel",20))
    lab8.grid(row=5,column=3)
    admissiontypeentry=Combobox(root,values=["Entrance","Direct"],textvar=admissiontypeentryv,state="readonly")
    admissiontypeentry.grid(row=5,column=5)
    admissiontypeentry.bind("<<ComboboxSelected>>",conditional)
    lab1=Label(root,text="Full Name",font=("Ariel",20))
    lab1.grid(row=8,column=3)
    nameentry=Entry(root,textvar=nameentryv,border=10)
    nameentry.grid(row=8,column=5)
    lab2 = Label(root, text="Father's Name", font=("Ariel", 20))
    lab2.grid(row=9, column=3)
    fnameentry = Entry(root,textvar=fnameentryv,border=10)
    fnameentry.grid(row=9, column=5)
    lab3 = Label(root, text="Mother's Name", font=("Ariel", 20))
    lab3.grid(row=10, column=3)
    mnameentry = Entry(root,textvar=mnameentryv,border=10)
    mnameentry.grid(row=10, column=5)
    lab4 = Label(root, text="Date Of Birth", font=("Ariel", 20))
    lab4.grid(row=11, column=3)
    dobentry=DateEntry(root,background="blue",border=10,date_pattern="DD-MM-YYYY",textvar=dobentryv,state="readonly")
    dobentry.grid(row=11,column=5)
    lab5 = Label(root, text="Qualification", font=("Ariel", 20))
    lab5.grid(row=12, column=3)
    qualificationentry = Combobox(root,values=["10th","12th"],textvar=qualificationentryv,state="readonly")
    qualificationentry.grid(row=12, column=5)
    lab6 = Label(root, text="Address", font=("Ariel", 20))
    lab6.grid(row=13, column=3)
    addressentry = Entry(root,textvar=addressentryv,border=10)
    addressentry.grid(row=13, column=5)
    lab7=Label(root,text="Password",font=("Ariel",20))
    lab7.grid(row=14,column=3)
    passentry=Entry(root,textvar=passentryv,border=10)
    passentry.grid(row=14,column=5)

    btn1=Button(root,text="Submit",bd=10,font=("Ariel",20,"bold"),command=registeredstdata)
    btn1.grid(row=15,column=4)


def back():
    removeallwidget()
    homepage()

def student1():
    removeallwidget()
    mainheading()
    lab=Label(root,text="Student LogIn Form",font=("Ariel",30))
    lab.grid(row=3,column=4)
    btn2=Button(root,text="Back",bd=5,command=back)
    btn2.grid(row=3,column=1)
    lab1=Label(root,text="RollNo",font=("Ariel",20))
    lab1.grid(row=4,column=3)
    lab2 = Label(root, text="Password", font=("Ariel", 20))
    lab2.grid(row=5, column=3)
    rollentry=Entry(root)
    rollentry.grid(row=4,column=5)
    passentry = Entry(root)
    passentry.grid(row=5, column=5)
    btn = Button(root, text="LogIN", font=("Ariel", 20, "bold"), bd=10)
    btn.grid(row=6, column=4)
    btn1 = Button(root, text="New Registration", font=("Ariel", 20, "bold"), bd=10,command=studentregistration)
    btn1.grid(row=7, column=4)



def newteacherentry():
    removeallwidget()
    mainheading()
    head=Label(root,text="New Teacher Entry",font=("Ariel",30,"bold"))
    head.grid(row=3,column=4)
    btn=Button(root,text="Back",bd=5,command=institute1)
    btn.grid(row=3,column=1)
    lab=Label(root,text="Full Name",font=("Ariel",20))
    lab.grid(row=4,column=3)
    tnameentry=Entry(root)
    tnameentry.grid(row=4,column=5)
    lab1=Label(root,text="Father's Name",font=("Ariel",20))
    lab1.grid(row=5,column=3)
    tfnameentry=Entry(root)
    tfnameentry.grid(row=5,column=5)
    lab2=Label(root,text="Mother's Name",font=("Ariel",20))
    lab2.grid(row=6,column=3)
    tmnameentry=Entry(root)
    tmnameentry.grid(row=6,column=5)
    lab3=Label(root,text="Date Of Birth",font=("Ariel",20))
    lab3.grid(row=7,column=3)
    tdobentry=DateEntry(root,date_pattern="DD-MM-YYYY",state="readonly")
    tdobentry.grid(row=7,column=5)
    lab4=Label(root,text="Qualification",font=("Ariel",20))
    lab4.grid(row=8,column=3)
    tqualification=Combobox(root,values=["B.Tech","M.Tech","Ph.D"],state="readonly")
    tqualification.grid(row=8,column=5)
    lab5=Label(root,text="Mobile Number",font=("Ariel",20))
    lab5.grid(row=9,column=3)
    tmobilenumber=Entry(root)
    tmobilenumber.grid(row=9,column=5)






def institute1():
    removeallwidget()
    mainheading()
    lab = Label(root, text="Teacher LogIn Form", font=("Ariel", 30))
    lab.grid(row=3, column=4)
    btn=Button(root,text="Back",bd=5,command=homepage)
    btn.grid(row=3,column=1)
    lab1 = Label(root, text="UserId", font=("Ariel", 20))
    lab1.grid(row=4, column=3)
    lab2 = Label(root, text="Password", font=("Ariel", 20))
    lab2.grid(row=5, column=3)
    rollentry = Entry(root)
    rollentry.grid(row=4, column=5)
    passentry = Entry(root)
    passentry.grid(row=5, column=5)
    btn1 = Button(root, text="LogIN", font=("Ariel", 20, "bold"), bd=10)
    btn1.grid(row=6, column=4)
    btn2 = Button(root, text="New Entry", font=("Ariel", 20, "bold"), bd=10,command=newteacherentry)
    btn2.grid(row=7, column=4)

def homepage():
    removeallwidget()
    mainheading()
    btn=Button(root,text="Student",font=("Ariel",20,"bold"),bd=10,command=student1)
    btn.grid(row=1,column=3)
    btn = Button(root, text="Institute", font=("Ariel", 20, "bold"),bd=10,command=institute1)
    btn.grid(row=1, column=5)




mainheading()
homepage()
mainloop()