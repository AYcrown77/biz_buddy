from tkinter import *
from tkinter import PhotoImage
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


#Login
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'Fields can not be empty')
    elif usernameEntry.get()=='Alan Pharmacy' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success', 'Successful')
        switch()
        passwordEntry.delete(0, tk.END)
    else:
        messagebox.showerror('Error', 'Enter correct credentials')

# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        brandLabel.config(bg="gray17", fg="green")
        homeLabel.config(bg=color["lime green"])
        topFrame.config(bg=color["lime green"])
        root.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        brandLabel.config(bg=color["nero"], fg="#5F5A33")
        homeLabel.config(bg=color["nero"])
        topFrame.config(bg=color["nero"])
        root.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True


def invoice():
    import invoice_page
    
def inventory():
    import product_page

def procurement():
    import procurement_page

def expenses():
    import expenses_page

def customer():
    import customer_page

def supplier():
    import supplier_page

#====================================================================================================

root = tk.Tk()
root.geometry('1360x750')
root.title('Main page')
root.resizable(False, False)
#root.state('zoomed')
#Add background image

backgroundImage = Image.open('images/keyboard.jpg')

global bgImage
bgImage = ImageTk.PhotoImage(backgroundImage,  master=root)

bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

# dictionary of colors:
color = {"nero": "#252726", "lime green": "#32CD32", "darkorange": "#FE6101"}

# setting switch state:
btnState = False

# loading Navbar icon image:
navIcon = PhotoImage(file="images/menu.png", master=root)
closeIcon = PhotoImage(file="images/close.png", master=root)


# top Navigation bar:
topFrame = tk.Frame(root, bg='sky blue')
topFrame.pack(side="top", fill=tk.X)

# Header label text:
homeLabel = tk.Label(topFrame, text="", font="Bahnschrift 15", bg='sky blue', fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

# Main label text:
brandLabel = tk.Label(root, text="", font="System 30", bg="gray17", fg="green")
brandLabel.place(x=100, y=250)

# Navbar button:
navbarBtn = tk.Button(topFrame, image=navIcon, bg='sky blue', activebackground='sky blue',
                    bd=0, padx=20)
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navRoot = tk.Frame(root, bg="gray17", height=1000, width=300)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg='sky blue', fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
#y = 80
"""
# option in the navbar:
options = ["inventory", "Settings", "Help", "About", "Feedback"]
# Navbar Option Buttons:
for i in range(5):
    tk.Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["lime green"], activebackground="gray17",
            activeforeground="green", bd=0).place(x=25, y=y)
    y += 40
"""
invoiceButton = tk.Button(navRoot, text="Sales Management", font="BahnschriftLight 15", bg="gray17", fg=color["lime green"], activebackground="gray17",
            activeforeground="green", bd=0, command=invoice).place(x=25, y=80)
inventoryButton = tk.Button(navRoot, text="Inventory Management", font="BahnschriftLight 15", bg="gray17", fg=color["lime green"], activebackground="gray17",
            activeforeground="green", bd=0, command=inventory).place(x=25, y=130)
procurementButton = tk.Button(navRoot, text="Procurement Manager", font="BahnschriftLight 15", bg="gray17", fg=color["lime green"], activebackground="gray17",
            activeforeground="green", bd=0, command=procurement).place(x=25, y=180)
expensesButton = tk.Button(navRoot, text="Expenses Management", font="BahnschriftLight 15", bg="gray17", fg=color["lime green"], activebackground="gray17",
            activeforeground="green", bd=0, command=expenses).place(x=25, y=230)
expensesButton = tk.Button(navRoot, text="Customer Management", font="BahnschriftLight 15", bg="gray17", fg=color["lime green"], activebackground="gray17",
            activeforeground="green", bd=0, command=customer).place(x=25, y=280)
supplierButton = tk.Button(navRoot, text="Supplier Management", font="BahnschriftLight 15", bg="gray17", fg=color["lime green"], activebackground="gray17",
            activeforeground="green", bd=0, command=supplier).place(x=25, y=330)

# Navbar Close Button:
closeBtn = tk.Button(navRoot, image=closeIcon, bg=color["lime green"], activebackground=color["lime green"], bd=0, command=switch)
closeBtn.place(x=250, y=10)

#global username, password
#username = 'Alan Pharmacy'

loginFrame = Frame(root,bg='#c8dae0')
loginFrame.place(x=400, y=150)

logoImage = PhotoImage(file='images/user.png', master=root)

logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameImage = PhotoImage(file='images/username.png', master=root)
usernameLabel = Label(loginFrame, image=usernameImage, text='Username', compound=LEFT,
                        font=('times new roman',20,'bold'),bg='#c8dae0')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)
usernameEntry = Entry(loginFrame,font=('times new roman',20,'bold'),bd=2,fg='black')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordImage = PhotoImage(file='images/padlock.png',master=root)
passwordLabel = Label(loginFrame, image=passwordImage, text='Password', compound=LEFT,
                        font=('times new roman',20,'bold'),bg='#c8dae0')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)
passwordEntry = Entry(loginFrame,font=('times new roman',20,'bold'),bd=2,fg='black',show="*")
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton = Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=15,
                        fg='black',bg='blue', activebackground='cornflowerblue',
                        activeforeground='black',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)

root.mainloop()