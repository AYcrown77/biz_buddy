import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'Fields can not be empty')
    elif usernameEntry.get()=='Alan P&S' and passwordEntry.get()=='Alan':
        messagebox.showinfo('Success', 'Welcome')
        window.destroy()
        import product_page
    else:
        messagebox.showerror('Error', 'Enter correct credentials')

window = Tk()

window.geometry('1280x700+0+0')
window.title('Login page')
window.resizable(False, False)

#Add background image
backgroundImage = Image.open('images/keyboard.jpg')
global bgImage
bgImage = ImageTk.PhotoImage(backgroundImage)

bgLabel = Label(window, image=bgImage)
bgLabel.place(x=0, y=0)

loginFrame = Frame(window,bg='#c8dae0')
loginFrame.place(x=400, y=150)

logoImage = PhotoImage(file='images/user.png')

logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameImage = PhotoImage(file='images/username.png')
usernameLabel = Label(loginFrame, image=usernameImage, text='Username', compound=LEFT,
                        font=('times new roman',20,'bold'),bg='#c8dae0')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)
usernameEntry = Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordImage = PhotoImage(file='images/padlock.png')
passwordLabel = Label(loginFrame, image=passwordImage, text='Password', compound=LEFT,
                        font=('times new roman',20,'bold'),bg='#c8dae0')
passwordEntry = Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

loginButton = Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=15,
                     fg='white',bg='cornflowerblue', activebackground='cornflowerblue',
                     activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)

window.mainloop()