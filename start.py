from tkinter import *
from PIL import ImageTk

#Func
def login_page():
    Swin.destroy()
    import signin

def signup_page():
    Swin.destroy()
    import signup

#GUI
Swin=Tk()
Swin.geometry('800x600+50+50')
Swin.resizable(0,0)
Swin.title("Start")
bgImage=ImageTk.PhotoImage(file='bg.png')

bgLable=Label(Swin,image=bgImage)
bgLable.place(x=0,y=0)


heading=Label(Swin,text='HELLO !',font=("Aharoni",25,"bold"),bg='white')
heading.place(x=340,y=140)
subHeading=Label(Swin,text='Welcome to sports leveling',font=("Aharoni",15),bg='white')
subHeading.place(x=280,y=180)

sport=PhotoImage(file='sport.png')
sportButton=Button(Swin,image=sport,bd=0,bg="white",activebackground="white",cursor='hand2')
sportButton.place(x=245,y=230)

loginButton=Button(Swin,text='LOGIN',font=("Aharoni",15,"bold"),fg='white',bg='royalblue',activeforeground='white',activebackground='deepskyblue',cursor='hand2',bd=1,width=25,command=login_page)
loginButton.place(x=245,y=350)

SignupButton=Button(Swin,text='Sign UP',font=("Aharoni",15,"bold"),fg='royalblue',bg='white',activeforeground='white',activebackground='deepskyblue',cursor='hand2',bd=1,width=25,command=signup_page)
SignupButton.place(x=245,y=410)

Swin.mainloop()