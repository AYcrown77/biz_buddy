from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title('Sales page')
root.geometry('1200x670')
root.iconphoto(False, tk.PhotoImage(file='images/billing.png'))

headingLabel = Label(root,text='Retail Billing System',font=('times new roman',30,'bold')
                     ,bg='lime green',bd=12,relief=GROOVE)
headingLabel.pack(fill=X,pady=1)

customer_details_frame = LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold')
                                    ,bd=8,relief=GROOVE,bg='lime green')
customer_details_frame.pack(fill=X)

nameLabel = Label(customer_details_frame, text='Name',font=('times new roman',15,'bold')
                  ,bg='lime green',fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry = Entry(customer_details_frame,font=('arial',15),bd=4,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel = Label(customer_details_frame, text='Phone No',font=('times new roman',15,'bold')
                  ,bg='lime green',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry = Entry(customer_details_frame,font=('arial',15),bd=4,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billNumberLabel = Label(customer_details_frame, text='Bill No',font=('times new roman',15,'bold')
                  ,bg='lime green',fg='white')
billNumberLabel.grid(row=0,column=4,padx=20,pady=2)

billNumberEntry = Entry(customer_details_frame,font=('arial',15),bd=4,width=18)
billNumberEntry.grid(row=0,column=5,padx=8)

searchButton = Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=3,width=10)
searchButton.grid(row=0,column=6,padx=20,pady=8)

root.mainloop()