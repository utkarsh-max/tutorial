from tkinter import *
from tkinter.ttk import Combobox
import pymysql
from tkcalendar import DateEntry


root=Tk()
root.title("College Management")
root.geometry("900x500")

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
    password=passentryv.get()
    dbconfig()
    que='insert into student_detail(Name,Father_Name,Mother_Name,) '


nameentryv=StringVar()
fnameentryv=StringVar()
mnameentryv=StringVar()
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
    admissiontypeentry=Combobox(root,values=["Entrance","Direct"])
    admissiontypeentry.grid(row=5,column=5)
    lab1=Label(root,text="Full Name",font=("Ariel",20))
    lab1.grid(row=6,column=3)
    nameentry=Entry(root,textvar=nameentryv)
    nameentry.grid(row=6,column=5)
    lab2 = Label(root, text="Father's Name", font=("Ariel", 20))
    lab2.grid(row=7, column=3)
    fnameentry = Entry(root,textvar=fnameentryv)
    fnameentry.grid(row=7, column=5)
    lab3 = Label(root, text="Mother's Name", font=("Ariel", 20))
    lab3.grid(row=8, column=3)
    mnameentry = Entry(root,textvar=mnameentryv)
    mnameentry.grid(row=8, column=5)
    lab4 = Label(root, text="Date Of Birth", font=("Ariel", 20))
    lab4.grid(row=9, column=3)
    dobentry=DateEntry(root)
    dobentry.grid(row=9,column=5)
    lab5 = Label(root, text="Qualification", font=("Ariel", 20))
    lab5.grid(row=10, column=3)
    qualificationentry = Combobox(root,values=["10th","12th"],textvar=qualificationentryv)
    qualificationentry.grid(row=10, column=5)
    lab6 = Label(root, text="Address", font=("Ariel", 20))
    lab6.grid(row=11, column=3)
    addressentry = Entry(root,textvar=addressentryv)
    addressentry.grid(row=11, column=5)
    lab7=Label(root,text="Password",font=("Ariel",20))
    lab7.grid(row=12,column=3)
    passentry=Entry(root,textvar=passentryv)
    passentry.grid(row=12,column=5)

    btn1=Button(root,text="Submit",bd=10,font=("Ariel",20,"bold"),command=registeredstdata)
    btn1.grid(row=13,column=4)


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

def institute1():
    removeallwidget()
    mainheading()
    lab = Label(root, text="Teacher LogIn Form", font=("Ariel", 30))
    lab.grid(row=3, column=4)
    lab1 = Label(root, text="UserId", font=("Ariel", 20))
    lab1.grid(row=4, column=3)
    lab2 = Label(root, text="Password", font=("Ariel", 20))
    lab2.grid(row=5, column=3)
    rollentry = Entry(root)
    rollentry.grid(row=4, column=5)
    passentry = Entry(root)
    passentry.grid(row=5, column=5)
    btn = Button(root, text="LogIN", font=("Ariel", 20, "bold"), bd=10)
    btn.grid(row=6, column=4)
    btn1 = Button(root, text="New Entry", font=("Ariel", 20, "bold"), bd=10)
    btn1.grid(row=7, column=4)

def homepage():
    mainheading()
    btn=Button(root,text="Student",font=("Ariel",20,"bold"),bd=10,command=student1)
    btn.grid(row=1,column=3)
    btn = Button(root, text="Institute", font=("Ariel", 20, "bold"),bd=10,command=institute1)
    btn.grid(row=1, column=5)





mainheading()
homepage()





mainloop()