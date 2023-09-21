from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql


def login_user():
    if username_entry.get()=='' or password_entry.get()=='':
        messagebox.showerror(title="error",message="Field can't be empty")
    else:
        con = pymysql.connect(host='localhost', user='root')
        mycursor = con.cursor()
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where Username=%s and Password=%s'
        mycursor.execute(query,(username_entry.get(),password_entry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror("error","Either Username or Password is invalid")
        else:
            messagebox.showinfo("Welcome","Login is successful")
            login.destroy()
            import Webpage


def user_enter(event):
    if username_entry.get=='username':
        username_entry.delete(0,END)
def password_enter(event):
    if username_entry.get=='username':
        username_entry.delete(0,END)
def hide():
    showimg.config(file='closeye.png')
    password_entry.config(show='*')
    Eyebtn.config(command=show)
def show():
    showimg.config(file='openeye.png')
    password_entry.config(show='')
    Eyebtn.config(command=hide)
def signup():
    login.destroy()
    import signup

login=Tk()
login.title('Login authentication')
login.configure(bg="#DB7093")
login.resizable(0,0)
login.geometry("990x660+200+100")
bgImg = ImageTk.PhotoImage(file='bg (1).jpg')
bgLabel= Label(login,image=bgImg)
bgLabel.grid(row=0,column=0)

heading=Label(login,text='USER LOGIN',font=('cambria',20,'bold'),bg='white',fg='crimson')
heading.place(x=620,y=110)

username_entry=Entry(login,width=20,font=('cambria',15),bg='white',fg='crimson',bd=0)
username_entry.place(x=580,y=180)
username_entry.insert(0,'Username')
username_entry.bind('<FocusIn>',user_enter)
frame1=Frame(login,width=250,height=2,bg='crimson').place(x=580,y=210)

password_entry=Entry(login,width=20,font=('cambria',15),bg='white',fg='crimson',bd=0)
password_entry.place(x=580,y=250)
password_entry.insert(0,'Password')
password_entry.bind('<FocusIn>',password_enter)
frame2=Frame(login,width=250,height=2,bg='crimson').place(x=580,y=280)

showimg=PhotoImage(file='openeye.png')
Eyebtn=Button(login,image=showimg,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
Eyebtn.place(x=800,y=250)

forgetbtn=Button(login,text="Forgot Password?",bd=0 ,activebackground='white',cursor='hand2',font=('cambria',12,'italic'),bg='white',fg='crimson',activeforeground='black')
forgetbtn.place(x=700,y=290)

loginbtn=Button(login,text='Login',bd=2,bg='crimson',fg='White',width=20,cursor='hand2',font=('cambria',15),activebackground='crimson',command=login_user)
loginbtn.place(x=590,y=330)

orlabel=Label(login,text='--------------or---------------',bg='white',fg='crimson',font=('cambria',15))
orlabel.place(x=590,y=390)

facebooklogo=PhotoImage(file='facebook.png')
facebooklabel=Label(login,image=facebooklogo,bg='white')
facebooklabel.place(x=640,y=440)

googlelogo=PhotoImage(file='google.png')
googlelabel=Label(login,image=googlelogo,bg='white')
googlelabel.place(x=690,y=440)

twitterlogo=PhotoImage(file='twitter.png')
twitterlabel=Label(login,image=twitterlogo,bg='white')
twitterlabel.place(x=740,y=440)

signuplabel=Label(login,text='Dont have an account?',font=('cambria',10,'bold'),bg='white',fg='crimson')
signuplabel.place(x=580,y=500)

newaccountbtn=Button(login,text='Create new account',font=('cambria',10,'bold underline'),bg='white',fg='blue',bd=0,activebackground='white',command=signup)
newaccountbtn.place(x=720,y=500)

login.mainloop()