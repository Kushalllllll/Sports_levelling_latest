from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

#func
def login_user():
    if userEntry.get()=='' or passEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='root')
            mycursor=con.cursor() 
        except:
            messagebox.showerror('Error','Database connectivity issue!')
            return 
        mycursor.execute('use userdata')
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(userEntry.get(),passEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password!')
            Lgwin.destroy()
            import start
        else:
            messagebox.showinfo('Welcome','Login successfull')
        Lgwin.destroy()
        import home

        

def signup_page():
    Lgwin.destroy()
    import signup

def start_page():
    Lgwin.destroy()
    import start

def hide():
    openeye.config(file='closeye.png')
    passEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if userEntry.get()=='Username':
        userEntry.delete(0,END)


def pass_enter(event):
    if passEntry.get()=='Password':
        passEntry.delete(0,END)


#Gui
Lgwin=Tk()
Lgwin.geometry('800x600+50+50')
Lgwin.resizable(0,0)
Lgwin.title("Login")
bgImage=ImageTk.PhotoImage(file='bg.png')

bgLable=Label(Lgwin,image=bgImage)
bgLable.place(x=0,y=0)

arrow=PhotoImage(file='arrow.png')
arrowButton=Button(Lgwin,image=arrow,bd=0,bg="white",activebackground="white",cursor='hand2',command=start_page)
arrowButton.place(x=230,y=100)

heading=Label(Lgwin,text='WELCOME !',font=("Aharoni",25,"bold"),bg='white')
heading.place(x=240,y=140)
subHeading=Label(Lgwin,text='Sign in to countinue',font=("Aharoni",15),bg='white')
subHeading.place(x=240,y=180)

userEntry=Entry(Lgwin, width=30,font=("Aharoni",15),bg='white',bd=0)
userEntry.place(x=230,y=240)
userEntry.insert(0,'Username')
userEntry.bind('<FocusIn>',user_enter)
Frame(Lgwin,width=340,height=2,bg='deepskyblue').place(x=230,y=270)

passEntry=Entry(Lgwin, width=30,font=("Aharoni",15),bg='white',bd=0)
passEntry.place(x=230,y=300)
passEntry.insert(0,'Password')
passEntry.bind('<FocusIn>',pass_enter)
Frame(Lgwin,width=340,height=2,bg='deepskyblue').place(x=230,y=330)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(Lgwin,image=openeye,bd=0,bg="white",activebackground="white",cursor='hand2',command=hide)
eyeButton.place(x=545,y=300)

loginButton=Button(Lgwin,text='LOGIN',font=("Aharoni",15,"bold"),fg='white',bg='royalblue',activeforeground='white',activebackground='deepskyblue',cursor='hand2',bd=1,width=25, command=login_user)
loginButton.place(x=240,y=380)

signupLabel=Label(Lgwin,text="Don't have an account?", font=("Aharoni",10),bg='white' )
signupLabel.place(x=240,y=460)
newButton=Button(Lgwin,text='Signup',font=("Aharoni",10,"underline"),fg='blue',bg='white',activeforeground='deepskyblue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newButton.place(x=380,y=458)


Lgwin.mainloop()