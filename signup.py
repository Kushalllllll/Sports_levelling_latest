from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    mailEntry.delete(0,END)
    userEntry.delete(0,END)
    passEntry.delete(0,END)


def connect_database():
    if mailEntry.get()=='' or userEntry.get()=='' or passEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='root')
            mycursor=con.cursor() 
        except:
            messagebox.showerror('Error','Database connectivity issue!')
            return
        mycursor.execute('use userdata')
        query1='select * from data where username=%s'
        mycursor.execute(query1,(userEntry.get()))
        row1=mycursor.fetchone()

        query2='select * from data where email=%s'
        mycursor.execute(query2,(mailEntry.get()))
        row2=mycursor.fetchone()

        if row1 !=None:
            messagebox.showerror('Error','Username already exits!')
        elif row2 !=None:
            messagebox.showerror('Error','Email already exits!')
        
        else:
            query='insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(mailEntry.get(),userEntry.get(),passEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Account created!')
            clear()
            Sgwin.destroy()
            import signin

def login_page():
    Sgwin.destroy()
    import signin


def start_page():
    Sgwin.destroy()
    import start

def hide():
    openeye.config(file='closeye.png')
    passEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passEntry.config(show='')
    eyeButton.config(command=hide)


def mail_enter(event):
    if mailEntry.get()=='Email':
        mailEntry.delete(0,END)

def user_enter(event):
    if userEntry.get()=='Username':
        userEntry.delete(0,END)


def pass_enter(event):
    if passEntry.get()=='Password':
        passEntry.delete(0,END)


Sgwin=Tk()
Sgwin.geometry('800x600+50+50')
Sgwin.resizable(0,0)
Sgwin.title("Signup")
bgImage=ImageTk.PhotoImage(file='bg.png')

bgLable=Label(Sgwin,image=bgImage)
bgLable.place(x=0,y=0)

arrow=PhotoImage(file='arrow.png')
arrowButton=Button(Sgwin,image=arrow,bd=0,bg="white",activebackground="white",cursor='hand2',command=start_page)
arrowButton.place(x=230,y=100)

heading=Label(Sgwin,text='Hi !',font=("Aharoni",25,"bold"),bg='white')
heading.place(x=240,y=140)
subHeading=Label(Sgwin,text="Create a new account",font=("Aharoni",15),bg='white')
subHeading.place(x=240,y=180)

mailEntry=Entry(Sgwin, width=30,font=("Aharoni",15),bg='white',bd=0)
mailEntry.place(x=230,y=240)
mailEntry.insert(0,'Email')
mailEntry.bind('<FocusIn>',mail_enter)
Frame(Sgwin,width=340,height=2,bg='deepskyblue').place(x=230,y=270)

userEntry=Entry(Sgwin, width=30,font=("Aharoni",15),bg='white',bd=0)
userEntry.place(x=230,y=290)
userEntry.insert(0,'Username')
userEntry.bind('<FocusIn>',user_enter)
Frame(Sgwin,width=340,height=2,bg='deepskyblue').place(x=230,y=320)

passEntry=Entry(Sgwin, width=30,font=("Aharoni",15),bg='white',bd=0)
passEntry.place(x=230,y=340)
passEntry.insert(0,'Password')
passEntry.bind('<FocusIn>',pass_enter)
Frame(Sgwin,width=340,height=2,bg='deepskyblue').place(x=230,y=370)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(Sgwin,image=openeye,bd=0,bg="white",activebackground="white",cursor='hand2',command=hide)
eyeButton.place(x=545,y=340)

SgButton=Button(Sgwin,text='SignUp',font=("Aharoni",15,"bold"),fg='white',bg='royalblue',activeforeground='white',activebackground='deepskyblue',cursor='hand2',bd=1,width=25,command=connect_database)
SgButton.place(x=240,y=400)

signupLabel=Label(Sgwin,text="Already have an account?", font=("Aharoni",10),bg='white' )
signupLabel.place(x=240,y=460)
newButton=Button(Sgwin,text='Login',font=("Aharoni",10,"underline"),fg='blue',bg='white',activeforeground='deepskyblue',activebackground='white',cursor='hand2',bd=0,command=login_page)
newButton.place(x=395,y=458)

Sgwin.mainloop()