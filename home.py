from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

#func
b=10
f=10
t=10
def search_ent(event):
    if search.get()=='   Search':
        search.delete(0,END)

def logout():
    home.destroy()
    import start



def bb_no():
    messagebox.showinfo('Basketball',b)
def issueb():
    global b
    if b>0:
        b-=1
    messagebox.showinfo('Issue',b)
def retb():
    global b
    if b<10:
        b+=1
    messagebox.showinfo('Return',b)


def fb_no():
    messagebox.showinfo('Football',f)
def issuef():
    global f
    if f>0:
        f-=1
    messagebox.showinfo('Issue',f)
def retf():
    global f
    if f<10:
        f+=1
    messagebox.showinfo('Return',f)

def tt_no():
    messagebox.showinfo('Table Tennis',t)
def issuet():
    global t
    if t>0:
        t-=1
    messagebox.showinfo('Issue',t)
def rett():
    global t
    if t<10:
        t+=1
    messagebox.showinfo('Return',t)

def ai_tr():
    import aitrain

#GUI
home=Tk()
home.geometry('900x600+50+50')
home.resizable(0,0)
home.title("Home Page")
bgImage=ImageTk.PhotoImage(file='hbg.jpg')
bgLable=Label(home,image=bgImage)
bgLable.place(x=0,y=0)


arrow=PhotoImage(file='arrow.png')
arrowButton=Button(home,image=arrow,bd=0,bg="white",activebackground="white",cursor='hand2')
arrowButton.place(x=1,y=1)

menu=PhotoImage(file='menu.png')
menuButton=Button(home,image=menu,bd=0,bg="white",activebackground="white",cursor='hand2')
menuButton.place(x=1,y=34)

pr=PhotoImage(file='pr.png')
prButton=Button(home,image=pr,bd=0,bg="white",activebackground="white",cursor='hand2')
prButton.place(x=40,y=80)

uname=Label(home,text='Username',font=("Aharoni",23),bg='white')
uname.place(x=20,y=190)

das=PhotoImage(file='das.png')
dasButton=Button(home,image=das,bd=0,bg="white",activebackground="white",cursor='hand2')
dasButton.place(x=1,y=250)

db=Label(home,text='Dashboard',font=("Aharoni",15),bg='white')
db.place(x=35,y=250)

feed=PhotoImage(file='feed.png')
feedButton=Button(home,image=feed,bd=0,bg="white",activebackground="white",cursor='hand2')
feedButton.place(x=5,y=285)
fd=Label(home,text='Feeds',font=("Aharoni",15),bg='white')
fd.place(x=35,y=280)

set=PhotoImage(file='set.png')
setButton=Button(home,image=set,bd=0,bg="white",activebackground="white",cursor='hand2')
setButton.place(x=5,y=315)
st=Label(home,text='Settings',font=("Aharoni",15),bg='white')
st.place(x=35,y=310)

mark=PhotoImage(file='mark.png')
mButton=Button(home,image=mark,bd=0,bg="white",activebackground="white",cursor='hand2')
mButton.place(x=5,y=530)
mk=Label(home,text='Help',font=("Aharoni",15),bg='white')
mk.place(x=35,y=526)

logt=PhotoImage(file='logout.png')
ltButton=Button(home,image=logt,bd=0,bg="white",activebackground="white",cursor='hand2',command=logout)
ltButton.place(x=5,y=560)
lt=Label(home,text='Logout',font=("Aharoni",15),bg='white')
lt.place(x=35,y=556)

sport=PhotoImage(file='sport2.png')
sportButton=Button(home,image=sport,bd=0,bg="white",activebackground="white",cursor='hand2')
sportButton.place(x=200,y=10)

search=Entry(home, width=35,font=("Aharoni",15),bg='white',bd=1)
search.place(x=420,y=40)
search.insert(0,'   Search')
search.bind('<FocusIn>',search_ent)
nott=PhotoImage(file='nott.png')
notButton=Button(home,image=nott,bd=0,bg="white",activebackground="white",cursor='hand2')
notButton.place(x=830,y=38)

eq=Label(home,text='Equipment Issue',font=("Aharoni",20,"bold"),bg='white')
eq.place(x=200,y=90)

bb=PhotoImage(file='bb.png')
bbButton=Button(home,image=bb,bd=0,bg="white",activebackground="white",cursor='hand2',command=bb_no)
bbButton.place(x=200,y=130)
bbl=Label(home,text='Basketball',font=("Aharoni",18),bg='white')
bbl.place(x=270,y=130)

issueButton=Button(home,text='Issue',font=("Aharoni",10,"bold"),fg='white',bg='royalblue',activeforeground='white',activebackground='deepskyblue',cursor='hand2',bd=1,width=5,command=issueb)
issueButton.place(x=272,y=160)
returnButton=Button(home,text='Return',font=("Aharoni",10,"bold"),fg='white',bg='royalblue',activeforeground='white',activebackground='deepskyblue',cursor='hand2',bd=1,width=5,command=retb)
returnButton.place(x=330,y=160)

fb=PhotoImage(file='football.png')
fbButton=Button(home,image=fb,bd=0,bg="white",activebackground="white",cursor='hand2',command=fb_no)
fbButton.place(x=200,y=210)
fbl=Label(home,text='Football',font=("Aharoni",18),bg='white')
fbl.place(x=270,y=210)

ifButton=Button(home,text='Issue',font=("Aharoni",10,"bold"),fg='white',bg='royalblue',activeforeground='white',activebackground='deepskyblue',cursor='hand2',bd=1,width=5,command=issuef)
ifButton.place(x=272,y=240)
rfButton=Button(home,text='Return',font=("Aharoni",10,"bold"),fg='white',bg='royalblue',activeforeground='white',activebackground='deepskyblue',cursor='hand2',bd=1,width=5,command=retf)
rfButton.place(x=330,y=240)

tt=PhotoImage(file='tt.png')
ttButton=Button(home,image=tt,bd=0,bg="white",activebackground="white",cursor='hand2',command=tt_no)
ttButton.place(x=200,y=290)
ttl=Label(home,text='Table Tennis',font=("Aharoni",18),bg='white')
ttl.place(x=272,y=280)

ittButton=Button(home,text='Issue',font=("Aharoni",10,"bold"),fg='white',bg='royalblue',activeforeground='white',activebackground='deepskyblue',cursor='hand2',bd=1,width=5,command=issuet)
ittButton.place(x=272,y=320)
rttButton=Button(home,text='Return',font=("Aharoni",10,"bold"),fg='white',bg='royalblue',activeforeground='white',activebackground='deepskyblue',cursor='hand2',bd=1,width=5,command=rett)
rttButton.place(x=330,y=320)

eq=Label(home,text='Training',font=("Aharoni",20,"bold"),bg='white')
eq.place(x=500,y=88)

bbt=PhotoImage(file='bb.png')
bbtButton=Button(home,image=bb,bd=0,bg="white",activebackground="white",cursor='hand2')
bbtButton.place(x=500,y=130)
bbtl=Label(home,text='Basketball',font=("Aharoni",18),bg='white')
bbtl.place(x=570,y=130)
trButton=Button(home,text='Start',font=("Aharoni",10,"bold"),fg='white',bg='royalblue',activeforeground='white',activebackground='deepskyblue',cursor='hand2',bd=1,width=10,command=ai_tr)
trButton.place(x=580,y=160)

home.mainloop()