from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailentry.delete(0,END)
    unameentry.delete(0,END)
    passentry.delete(0,END)
    cpassentry.delete(0,END)
    check.set(0)
def database_connect():
    if emailentry.get()=='' or unameentry.get()=='' or passentry.get()=='' or cpassentry.get()=='':
        messagebox.showerror(title='Error',message='All fields are required')
    elif passentry.get() != cpassentry.get():
        messagebox.showerror(title="Error",message="Password doesn't match")
    elif check.get()==0:
        messagebox.showerror(title="Error",message="Accept the terms and conditions")
    else:
        con=pymysql.connect(host='localhost',user='root')
        mycursor=con.cursor()
        try:
             query='create database userdata'
             mycursor.execute(query)
             query='use userdata'
             mycursor.execute(query)
             sql='create table data(Email varchar(50),Username varchar(50),Password varchar(20))'
             mycursor.execute(sql)
        except:
             mycursor.execute('use userdata')
        query='select * from data where Username=%s'
        mycursor.execute(query,(unameentry.get()))
        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror(title="error",message="username already exists")
        else:
            sqlins='insert into data(Email,Username,Password) values(%s,%s,%s)'
            mycursor.execute(sqlins,(emailentry.get(),unameentry.get(),passentry.get()))
            con.commit()
            con.close()
            messagebox.showinfo(title="success",message="registration is sucessful")
            clear()
            signup.destroy()
            import signin




def signin():
    signup.destroy()
    import signin

signup=Tk()
signup.title('Signup Page')
signup.resizable(0,0)
background=ImageTk.PhotoImage(file='bg (1).jpg')
bglabel=Label(signup,image=background)
bglabel.grid(row=0,column=0)

frame=Frame(signup,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='USER SIGNUP PAGE',font=('cambria',24,'bold'),bg='white',fg='crimson')
heading.grid(row=0,column=0,padx=5)

emailLabel=Label(frame,text='Email',font=('cambria',13,'bold'),bg='white',fg='crimson')
emailLabel.grid(row=1,column=0,sticky='w',padx=25)
emailentry=Entry(frame,font=('cambria',10,'bold'),bg='crimson',fg='white',width=30)
emailentry.grid(row=2,column=0,sticky='w',padx=25)

UsernameLabel=Label(frame,text='Username',font=('cambria',13,'bold'),bg='white',fg='crimson')
UsernameLabel.grid(row=3,column=0,sticky='w',padx=25)
unameentry=Entry(frame,font=('cambria',10,'bold'),bg='crimson',fg='white',width=30)
unameentry.grid(row=4,column=0,sticky='w',padx=25)

PasswordLabel=Label(frame,text='Password',font=('cambria',13,'bold'),bg='white',fg='crimson')
PasswordLabel.grid(row=5,column=0,sticky='w',padx=25)
passentry=Entry(frame,font=('cambria',10,'bold'),bg='crimson',fg='white',width=30)
passentry.grid(row=6,column=0,sticky='w',padx=25)

ConfirmpassLabel=Label(frame,text='Confirm Password',font=('cambria',13,'bold'),bg='white',fg='crimson')
ConfirmpassLabel.grid(row=7,column=0,sticky='w',padx=25)
cpassentry=Entry(frame,font=('cambria',10,'bold'),bg='crimson',fg='white',width=30)
cpassentry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
checkbutton=Checkbutton(frame,text="I agree to terms and conditions",font=('cambria',11,'bold'),fg='crimson',bg='white',activebackground='white',activeforeground='crimson',variable=check)
checkbutton.grid(row=9,column=0,sticky='w',padx=13,pady=10)

signupbtn=Button(frame,text='Signup',bd=2,bg='crimson',fg='White',width=20,cursor='hand2',font=('cambria',15),activebackground='crimson',command=database_connect)
signupbtn.grid(row=10,column=0,pady=10)

alreadyaccountLabel=Label(frame,text='Already have an account?',font=('cambria',11,'bold'),fg='crimson',bg='white')
alreadyaccountLabel.grid(row=11,column=0,pady=10)

loginBtn=Button(frame,text='Login here',bg='white',activebackground='white',fg='blue',font=('cambria',11,'bold underline'),bd=0,command=signin)
loginBtn.grid(row=12,column=0)
signup.mainloop()
