from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

root = Tk()
h = 1024
w = 720
root.title("Apollo Form")
#inserting an icon
root.iconbitmap('C:/Users/sudee/Desktop/programs/tkinter app/images.ico')
root.geometry('1024x720')
#create a database connection
#conn = sqlite3.connect('apollo_forms.db')
#defining a cursor
#c = conn.cursor()
#Create table
#c.execute(""" CREATE TABLE Registrations2(
#Patient TEXT,
#Age INTEGER,
#Gender INTEGER,
#Occupation TEXT,
#Address TEXT)""")
#conn.commit()
#conn.close()

frame = LabelFrame(root)
frame.place(relwidth = 1, relheight = 1, relx = 0, rely = 0)

label_0 = Label(frame, text = "Vistor's form", width = 47, font = ("bold", 25))
label_0.place(x= 70, y=195)

label_1 = Label(frame, text="Patient_name",width=21,fg = "green",font=("bold", 12))
label_1.place(x=300,y=280)

entry_1 = Entry(frame,fg = 'BLUE')
entry_1.place(x=490,y=280)

label_2 = Label(frame, text="Age",width=21,fg = "green",font=("bold", 12))
label_2.place(x=280,y=310)

entry_2 = Entry(frame,fg = 'BLUE')
entry_2.place(x=490,y=315)

label_3 = Label(frame, text="Gender",width=21,fg = "green",font=("bold", 12))
label_3.place(x=282,y=350)

var = IntVar()
Radiobutton(frame, text="Male",padx = 10,fg = 'green' ,variable=var, value=1).place(x=470,y=350)
Radiobutton(frame, text="Female",padx = 10,fg = 'green', variable=var, value=2).place(x=570,y=350)

label_3 = Label(frame, text="Occupation:",width=21,fg = 'green',font=("bold", 12))
label_3.place(x=290,y=380)

entry_3 = Entry(frame,fg = 'BLUE')
entry_3.place(x=492,y=385)


label_4 = Label(frame, text="Address",width=21,fg = 'green',font=("bold", 12))
label_4.place(x=292,y=410)

entry_4 = Entry(frame, width = 45,fg = 'BLUE')
entry_4.place(x=491,y=425)

def OnClick():
    conn = sqlite3.connect('apollo_forms.db')
    #defining a cursor
    c = conn.cursor()
    c.execute("INSERT INTO Registrations2 VALUES(:entry_1, :entry_2, :var, :entry_3, :entry_4)",
              {'entry_1': entry_1.get(),
               'entry_2': entry_2.get(),
               'var': var.get(),
               'entry_3': entry_3.get(),
               'entry_4': entry_4.get()
                  })
    conn.commit()
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    entry_3.delete(0,END)
    entry_4.delete(0,END)
    messagebox.showinfo("1 OF 2","Submitted")
    conn.close()
    
Button(frame, text="Submit",width=10,bg='red',fg='white',command = OnClick).place(x=520,y=485)

def OnClick1():
    #create a database connection
    conn = sqlite3.connect('apollo_forms.db')
    #defining a cursor
    c = conn.cursor()
    c.execute("SELECT * FROM Registrations2")
    records = c.fetchall()
    #print(records)
    print_records = ''
    for record in records:
        print_records += str(record[0])+" " +str(record[1])+" "+str(record[2])+" " + "\n"
        query_label = Label(frame,text=print_records)
        query_label.place(x=650,y=510)

    conn.commit()
    conn.close()
    
query =Button(frame, text="Show Records",width=10,bg='teal',fg='white',command = OnClick1).place(x=590,y=485) 

watermark = ImageTk.PhotoImage(file = "apollo-logo-new.gif")
w = Label(root,image = watermark)
w.pack(side= "top", pady = 19, ipady = 15)

#conn.commit()
#conn.close()
root.mainloop()

