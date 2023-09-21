from tkinter import*
from tkinter import messagebox

def database_connect():
    root.destroy()
    import signup
def login_user():
    root.destroy()
    import signin
root=Tk()
root.title('Login authentication')
root.configure(bg="#DB7093")
root.resizable(0,0)
root.geometry("990x660+200+100")
h=root.winfo_screenheight()
w=root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(w,h))

label=Label(root,text="                        Login successfully            ",font=("algerian",45,"bold"),bg="#DB7093")
label.grid(row=4,column=8)

signupbtn=Button(root,text='Signup',bd=2,bg='crimson',fg='White',width=20,cursor='hand2',font=('cambria',15),activebackground='crimson',command=database_connect)
signupbtn.grid(row=10,column=8,pady=10)

loginbtn=Button(root,text='Back',bd=2,bg='crimson',fg='White',width=20,cursor='hand2',font=('cambria',15),activebackground='crimson',command=login_user)
loginbtn.grid(row=11,column=8,pady=10)

root.mainloop()
